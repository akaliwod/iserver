from lib.intersight.intersight_common import IntersightCommon


class EquipmentPsu(IntersightCommon):
    """Class for intersight equipment led objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5efdfb9d6176752d3559bb60",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/5efdfb9d6176752d3559bb60"
            }
        ],
        "ClassId": "equipment.Psu",
        "ComputeRackUnit": null,
        "CreateTime": "2020-07-02T15:22:12.078Z",
        "Description": "",
        "DeviceMoId": "5efdfb7e6f72612d30e4501e",
        "Dn": "sys/chassis-1/psu-4",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "EquipmentChassis": {
            "ClassId": "mo.MoRef",
            "Moid": "5efdfb9d6176752d3559bb60",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/5efdfb9d6176752d3559bb60"
        },
        "EquipmentFex": null,
        "EquipmentRackEnclosure": null,
        "InventoryDeviceInfo": null,
        "ModTime": "2021-06-11T06:52:19.353Z",
        "Model": "PS-2112-9S-LF",
        "Moid": "5efdfba46176752d3559be1a",
        "Name": "",
        "NetworkElement": null,
        "ObjectType": "equipment.Psu",
        "OperReason": [],
            "ClassId": "mo.MoRef",
            "Moid": "62614bdd6f72612d3331038b",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/62614bdd6f72612d3331038b"
        },
        "Revision": "",
        "Rn": "",
        "Serial": "LIT21182DMM",
        "SharedScope": "",
        "Sku": "",
        "Tags": [],
        "Vendor": "Cisco Systems Inc",
        "Vid": "",
        "Voltage": ""
    }
    """
    def __init__(self, iaccount):
        self.iobject = 'equipment psu'
        IntersightCommon.__init__(self, iaccount, self.iobject)

    def is_psu_on(self, item):
        if item is None:
            return False

        if item['Voltage'] == 'ok':
            return True

        try:
            if int(item['Voltage']) > 0:
                return True
        except BaseException:
            pass

        return False

    def get_all(self, max_errors=3, error_timeout=1):
        items = IntersightCommon.get_all(self, max_errors=max_errors, error_timeout=error_timeout)
        if items is not None:
            for item in items:
                item['On'] = self.is_psu_on(item)

        return items

    def get_psu_state(self, moid, cache=True):
        if not cache:
            return self.is_psu_on(self.get(moid))
        return self.is_psu_on(self.get_cache_moid(moid))

    def get_psu_info(self, moid, cache=True):
        if cache:
            psu_device = self.get_cache_moid(moid)
        else:
            psu_device = self.get(moid)

        if psu_device is None:
            return None

        info = {}
        for key in ['Moid', 'Name', 'Model', 'Serial', 'Vendor', 'Dn', 'Model', 'Vendor', 'On', 'Voltage']:
            info[key] = psu_device[key]

        return info
