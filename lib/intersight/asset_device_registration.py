from lib.intersight.intersight_common import IntersightCommon


class AssetDeviceContractInformation(IntersightCommon):
    """Class for intersight asset device contract information objects
    {
    "Account": {
        "ClassId": "mo.MoRef",
        "Moid": "5a58c3ba3768393836cb0f1b",
        "ObjectType": "iam.Account",
        "link": "https://www.intersight.com/api/v1/iam/Accounts/5a58c3ba3768393836cb0f1b"
    },
    "AccountMoid": "5a58c3ba3768393836cb0f1b",
    "Ancestors": [],
    "ApiVersion": 11,
    "AppPartitionNumber": 125,
    "ClaimedByUser": {
        "ClassId": "mo.MoRef",
        "Moid": "5a58c41a3768393836cb10bc",
        "ObjectType": "iam.User",
        "link": "https://www.intersight.com/api/v1/iam/Users/5a58c41a3768393836cb10bc"
    },
    "ClaimedByUserName": "sesousa@cisco.com",
    "ClaimedTime": "2022-09-20T10:43:18.327Z",
    "ClassId": "asset.DeviceRegistration",
    "ClusterMembers": [
        {
        "ClassId": "mo.MoRef",
        "Moid": "632999466f72612d39b26945",
        "ObjectType": "asset.ClusterMember",
        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/632999466f72612d39b26945"
        },
        {
        "ClassId": "mo.MoRef",
        "Moid": "632999466f72612d39b26946",
        "ObjectType": "asset.ClusterMember",
        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/632999466f72612d39b26946"
        }
    ],
    "ConnectionId": "e53fb7c94631f12a96832ed63dcdb8d4:8e008439-dc1d-4f25-89b9-8471e6262801",
    "ConnectionReason": "",
    "ConnectionStatus": "Connected",
    "ConnectionStatusLastChangeTime": "2022-11-13T03:27:22.596Z",
    "ConnectorVersion": "1.0.11-2396",
    "CreateTime": "2022-09-20T10:43:18.301Z",
    "DeviceClaim": {
        "ClassId": "mo.MoRef",
        "Moid": "632999466f72612d39b26939",
        "ObjectType": "asset.DeviceClaim",
        "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/632999466f72612d39b26939"
    },
    "DeviceConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "632999466f72612d39b26943",
        "ObjectType": "asset.DeviceConfiguration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/632999466f72612d39b26943"
    },
    "DeviceExternalIpAddress": "62.28.62.162",
    "DeviceHostname": [
        "ucsX"
    ],
    "DeviceIpAddress": [
        "10.90.90.13",
        "10.90.90.14"
    ],
    "DisplayNames": {
        "hierarchical": [
        "[ucsX]"
        ],
        "short": [
        "[ucsX]"
        ]
    },
    "DomainGroup": {
        "ClassId": "mo.MoRef",
        "Moid": "5b2541957a7662743465d06d",
        "ObjectType": "iam.DomainGroup",
        "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5b2541957a7662743465d06d"
    },
    "DomainGroupMoid": "5b2541957a7662743465d06d",
    "ExecutionMode": "Normal",
    "ModTime": "2022-11-13T03:27:22.648Z",
    "Moid": "632999466f72612d39b26942",
    "ObjectType": "asset.DeviceRegistration",
    "Owners": [
        "5a58c3ba3768393836cb0f1b",
        "632999466f72612d39b26942"
    ],
    "ParentConnection": null,
    "ParentSignature": null,
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
    "Pid": [
        "UCS-FI-6454"
    ],
    "PlatformType": "UCSFIISM",
    "ProxyApp": "astro",
    "PublicAccessKey": "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu/kLAlQkjn2D6AB/BiHK\n995WhFbn7Ab+t9iEW8dZm3iC/ZiG9t5FTl3N8XImac43k8VCRl31HYsCTkx/DOwG\nnFfkUsjWZ0gdILkml911anN6Y/5ziMLDclX+E+kLhFF7ZnauHPY7/Q22w6/grvUh\nnqeEGhADBu9cBf+JtMOX0qYiHbs7n5oOykx0aCPknDaWXPjSq4YJfXw2KNqAIuXa\nCiGpzX7Zvapzln9w1zMpn+t82+hwuSiw6gI6idn5gYBCXoUdADtm0rO5+h7MmzS4\nPJnVyFPFLha0Fb458xm3XEKyGgQOAirgRmiJUL2vTu7pLsCJg9JA5RVyme3XqbBJ\n1QIDAQAB\n-----END RSA PUBLIC KEY-----\n",
    "ReadOnly": false,
    "SecurityToken": null,
    "Serial": [
        "FDO26340DE3",
        "FDO26340CVC"
    ],
    "SharedScope": "",
    "Tags": [
        {
        "Key": "cisco.meta.ManagementMode",
        "Value": "Intersight"
        }
    ],
    "Vendor": "Cisco Systems, Inc."
    }
    """
    def __init__(self, iaccount):
        self.iobject = 'asset deviceregistration'
        IntersightCommon.__init__(self, iaccount, self.iobject)
