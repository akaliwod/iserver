import re
import traceback

from lib.intersight_common import IntersightCommon


class StorageController(IntersightCommon):
    """Class for intersight storage controller objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
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
        "BackupBatteryUnit": null,
        "ClassId": "storage.Controller",
        "ComputeBlade": null,
        "ComputeBoard": {
            "ClassId": "mo.MoRef",
            "Moid": "6311ac4676752d31398e5331",
            "ObjectType": "compute.Board",
            "link": "https://www.intersight.com/api/v1/compute/Boards/6311ac4676752d31398e5331"
        },
        "ComputeRackUnit": null,
        "ConnectedSasExpander": false,
        "ControllerFlags": "driveSecurityCapable",
        "ControllerId": "1",
        "ControllerStatus": "optimal",
        "CreateTime": "2022-09-02T07:26:18.427Z",
        "DefaultDriveMode": "",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "DiskGroup": [],
        "DiskSlot": [],
        "DisplayNames": {
            "hierarchical": [
            "controller-1"
            ],
            "short": [
            "Controller-1"
            ]
        },
        "Dn": "sys/rack-unit-3/board/storage-SAS-1",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "EccBucketLeakRate": 0,
        "ForeignConfigPresent": false,
        "HwRevision": "C0",
        "InterfaceType": "",
        "InventoryDeviceInfo": null,
        "MaxVolumesSupported": 0,
        "MemoryCorrectableErrors": 0,
        "ModTime": "2022-09-02T07:41:09.15Z",
        "Model": "LSI MegaRAID SAS 3108",
        "Moid": "6311b01a76752d31398ef2c4",
        "Name": "",
        "ObjectType": "storage.Controller",
        "OobInterfaceSupported": "yes",
        "OperState": "unknown",
        "Operability": "operable",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "61c35fa36f72612d3005590c"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "6311ac4676752d31398e5331",
            "ObjectType": "compute.Board",
            "link": "https://www.intersight.com/api/v1/compute/Boards/6311ac4676752d31398e5331"
        },
        "PciAddr": "04:00.0",
        "PciSlot": "HBA",
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
        "PersistentCacheSize": 0,
        "PhysicalDiskExtensions": [],
        "PhysicalDisks": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6311b01a76752d31398ef2cc",
                "ObjectType": "storage.PhysicalDisk",
                "link": "https://www.intersight.com/api/v1/storage/PhysicalDisks/6311b01a76752d31398ef2cc"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "6311b01a76752d31398ef2d2",
                "ObjectType": "storage.PhysicalDisk",
                "link": "https://www.intersight.com/api/v1/storage/PhysicalDisks/6311b01a76752d31398ef2d2"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "6311b01a76752d31398ef2d6",
                "ObjectType": "storage.PhysicalDisk",
                "link": "https://www.intersight.com/api/v1/storage/PhysicalDisks/6311b01a76752d31398ef2d6"
            }
        ],
        "PinnedCacheState": 0,
        "Presence": "equipped",
        "PreviousFru": null,
        "RaidSupport": "RAID0, RAID1, RAID5, RAID10, RAID50",
        "RebuildRate": "30",
        "RebuildRatePercent": 0,
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
                "Moid": "6311b01a76752d31398ef2c8",
                "ObjectType": "firmware.RunningFirmware",
                "link": "https://www.intersight.com/api/v1/firmware/RunningFirmwares/6311b01a76752d31398ef2c8"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "6311b01a76752d31398ef2ca",
                "ObjectType": "firmware.RunningFirmware",
                "link": "https://www.intersight.com/api/v1/firmware/RunningFirmwares/6311b01a76752d31398ef2ca"
            }
        ],
        "SelfEncryptEnabled": "",
        "Serial": "SK61026231",
        "SharedScope": "",
        "SubOemId": "",
        "SupportedStripSizes": "",
        "Tags": [],
        "TotalCacheSize": 0,
        "Type": "SAS",
        "Vendor": "LSI Corp.",
        "VirtualDriveExtensions": [],
        "VirtualDrives": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6311b01a76752d31398ef2f6",
                "ObjectType": "storage.VirtualDrive",
                "link": "https://www.intersight.com/api/v1/storage/VirtualDrives/6311b01a76752d31398ef2f6"
            }
        ]
        }
    """
    def __init__(self, iaccount):
        self.iobject = 'storage controller'
        IntersightCommon.__init__(self, iaccount, self.iobject)

    def get_board_storage_controllers(self, board_id, cache=True):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        controllers = []

        for item in self.cache:
            if item['ComputeBoard']['Moid'] == board_id:
                controllers.append(item)

        return controllers

    def get_board_storage_controllers_info(self, board_id, cache=True):
        controllers = self.get_board_storage_controllers(board_id, cache=cache)
        if controllers is None:
            return None

        controllers_info = []
        for controller in controllers:
            controller_info = {}
            for key in ['Model', 'Moid', 'Vendor', 'Serial', 'Presence', 'PciSlot', 'ControllerId', 'Dn', 'RaidSupport']:
                controller_info[key] = controller[key]

            controller_info['PhysicalDiskCount'] = len(controller['PhysicalDisks'])
            controller_info['PhysicalDiskIds'] = []
            for physical_disk in controller['PhysicalDisks']:
                controller_info['PhysicalDiskIds'].append(physical_disk['Moid'])

            controller_info['VirtualDriveCount'] = len(controller['VirtualDrives'])
            controller_info['VirtualDriveIds'] = []
            for virtual_drive in controller['VirtualDrives']:
                controller_info['VirtualDriveIds'].append(virtual_drive['Moid'])

            controllers_info.append(controller_info)

            # "RunningFirmware": [
            #     {
            #         "ClassId": "mo.MoRef",
            #         "Moid": "5fdf9c2c6176752d35e457d8",
            #         "ObjectType": "firmware.RunningFirmware",
            #         "link": "https://www.intersight.com/api/v1/firmware/RunningFirmwares/5fdf9c2c6176752d35e457d8"
            #     },
            #     {
            #         "ClassId": "mo.MoRef",
            #         "Moid": "5fdf9c866176752d35e47722",
            #         "ObjectType": "firmware.RunningFirmware",
            #         "link": "https://www.intersight.com/api/v1/firmware/RunningFirmwares/5fdf9c866176752d35e47722"
            #     }
            # ],

        return controllers_info
