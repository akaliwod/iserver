from lib.intersight_common import IntersightCommon


class EquipmentFanModule(IntersightCommon):
    """Class for intersight equipment led objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6311aae876752d31398e1a50",
                "ObjectType": "compute.RackUnit",
                "link": "https://www.intersight.com/api/v1/compute/RackUnits/6311aae876752d31398e1a50"
            }
        ],
        "ClassId": "equipment.FanModule",
        "ComputeRackUnit": {
            "ClassId": "mo.MoRef",
            "Moid": "6311aae876752d31398e1a50",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/6311aae876752d31398e1a50"
        },
        "CreateTime": "2022-09-02T07:10:59.837Z",
        "Description": "",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Dn": "sys/rack-unit-3/fan-module-1-3",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "EquipmentChassis": null,
        "EquipmentExpanderModule": null,
        "EquipmentIoCard": null,
        "EquipmentRackEnclosure": null,
        "Fans": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6311ac8376752d31398e5c97",
                "ObjectType": "equipment.Fan",
                "link": "https://www.intersight.com/api/v1/equipment/Fans/6311ac8376752d31398e5c97"
            }
        ],
        "InventoryDeviceInfo": null,
        "ModTime": "2022-09-02T07:12:59.708Z",
        "Model": "",
        "ModuleId": 3,
        "Moid": "6311ac8376752d31398e5c95",
        "NetworkElement": null,
        "ObjectType": "equipment.FanModule",
        "OperReason": [],
        "OperState": "operable",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "61c35fa36f72612d3005590c"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "6311aae876752d31398e1a50",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/6311aae876752d31398e1a50"
        },
        "PartNumber": "",
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
        "Pid": "",
        "Presence": "equipped",
        "PreviousFru": null,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "61c35fa36f72612d3005590c",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c"
        },
        "Revision": "0",
        "Rn": "",
        "Serial": "N/A",
        "SharedScope": "",
        "Sku": "",
        "Tags": [],
        "TrayId": 0,
        "Vendor": "N/A",
        "Vid": ""
    }
    """
    def __init__(self, iaccount, get_filter=None):
        self.iobject = 'equipment fanmodule'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter)

    def is_fan_on(self, item):
        if item is None:
            return False

        if item['Presence'] == 'equipped' and item['OperState'] == 'operable':
            return True

        return False

    def get_all(self, max_errors=3, error_timeout=1):
        items = IntersightCommon.get_all(self, max_errors=max_errors, error_timeout=error_timeout)
        if items is not None:
            for item in items:
                item['On'] = self.is_fan_on(item)

        return items

    def get_fan_state(self, moid, cache=True):
        if not cache:
            return self.is_fan_on(self.get_moid(moid))
        return self.is_fan_on(self.get_cache_moid(moid))

    def get_fan_info(self, moid, cache=True):
        if cache:
            fan_device = self.get_cache_moid(moid)
        else:
            fan_device = self.get_moid(moid)

        if fan_device is None:
            return None

        info = {}
        for key in ['ModuleId', 'OperState', 'Presence', 'Dn']:
            info[key] = fan_device[key]

        return info
