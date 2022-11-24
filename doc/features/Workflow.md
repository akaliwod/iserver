# Workflow

Get workflow's detail selected by Moid in table, json or yaml formats.

```
# iserver get workflow --help

Usage: iserver.py get workflow [OPTIONS] WORKFLOW_ID

  Get workflow

Options:
  --iaccount TEXT                 Intersight account  [default: isctl]
  -o, --output [default|json|yaml]
                                  [default: default]
  --devel                         Developer output  [default: False]
  --help                          Show this message and exit.
```

Default output

```
# iserver get workflow 6346a23c696f6e2d30f93ad5

Get server workflow info...

Server
- Name: comp-1-p2b-eu-spdc-WMP240400FM
- Model: UCSC-C220-M5SX
- Serial: WMP240400FM
- IP: 10.58.50.44


Workflow
- Workflow ID: 6346a23c696f6e2d30f93ad5
- Name: Reboot IMC
- Status: COMPLETED
- Create Time: 2022-10-12T11:17:16.245Z
- Start Time: 2022-10-12T11:17:16.286Z
- End Time: 2022-10-12T11:17:27.422Z
- Duration: 00:00:11


+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| Task Moid                 | Description                      | Create Time               | Status     | Duration  | Details                        |
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
| 6346a23c696f6e2d30f93ae6  | workflow.StartWorkflowTask       | 2022-10-12T11:17:16.398Z  | COMPLETED  | 00:00:00  |                                | 
| 6346a23c696f6e2d30f93aef  | Invoke IMC Reboot                | 2022-10-12T11:17:16.476Z  | COMPLETED  | 00:00:10  | Cisco IMC reboot is initiated  | 
| 6346a246696f6e2d30f93b17  | Invoke the IMC Reboot            | 2022-10-12T11:17:26.713Z  | NO_OP      | 00:00:00  |                                | 
| 6346a246696f6e2d30f93b24  | Invoke IMC Reboot                | 2022-10-12T11:17:26.935Z  | NO_OP      | 00:00:01  |                                | 
| 6346a247696f6e2d30f93b2f  | Update Server Inventory          | 2022-10-12T11:17:27.18Z   | NO_OP      | 00:00:00  | Skipped                        | 
| 6346a247696f6e2d30f93b42  | workflow.SuccessEndWorkflowTask  | 2022-10-12T11:17:27.346Z  | COMPLETED  | 00:00:00  |                                | 
+---------------------------+----------------------------------+---------------------------+------------+-----------+--------------------------------+
```

JSON output

