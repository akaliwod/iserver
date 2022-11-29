import copy
from lib.intersight.compute_filter import ComputeFilter
from lib.intersight.compute_extra_attributes import ComputeExtraAttributes
from lib.intersight.computes_summary import ComputesSummary
from lib.intersight.computes_worfklow import ComputesWorkflow
from lib.intersight import compute_rack
from lib.intersight import compute_blade
from lib import output_helper


class ComputesInfo(ComputeExtraAttributes, ComputeFilter, ComputesWorkflow, ComputesSummary):
    """Class for intersight compute blade and rack objects
    """
    def __init__(self, iaccount, settings):
        ComputeExtraAttributes.__init__(self, iaccount, settings)
        ComputeFilter.__init__(self)
        ComputesWorkflow.__init__(self)
        ComputesSummary.__init__(self, settings)
        self.rack_handler = compute_rack.ComputeRack(iaccount)
        self.blade_handler = compute_blade.ComputeBlade(iaccount)
        self.my_output = output_helper.OutputHelper()
        self.settings = settings

    def get(self, match_rules=None, base_search=False):
        base_servers = []

        if self.settings['rack']:
            rack_servers = self.rack_handler.get_all()
            if rack_servers is not None:
                base_servers = base_servers + rack_servers

        if self.settings['blade']:
            blade_servers = self.blade_handler.get_all()
            if blade_servers is not None:
                base_servers = base_servers + blade_servers

        servers = []
        if base_search:
            for base_server in base_servers:
                server = self.add_management_ip(base_server)
                if self.match_server(server, match_rules, base_match=True):
                    servers.append(server)

        if not base_search:
            for base_server in base_servers:
                server = self.add_server_attributes(base_server)
                if server is None:
                    continue

                if self.match_server(server, match_rules):
                    servers.append(server)

        return servers

    def print(self, servers, legend_on=True, force_base_output=False):
        # Always sort by Name

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
                'State',
                'Name',
                'Model',
                'Serial',
                'ManagementIp',
                'Cpu',
                'TotalMemoryUnit'
            ]

            headers = [
                'Flags',
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

        # Print servers table

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            table=True
        )

        if legend_on:
            legend = {}
            legend['power'] = '(P+) on (P-) off'
            legend['health'] = '(H)ealthy (W)arning (C)ritical'
            legend['management'] = '(U)CSM (S)tandalone'
            legend['type'] = '(R)ack (B)lade'
            legend['locator'] = '(L)ocator on'
            legend['disconnected'] = '(D)isconnected'
            legend['workflow'] = 'W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours'

            self.my_output.dictionary(
                legend,
                title='Flags',
                underline=False,
                prefix="- ",
                justify=True,
                keys=[
                    'power',
                    'health',
                    'type',
                    'management',
                    'locator',
                    'disconnected',
                    'workflow'
                ],
                title_keys=[
                    'Power',
                    'Health',
                    'Type',
                    'Management',
                    'Locator',
                    'Connection',
                    'Workflow'
                ]
            )
