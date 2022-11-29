import os
from lib.intersight.compute_extra_attributes import ComputeExtraAttributes
from lib.intersight import compute_rack
from lib.intersight import compute_blade
from lib import output_helper


class ComputeInfo(ComputeExtraAttributes):
    """Class for intersight compute blade and rack objects
    """
    def __init__(self, iaccount, settings=None):
        self.settings = settings
        if settings is None:
            self.settings = self.get_default_settings()

        ComputeExtraAttributes.__init__(self, iaccount, self.settings)
        self.get_info_cache_mode = False

        self.rack_handler = compute_rack.ComputeRack(iaccount)
        self.blade_handler = compute_blade.ComputeBlade(iaccount)
        self.my_output = output_helper.OutputHelper()

    def get_default_settings(self):
        settings = {}
        settings['rack'] = True
        settings['blade'] = True
        settings['server_setting_id'] = False
        settings['workflow'] = None
        for key in ['id', 'cpu', 'memory', 'fw', 'pci', 'fan', 'psu', 'group', 'storage', 'locator']:
            settings[key] = False
        return settings

    def get(self, moid=None, server=None):
        if moid is None and server is None:
            return None

        if moid is not None:
            server = self.rack_handler.get(moid)
            if server is None:
                server = self.blade_handler.get(moid)

        if server is None:
            return None

        if server['ObjectType'] == 'compute.RackUnit':
            self.set_rack_compute_filter(server)

        return self.add_server_attributes(server)

    def print_summary_columns(self, server):
        data = self.my_output.dictionary(
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
                'ManagementIp',
                'AssetTag',
                'ManagementMode'
            ],
            title_keys=[
                'Server ID',
                'Name',
                'Type',
                'Model',
                'Serial',
                'IP',
                'AssetTag',
                'Mode'
            ],
            stream=None
        )
        column1 = []
        for line in data.split('\n'):
            if len(line) > 0:
                column1.append(line)

        data = self.my_output.dictionary(
            server,
            title='State',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'OperPowerState',
                'LocatorLedOn',
                'Health',
                'Fw',
                'PsuSummary',
                'FanSummary'
            ],
            title_keys=[
                'Power',
                'Locator',
                'Health',
                'Firmware',
                'PSU',
                'Fan'
            ],
            stream=None
        )
        column2 = []
        for line in data.split('\n'):
            if len(line) > 0:
                column2.append(line)

        data = self.my_output.dictionary(
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
            ],
            stream=None
        )
        column3 = []
        for line in data.split('\n'):
            if len(line) > 0:
                column3.append(line)

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

        column4 = None
        if match:
            data = self.my_output.dictionary(
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
                ],
                stream=None
            )
            column4 = []
            for line in data.split('\n'):
                if len(line) > 0:
                    column4.append(line)

        data = []
        data.append(column1)
        data.append(column2)
        data.append(column3)
        if column4 is not None:
            data.append(column4)

        self.my_output.columns(data, max_length=os.get_terminal_size()[0])

    def print_summary_standard(self, server):
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
            'Processor Id',
            'Socket',
            'Vendor',
            'Arch',
            'Model',
            'Presence',
            'OperState',
            'Cores',
            'Cores Enabled',
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

    def print_workflows(self, workflows):
        if len(workflows) == 0:
            self.my_output.default('\nNo workflows')
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

    def print(self, server, workflow_count=10):
        self.print_summary_standard(server)

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

        if 'WorkflowsLast' in server:
            self.print_workflows(server['WorkflowsLast'][:workflow_count])
