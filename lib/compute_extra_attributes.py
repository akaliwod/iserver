import json
import traceback
from lib import info_helper

from lib import equipment_led
from lib import equipment_fan_module
from lib import equipment_psu
from lib import processor_unit
from lib import memory_unit
from lib import pci_device
from lib import running_firmware
from lib import storage_physical_disk
from lib import storage_virtual_drive
from lib import storage_controller
from lib import compute_server_setting
from lib import workflow
from lib import my_servers_helper


class ComputeExtraAttributes():
    """Class for rack/blade compute object extra attributes
    """
    def __init__(self, iaccount, settings):
        self.settings = settings
        self.my_servers_handler = my_servers_helper.MyServers()
        self.my_servers_serials = self.my_servers_handler.get_serials()
        self.info_handler = info_helper.InfoHelper()
        self.locator_handler = equipment_led.EquipmentLed(iaccount)
        self.processor_unit_handler = processor_unit.ProcessorUnit(iaccount)
        self.memory_unit_handler = memory_unit.MemoryUnit(iaccount)
        self.fan_handler = equipment_fan_module.EquipmentFanModule(iaccount)
        self.psu_handler = equipment_psu.EquipmentPsu(iaccount)
        self.pci_handler = pci_device.PciDevice(iaccount)
        running_firmware_filter = '"Component eq \'system\' and Type eq \'blade-controller\'"'
        self.running_firmware_handler = running_firmware.RunningFirmware(
            iaccount,
            get_filter=running_firmware_filter
        )
        self.storage_physical_disk_handler = storage_physical_disk.StoragePhysicalDisk(iaccount)
        self.storage_virtual_drive_handler = storage_virtual_drive.StorageVirtualDrive(iaccount)
        self.storage_controller_handler = storage_controller.StorageController(iaccount)
        self.compute_server_setting_handler = compute_server_setting.ComputeServerSetting(iaccount)
        self.workflow = workflow.Workflow(iaccount)
        self.last_workflows = None

    def set_rack_compute_filter(self, server):
        self.processor_unit_handler.set_get_filter("ComputeBoard/Moid eq '%s'" % (server['Board']['Moid']))
        self.memory_unit_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        self.pci_handler.set_get_filter("Parent/Moid eq '%s'" % (server['Moid']))
        self.fan_handler.set_get_filter("Parent/Moid eq '%s'" % (server['Moid']))
        self.psu_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        self.locator_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        self.running_firmware_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        self.storage_controller_handler.set_get_filter("Parent/Moid eq '%s'" % (server['Board']['Moid']))
        self.storage_physical_disk_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        self.storage_virtual_drive_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))

    def get_last_workflows(self):
        if self.last_workflows is None:
            self.last_workflows = self.workflow.get_last(seconds=self.settings['workflow'])

    def add_management_ip(self, server):
        server['ManagementIp'] = None
        try:
            if 'KvmIpAddresses' in server:
                for kvm_ip in server['KvmIpAddresses']:
                    if kvm_ip['ClassId'] == 'compute.IpAddress':
                        server['ManagementIp'] = kvm_ip['Address']
        except BaseException:
            pass
        return server

    def add_common_attributes(self, server):
        if server is None:
            return None

        server = self.add_management_ip(server)

        server['Cpu'] = '%sS %sC %sT' % (
            server['NumCpus'],
            server['NumCpuCores'],
            server['NumThreads']
        )

        if server['AlarmSummary']['Warning'] == 0 and server['AlarmSummary']['Critical'] == 0:
            server['Health'] = 'Healthy'
        if server['AlarmSummary']['Warning'] > 0 and server['AlarmSummary']['Critical'] == 0:
            server['Health'] = 'Warnings (%s)' % (server['AlarmSummary']['Warning'])
        if server['AlarmSummary']['Critical'] > 0:
            server['Health'] = 'Critical (%s)' % (server['AlarmSummary']['Critical'])

        server['TotalMemoryUnit'] = self.info_handler.convert_memory(server['TotalMemory'] * 1024 * 1024, precision=0)
        server['TotalMemoryGB'] = int(server['TotalMemory'] / 1024)

        server['Groups'] = ''
        if self.my_servers_serials is not None:
            if server['Serial'] in self.my_servers_serials:
                server['Groups'] = ','.join(
                    self.my_servers_serials[server['Serial']]
                )

        if self.settings['server_setting_id']:
            server['ServerSettingId'] = self.compute_server_setting_handler.get_id_by_device_moid(
                server['DeviceMoId']
            )

        if self.settings['workflow'] is not None:
            server['WorkflowRunning'] = None
            server['WorkflowLast'] = None
            server['WorkflowsLast'] = []
            server['WorkflowsLastIds'] = []
            server['WorkflowsLastFailedIds'] = []

            self.get_last_workflows()
            latest_create_time = None
            if self.last_workflows is not None:
                for last_workflow in self.last_workflows:
                    if self.workflow.is_server_workflow(server['Moid'], last_workflow):
                        workflow_info = self.workflow.get_workflow_info(last_workflow)
                        if workflow_info['Running']:
                            server['WorkflowRunning'] = workflow_info
                            continue

                        if latest_create_time is None or latest_create_time < workflow_info['CreateTimeEpoch']:
                            server['WorkflowLast'] = workflow_info
                            latest_create_time = workflow_info['CreateTimeEpoch']

                        server['WorkflowsLast'].append(workflow_info)
                        server['WorkflowsLastIds'].append(workflow_info['Moid'])

                        if not workflow_info['Running'] and not workflow_info['Completed']:
                            server['WorkflowsLastFailedIds'].append(workflow_info['Moid'])

                server['WorkflowsLast'] = sorted(server['WorkflowsLast'], key=lambda i: i['CreateTimeEpoch'], reverse=True)

        return server

    def get_state_flags(self, server):
        if server['OperPowerState'] == 'on':
            state = 'P+'
        else:
            state = 'P-'

        if server['AlarmSummary']['Warning'] == 0 and server['AlarmSummary']['Critical'] == 0:
            state = '%sH' % (state)
        if server['AlarmSummary']['Warning'] > 0 and server['AlarmSummary']['Critical'] == 0:
            state = '%sW' % (state)
        if server['AlarmSummary']['Critical'] > 0:
            state = '%sC' % (state)

        if server['Type'] == 'Rack':
            state = '%sR' % (state)
        else:
            state = '%sB' % (state)

        if server['ManagementMode'] == 'UCSM':
            state = '%sU' % (state)
        else:
            state = '%sS' % (state)

        if 'LocatorLedOn' in server and server['LocatorLedOn']:
            state = '%sL' % (state)

        if self.settings['workflow'] is not None:
            if server['WorkflowRunning'] is not None or len(server['WorkflowsLast']) > 0:
                state = '%s W' % (state)

                if server['WorkflowRunning'] is not None:
                    state = '%sR' % (state)

                if not server['WorkflowLast']['Completed']:
                    state = '%sF' % (state)
                else:
                    if len(server['WorkflowsLastFailedIds']) > 0:
                        state = '%sf' % (state)

                state = '%s%s' % (state, len(server['WorkflowsLastIds']))

        return state

    def add_rack_server_attributes(self, server):
        server = self.add_common_attributes(server)
        if server is None:
            return None

        server['Type'] = 'Rack'

        if self.settings['locator']:
            try:
                server['LocatorLedOn'] = self.locator_handler.get_locator_led(
                    server['LocatorLed']['Moid']
                )
            except BaseException:
                # self.my_output.error('LocatorLed state check failure')
                # self.my_output.default(traceback.format_exc())
                # self.my_output.default(json.dumps(server, indent=4))
                server['LocatorLedOn'] = False

        if self.settings['cpu']:
            server['CpuInfo'] = self.processor_unit_handler.get_processor_units_info()

        if self.settings['memory']:
            server['MemoryInfo'] = self.memory_unit_handler.get_memory_units_info()

        if self.settings['fan']:
            server['FanInfo'] = []
            for fan_module in server['Fanmodules']:
                server['FanInfo'].append(
                    self.fan_handler.get_fan_info(fan_module['Moid'])
                )
            server['FanInfo'] = sorted(server['FanInfo'], key=lambda i: i['Dn'])

            server['FanOn'] = 0
            for fan_module in server['Fanmodules']:
                if self.fan_handler.get_fan_state(fan_module['Moid']):
                    server['FanOn'] = server['FanOn'] + 1
            server['FanCount'] = len(server['Fanmodules'])
            server['FanSummary'] = '%s/%s' % (server['FanOn'], server['FanCount'])
            server['FanHealthy'] = True
            if server['FanOn'] < server['FanCount']:
                server['FanHealthy'] = False

        if self.settings['psu']:
            server['PsuInfo'] = []
            for psu in server['Psus']:
                server['PsuInfo'].append(
                    self.psu_handler.get_psu_info(psu['Moid'])
                )
            server['PsuInfo'] = sorted(server['PsuInfo'], key=lambda i: i['Dn'])

            server['PsuOn'] = 0
            for psu in server['Psus']:
                if self.psu_handler.get_psu_state(psu['Moid']):
                    server['PsuOn'] = server['PsuOn'] + 1
            server['PsuCount'] = len(server['Psus'])
            server['PsuSummary'] = '%s/%s' % (server['PsuOn'], server['PsuCount'])
            server['PsuHealthy'] = True
            if server['PsuOn'] < server['PsuCount']:
                server['PsuHealthy'] = False

        if self.settings['pci']:
            server['PciDevicesInfo'] = []
            for server_pci_device in server['PciDevices']:
                server['PciDevicesInfo'].append(
                    self.pci_handler.get_pci_info(server_pci_device['Moid'])
                )
            server['PciDevicesInfo'] = sorted(server['PciDevicesInfo'], key=lambda i: i['Dn'])

            server['PciModels'] = []
            for server_pci_device in server['PciDevices']:
                server['PciModels'].append(
                    self.pci_handler.get_pci_model(server_pci_device['Moid'])
                )

        if self.settings['fw']:
            server['Fw'] = self.running_firmware_handler.get_registered_device_system_version(server['DeviceMoId'])

        if self.settings['storage']:
            server['StorageControllersInfo'] = self.storage_controller_handler.get_board_storage_controllers_info(server['Board']['Moid'])
            if server['StorageControllersInfo'] is None:
                server['StorageControllersCount'] = 0
            else:
                server['StorageControllersCount'] = len(server['StorageControllersInfo'])

            server['VirtualDisks'] = self.storage_virtual_drive_handler.get_virtual_drives_info(
                server['Board']['Moid'],
                storage_controllers_info=server['StorageControllersInfo']
            )
            server['VirtualDiskCount'] = self.storage_virtual_drive_handler.get_virtual_drives_count(
                server['Board']['Moid']
            )
            server['VirtualDiskCapacity'] = self.storage_virtual_drive_handler.get_virtual_drives_size(
                server['Board']['Moid']
            )
            server['VirtualDiskCapacityUnit'] = self.info_handler.convert_storage(server['VirtualDiskCapacity'])

            server['HddDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
                server['Board']['Moid'],
                disk_type='HDD',
                virtual_drives_info=server['VirtualDisks'],
                storage_controllers_info=server['StorageControllersInfo']
            )
            server['HddDiskCount'] = self.storage_physical_disk_handler.get_compute_disks_count(
                server['Board']['Moid'],
                disk_type='HDD'
            )
            server['HddDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
                server['Board']['Moid'],
                disk_type='HDD'
            )
            server['HddDiskCapacityUnit'] = self.info_handler.convert_storage(server['HddDiskCapacity'])

            server['SsdDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
                server['Board']['Moid'],
                disk_type='SSD',
                virtual_drives_info=server['VirtualDisks'],
                storage_controllers_info=server['StorageControllersInfo']
            )
            server['SsdDiskCount'] = self.storage_physical_disk_handler.get_compute_disks_count(
                server['Board']['Moid'],
                disk_type='SSD'
            )
            server['SsdDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
                server['Board']['Moid'],
                disk_type='SSD'
            )
            server['SsdDiskCapacityUnit'] = self.info_handler.convert_storage(server['SsdDiskCapacity'])

            server['PhysicalDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
                server['Board']['Moid'],
                virtual_drives_info=server['VirtualDisks'],
                storage_controllers_info=server['StorageControllersInfo']
            )
            server['PhysicalDiskCount'] = self.storage_physical_disk_handler.get_compute_disks_count(
                server['Board']['Moid']
            )
            server['PhysicalDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
                server['Board']['Moid']
            )
            server['PhysicalDiskCapacityUnit'] = self.info_handler.convert_storage(server['PhysicalDiskCapacity'])

            server['StorageDrives'] = '%sC %sH %sS %sVD' % (
                server['StorageControllersCount'],
                server['HddDiskCount'],
                server['SsdDiskCount'],
                server['VirtualDiskCount']
            )

            server['StorageCapacity'] = 'R %s , VD %s' % (
                server['PhysicalDiskCapacityUnit'],
                server['VirtualDiskCapacityUnit']
            )

            server['StorageSummary'] = '%sC %sH %sS %sVD R%s L%s' % (
                server['StorageControllersCount'],
                server['HddDiskCount'],
                server['SsdDiskCount'],
                server['VirtualDiskCount'],
                server['PhysicalDiskCapacityUnit'],
                server['VirtualDiskCapacityUnit']
            )

        server['State'] = self.get_state_flags(server)

        return server

    def add_blade_server_attributes(self, server):
        server = self.add_common_attributes(server)
        if server is None:
            return None

        server['Type'] = 'Blade'

        if self.settings['locator']:
            server['LocatorLedOn'] = False

        if self.settings['fan']:
            server['FanSummary'] = ''
            server['FanHealthy'] = True

        if self.settings['psu']:
            server['PsuSummary'] = ''
            server['PsuHealthy'] = True

        if self.settings['pci']:
            server['PciModels'] = []

        if self.settings['fw']:
            server['Fw'] = self.running_firmware_handler.get_registered_device_system_version(server['DeviceMoId'])

        if self.settings['storage']:
            server['StorageControllersCount'] = 0
            server['HddDiskCount'] = 0
            server['HddDiskCapacity'] = 0
            server['SsdDiskCount'] = 0
            server['SsdDiskCapacity'] = 0
            server['PhysicalDiskCount'] = 0
            server['PhysicalDiskCapacity'] = 0
            server['PhysicalDiskCapacityUnit'] = 0
            server['VirtualDiskCount'] = 0
            server['VirtualDiskCapacity'] = 0
            server['VirtualDiskCapacityUnit'] = 0
            server['StorageDrives'] = '%sC %sH %sS %sVD' % (
                server['StorageControllersCount'],
                server['HddDiskCount'],
                server['SsdDiskCount'],
                server['VirtualDiskCount']
            )
            server['StorageCapacity'] = 'R %s , VD %s' % (
                server['PhysicalDiskCapacityUnit'],
                server['VirtualDiskCapacityUnit']
            )
            server['StorageSummary'] = '%sC %sH %sS %sVD R%s L%s' % (
                server['StorageControllersCount'],
                server['HddDiskCount'],
                server['SsdDiskCount'],
                server['VirtualDiskCount'],
                server['PhysicalDiskCapacityUnit'],
                server['VirtualDiskCapacityUnit']
            )

        server['State'] = self.get_state_flags(server)

        return server

    def add_server_attributes(self, server):
        if server is None:
            return None

        if server['ObjectType'] == 'compute.RackUnit':
            return self.add_rack_server_attributes(server)

        if server['ObjectType'] == 'compute.Blade':
            return self.add_blade_server_attributes(server)

        return None
