from re import I
from lib import storage_physical_disk_usage
from lib.intersight_common import IntersightCommon


class StorageVirtualDrive(IntersightCommon):
    """Class for intersight storage virtual drive objects
    {
        "AccessPolicy": "read-write",
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "ActualWriteCachePolicy": "write-through",
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
        "AvailableSize": "0",
        "BlockSize": "512",
        "Bootable": "true",
        "ClassId": "storage.VirtualDrive",
        "ConfigState": "orphaned",
        "ConfiguredWriteCachePolicy": "write-through",
        "ConnectionProtocol": "unspecified",
        "CreateTime": "2022-09-02T07:26:18.446Z",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "DiskGroup": null,
        "DisplayNames": {
            "hierarchical": [
            "virtualDrive-RAID10_3456"
            ],
            "short": [
            "VirtualDrive-RAID10_3456"
            ]
        },
        "Dn": "sys/rack-unit-3/board/storage-SAS-1/vd-0",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "DriveCache": "no-change",
        "DriveSecurity": "no",
        "DriveState": "optimal",
        "InventoryDeviceInfo": null,
        "IoPolicy": "direct",
        "ModTime": "2022-09-02T07:41:09.149Z",
        "Model": "",
        "Moid": "6311b01a76752d31398ef2f6",
        "Name": "RAID10_3456",
        "NumBlocks": "388624384",
        "ObjectType": "storage.VirtualDrive",
        "OperState": "undefined",
        "Operability": "operable",
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
        "PhysicalBlockSize": "unknown",
        "PhysicalDiskUsages": [],
        "Presence": "equipped",
        "PreviousFru": null,
        "ReadPolicy": "normal",
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "61c35fa36f72612d3005590c",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c"
        },
        "Revision": "0",
        "Rn": "",
        "SecurityFlags": "",
        "Serial": "",
        "SharedScope": "",
        "Size": "2286910",
        "StorageController": {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2c4",
            "ObjectType": "storage.Controller",
            "link": "https://www.intersight.com/api/v1/storage/Controllers/6311b01a76752d31398ef2c4"
        },
        "StorageVirtualDriveContainer": null,
        "StripSize": "64",
        "Tags": [],
        "Type": "mirror-stripe",
        "Uuid": "41b43588-6ba3-4849-8dca-2a0420468108",
        "VdMemberEps": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef305",
            "ObjectType": "storage.VdMemberEp",
            "link": "https://www.intersight.com/api/v1/storage/VdMemberEps/6311b01a76752d31398ef305"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef309",
            "ObjectType": "storage.VdMemberEp",
            "link": "https://www.intersight.com/api/v1/storage/VdMemberEps/6311b01a76752d31398ef309"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef30b",
            "ObjectType": "storage.VdMemberEp",
            "link": "https://www.intersight.com/api/v1/storage/VdMemberEps/6311b01a76752d31398ef30b"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef30d",
            "ObjectType": "storage.VdMemberEp",
            "link": "https://www.intersight.com/api/v1/storage/VdMemberEps/6311b01a76752d31398ef30d"
            }
        ],
        "Vendor": "",
        "VendorUuid": "678da6e7-15d5-7460-23fe-a8c7196781e6",
        "VirtualDriveExtension": null,
        "VirtualDriveId": "0"
    }
    """
    def __init__(self, iaccount):
        self.iobject = 'storage virtualdrive'
        IntersightCommon.__init__(self, iaccount, self.iobject)

    def get_virtual_drives(self, board_id, cache=True):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        disks = []

        for item in self.cache:
            match = False
            for ancestor in item['Ancestors']:
                if ancestor['ObjectType'] == 'compute.Board' and ancestor['Moid'] == board_id:
                    match = True
                    break

            if match:
                disks.append(item)

        return disks

    def get_virtual_drives_count(self, board_id):
        disks = self.get_virtual_drives(board_id)
        if disks is None:
            return 0
        return len(disks)

    def get_virtual_drives_size(self, board_id):
        disks = self.get_virtual_drives(board_id)
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

    def get_virtual_drives_info(self, board_id, storage_controllers_info=None):
        virtual_drives = self.get_virtual_drives(board_id)
        if virtual_drives is None:
            return None

        virtual_drives_info = []
        for virtual_drive in virtual_drives:
            virtual_drive_info = {}

            for key in ['Moid', 'Name', 'Dn', 'Size', 'Type', 'VirtualDriveId']:
                virtual_drive_info[key] = virtual_drive[key]

            virtual_drive_info['PhysicalDiskCount'] = len(virtual_drive['PhysicalDiskUsages'])

            virtual_drive_info['StorageControllerId'] = None
            if storage_controllers_info is not None:
                for storage_controller_info in storage_controllers_info:
                    if virtual_drive_info['Moid'] in storage_controller_info['VirtualDriveIds']:
                        virtual_drive_info['StorageControllerId'] = storage_controller_info['ControllerId']

            virtual_drives_info.append(virtual_drive_info)

        virtual_drives_info = sorted(virtual_drives_info, key=lambda i: i['Dn'])

        for virtual_drive_info in virtual_drives_info:
            virtual_drive_info['PhysicalDiskIds'] = []
            if virtual_drive_info['PhysicalDiskCount'] > 0:
                storage_physical_disk_usage_handler = storage_physical_disk_usage.StoragePhysicalDiskUsage(self.iaccount)
                storage_physical_disk_usage_handler.set_get_filter("StorageVirtualDrive/Moid eq '%s'" % (virtual_drive_info['Moid']))
                disk_usages = storage_physical_disk_usage_handler.get_all()
                if disk_usages is not None:
                    for disk_usage in disk_usages:
                        virtual_drive_info['PhysicalDiskIds'].append(disk_usage['PhysicalDrive'])

        return virtual_drives_info
