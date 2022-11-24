from lib import ip_helper
from lib.intersight.intersight_common import IntersightCommon


class EquipmentIoCard(IntersightCommon):
    """Class for intersight equipment io card objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13c876752d32362fc175",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13c876752d32362fc175"
            }
        ],
        "ClassId": "equipment.IoCard",
        "ConnectionPath": "A",
        "ConnectionStatus": "A",
        "CreateTime": "2022-09-21T13:38:16.424Z",
        "DcSupported": true,
        "Description": "Cisco UCS 9108-25G 8 Port IFM",
        "DeviceMoId": "632999466f72612d39b26942",
        "Dn": "chassis-1-ioc-2",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "EquipmentChassis": {
            "ClassId": "mo.MoRef",
            "Moid": "632b13c876752d32362fc175",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13c876752d32362fc175"
        },
        "EquipmentFex": null,
        "FanModules": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b15b576752d3236304d3d",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/632b15b576752d3236304d3d"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b15b576752d3236304d58",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/632b15b576752d3236304d58"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b15b576752d3236304d6f",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/632b15b576752d3236304d6f"
            }
        ],
        "HostPorts": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad6",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad6"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac0",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac0"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5acc",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5acc"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5abf",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5abf"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac6",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac6"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac7",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac7"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad4",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad4"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad8",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad8"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac1",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac1"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac4",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac4"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5acf",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5acf"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad2",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad2"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad3",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad3"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac9",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac9"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad5",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad5"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5adb",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5adb"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac2",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac2"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac8",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac8"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5add",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5add"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5aca",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5aca"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5acb",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5acb"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5acd",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5acd"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ace",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ace"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac5",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac5"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ac3",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac3"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad0",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad0"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5adc",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5adc"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad7",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad7"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5abe",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5abe"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad1",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad1"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ad9",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ad9"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b158c6373582d415a5ada",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ada"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c6acd6373582d415a8b96",
                "ObjectType": "ether.HostPort",
                "link": "https://www.intersight.com/api/v1/ether/HostPorts/632c6acd6373582d415a8b96"
            }
        ],
        "InbandIpAddresses": [
            {
                "Address": "10.90.90.48",
                "Category": "Equipment",
                "ClassId": "compute.IpAddress",
                "DefaultGateway": "10.90.89.1",
                "Dn": "",
                "HttpPort": 80,
                "HttpsPort": 443,
                "KvmPort": 2068,
                "KvmVlan": 89,
                "Name": "Inband",
                "ObjectType": "compute.IpAddress",
                "Subnet": "255.255.255.0",
                "Type": "MgmtInterface"
            }
        ],
        "InventoryDeviceInfo": null,
        "MgmtController": {
            "ClassId": "mo.MoRef",
            "Moid": "632b15b676752d3236304def",
            "ObjectType": "management.Controller",
            "link": "https://www.intersight.com/api/v1/management/Controllers/632b15b676752d3236304def"
        },
        "ModTime": "2022-10-14T10:35:57.125Z",
        "Model": "UCSX-I-9108-25G",
        "ModuleId": 2,
        "Moid": "632b13c876752d32362fc17c",
        "NetworkPorts": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13c876752d32362fc189",
                "ObjectType": "ether.NetworkPort",
                "link": "https://www.intersight.com/api/v1/ether/NetworkPorts/632b13c876752d32362fc189"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c81e776752d32369da82f",
                "ObjectType": "ether.NetworkPort",
                "link": "https://www.intersight.com/api/v1/ether/NetworkPorts/632c81e776752d32369da82f"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c81ed76752d32369daa9c",
                "ObjectType": "ether.NetworkPort",
                "link": "https://www.intersight.com/api/v1/ether/NetworkPorts/632c81ed76752d32369daa9c"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c81fe76752d32369db10a",
                "ObjectType": "ether.NetworkPort",
                "link": "https://www.intersight.com/api/v1/ether/NetworkPorts/632c81fe76752d32369db10a"
            }
        ],
        "ObjectType": "equipment.IoCard",
        "OperReason": [],
        "OperState": "OK",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "632b13c876752d32362fc175",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13c876752d32362fc175"
        },
        "PartNumber": "73-20533-03 ",
        "PermissionResources": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5ddee0c26972652d33555a3b",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/5ddee0c26972652d33555a3b"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "63493b8a6972652d33272ab6",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/63493b8a6972652d33272ab6"
            }
        ],
        "PhysicalDeviceRegistration": {
            "ClassId": "mo.MoRef",
            "Moid": "632b15886f72612d39c6702a",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632b15886f72612d39c6702a"
        },
        "Pid": "UCSX-I-9108-25G",
        "Presence": "equipped",
        "PreviousFru": null,
        "ProductName": "Cisco UCS 9108-25G",
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "Revision": "0",
        "Rn": "",
        "Serial": "FCH261770RN",
        "SharedScope": "",
        "Side": "bottom",
        "Sku": "UCSX-I-9108-25G",
        "Tags": [],
        "Vendor": "Cisco Systems Inc",
        "Version": "4.2(2c)",
        "Vid": "V01"
    }
    """
    def __init__(self, iaccount):
        self.iobject = 'equipment iocard'
        IntersightCommon.__init__(self, iaccount, self.iobject)

    def is_iocard_on(self, item):
        if item is None:
            return False

        if item['Presence'] == 'equipped' and item['OperState'] == 'OK':
            return True

        return False

    def get_all(self, max_errors=3, error_timeout=1):
        items = IntersightCommon.get_all(self, max_errors=max_errors, error_timeout=error_timeout)
        if items is not None:
            for item in items:
                item['On'] = self.is_iocard_on(item)

        return items

    def get_info(self, moid, cache=True):
        if cache:
            io_module = self.get_cache_moid(moid)
        else:
            io_module = self.get(moid)

        if io_module is None:
            return None

        info = {}
        info['Moid'] = io_module['Moid']
        info['Dn'] = io_module['Dn']
        info['Model'] = io_module['Model']
        info['ConnectionPath'] = io_module['ConnectionPath']
        info['ConnectionStatus'] = io_module['ConnectionStatus']
        info['Description'] = io_module['Description']
        info['ManagementIp'] = None
        info['ManagementSubnet'] = None
        info['ManagementPrefix'] = None
        info['ManagementCidr'] = None
        info['ManagementGateway'] = None
        info['ManagementVlan'] = None
        if io_module['InbandIpAddresses'] is not None:
            for inband in io_module['InbandIpAddresses']:
                if inband['ClassId'] == 'compute.IpAddress':
                    info['ManagementIp'] = inband['Address']
                    info['ManagementSubnet'] = inband['Subnet']
                    info['ManagementPrefix'] = ip_helper.netmask_to_prefix(
                        info['ManagementSubnet']
                    )
                    info['ManagementCidr'] = '%s/%s' % (
                        info['ManagementIp'],
                        info['ManagementPrefix']
                    )
                    info['ManagementGateway'] = inband['DefaultGateway']
                    info['ManagementVlan'] = inband['KvmVlan']

        info['FanMoids'] = []
        for fan in io_module['FanModules']:
            info['FanMoids'].append(fan['Moid'])

        info['HostPorts'] = []
        for port in io_module['HostPorts']:
            info['HostPorts'].append(port['Moid'])

        info['NetworkPorts'] = []
        for port in io_module['NetworkPorts']:
            info['NetworkPorts'].append(port['Moid'])

        info['NetworkPortMax'] = None
        if io_module['Model'] == 'UCSX-I-9108-25G':
            info['NetworkPortMax'] = 8

        info['Name'] = 'IFM #%s (%s)' % (
            io_module['ModuleId'],
            io_module['Side'].lower()
        )

        info['ModuleId'] = io_module['ModuleId']
        info['On'] = io_module['On']
        info['OperState'] = io_module['OperState']
        info['PartNumber'] = io_module['PartNumber'].strip()
        info['Pid'] = io_module['Pid']
        info['Presence'] = io_module['Presence']
        info['ProductName'] = io_module['ProductName']
        info['Serial'] = io_module['Serial']
        info['Side'] = io_module['Side']
        info['Version'] = io_module['Version']

        return info