```
# iserver get workflow 6346a23c696f6e2d30f93ad5 -o json

{
    "workflow": {
        "Moid": "6346a23c696f6e2d30f93ad5",
        "Name": "Reboot IMC",
        "Progress": 100,
        "CreateTime": "2022-10-12T11:17:16.245Z",
        "StartTime": "2022-10-12T11:17:16.286Z",
        "EndTime": "2022-10-12T11:17:27.422Z",
        "Status": "COMPLETED",
        "Type": "UserDefined",
        "CreateTimeEpoch": 1665566236245,
        "StartTimeEpoch": 1665566236286,
        "EndTimeEpoch": 1665566247422,
        "Running": false,
        "Completed": true,
        "Duration": "00:00:11"
    },
    "tasks": [
        {
            "Moid": "6346a23c696f6e2d30f93ae6",
            "Name": "workflow.StartWorkflowTask",
            "Label": "",
            "CreateTime": "2022-10-12T11:17:16.398Z",
            "StartTime": "2022-10-12T11:17:16.392Z",
            "EndTime": "2022-10-12T11:17:16.4Z",
            "Status": "COMPLETED",
            "FailureReason": "",
            "Description": "workflow.StartWorkflowTask",
            "CreateTimeEpoch": 1665566236398,
            "StartTimeEpoch": 1665566236392,
            "EndTimeEpoch": 1665566236400,
            "Duration": "00:00:00"
        },
        {
            "Moid": "6346a23c696f6e2d30f93aef",
            "Name": "compute.ServerOperationTask",
            "Label": "Invoke IMC Reboot",
            "CreateTime": "2022-10-12T11:17:16.476Z",
            "StartTime": "2022-10-12T11:17:16.467Z",
            "EndTime": "2022-10-12T11:17:26.622Z",
            "Status": "COMPLETED",
            "FailureReason": "Cisco IMC reboot is initiated",
            "Description": "Invoke IMC Reboot",
            "CreateTimeEpoch": 1665566236476,
            "StartTimeEpoch": 1665566236467,
            "EndTimeEpoch": 1665566246622,
            "Duration": "00:00:10"
        },
        {
            "Moid": "6346a246696f6e2d30f93b17",
            "Name": "compute.ServerRedfishOperationTask",
            "Label": "Invoke the IMC Reboot",
            "CreateTime": "2022-10-12T11:17:26.713Z",
            "StartTime": "2022-10-12T11:17:26.702Z",
            "EndTime": "2022-10-12T11:17:26.809Z",
            "Status": "NO_OP",
            "FailureReason": "",
            "Description": "Invoke the IMC Reboot",
            "CreateTimeEpoch": 1665566246713,
            "StartTimeEpoch": 1665566246702,
            "EndTimeEpoch": 1665566246809,
            "Duration": "00:00:00"
        },
        {
            "Moid": "6346a246696f6e2d30f93b24",
            "Name": "RestartIMCInAssistManagedDevices",
            "Label": "Invoke IMC Reboot",
            "CreateTime": "2022-10-12T11:17:26.935Z",
            "StartTime": "2022-10-12T11:17:26.927Z",
            "EndTime": "2022-10-12T11:17:27.089Z",
            "Status": "NO_OP",
            "FailureReason": "",
            "Description": "Invoke IMC Reboot",
            "CreateTimeEpoch": 1665566246935,
            "StartTimeEpoch": 1665566246927,
            "EndTimeEpoch": 1665566247089,
            "Duration": "00:00:01"
        },
        {
            "Moid": "6346a247696f6e2d30f93b2f",
            "Name": "UpdateServerInventoryTask",
            "Label": "Update Server Inventory",
            "CreateTime": "2022-10-12T11:17:27.18Z",
            "StartTime": "2022-10-12T11:17:27.169Z",
            "EndTime": "2022-10-12T11:17:27.248Z",
            "Status": "NO_OP",
            "FailureReason": "Skipped",
            "Description": "Update Server Inventory",
            "CreateTimeEpoch": 1665566247180,
            "StartTimeEpoch": 1665566247169,
            "EndTimeEpoch": 1665566247248,
            "Duration": "00:00:00"
        },
        {
            "Moid": "6346a247696f6e2d30f93b42",
            "Name": "workflow.SuccessEndWorkflowTask",
            "Label": "",
            "CreateTime": "2022-10-12T11:17:27.346Z",
            "StartTime": "2022-10-12T11:17:27.339Z",
            "EndTime": "2022-10-12T11:17:27.349Z",
            "Status": "COMPLETED",
            "FailureReason": "",
            "Description": "workflow.SuccessEndWorkflowTask",
            "CreateTimeEpoch": 1665566247346,
            "StartTimeEpoch": 1665566247339,
            "EndTimeEpoch": 1665566247349,
            "Duration": "00:00:00"
        }
    ],
    "server": {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Adapters": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa1736176752d35e673d8",
                "ObjectType": "adapter.Unit",
                "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfa1736176752d35e673d8"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa2076176752d35e6b71d",
                "ObjectType": "adapter.Unit",
                "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfa2076176752d35e6b71d"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa2076176752d35e6b726",
                "ObjectType": "adapter.Unit",
                "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfa2076176752d35e6b726"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa2076176752d35e6b72f",
                "ObjectType": "adapter.Unit",
                "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfa2076176752d35e6b72f"
            }
        ],
        "AdminPowerState": "policy",
        "AlarmSummary": {
            "ClassId": "compute.AlarmSummary",
            "Critical": 0,
            "ObjectType": "compute.AlarmSummary",
            "Warning": 0
        },
        "Alerts": [],
        "Ancestors": [],
        "AssetTag": "022C2B2",
        "AvailableMemory": 393216,
        "BiosBootmode": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfa17d6176752d35e677fe",
            "ObjectType": "bios.BootMode",
            "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdfa17d6176752d35e677fe"
        },
        "BiosPostComplete": false,
        "BiosTokenSettings": null,
        "BiosVfSelectMemoryRasConfiguration": {
            "ClassId": "mo.MoRef",
            "Moid": "60d5fbe96176752d35a30a97",
            "ObjectType": "bios.VfSelectMemoryRasConfiguration",
            "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5fbe96176752d35a30a97"
        },
        "Biosunits": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa17b6176752d35e67765",
                "ObjectType": "bios.Unit",
                "link": "https://www.intersight.com/api/v1/bios/Units/5fdfa17b6176752d35e67765"
            }
        ],
        "Bmc": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfa1bc6176752d35e693d4",
            "ObjectType": "management.Controller",
            "link": "https://www.intersight.com/api/v1/management/Controllers/5fdfa1bc6176752d35e693d4"
        },
        "Board": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfa1846176752d35e67a50",
            "ObjectType": "compute.Board",
            "link": "https://www.intersight.com/api/v1/compute/Boards/5fdfa1846176752d35e67a50"
        },
        "BootCddDevices": [],
        "BootDeviceBootSecurity": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfa1a86176752d35e68947",
            "ObjectType": "boot.DeviceBootSecurity",
            "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdfa1a86176752d35e68947"
        },
        "BootDeviceBootmode": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfa1a86176752d35e6896b",
            "ObjectType": "boot.DeviceBootMode",
            "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdfa1a86176752d35e6896b"
        },
        "BootHddDevices": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "60000bfa6176752d35b76833",
                "ObjectType": "boot.HddDevice",
                "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000bfa6176752d35b76833"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "61b9d31376752d31394dd98b",
                "ObjectType": "boot.HddDevice",
                "link": "https://www.intersight.com/api/v1/boot/HddDevices/61b9d31376752d31394dd98b"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "61c1e5c376752d3139f1d90a",
                "ObjectType": "boot.HddDevice",
                "link": "https://www.intersight.com/api/v1/boot/HddDevices/61c1e5c376752d3139f1d90a"
            }
        ],
        "BootIscsiDevices": [],
        "BootNvmeDevices": [],
        "BootPchStorageDevices": [],
        "BootPxeDevices": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "60000bf76176752d35b76641",
                "ObjectType": "boot.PxeDevice",
                "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000bf76176752d35b76641"
            }
        ],
        "BootSanDevices": [],
        "BootSdDevices": [],
        "BootUefiShellDevices": [],
        "BootUsbDevices": [],
        "BootVmediaDevices": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6013f13a6176752d35458792",
                "ObjectType": "boot.VmediaDevice",
                "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f13a6176752d35458792"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "61b9d31376752d31394dd99b",
                "ObjectType": "boot.VmediaDevice",
                "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/61b9d31376752d31394dd99b"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "61c1e32276752d3139f1582d",
                "ObjectType": "boot.VmediaDevice",
                "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/61c1e32276752d3139f1582d"
            }
        ],
        "ClassId": "compute.RackUnit",
        "ConnectionStatus": "",
        "CreateTime": "2020-12-20T19:09:52.345Z",
        "DeviceMoId": "5fdfa1686f72612d300b383f",
        "DisplayNames": {
            "hierarchical": [
                "server-1"
            ],
            "short": [
                "Server-1"
            ]
        },
        "Dn": "sys/rack-unit-1",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "Fanmodules": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa18f6176752d35e67e6a",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e6a"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa18f6176752d35e67e70",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e70"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa18f6176752d35e67e72",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e72"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa18f6176752d35e67e74",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e74"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa18f6176752d35e67e76",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e76"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa18f6176752d35e67e78",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e78"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa18f6176752d35e67e7a",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e7a"
            }
        ],
        "FaultSummary": 0,
        "GenericInventoryHolders": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa1fe6176752d35e6b22f",
                "ObjectType": "inventory.GenericInventoryHolder",
                "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdfa1fe6176752d35e6b22f"
            }
        ],
        "GraphicsCards": [],
        "HardwareUuid": "",
        "InventoryDeviceInfo": null,
        "KvmIpAddresses": [
            {
                "Address": "10.58.50.44",
                "Category": "Equipment",
                "ClassId": "compute.IpAddress",
                "DefaultGateway": "10.58.50.62",
                "Dn": "sys/rack-unit-1/mgmt/if-1",
                "HttpPort": 80,
                "HttpsPort": 443,
                "KvmPort": 2068,
                "KvmVlan": 1,
                "Name": "Outband",
                "ObjectType": "compute.IpAddress",
                "Subnet": "255.255.255.224",
                "Type": "MgmtInterface"
            }
        ],
        "KvmServerStateEnabled": false,
        "KvmVendor": "Avocent",
        "LocatorLed": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfa1936176752d35e68058",
            "ObjectType": "equipment.LocatorLed",
            "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdfa1936176752d35e68058"
        },
        "ManagementMode": "IntersightStandalone",
        "MemoryArrays": [],
        "MemorySpeed": "2933",
        "MgmtIdentity": null,
        "MgmtIpAddress": "10.58.50.44",
        "ModTime": "2022-10-12T11:16:18.093Z",
        "Model": "UCSC-C220-M5SX",
        "Moid": "5fdfa1806176752d35e678c2",
        "Name": "comp-1-p2b-eu-spdc-WMP240400FM",
        "NumAdaptors": 1,
        "NumCpuCores": 40,
        "NumCpuCoresEnabled": 40,
        "NumCpus": 2,
        "NumEthHostInterfaces": 10,
        "NumFcHostInterfaces": 2,
        "NumThreads": 80,
        "ObjectType": "compute.RackUnit",
        "OperPowerState": "on",
        "OperReason": [],
        "OperState": "",
        "Operability": "",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "5fdfa1686f72612d300b383f"
        ],
        "PciDevices": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa1d46176752d35e69f99",
                "ObjectType": "pci.Device",
                "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69f99"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa1d46176752d35e69f9b",
                "ObjectType": "pci.Device",
                "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69f9b"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa1d46176752d35e69f9d",
                "ObjectType": "pci.Device",
                "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69f9d"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa1d46176752d35e69fa2",
                "ObjectType": "pci.Device",
                "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69fa2"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5fdfa1d46176752d35e69fa4",
                "ObjectType": "pci.Device",
                "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69fa4"
            }
        ],
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
        "PlatformType": "IMCM5",
        "Presence": "equipped",
        "PreviousFru": null,
        "Processors": [],
        "Psus": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "62a7eebf76752d313928bfbc",
                "ObjectType": "equipment.Psu",
                "link": "https://www.intersight.com/api/v1/equipment/Psus/62a7eebf76752d313928bfbc"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "62a7eebf76752d313928bfbe",
                "ObjectType": "equipment.Psu",
                "link": "https://www.intersight.com/api/v1/equipment/Psus/62a7eebf76752d313928bfbe"
            }
        ],
        "RackEnclosureSlot": null,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfa1686f72612d300b383f",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdfa1686f72612d300b383f"
        },
        "Revision": "",
        "Rn": "",
        "SasExpanders": [],
        "Serial": "WMP240400FM",
        "ServerId": 1,
        "ServiceProfile": "",
        "SharedScope": "",
        "StorageControllers": [],
        "StorageEnclosures": [],
        "Tags": [
            {
                "Key": "Intersight.LicenseTier",
                "Value": "Premier"
            }
        ],
        "TopSystem": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfa1d16176752d35e69dd1",
            "ObjectType": "top.System",
            "link": "https://www.intersight.com/api/v1/top/Systems/5fdfa1d16176752d35e69dd1"
        },
        "TopologyScanStatus": "",
        "TotalMemory": 393216,
        "TunneledKvm": true,
        "UnitPersonality": [],
        "UserLabel": "comp-1-p2b-eu-spdc-WMP240400FM",
        "Uuid": "E6FB96C5-2DA8-465D-A83E-E1764CA90D5B",
        "Vendor": "Cisco Systems Inc",
        "Vmedia": null,
        "ManagementIp": "10.58.50.44",
        "Cpu": "2S 40C 80T",
        "Health": "Healthy",
        "TotalMemoryUnit": "384 [GiB]",
        "TotalMemoryGB": 384,
        "Groups": "self-test-power,p2b",
        "Type": "Rack",
        "State": "P+HRS"
    }
}
```

