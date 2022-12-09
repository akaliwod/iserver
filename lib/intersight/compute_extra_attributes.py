import json
import traceback

from lib import info_helper

from lib.intersight import equipment_led
from lib.intersight import equipment_fan_module
from lib.intersight import equipment_psu
from lib.intersight import processor_unit
from lib.intersight import memory_unit
from lib.intersight import pci_device
from lib.intersight import running_firmware
from lib.intersight import storage_physical_disk
from lib.intersight import storage_virtual_drive
from lib.intersight import storage_controller
from lib.intersight import compute_server_setting
from lib.intersight import workflow
from lib.intersight import asset_device_registration

from lib.redfish import endpoint_settings as redfish_endpoint_settings
from lib.ucsm import endpoint_settings as ucsm_endpoint_settings
from lib import my_servers_helper
from lib import log_helper
from lib import output_helper


class ComputeExtraAttributes():
    """Class for rack/blade compute object extra attributes
    """
    def __init__(self, iaccount, settings, log_id=None):
        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)

        self.settings = settings
        self.my_servers_handler = my_servers_helper.MyServers()
        self.my_servers_serials = self.my_servers_handler.get_serials()
        self.info_handler = info_helper.InfoHelper(log_id=log_id)
        self.locator_handler = equipment_led.EquipmentLed(iaccount, log_id=log_id)
        self.processor_unit_handler = processor_unit.ProcessorUnit(iaccount, log_id=log_id)
        self.memory_unit_handler = memory_unit.MemoryUnit(iaccount, log_id=log_id)
        self.fan_handler = equipment_fan_module.EquipmentFanModule(iaccount, log_id=log_id)
        self.psu_handler = equipment_psu.EquipmentPsu(iaccount, log_id=log_id)
        self.pci_handler = pci_device.PciDevice(iaccount, log_id=log_id)
        running_firmware_filter = '"Component eq \'system\' and Type eq \'blade-controller\'"'
        self.running_firmware_handler = running_firmware.RunningFirmware(
            iaccount,
            get_filter=running_firmware_filter,
            log_id=log_id
        )
        self.storage_physical_disk_handler = storage_physical_disk.StoragePhysicalDisk(iaccount, log_id=log_id)
        self.storage_virtual_drive_handler = storage_virtual_drive.StorageVirtualDrive(iaccount, log_id=log_id)
        self.storage_controller_handler = storage_controller.StorageController(iaccount, log_id=log_id)
        self.compute_server_setting_handler = compute_server_setting.ComputeServerSetting(iaccount, log_id=log_id)
        self.asset_device_registration_handler = asset_device_registration.AssetDeviceContractInformation(iaccount, log_id=log_id)
        self.workflow = workflow.Workflow(iaccount, log_id=log_id)
        self.last_workflows = None

        self.redfish_endpoint_settings_handler = redfish_endpoint_settings.RedfishEndpointSettings(log_id=log_id)
        self.ucsm_endpoint_settings_handler = ucsm_endpoint_settings.UcsmEndpointSettings(log_id=log_id)

        self.server_info = {}

    def set_cache(self, key, moids, device_moids, registration_moids, board_moids, filter_length_threshold=20):
        moids_list = []
        for moid in moids:
            moids_list.append('\'%s\'' % (moid))
        moids_filter = ', '.join(moids_list)

        device_moids_list = []
        for device_moid in device_moids:
            device_moids_list.append('\'%s\'' % (device_moid))
        device_moids_filter = ', '.join(device_moids_list)

        registration_moids_list = []
        for registration_moid in registration_moids:
            registration_moids_list.append('\'%s\'' % (registration_moid))
        registration_moids_filter = ', '.join(registration_moids_list)

        board_moids_list = []
        for board_moid in board_moids:
            board_moids_list.append('\'%s\'' % (board_moid))
        board_moids_filter = ', '.join(board_moids_list)

        if key == 'asset_device_registration':
            if self.settings['registration']:
                if len(registration_moids_list) < filter_length_threshold:
                    self.asset_device_registration_handler.set_get_filter(
                        "Moid in (%s)" % (registration_moids_filter)
                    )
                cache = self.asset_device_registration_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'locator_led':
            if self.settings['locator']:
                cache = self.locator_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'workflow':
            if self.settings['workflow'] is not None:
                cache = self.workflow.get_last(
                    seconds=self.settings['workflow']
                )
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'fanmodule':
            if self.settings['fan']:
                if len(moids) < filter_length_threshold:
                    self.fan_handler.set_get_filter(
                        "Parent/Moid in (%s)" % (moids_filter)
                    )
                cache = self.fan_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'pci':
            if self.settings['pci']:
                if len(moids) < filter_length_threshold:
                    self.pci_handler.set_get_filter(
                        "Parent/Moid in (%s)" % (moids_filter)
                    )
                cache = self.pci_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'psu':
            if self.settings['psu']:
                if len(moids) < filter_length_threshold:
                    self.psu_handler.set_get_filter(
                        "Parent/Moid in (%s)" % (moids_filter)
                    )
                cache = self.psu_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'firmware':
            if self.settings['fw']:
                if len(device_moids) < filter_length_threshold:
                    self.running_firmware_handler.set_get_filter(
                        "RegisteredDevice/Moid in (%s)" % (device_moids_filter)
                    )
                cache = self.running_firmware_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'storage_controller':
            if self.settings['storage']:
                if len(board_moids_list) < filter_length_threshold:
                    self.storage_controller_handler.set_get_filter(
                        "Parent/Moid in (%s)" % (board_moids_filter)
                    )
                cache = self.storage_controller_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'virtual_drive':
            if self.settings['storage']:
                if len(registration_moids) < filter_length_threshold:
                    self.storage_virtual_drive_handler.set_get_filter(
                        "RegisteredDevice/Moid in (%s)" % (registration_moids_filter)
                    )
                cache = self.storage_virtual_drive_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        if key == 'physical_disk':
            if self.settings['storage']:
                if len(registration_moids) < filter_length_threshold:
                    self.storage_physical_disk_handler.set_get_filter(
                        "RegisteredDevice/Moid in (%s)" % (registration_moids_filter)
                    )
                cache = self.storage_physical_disk_handler.get_all()
                if cache is None:
                    return False
                return self.log.set_cache(key, cache)

        return True

    def add_state_flag(self):
        if self.server_info['OperPowerState'] == 'on':
            state = 'P+'
        else:
            state = 'P-'

        if self.server_info['AlarmSummary']['Warning'] == 0 and self.server_info['AlarmSummary']['Critical'] == 0:
            state = '%s H' % (state)
        if self.server_info['AlarmSummary']['Warning'] > 0 and self.server_info['AlarmSummary']['Critical'] == 0:
            state = '%s W(%s)' % (state, self.server_info['AlarmSummary']['Warning'])
        if self.server_info['AlarmSummary']['Critical'] > 0:
            state = '%s C(%s)' % (state, self.server_info['AlarmSummary']['Critical'])

        if self.server_info['LocatorLedOn']:
            state = '%s L' % (state)

        self.server_info['FlagState'] = state

    def add_management_flag(self):
        state = ''

        if self.server_info['Connected']:
            state = '%sC' % (state)
        else:
            state = '%sc' % (state)

        if self.server_info['UCSM']['Capable']:
            if self.server_info['UCSM']['Enabled']:
                state = '%sU' % (state)
            else:
                state = '%su' % (state)

        if self.server_info['Redfish']['Capable']:
            if self.server_info['Redfish']['Enabled']:
                state = '%sR' % (state)
            else:
                state = '%sr' % (state)

        if self.server_info['IMC']['Capable']:
            if self.server_info['IMC']['Enabled']:
                state = '%sI' % (state)
            else:
                state = '%si' % (state)

        self.server_info['FlagManagement'] = state

    def add_workflow_flag(self):
        state = ''
        if self.settings['workflow'] is not None:
            if self.server_info['Workflow']['Running'] is not None:
                state = '%sR' % (state)

            if len(self.server_info['Workflow']['Last']) > 0:
                latest = None
                failed = 0
                for workflow_info in self.server_info['Workflow']['Last']:
                    if workflow_info['Moid'] == self.server_info['Workflow']['LatestMoid']:
                        latest = workflow_info

                    if not workflow_info['Completed']:
                        failed = failed + 1

                if not latest['Completed']:
                    state = '%sF' % (state)

                if latest['Completed'] and failed > 0:
                    state = '%sf' % (state)

                state = '%s%s' % (state, len(self.server_info['Workflow']['Last']))

        self.server_info['FlagWorkflow'] = state

    def add_flags(self):
        self.add_state_flag()
        self.add_management_flag()
        self.add_workflow_flag()

    def add_cpu_info(self, server):
        keys = [
            'NumCpus',
            'NumCpuCores',
            'NumThreads'
        ]
        for key in keys:
            if key in keys:
                self.server_info[key] = server[key]
        self.server_info['Cpu'] = '%sS %sC %sT' % (
            server['NumCpus'],
            server['NumCpuCores'],
            server['NumThreads']
        )

    def add_memory_info(self, server):
        keys = [
            'AvailableMemory',
            'TotalMemory'
        ]
        for key in keys:
            if key in keys:
                self.server_info[key] = server[key]

        self.server_info['UsedMemory'] = self.server_info['TotalMemory'] - self.server_info['AvailableMemory']

        self.server_info['TotalMemoryUnit'] = self.info_handler.convert_memory(
            self.server_info['TotalMemory'] * 1024 * 1024,
            precision=0
        )

        self.server_info['TotalMemoryGB'] = int(
            self.server_info['TotalMemory'] / 1024
        )

        self.server_info['AvailableMemoryUnit'] = self.info_handler.convert_memory(
            self.server_info['AvailableMemory'] * 1024 * 1024,
            precision=0
        )

        self.server_info['AvailableMemoryGB'] = int(
            self.server_info['AvailableMemory'] / 1024
        )

        self.server_info['UsedMemoryUnit'] = self.info_handler.convert_memory(
            self.server_info['UsedMemory'] * 1024 * 1024,
            precision=0
        )

        self.server_info['UsedMemoryGB'] = int(
            self.server_info['UsedMemory'] / 1024
        )

        usage = int(self.server_info['UsedMemory'] * 100 / self.server_info['TotalMemory'])
        self.server_info['UsedMemoryPct'] = usage
        self.server_info['UsedMemoryPctUnit'] = '%s%%' % (usage)

    def get_management_ip(self, server):
        try:
            if 'KvmIpAddresses' in server:
                for kvm_ip in server['KvmIpAddresses']:
                    if kvm_ip['ClassId'] == 'compute.IpAddress':
                        return kvm_ip['Address']
        except BaseException:
            print(traceback.format_exc())
        return None

    def add_management_ip(self, server):
        self.server_info['ManagementIp'] = self.get_management_ip(server)

    def add_health(self, server):
        # Rack
        #
        # "AlarmSummary": {
        #     "ClassId": "compute.AlarmSummary",
        #     "Critical": 0,
        #     "ObjectType": "compute.AlarmSummary",
        #     "Warning": 1
        # },
        #
        # Blade
        #
        # "AlarmSummary": {
        #     "ClassId": "compute.AlarmSummary",
        #     "Critical": 9,
        #     "Health": "Critical",
        #     "Info": 0,
        #     "ObjectType": "compute.AlarmSummary",
        #     "Warning": 0
        # },
        self.server_info['AlarmSummary'] = {}
        for key in ['Critical', 'Warning', 'Info']:
            if key in server['AlarmSummary']:
                self.server_info['AlarmSummary'][key] = server['AlarmSummary'][key]

        self.server_info['Health'] = 'Healthy'

        if self.server_info['AlarmSummary']['Warning'] == 0 and self.server_info['AlarmSummary']['Critical'] == 0:
            if 'Info' in self.server_info['AlarmSummary'] and self.server_info['AlarmSummary']['Info'] > 0:
                self.server_info['Health'] = 'Healthy (%s)' % (
                    self.server_info['AlarmSummary']['Info']
                )

        if self.server_info['AlarmSummary']['Warning'] > 0 and self.server_info['AlarmSummary']['Critical'] == 0:
            self.server_info['Health'] = 'Warnings (%s)' % (
                self.server_info['AlarmSummary']['Warning']
            )

        if self.server_info['AlarmSummary']['Critical'] > 0:
            self.server_info['Health'] = 'Critical (%s)' % (
                self.server_info['AlarmSummary']['Critical']
            )

    def add_connected_state(self, server):
        if not self.settings['registration']:
            self.server_info['Connected'] = False
            return

        self.server_info['Connected'] = False
        device_registration_info = self.asset_device_registration_handler.get_info(
            server['RegisteredDevice']['Moid'],
            cache=False
        )
        if device_registration_info is None:
            self.log.debug(
                'add_connected_state',
                'Device registration info not found'
            )
        else:
            self.server_info['Connected'] = device_registration_info['Connected']

    def add_workflow_info(self):
        if self.settings['workflow'] is None:
            return

        self.server_info['Workflow'] = {}
        self.server_info['Workflow']['Running'] = None
        self.server_info['Workflow']['LatestMoid'] = None
        self.server_info['Workflow']['Last'] = []

        if self.last_workflows is None:
            self.last_workflows = self.workflow.get_last(
                seconds=self.settings['workflow']
            )
            if self.last_workflows is None:
                return

        latest_create_time = None
        for last_workflow in self.last_workflows:
            if self.workflow.is_server_workflow(self.server_info['Moid'], last_workflow):
                workflow_info = self.workflow.get_workflow_info(
                    last_workflow
                )
                if workflow_info['Running']:
                    self.server_info['Workflow']['Running'] = workflow_info
                    continue

                if latest_create_time is None or latest_create_time < workflow_info['CreateTimeEpoch']:
                    self.server_info['Workflow']['LatestMoid'] = workflow_info['Moid']
                    latest_create_time = workflow_info['CreateTimeEpoch']

                self.server_info['Workflow']['Last'].append(
                    workflow_info
                )

        self.server_info['Workflow']['Last'] = sorted(self.server_info['Workflow']['Last'], key=lambda i: i['CreateTimeEpoch'], reverse=True)

    def add_groups(self):
        self.server_info['Groups'] = ''
        if self.my_servers_serials is not None:
            if self.server_info['Serial'] in self.my_servers_serials:
                self.server_info['Groups'] = ','.join(
                    self.my_servers_serials[self.server_info['Serial']]
                )

    def add_management_options(self):
        self.server_info['Redfish'] = {}
        self.server_info['UCSM'] = {}
        self.server_info['IMC'] = {}

        if self.server_info['ManagementMode'] == 'UCSM':
            self.server_info['Redfish']['Capable'] = False
            self.server_info['Redfish']['Enabled'] = False
            self.server_info['UCSM']['Capable'] = True
            self.server_info['UCSM']['Enabled'] = self.ucsm_endpoint_settings_handler.is_ucsm_endpoint(
                self.server_info['Serial']
            )
            self.server_info['IMC']['Capable'] = False
            self.server_info['IMC']['Enabled'] = False

        else:
            self.server_info['Redfish']['Capable'] = True
            self.server_info['Redfish']['Enabled'] = self.redfish_endpoint_settings_handler.is_redfish_endpoint(
                self.server_info['Serial']
            )
            self.server_info['UCSM']['Capable'] = False
            self.server_info['UCSM']['Enabled'] = False
            self.server_info['IMC']['Capable'] = True
            self.server_info['IMC']['Enabled'] = False

    def add_power(self):
        if not self.settings['power']:
            return

        self.server_info['Power'] = None

        if self.server_info['Redfish']['Enabled']:
            self.server_info['Power'] = self.redfish_endpoint_settings_handler.get_redfish_endpoint_template(
                self.server_info['Serial'],
                'power'
            )

        if self.server_info['UCSM']['Enabled']:
            self.server_info['Power'] = self.ucsm_endpoint_settings_handler.get_ucsm_endpoint_template(
                self.server_info['Serial'],
                'power'
            )

    def add_thermal(self):
        if not self.settings['thermal']:
            return

        self.server_info['Thermal'] = None

        if self.server_info['Redfish']['Enabled']:
            if self.server_info['OperPowerState'] == 'on':
                self.server_info['Thermal'] = self.redfish_endpoint_settings_handler.get_redfish_endpoint_template(
                    self.server_info['Serial'],
                    'thermal'
                )

        if self.server_info['UCSM']['Enabled']:
            self.server_info['Thermal'] = self.ucsm_endpoint_settings_handler.get_ucsm_endpoint_template(
                self.server_info['Serial'],
                'thermal'
            )

    def add_setting_id(self):
        if self.settings['server_setting_id']:
            self.server_info['ServerSettingId'] = self.compute_server_setting_handler.get_id_by_device_moid(
                self.server_info['DeviceMoId']
            )

    def add_common_attributes(self, server):
        keys = [
            'Moid',
            'DeviceMoId',
            'Name',
            'Model',
            'Serial',
            'ManagementMode',
            'OperPowerState'
        ]
        for key in keys:
            self.server_info[key] = server[key]

        self.add_cpu_info(server)
        self.add_memory_info(server)
        self.add_management_ip(server)
        self.add_health(server)
        self.add_connected_state(server)
        self.add_workflow_info()
        self.add_groups()
        self.add_management_options()
        self.add_power()
        self.add_thermal()
        self.add_setting_id()

        if self.settings['cpu']:
            self.server_info['CpuInfo'] = self.processor_unit_handler.get_processor_units_info()

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

    def set_blade_compute_filter(self, server):
        self.processor_unit_handler.set_get_filter("ComputeBoard/Moid eq '%s'" % (server['Board']['Moid']))
        self.memory_unit_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        self.pci_handler.set_get_filter("Parent/Moid eq '%s'" % (server['Moid']))
        # self.fan_handler.set_get_filter("Parent/Moid eq '%s'" % (server['Moid']))
        # self.psu_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        # self.locator_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        self.running_firmware_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        self.storage_controller_handler.set_get_filter("Parent/Moid eq '%s'" % (server['Board']['Moid']))
        self.storage_physical_disk_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))
        self.storage_virtual_drive_handler.set_get_filter("RegisteredDevice/Moid eq '%s'" % (server['RegisteredDevice']['Moid']))

    def add_fan_info(self, server):
        self.server_info['FanInfo'] = []

        for fan_module in server['Fanmodules']:
            self.server_info['FanInfo'].append(
                self.fan_handler.get_fan_info(
                    fan_module['Moid']
                )
            )

        self.server_info['FanInfo'] = sorted(
            self.server_info['FanInfo'],
            key=lambda i: i['Dn']
        )

        self.server_info['FanOn'] = 0
        for fan_module in server['Fanmodules']:
            if self.fan_handler.get_fan_state(fan_module['Moid']):
                self.server_info['FanOn'] = self.server_info['FanOn'] + 1

        self.server_info['FanCount'] = len(server['Fanmodules'])
        self.server_info['FanSummary'] = '%s/%s' % (
            self.server_info['FanOn'],
            self.server_info['FanCount']
        )
        self.server_info['FanHealthy'] = True
        if self.server_info['FanOn'] < self.server_info['FanCount']:
            self.server_info['FanHealthy'] = False

    def add_psu_info(self, server):
        self.server_info['PsuInfo'] = []

        for psu in server['Psus']:
            self.server_info['PsuInfo'].append(
                self.psu_handler.get_psu_info(
                    psu['Moid']
                )
            )

        self.server_info['PsuInfo'] = sorted(self.server_info['PsuInfo'], key=lambda i: i['Dn'])

        self.server_info['PsuOn'] = 0
        for psu in server['Psus']:
            if self.psu_handler.get_psu_state(psu['Moid']):
                self.server_info['PsuOn'] = self.server_info['PsuOn'] + 1

        self.server_info['PsuCount'] = len(server['Psus'])
        self.server_info['PsuSummary'] = '%s/%s' % (
            self.server_info['PsuOn'],
            self.server_info['PsuCount']
        )
        self.server_info['PsuHealthy'] = True
        if self.server_info['PsuOn'] < self.server_info['PsuCount']:
            self.server_info['PsuHealthy'] = False

    def add_pci_info(self, server):
        self.server_info['PciDevicesInfo'] = []
        for server_pci_device in server['PciDevices']:
            self.server_info['PciDevicesInfo'].append(
                self.pci_handler.get_pci_info(
                    server_pci_device['Moid']
                )
            )
        self.server_info['PciDevicesInfo'] = sorted(self.server_info['PciDevicesInfo'], key=lambda i: i['Dn'])

        self.server_info['PciModels'] = []
        for server_pci_device in server['PciDevices']:
            self.server_info['PciModels'].append(
                self.pci_handler.get_pci_model(
                    server_pci_device['Moid']
                )
            )

    def add_rack_storage_controller_info(self, server):
        self.server_info['StorageControllersInfo'] = self.storage_controller_handler.get_board_storage_controllers_info(
            server['Board']['Moid']
        )

        if self.server_info['StorageControllersInfo'] is None:
            self.server_info['StorageControllersCount'] = 0
        else:
            self.server_info['StorageControllersCount'] = len(self.server_info['StorageControllersInfo'])

    def add_blade_storage_controller_info(self, server):
        self.server_info['StorageControllersInfo'] = self.storage_controller_handler.get_blade_storage_controllers_info(
            self.server_info['Moid']
        )
        if self.server_info['StorageControllersInfo'] is None:
            self.server_info['StorageControllersCount'] = 0
        else:
            self.server_info['StorageControllersCount'] = len(self.server_info['StorageControllersInfo'])

    def add_storage_virtual_disk_info(self, server_id):
        self.server_info['VirtualDisks'] = self.storage_virtual_drive_handler.get_virtual_drives_info(
            server_id,
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )

        self.server_info['VirtualDiskCount'] = self.storage_virtual_drive_handler.get_virtual_drives_count(
            server_id
        )

        self.server_info['VirtualDiskCapacity'] = self.storage_virtual_drive_handler.get_virtual_drives_size(
            server_id
        )
        self.server_info['VirtualDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['VirtualDiskCapacity']
        )

    def add_storage_hdd_info(self, server_id):
        self.server_info['HddDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
            server_id,
            disk_type='HDD',
            virtual_drives_info=self.server_info['VirtualDisks'],
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )
        self.server_info['HddDiskCount'] = self.storage_physical_disk_handler.get_compute_disks_count(
            server_id,
            disk_type='HDD'
        )
        self.server_info['HddDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
            server_id,
            disk_type='HDD'
        )
        self.server_info['HddDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['HddDiskCapacity']
        )

    def add_storage_ssd_info(self, server_id):
        self.server_info['SsdDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
            server_id,
            disk_type='SSD',
            virtual_drives_info=self.server_info['VirtualDisks'],
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )
        self.server_info['SsdDiskCount'] = self.storage_physical_disk_handler.get_compute_disks_count(
            server_id,
            disk_type='SSD'
        )
        self.server_info['SsdDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
            server_id,
            disk_type='SSD'
        )
        self.server_info['SsdDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['SsdDiskCapacity']
        )

    def add_storage_physical_disk_info(self, server_id):
        self.server_info['PhysicalDisks'] = self.storage_physical_disk_handler.get_compute_disks_info(
            server_id,
            virtual_drives_info=self.server_info['VirtualDisks'],
            storage_controllers_info=self.server_info['StorageControllersInfo']
        )
        self.server_info['PhysicalDiskCount'] = self.storage_physical_disk_handler.get_compute_disks_count(
            server_id
        )
        self.server_info['PhysicalDiskCapacity'] = self.storage_physical_disk_handler.get_compute_disks_size(
            server_id
        )
        self.server_info['PhysicalDiskCapacityUnit'] = self.info_handler.convert_storage(
            self.server_info['PhysicalDiskCapacity']
        )

    def add_storage_info(self, server):
        if self.server_info['Type'] == 'Rack':
            storage_server_id = server['Board']['Moid']
            self.add_rack_storage_controller_info(server)

        if self.server_info['Type'] == 'Blade':
            storage_server_id = server['Moid']
            self.add_blade_storage_controller_info(server)

        self.add_storage_virtual_disk_info(storage_server_id)
        self.add_storage_hdd_info(storage_server_id)
        self.add_storage_ssd_info(storage_server_id)
        self.add_storage_physical_disk_info(storage_server_id)

        self.server_info['StorageDrives'] = '%sC %sH %sS %sVD' % (
            self.server_info['StorageControllersCount'],
            self.server_info['HddDiskCount'],
            self.server_info['SsdDiskCount'],
            self.server_info['VirtualDiskCount']
        )

        self.server_info['StorageCapacity'] = 'R %s , VD %s' % (
            self.server_info['PhysicalDiskCapacityUnit'],
            self.server_info['VirtualDiskCapacityUnit']
        )

        self.server_info['StorageSummary'] = '%sC %sH %sS %sVD R%s L%s' % (
            self.server_info['StorageControllersCount'],
            self.server_info['HddDiskCount'],
            self.server_info['SsdDiskCount'],
            self.server_info['VirtualDiskCount'],
            self.server_info['PhysicalDiskCapacityUnit'],
            self.server_info['VirtualDiskCapacityUnit']
        )

    def add_rack_server_attributes(self, server):
        self.server_info['Type'] = 'Rack'
        self.server_info['TypeModel'] = '(R) %s' % (self.server_info['Model'])

        self.server_info['LocatorLedOn'] = False
        if self.settings['locator']:
            try:
                self.server_info['LocatorLedOn'] = self.locator_handler.get_locator_led(
                    server['LocatorLed']['Moid']
                )
            except BaseException:
                pass

        if self.settings['memory']:
            self.server_info['MemoryInfo'] = self.memory_unit_handler.get_memory_units_info()

        if self.settings['fan']:
            self.add_fan_info(server)

        if self.settings['psu']:
            self.add_psu_info(server)

        if self.settings['pci']:
            self.add_pci_info(server)

        if self.settings['fw']:
            self.server_info['Fw'] = self.running_firmware_handler.get_registered_device_system_version(server['DeviceMoId'])

        if self.settings['storage']:
            self.add_storage_info(server)

    def add_blade_server_attributes(self, server):
        self.server_info['Type'] = 'Blade'
        self.server_info['TypeModel'] = '(B) %s' % (server['Model'])
        self.server_info['LocatorLedOn'] = False

        if self.settings['memory']:
            chassis_memory_info = self.memory_unit_handler.get_memory_units_info()
            memory_info = []

            for item in chassis_memory_info:
                if item['ServerId'] == server['Moid']:
                    memory_info.append(item)

            self.server_info['MemoryInfo'] = memory_info

        if self.settings['fan']:
            self.server_info['FanSummary'] = ''
            self.server_info['FanHealthy'] = True

        if self.settings['psu']:
            self.server_info['PsuSummary'] = ''
            self.server_info['PsuHealthy'] = True

        if self.settings['pci']:
            self.add_pci_info(server)

        if self.settings['fw']:
            self.server_info['Fw'] = self.running_firmware_handler.get_registered_device_system_version(
                self.server_info['DeviceMoId']
            )

        if self.settings['storage']:
            self.add_storage_info(server)

    def get_server_info(self, server, include_object=False):
        if server is None:
            return None

        self.log.debug(
            'compute_info.get',
            json.dumps(server, indent=4)
        )
        self.server_info = {}
        if include_object:
            self.server_info['IntersightObject'] = server

        if server['ObjectType'] == 'compute.RackUnit':
            self.set_rack_compute_filter(server)
            self.add_common_attributes(server)
            self.add_rack_server_attributes(server)
            self.add_flags()

        if server['ObjectType'] == 'compute.Blade':
            self.set_blade_compute_filter(server)
            self.add_common_attributes(server)
            self.add_blade_server_attributes(server)
            self.add_flags()

        return self.server_info
