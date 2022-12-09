from lib.intersight.intersight_common import IntersightCommon


class PciDevice(IntersightCommon):
    """Class for intersight pci device objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fe295aa6176752d35119a62",
                "ObjectType": "compute.RackUnit",
                "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fe295aa6176752d35119a62"
            }
        ],
        "ClassId": "pci.Device",
        "ComputeBlade": null,
        "ComputeRackUnit": {
            "ClassId": "mo.MoRef",
            "Moid": "5fe295aa6176752d35119a62",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fe295aa6176752d35119a62"
        },
        "CreateTime": "2020-12-23T00:57:54.621Z",
        "DeviceId": "",
        "DeviceMoId": "5fe295916f72612d306438ac",
        "Dn": "sys/rack-unit-1/equipped-slot-MLOM",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "FirmwareVersion": "4.4(1g)",
        "GraphicsCards": [],
        "InventoryDeviceInfo": null,
        "ModTime": "2022-06-13T09:25:04.527Z",
        "Model": "UCS VIC 1227 10Gbps 2 port CNA SFP+",
        "Moid": "5fe296126176752d3511c18a",
        "ObjectType": "pci.Device",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "5fe295916f72612d306438ac"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "5fe295aa6176752d35119a62",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fe295aa6176752d35119a62"
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
        "Pid": "UCSC-MLOM-CSC-02",
        "Presence": "",
        "PreviousFru": null,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "5fe295916f72612d306438ac",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fe295916f72612d306438ac"
        },
        "Revision": "",
        "Rn": "",
        "Serial": "",
        "SharedScope": "",
        "SlotId": "MLOM",
        "Tags": [],
        "Vendor": "0x1137"
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'pci device'
        self.cache_key = 'pci'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id, cache_key=self.cache_key)

    def get_pci_model(self, moid, cache=True):
        if cache:
            pci_device = self.get_cache_moid(moid)
        else:
            pci_device = self.get(moid)

        if pci_device is None:
            return None

        if pci_device['Pid'] not in [None, 'N/A', 'UNKNOWN', '']:
            return pci_device['Pid']

        return pci_device['Model']

    def get_pci_info(self, moid, cache=True):
        if cache:
            pci_device = self.get_cache_moid(moid)
        else:
            pci_device = self.get(moid)

        if pci_device is None:
            return None

        info = {}
        for key in ['Model', 'Pid', 'SlotId', 'Vendor', 'FirmwareVersion', 'Dn']:
            info[key] = pci_device[key]

        return info
