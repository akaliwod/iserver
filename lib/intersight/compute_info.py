from lib.intersight.compute_extra_attributes import ComputeExtraAttributes
from lib.intersight import compute_rack
from lib.intersight import compute_blade
from lib import output_helper


class ComputeInfo(ComputeExtraAttributes):
    """Class for intersight compute blade and rack objects
    """
    def __init__(self, iaccount, settings=None, log_id=None):
        self.settings = settings
        if settings is None:
            self.settings = self.get_default_settings()

        ComputeExtraAttributes.__init__(self, iaccount, self.settings, log_id=log_id)
        self.get_info_cache_mode = False

        self.rack_handler = compute_rack.ComputeRack(iaccount, log_id=log_id)
        self.blade_handler = compute_blade.ComputeBlade(iaccount, log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def get_default_settings(self):
        settings = {}
        settings['rack'] = True
        settings['blade'] = True
        settings['server_setting_id'] = False
        settings['workflow'] = None
        settings['registration'] = False
        for key in ['id', 'cpu', 'memory', 'fw', 'pci', 'fan', 'psu', 'group', 'storage', 'locator', 'power', 'thermal']:
            settings[key] = False
        return settings

    def get(self, server_id, include_object=False):
        server = self.rack_handler.get(server_id)
        if server is None:
            server = self.blade_handler.get(server_id)

        if server is None:
            return None

        server_info = self.get_server_info(
            server,
            include_object=include_object
        )

        return server_info

    def print_summary_table(self, server, legend_on=False):
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

        self.my_output.my_table(
            [server],
            order=order,
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

    def print_summary_dictionary(self, server):
        self.my_output.dictionary(
            server,
            title='Identity',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'Moid',
                'Name',
                'Type',
                'Model',
                'Serial',
                'ManagementIp'
            ],
            title_keys=[
                'Server ID',
                'Name',
                'Type',
                'Model',
                'Serial',
                'IP'
            ]
        )

        if server['Redfish']['Capable']:
            self.my_output.dictionary(
                server['Redfish'],
                title='Redfish',
                underline=False,
                prefix="- ",
                justify=True,
                keys=[
                    'Capable',
                    'Enabled'
                ],
                title_keys=[
                    'Capable',
                    'Enabled'
                ]
            )

        self.my_output.dictionary(
            server,
            title='State',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'OperPowerState',
                'LocatorLedOn',
                'Health',
                'ManagementMode',
                'Connected',
                'Fw',
                'PsuSummary',
                'FanSummary'
            ],
            title_keys=[
                'Power',
                'Locator',
                'Health',
                'Mode',
                'Connected',
                'Firmware',
                'PSU',
                'Fan'
            ]
        )

        self.my_output.dictionary(
            server,
            title='CPU and Memory',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'NumCpus',
                'NumThreads',
                'NumCpuCores',
                'NumCpuCoresEnabled',
                'TotalMemoryUnit'
            ],
            title_keys=[
                'CPU Sockets',
                'Threads',
                'Cores',
                'Enabled Cores',
                'Memory'
            ]
        )

        keys = [
            'StorageControllersCount',
            'PhysicalDiskCount',
            'PhysicalDiskCapacityUnit',
            'HddDiskCount',
            'HddDiskCapacityUnit',
            'SsdDiskCount',
            'SsdDiskCapacityUnit',
            'VirtualDiskCount'
        ]

        match = False
        for key in keys:
            if key in server:
                match = True
                break

        if match:
            self.my_output.dictionary(
                server,
                title='Storage',
                underline=False,
                prefix="- ",
                justify=True,
                keys=keys,
                title_keys=[
                    'Controllers',
                    'Disks count',
                    'Disks capacity',
                    'HDD count',
                    'HDD capacity',
                    'SSD count',
                    'SSD capacity',
                    'Virtual Disks'
                ]
            )

    def print_cpu(self, cpus):
        order = [
            'ProcessorId',
            'SocketDesignation',
            'Vendor',
            'Architecture',
            'Model',
            'Presence',
            'OperState',
            'NumCores',
            'NumCoresEnabled',
            'NumThreads',
            'Speed',
            'Stepping'
        ]

        headers = [
            'CPU Id',
            'Socket',
            'Vendor',
            'Arch',
            'Model',
            'Presence',
            'OperState',
            'Cores',
            'Enabled',
            'Threads',
            'Speed',
            'Stepping'
        ]

        self.my_output.my_table(
            cpus,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_memory(self, memory_info):
        order = [
            'MemoryId',
            'ArrayId',
            'Bank',
            'Location',
            'Capacity',
            'Clock',
            'FormFactor',
            'Type',
            'Model',
            'Serial',
            'OperState',
            'Presence'
        ]

        headers = [
            'Memory Id',
            'Array',
            'Bank',
            'Location',
            'Capacity',
            'Clock',
            'Form Factor',
            'Type',
            'Model',
            'Serial',
            'Oper State',
            'Presence'
        ]

        self.my_output.my_table(
            memory_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_storage_controllers(self, storage_controllers):
        for storage_controller in storage_controllers:
            self.my_output.dictionary(
                storage_controller,
                title='Storage Controller',
                underline=False,
                prefix="- ",
                justify=True,
                keys=[
                    'Model',
                    'Vendor',
                    'Serial',
                    'Presence',
                    'PciSlot',
                    'ControllerId',
                    'Dn',
                    'RaidSupport',
                    'PhysicalDisksCount',
                    'VirtualDrivesCount'
                ],
                title_keys=[
                    'Model',
                    'Vendor',
                    'Serial',
                    'Presence',
                    'Pci Slot',
                    'Controller Id',
                    'Dn',
                    'Raid Support',
                    'Physical Disks Count',
                    'Virtual Drives Count'
                ]
            )

    def print_physical_disks(self, disks_info):
        order = [
            'DiskId',
            'DiskState',
            'Size',
            'Presence',
            'Model',
            'Vendor',
            'Type',
            'StorageControllerId',
            'VirtualDriveId',
            'Dn'
        ]

        headers = [
            'Physical Disk Id',
            'State',
            'Size',
            'Presence',
            'Model',
            'Vendor',
            'Type',
            'Controller',
            'VD',
            'Dn'
        ]

        self.my_output.my_table(
            disks_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_virtual_drives(self, drives_info):
        order = [
            'VirtualDriveId',
            'Size',
            'PhysicalDiskCount',
            'Type',
            'Name',
            'StorageControllerId',
            'Dn'
        ]

        headers = [
            'Virtual Drive Id',
            'Size',
            'Physical Disks',
            'Type',
            'Name',
            'Controller',
            'Dn'
        ]

        self.my_output.my_table(
            drives_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_pci(self, pci_info):
        order = [
            'Model',
            'Pid',
            'SlotId',
            'Vendor',
            'FirmwareVersion',
            'Dn'
        ]

        headers = [
            'PCI Device Model',
            'Pid',
            'SlotId',
            'Vendor',
            'Firmware',
            'Dn'
        ]

        self.my_output.my_table(
            pci_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_fan(self, fan_info):
        order = [
            'ModuleId',
            'OperState',
            'Presence',
            'Dn'
        ]

        headers = [
            'Fan Module Id',
            'OperState',
            'Presence',
            'Dn'
        ]

        self.my_output.my_table(
            fan_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_psu(self, psu_info):
        order = [
            'Model',
            'Serial',
            'Vendor',
            'Dn'
        ]

        headers = [
            'PSU Model',
            'Serial',
            'Vendor',
            'Dn'
        ]

        self.my_output.my_table(
            psu_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_workflows(self, workflows, show_empty_table=False):
        if len(workflows) == 0:
            if not show_empty_table:
                return

        order = [
            'Moid',
            'Name',
            'CreateTime',
            'Status',
            'Duration'
        ]

        headers = [
            'Workflow Moid',
            'Name',
            'Create Time',
            'Status',
            'Duration'
        ]

        self.my_output.my_table(
            workflows,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print(self, server, workflow_count=10, legend_on=False):
        self.print_summary_table(server, legend_on=legend_on)

        if 'CpuInfo' in server:
            self.print_cpu(server['CpuInfo'])

        if 'MemoryInfo' in server:
            self.print_memory(server['MemoryInfo'])

        if 'StorageControllersInfo' in server:
            self.print_storage_controllers(server['StorageControllersInfo'])

        if 'PhysicalDisks' in server:
            self.print_physical_disks(server['PhysicalDisks'])

        if 'VirtualDisks' in server:
            self.print_virtual_drives(server['VirtualDisks'])

        if 'PciDevicesInfo' in server:
            self.print_pci(server['PciDevicesInfo'])

        if 'FanInfo' in server:
            self.print_fan(server['FanInfo'])

        if 'PsuInfo' in server:
            self.print_psu(server['PsuInfo'])

        if 'Power' in server:
            if server['Power'] is None:
                self.my_output.default('No power consumption information found')

            if server['Power'] is not None and server['Redfish']['Enabled']:
                self.redfish_endpoint_settings_handler.print_redfish_endpoint_template(
                    server['Serial'],
                    'power',
                    server['Power']
                )

            if server['Power'] is not None and server['UCSM']['Enabled']:
                self.ucsm_endpoint_settings_handler.print_ucsm_endpoint_template(
                    server['Serial'],
                    'power',
                    server['Power']
                )

        if 'Thermal' in server:
            if server['Thermal'] is None:
                self.my_output.default('No thermal information found')

            if server['Thermal'] is not None and server['Redfish']['Enabled']:
                self.redfish_endpoint_settings_handler.print_redfish_endpoint_template(
                    server['Serial'],
                    'thermal',
                    server['Thermal']
                )

            if server['Thermal'] is not None and server['UCSM']['Enabled']:
                self.ucsm_endpoint_settings_handler.print_ucsm_endpoint_template(
                    server['Serial'],
                    'thermal',
                    server['Thermal']
                )

        if 'WorkflowsLast' in server:
            self.print_workflows(server['WorkflowsLast'][:workflow_count])
