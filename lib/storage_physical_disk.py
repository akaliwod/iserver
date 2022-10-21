from lib.intersight_common import IntersightCommon


class StoragePhysicalDisk(IntersightCommon):
    """Class for intersight storage physical disk objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2c4",
            "ObjectType": "storage.Controller",
            "link": "https://www.intersight.com/api/v1/storage/Controllers/6311b01a76752d31398ef2c4"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311ac4676752d31398e5331",
            "ObjectType": "compute.Board",
            "link": "https://www.intersight.com/api/v1/compute/Boards/6311ac4676752d31398e5331"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311aae876752d31398e1a50",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/6311aae876752d31398e1a50"
            }
        ],
        "BackgroundOperations": "",
        "BlockSize": "512",
        "Bootable": "false",
        "ClassId": "storage.PhysicalDisk",
        "ConfigurationCheckpoint": "",
        "ConfigurationState": "not-applied",
        "CreateTime": "2022-09-02T07:26:18.436Z",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "DisabledForRemoval": false,
        "DiscoveredPath": "default",
        "DiskId": "3",
        "DiskState": "online",
        "DisplayNames": {
            "hierarchical": [
            "physicalDisk-3"
            ],
            "short": [
            "PhysicalDisk-3"
            ]
        },
        "Dn": "sys/rack-unit-3/board/storage-SAS-1/disk-3",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "DriveFirmware": "",
        "DriveState": "",
        "EncryptionStatus": "",
        "FailurePredicted": false,
        "FdeCapable": "",
        "HotSpareType": "",
        "IndicatorLed": "",
        "InventoryDeviceInfo": null,
        "LinkSpeed": "12-gbps",
        "LinkState": "unknown",
        "LocatorLed": {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2fd",
            "ObjectType": "equipment.LocatorLed",
            "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6311b01a76752d31398ef2fd"
        },
        "MaximumOperatingTemperature": 0,
        "MediaErrorCount": 0,
        "ModTime": "2022-09-02T07:41:09.148Z",
        "Model": "ST1200MM0088",
        "Moid": "6311b01a76752d31398ef2d6",
        "Name": "",
        "NonCoercedSizeBytes": 0,
        "NumBlocks": "2341795840",
        "ObjectType": "storage.PhysicalDisk",
        "OperPowerState": "active",
        "OperQualifierReason": "N/A",
        "Operability": "operable",
        "OperatingTemperature": 0,
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "61c35fa36f72612d3005590c"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2c4",
            "ObjectType": "storage.Controller",
            "link": "https://www.intersight.com/api/v1/storage/Controllers/6311b01a76752d31398ef2c4"
        },
        "PercentLifeLeft": 0,
        "PercentReservedCapacityConsumed": 0,
        "PerformancePercent": 0,
        "PermissionResources": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736972652d321d26b5",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "625706a06972652d3202a8f9",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6242d1016972652d32eda017",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
            }
        ],
        "PhysicalBlockSize": "512",
        "PhysicalDiskExtensions": [],
        "Pid": "",
        "PowerCycleCount": 0,
        "PowerOnHours": 0,
        "PowerOnHoursPercentage": 0,
        "PredictedMediaLifeLeftPercent": 0,
        "PredictiveFailureCount": 0,
        "Presence": "equipped",
        "PreviousFru": null,
        "Protocol": "SAS",
        "RawSize": "1144641",
        "ReadErrorCountThreshold": 0,
        "ReadIoErrorCount": 0,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "61c35fa36f72612d3005590c",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c"
        },
        "Revision": "0",
        "Rn": "",
        "RunningFirmware": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2d8",
            "ObjectType": "firmware.RunningFirmware",
            "link": "https://www.intersight.com/api/v1/firmware/RunningFirmwares/6311b01a76752d31398ef2d8"
            }
        ],
        "SasPorts": [],
        "Secured": "",
        "Serial": "S40222EH0000K701JJQ3",
        "SharedScope": "",
        "Size": "1143455",
        "StorageController": {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2c4",
            "ObjectType": "storage.Controller",
            "link": "https://www.intersight.com/api/v1/storage/Controllers/6311b01a76752d31398ef2c4"
        },
        "StorageEnclosure": null,
        "Tags": [],
        "Thermal": "unknown",
        "ThresholdOperatingTemperature": 0,
        "Type": "HDD",
        "VariantType": "default",
        "Vendor": "SEAGATE",
        "WearStatusInDays": 0,
        "WriteErrorCountThreshold": 0,
        "WriteIoErrorCount": 0
    }
    """
    def __init__(self, iaccount):
        self.iobject = 'storage physicaldisk'
        IntersightCommon.__init__(self, iaccount, self.iobject)

    def get_compute_disks(self, board_id, cache=True, disk_type=None):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        disks = []

        for item in self.cache:
            if disk_type is not None and item['Type'] != disk_type:
                continue

            match = False
            for ancestor in item['Ancestors']:
                if ancestor['ObjectType'] == 'compute.Board' and ancestor['Moid'] == board_id:
                    match = True
                    break

            if match:
                disks.append(item)

        return disks

    def get_compute_disks_count(self, board_id, disk_type=None):
        disks = self.get_compute_disks(board_id, disk_type=disk_type)
        if disks is None:
            return 0
        return len(disks)

    def get_compute_disks_size(self, board_id, disk_type=None):
        disks = self.get_compute_disks(board_id, disk_type=disk_type)
        if disks is None:
            return 0

        size = 0
        for disk in disks:
            if disk['Size'].endswith(' MB'):
                size = size + int(disk['Size'].split(' ')[0])
                continue

            size = size + int(disk['Size'])

        size = size * 1024 * 1024
        return size

    def get_compute_disks_info(self, board_id, disk_type=None, virtual_drives_info=None, storage_controllers_info=None):
        compute_disks = self.get_compute_disks(board_id, disk_type=disk_type)
        if compute_disks is None:
            return None

        compute_disks_info = []
        for compute_disk in compute_disks:
            compute_disk_info = {}

            for key in ['Moid', 'DiskId', 'DiskState', 'Dn', 'DriveFirmware', 'DriveState', 'LinkSpeed', 'Model', 'Pid', 'Presence', 'Serial', 'Size', 'Type', 'Vendor']:
                compute_disk_info[key] = compute_disk[key]

            compute_disk_info['VirtualDriveMoid'] = None
            compute_disk_info['VirtualDriveId'] = ''
            if virtual_drives_info is not None:
                for virtual_drive_info in virtual_drives_info:
                    if compute_disk['DiskId'] in virtual_drive_info['PhysicalDiskIds']:
                        compute_disk_info['VirtualDriveMoid'] = virtual_drive_info['Moid']
                        compute_disk_info['VirtualDriveId'] = virtual_drive_info['VirtualDriveId']

            compute_disk_info['StorageControllerId'] = ''
            if storage_controllers_info is not None:
                for storage_controller_info in storage_controllers_info:
                    if compute_disk['Moid'] in storage_controller_info['PhysicalDiskIds']:
                        compute_disk_info['StorageControllerId'] = storage_controller_info['ControllerId']

            compute_disks_info.append(compute_disk_info)

        compute_disks_info = sorted(compute_disks_info, key=lambda i: i['Dn'])

        return compute_disks_info
