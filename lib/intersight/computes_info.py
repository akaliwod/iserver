import copy
import json
import time

import concurrent.futures
from concurrent.futures import ProcessPoolExecutor

from lib.intersight.compute_filter import ComputeFilter
from lib.intersight.computes_summary import ComputesSummary
from lib.intersight.computes_worfklow import ComputesWorkflow

from lib.intersight import compute_extra_attributes
from lib.intersight import compute_rack
from lib.intersight import compute_blade

from lib import log_helper
from lib import output_helper


class ComputesInfo(ComputeFilter, ComputesWorkflow, ComputesSummary):
    """Class for intersight compute blade and rack objects
    """
    def __init__(self, iaccount, settings, log_id=None):
        ComputeFilter.__init__(self)
        ComputesWorkflow.__init__(self)
        ComputesSummary.__init__(self, settings, log_id=log_id)

        self.log = log_helper.Log(log_id=log_id)
        self.rack_handler = compute_rack.ComputeRack(iaccount, log_id=log_id)
        self.blade_handler = compute_blade.ComputeBlade(iaccount, log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)

        self.iaccount = iaccount
        self.settings = settings
        self.log_id = log_id

    def get_server_info(self, server, log_id=None, include_object=False):
        server_info_handler = compute_extra_attributes.ComputeExtraAttributes(
            self.iaccount,
            self.settings,
            log_id=log_id
        )
        server_info = server_info_handler.get_server_info(
            server,
            include_object=include_object
        )
        return server_info

    def prepare_cache_key(self, key, moids, device_moids, registration_moids, board_moids):
        server_info_handler = compute_extra_attributes.ComputeExtraAttributes(
            self.iaccount,
            self.settings,
            log_id=self.log_id
        )

        return server_info_handler.set_cache(key, moids, device_moids, registration_moids, board_moids)

    def prepare_cache(self, moids, device_moids, registration_moids, board_moids):
        keys = [
            'asset_device_registration',
            'locator_led',
            'workflow',
            'fanmodule',
            'pci',
            'psu',
            'firmware',
            'storage_controller',
            'virtual_drive',
            'physical_disk'
        ]
        with ProcessPoolExecutor() as executor:
            pool = [executor.submit(self.prepare_cache_key, key, moids, device_moids, registration_moids, board_moids) for key in keys]
            for i in concurrent.futures.as_completed(pool):
                success = i.result()
                if not success:
                    self.log.error(
                        'computes_info.prepare_cache',
                        'Cache failed'
                    )

    def get(self, match_rules=None, parallel=True, include_object=False):
        complete_start_time = int(time.time() * 1000)

        self.log.debug(
            'computes_info.get',
            'Get servers settings: %s' % (
                json.dumps(self.settings, indent=4)
            )
        )
        self.log.debug(
            'computes_info.get',
            'Get servers match rules: %s' % (
                json.dumps(match_rules, indent=4)
            )
        )
        all_servers = []

        start_time = int(time.time() * 1000)

        if self.settings['rack']:
            rack_servers = self.rack_handler.get_all()
            if rack_servers is not None:
                all_servers = all_servers + rack_servers

        if self.settings['blade']:
            blade_servers = self.blade_handler.get_all()
            if blade_servers is not None:
                all_servers = all_servers + blade_servers

        end_time = int(time.time() * 1000)
        duration = end_time - start_time

        self.log.debug(
            'computes_info.get',
            'All %s servers base information in %s ms' % (len(all_servers), duration)
        )

        start_time = int(time.time() * 1000)

        base_servers = []
        for server in all_servers:
            if self.match_server(server, match_rules, base_match=True):
                base_servers.append(server)

        end_time = int(time.time() * 1000)
        duration = end_time - start_time

        self.log.debug(
            'computes_info.get',
            'Base filter %s servers in %s ms' % (len(base_servers), duration)
        )

        start_time = int(time.time() * 1000)

        servers = []

        if len(base_servers) > 0:
            moids = []
            device_moids = []
            registration_moids = []
            board_moids = []
            for base_server in base_servers:
                moids.append(base_server['Moid'])
                device_moids.append(base_server['DeviceMoId'])
                registration_moids.append(base_server['RegisteredDevice']['Moid'])
                board_moids.append(base_server['Board']['Moid'])

            self.prepare_cache(moids, device_moids, registration_moids, board_moids)

        if parallel:
            with ProcessPoolExecutor() as executor:
                pool = [executor.submit(self.get_server_info, server, log_id=self.log_id, include_object=include_object) for server in base_servers]
                for i in concurrent.futures.as_completed(pool):
                    server_info = i.result()
                    self.log.debug(
                        'computes_info.get_server_info',
                        'Thread result: %s' % (server_info['Moid'])
                    )

                    if server_info is None:
                        self.log.error(
                            'computes_info.get_server_info',
                            'No server info: %s' % (server_info['Moid'])
                        )

                    if server_info is not None:
                        if self.match_server(server_info, match_rules, base_match=False):
                            servers.append(server_info)
                            continue

        if not parallel:
            for server in base_servers:
                server_info = self.get_server_info(
                    server,
                    include_object=include_object
                )
                if server_info is None:
                    continue

                if self.match_server(server_info, match_rules, base_match=False):
                    servers.append(server_info)
                    continue

        end_time = int(time.time() * 1000)
        duration = end_time - start_time

        self.log.debug(
            'computes_info.get',
            'Selected %s servers with requested details in %s ms' % (len(servers), duration)
        )

        duration = end_time - complete_start_time
        self.log.debug(
            'computes_info.get',
            'Total time %s ms' % (duration)
        )

        return servers

    def print(self, servers, legend_on=True, force_base_output=False):
        servers = sorted(servers, key=lambda i: i['Name'])

        if force_base_output:
            order = [
                'Name',
                'Model',
                'Serial',
                'ManagementIp'
            ]

            headers = [
                'Name',
                'Model',
                'Serial',
                'IP'
            ]

        if not force_base_output:
            order = [
                'FlagState',
                'FlagManagement',
                'FlagWorkflow',
                'Name',
                'TypeModel',
                'Serial',
                'ManagementIp',
                'Cpu',
                'TotalMemoryUnit'
            ]

            headers = [
                'SF',
                'MF',
                'WF',
                'Name',
                'Model',
                'Serial',
                'IP',
                'CPU',
                'Memory'
            ]

            # Extra columns based on settings

            if self.settings['id']:
                order.append('Moid')
                headers.append('Moid')

            if self.settings['fw']:
                order.append('Fw')
                headers.append('Fw')

            if self.settings['pci']:
                order.append('PciModel')
                headers.append('PCI')

            if self.settings['fan']:
                order.append('FanSummary')
                headers.append('Fan')

            if self.settings['psu']:
                order.append('PsuSummary')
                headers.append('Psu')

            if self.settings['group']:
                order.append('Groups')
                headers.append('Groups')

            if self.settings['storage']:
                order.append('StorageDrives')
                headers.append('Storage Drives')
                order.append('StorageCapacity')
                headers.append('Storage Capacity')

            # PCI output requires special handling for multi-line support

            if self.settings['pci']:
                pci_servers = []
                for server in servers:
                    if self.settings['pci']:
                        if len(server['PciModels']) == 0:
                            server['PciModel'] = ''
                            pci_servers.append(server)
                            continue

                        if len(server['PciModels']) == 1:
                            server['PciModel'] = server['PciModels'][0]
                            pci_servers.append(server)
                            continue

                        if len(server['PciModels']) > 1:
                            pci_index = 1
                            for pci_model in server['PciModels']:
                                if pci_index == 1:
                                    new_server = copy.deepcopy(server)
                                    new_server['PciModel'] = pci_model
                                else:
                                    new_server = copy.deepcopy(server)
                                    for displayed_field in order:
                                        new_server[displayed_field] = ''
                                    new_server['PciModel'] = pci_model
                                pci_servers.append(new_server)
                                pci_index = pci_index + 1

                            continue

                    pci_servers.append(server)

                servers = copy.deepcopy(pci_servers)

            if self.settings['power']:
                if 'Cpu' in order:
                    order.remove('Cpu')
                if 'TotalMemoryUnit' in order:
                    order.remove('TotalMemoryUnit')
                if 'CPU' in headers:
                    headers.remove('CPU')
                if 'Memory' in headers:
                    headers.remove('Memory')

                order.append('Power.Summary.PowerNow')
                headers.append('Consumed [W]')
                order.append('Power.Summary.PowerMin')
                headers.append('Min [W]')
                order.append('Power.Summary.PowerAvg')
                headers.append('Avg [W]')
                order.append('Power.Summary.PowerMax')
                headers.append('Max [W]')

            if self.settings['thermal']:
                if 'Cpu' in order:
                    order.remove('Cpu')
                if 'TotalMemoryUnit' in order:
                    order.remove('TotalMemoryUnit')
                if 'CPU' in headers:
                    headers.remove('CPU')
                if 'Memory' in headers:
                    headers.remove('Memory')

                order.append('Thermal.Summary.FanHealth')
                headers.append('Fans')
                order.append('Thermal.Summary.SensorHealth')
                headers.append('Sensors')
                order.append('Thermal.Summary.HighestTemperature')
                headers.append('Highest (C)')
                order.append('Thermal.Summary.SmallestGap')
                headers.append('Min Gap (C)')
                order.append('Thermal.Summary.OverThreshold')
                headers.append('Over Threshold')

        # Print servers table

        self.my_output.my_table(
            servers,
            order=order,
            allow_order_subkeys=True,
            headers=headers,
            table=True
        )

        if legend_on:
            self.print_flags_legend()

    def print_flags_legend(self):
        legend = {}
        legend['power'] = '(P+) on (P-) off'
        legend['health'] = '(H)ealthy (W)arning (C)ritical'
        legend['locator'] = '(L)ocator on'

        self.my_output.dictionary(
            legend,
            title='State Flags (SF)',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'power',
                'health',
                'locator'
            ],
            title_keys=[
                'Power',
                'Health',
                'Locator'
            ]
        )

        legend = {}
        legend['connected'] = '(C) connected (c) disconnected'
        legend['ucsm'] = '(U)csm ready (u)csm capable'
        legend['redfish'] = '(R)edfish ready (r)edfish capable'
        legend['imc'] = '(I)mc ready (i)imc capable'

        self.my_output.dictionary(
            legend,
            title='Management Flags (MF)',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'connected',
                'ucsm',
                'redfish',
                'imc'
            ],
            title_keys=[
                'Intersight API',
                'UCSM API',
                'Redfish API',
                'IMC API'
            ]
        )

        legend = {}
        legend['running'] = '(R)'
        legend['last'] = '(F)'
        legend['some'] = '(f)'

        self.my_output.dictionary(
            legend,
            title='Workflow Flags (SF)',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'running',
                'last',
                'some'
            ],
            title_keys=[
                'Running',
                'Last Failed',
                'Failed'
            ]
        )

    def print_power(self, servers):
        servers = sorted(servers, key=lambda i: i['Name'])

        order = [
            'PowerSource',
            'Name',
            'Model',
            'ManagementIp',
            'Serial',
            'OperPowerState',
            'PowerConsumedWatts',
            'PowerMinConsumedWatts',
            'PowerAvgConsumedWatts',
            'PowerMaxConsumedWatts'
        ]

        headers = [
            'Source',
            'Name',
            'Model',
            'IP',
            'Serial',
            'Power State',
            'Consumed [W]',
            'Min [W]',
            'Avg [W]',
            'Max [W]'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            table=True
        )

    def print_thermal(self, servers):
        servers = sorted(servers, key=lambda i: i['Name'])

        order = [
            'ThermalSource',
            'Name',
            'Model',
            'ManagementIp',
            'Serial',
            'OperPowerState',
            'ThermalFanHealth',
            'ThermalSensorHealth',
            'ThermalHighestTemperature',
            'ThermalSmallestGap',
            'ThermalOverThreshold'
        ]

        headers = [
            'Source',
            'Name',
            'Model',
            'IP',
            'Serial',
            'Power State',
            'Fans Healthy',
            'Sensors Healthy',
            'Highest (C)',
            'Smallest Gap (C)',
            'Over Threshold'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            table=True
        )