YAML output

```
# iserver get workflow 6346a23c696f6e2d30f93ad5 -o yaml

server:
  AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fdfa1736176752d35e673d8
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfa1736176752d35e673d8
  - ClassId: mo.MoRef
    Moid: 5fdfa2076176752d35e6b71d
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfa2076176752d35e6b71d
  - ClassId: mo.MoRef
    Moid: 5fdfa2076176752d35e6b726
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfa2076176752d35e6b726
  - ClassId: mo.MoRef
    Moid: 5fdfa2076176752d35e6b72f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfa2076176752d35e6b72f
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 022C2B2
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fdfa17d6176752d35e677fe
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fdfa17d6176752d35e677fe
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5fbe96176752d35a30a97
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5fbe96176752d35a30a97
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fdfa17b6176752d35e67765
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fdfa17b6176752d35e67765
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fdfa1bc6176752d35e693d4
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fdfa1bc6176752d35e693d4
  Board:
    ClassId: mo.MoRef
    Moid: 5fdfa1846176752d35e67a50
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fdfa1846176752d35e67a50
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdfa1a86176752d35e68947
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdfa1a86176752d35e68947
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fdfa1a86176752d35e6896b
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdfa1a86176752d35e6896b
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 60000bfa6176752d35b76833
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/60000bfa6176752d35b76833
  - ClassId: mo.MoRef
    Moid: 61b9d31376752d31394dd98b
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61b9d31376752d31394dd98b
  - ClassId: mo.MoRef
    Moid: 61c1e5c376752d3139f1d90a
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61c1e5c376752d3139f1d90a
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 60000bf76176752d35b76641
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/60000bf76176752d35b76641
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 6013f13a6176752d35458792
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/6013f13a6176752d35458792
  - ClassId: mo.MoRef
    Moid: 61b9d31376752d31394dd99b
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/61b9d31376752d31394dd99b
  - ClassId: mo.MoRef
    Moid: 61c1e32276752d3139f1582d
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/61c1e32276752d3139f1582d
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2020-12-20T19:09:52.345Z'
  DeviceMoId: 5fdfa1686f72612d300b383f
  DisplayNames:
    hierarchical:
    - server-1
    short:
    - Server-1
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e6a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e6a
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e70
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e70
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e72
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e72
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e74
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e74
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e76
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e76
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e78
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e78
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e7a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e7a
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fdfa1fe6176752d35e6b22f
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdfa1fe6176752d35e6b22f
  GraphicsCards: []
  Groups: self-test-power,p2b
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.44
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.50.62
    Dn: sys/rack-unit-1/mgmt/if-1
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 1
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.224
    Type: MgmtInterface
  KvmServerStateEnabled: false
  KvmVendor: Avocent
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 5fdfa1936176752d35e68058
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdfa1936176752d35e68058
  ManagementIp: 10.58.50.44
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.44
  ModTime: '2022-10-12T11:16:18.093Z'
  Model: UCSC-C220-M5SX
  Moid: 5fdfa1806176752d35e678c2
  Name: comp-1-p2b-eu-spdc-WMP240400FM
  NumAdaptors: 1
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 10
  NumFcHostInterfaces: 2
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fdfa1686f72612d300b383f
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69f99
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69f99
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69f9b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69f9b
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69f9d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69f9d
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69fa2
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69fa2
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69fa4
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69fa4
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 5dee1d736972652d321d26b5
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5
  - ClassId: mo.MoRef
    Moid: 625706a06972652d3202a8f9
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9
  - ClassId: mo.MoRef
    Moid: 6242d1016972652d32eda017
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62a7eebf76752d313928bfbc
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62a7eebf76752d313928bfbc
  - ClassId: mo.MoRef
    Moid: 62a7eebf76752d313928bfbe
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62a7eebf76752d313928bfbe
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fdfa1686f72612d300b383f
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdfa1686f72612d300b383f
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WMP240400FM
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fdfa1d16176752d35e69dd1
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fdfa1d16176752d35e69dd1
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: true
  Type: Rack
  UnitPersonality: []
  UserLabel: comp-1-p2b-eu-spdc-WMP240400FM
  Uuid: E6FB96C5-2DA8-465D-A83E-E1764CA90D5B
  Vendor: Cisco Systems Inc
  Vmedia: null
tasks:
- CreateTime: '2022-10-12T11:17:16.398Z'
  CreateTimeEpoch: 1665566236398
  Description: workflow.StartWorkflowTask
  Duration: 00:00:00
  EndTime: '2022-10-12T11:17:16.4Z'
  EndTimeEpoch: 1665566236400
  FailureReason: ''
  Label: ''
  Moid: 6346a23c696f6e2d30f93ae6
  Name: workflow.StartWorkflowTask
  StartTime: '2022-10-12T11:17:16.392Z'
  StartTimeEpoch: 1665566236392
  Status: COMPLETED
- CreateTime: '2022-10-12T11:17:16.476Z'
  CreateTimeEpoch: 1665566236476
  Description: Invoke IMC Reboot
  Duration: 00:00:10
  EndTime: '2022-10-12T11:17:26.622Z'
  EndTimeEpoch: 1665566246622
  FailureReason: Cisco IMC reboot is initiated
  Label: Invoke IMC Reboot
  Moid: 6346a23c696f6e2d30f93aef
  Name: compute.ServerOperationTask
  StartTime: '2022-10-12T11:17:16.467Z'
  StartTimeEpoch: 1665566236467
  Status: COMPLETED
- CreateTime: '2022-10-12T11:17:26.713Z'
  CreateTimeEpoch: 1665566246713
  Description: Invoke the IMC Reboot
  Duration: 00:00:00
  EndTime: '2022-10-12T11:17:26.809Z'
  EndTimeEpoch: 1665566246809
  FailureReason: ''
  Label: Invoke the IMC Reboot
  Moid: 6346a246696f6e2d30f93b17
  Name: compute.ServerRedfishOperationTask
  StartTime: '2022-10-12T11:17:26.702Z'
  StartTimeEpoch: 1665566246702
  Status: NO_OP
- CreateTime: '2022-10-12T11:17:26.935Z'
  CreateTimeEpoch: 1665566246935
  Description: Invoke IMC Reboot
  Duration: 00:00:01
  EndTime: '2022-10-12T11:17:27.089Z'
  EndTimeEpoch: 1665566247089
  FailureReason: ''
  Label: Invoke IMC Reboot
  Moid: 6346a246696f6e2d30f93b24
  Name: RestartIMCInAssistManagedDevices
  StartTime: '2022-10-12T11:17:26.927Z'
  StartTimeEpoch: 1665566246927
  Status: NO_OP
- CreateTime: '2022-10-12T11:17:27.18Z'
  CreateTimeEpoch: 1665566247180
  Description: Update Server Inventory
  Duration: 00:00:00
  EndTime: '2022-10-12T11:17:27.248Z'
  EndTimeEpoch: 1665566247248
  FailureReason: Skipped
  Label: Update Server Inventory
  Moid: 6346a247696f6e2d30f93b2f
  Name: UpdateServerInventoryTask
  StartTime: '2022-10-12T11:17:27.169Z'
  StartTimeEpoch: 1665566247169
  Status: NO_OP
- CreateTime: '2022-10-12T11:17:27.346Z'
  CreateTimeEpoch: 1665566247346
  Description: workflow.SuccessEndWorkflowTask
  Duration: 00:00:00
  EndTime: '2022-10-12T11:17:27.349Z'
  EndTimeEpoch: 1665566247349
  FailureReason: ''
  Label: ''
  Moid: 6346a247696f6e2d30f93b42
  Name: workflow.SuccessEndWorkflowTask
  StartTime: '2022-10-12T11:17:27.339Z'
  StartTimeEpoch: 1665566247339
  Status: COMPLETED
workflow:
  Completed: true
  CreateTime: '2022-10-12T11:17:16.245Z'
  CreateTimeEpoch: 1665566236245
  Duration: 00:00:11
  EndTime: '2022-10-12T11:17:27.422Z'
  EndTimeEpoch: 1665566247422
  Moid: 6346a23c696f6e2d30f93ad5
  Name: Reboot IMC
  Progress: 100
  Running: false
  StartTime: '2022-10-12T11:17:16.286Z'
  StartTimeEpoch: 1665566236286
  Status: COMPLETED
  Type: UserDefined
```