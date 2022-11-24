from lib.intersight.intersight_common import IntersightCommon


class EthernetNetworkPort(IntersightCommon):
    """Class for intersight ethernet network port objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "AcknowledgedPeerInterface": {
            "ClassId": "mo.MoRef",
            "Moid": "6329994b76752d3236cd98dd",
            "ObjectType": "ether.PhysicalPort",
            "link": "https://www.intersight.com/api/v1/ether/PhysicalPorts/6329994b76752d3236cd98dd"
        },
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13c876752d32362fc17c",
                "ObjectType": "equipment.IoCard",
                "link": "https://www.intersight.com/api/v1/equipment/IoCards/632b13c876752d32362fc17c"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13c876752d32362fc175",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13c876752d32362fc175"
            }
        ],
        "ClassId": "ether.NetworkPort",
        "CreateTime": "2022-09-22T15:40:29.432Z",
        "DeviceMoId": "632999466f72612d39b26942",
        "Dn": "chassis-1-ioc-2-slot-2-port-3",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "EquipmentIoCardBase": {
            "ClassId": "mo.MoRef",
            "Moid": "632b13c876752d32362fc17c",
            "ObjectType": "equipment.IoCard",
            "link": "https://www.intersight.com/api/v1/equipment/IoCards/632b13c876752d32362fc17c"
        },
        "ModTime": "2022-10-14T10:35:57.25Z",
        "ModuleId": 0,
        "Moid": "632c81ed76752d32369daa9c",
        "ObjectType": "ether.NetworkPort",
        "OperState": "up",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "632b13c876752d32362fc17c",
            "ObjectType": "equipment.IoCard",
            "link": "https://www.intersight.com/api/v1/equipment/IoCards/632b13c876752d32362fc17c"
        },
        "PeerDn": "",
        "PeerInterface": {
            "ClassId": "mo.MoRef",
            "Moid": "6329994b76752d3236cd98dd",
            "ObjectType": "ether.PhysicalPort",
            "link": "https://www.intersight.com/api/v1/ether/PhysicalPorts/6329994b76752d3236cd98dd"
        },
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
        "PortId": 3,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "Rn": "",
        "SharedScope": "",
        "SlotId": 2,
        "Speed": "10G",
        "SwitchId": "A",
        "Tags": []
    }
    """
    def __init__(self, iaccount, get_filter=None):
        self.iobject = 'ether networkport'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter)

    def get_info(self, moid, cache=True):
        if cache:
            network_port = self.get_cache_moid(moid)
        else:
            network_port = self.get(moid)

        if network_port is None:
            return None

        info = {}
        info['Moid'] = network_port['Moid']
        info['Dn'] = network_port['Dn']
        info['Name'] = '%s/%s' % (
            network_port['SlotId'],
            network_port['PortId']
        )

        info['IoModuleId'] = network_port['EquipmentIoCardBase']['Moid']
        info['ModuleId'] = network_port['ModuleId']
        info['OperState'] = network_port['OperState']
        info['Up'] = False
        if info['OperState'] == 'up':
            info['Up'] = True
        info['PeerDn'] = network_port['PeerDn']
        info['PeerInterfaceId'] = None
        info['PeerInterfaceType'] = None
        if network_port['PeerInterface'] is not None:
            info['PeerInterfaceId'] = network_port['PeerInterface']['Moid']
            info['PeerInterfaceType'] = network_port['PeerInterface']['ObjectType']
        info['PortId'] = network_port['PortId']
        info['SlotId'] = network_port['SlotId']
        info['Speed'] = network_port['Speed']
        info['SwitchId'] = network_port['SwitchId']

        return info
