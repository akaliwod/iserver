# Extra server information - Power Utilization and State

```
# iserver get server --ip 10.58.50.41 --power

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | 4  | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+

Power Consumption (Watt)
------------------------
- Current      : 324
- Min          : 176
- Average      : 330
- Max          : 435
- Limit action : NoAction


+----------------+---------+--------+-------+-----------------+
| Sensor Name    | State   | Health | Volts | Upper Threshold |
+----------------+---------+--------+-------+-----------------+
| PSU1_VOUT      | Enabled | OK     | 12    | 14              | 
| PSU2_VOUT      | Enabled | OK     | 12.2  | 14              | 
| P12V           | Enabled | OK     | 11.89 | 13.166          | 
| P3V_BAT_SCALED | Enabled | OK     | 3.011 | 3.588           | 
+----------------+---------+--------+-------+-----------------+

+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU Name | State   | Health | Serial      | Firmware | Output (Watt) | Input (Watt) | Max (V) | Min (V) | Max (Hz) | Min (Hz) |
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU1     | Enabled | OK     | LIT241244MU | 10062019 | 142           | 163          | 264     | 180     | 63       | 47       | 
| PSU2     | Enabled | OK     | LIT241244Z5 | 10062019 | 148           | 163          | 264     | 180     | 63       | 47       | 
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
```

JSON Output

```
# iserver get server --ip 10.58.50.41 --power

{
    "Moid": "5fdf9c016176752d35e44795",
    "DeviceMoId": "5fdf9be76f72612d300a8d81",
    "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "Model": "UCSC-C240-M5SN",
    "Serial": "WZP23400AJW",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "on",
    "NumCpus": 2,
    "NumCpuCores": 40,
    "NumThreads": 80,
    "Cpu": "2S 40C 80T",
    "AvailableMemory": 393216,
    "TotalMemory": 393216,
    "UsedMemory": 0,
    "TotalMemoryUnit": "384 [GiB]",
    "TotalMemoryGB": 384,
    "AvailableMemoryUnit": "384 [GiB]",
    "AvailableMemoryGB": 384,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "ManagementIp": "10.58.50.41",
    "AlarmSummary": {
        "Critical": 0,
        "Warning": 0,
        "Info": 0
    },
    "Health": "Healthy",
    "Connected": true,
    "Workflow": {
        "Running": null,
        "LatestMoid": "638f7086696f6e2d308a2da5",
        "Last": [
            {
                "Moid": "638f7086696f6e2d308a2da5",
                "Name": "InstallOS",
                "Progress": 100,
                "CreateTime": "2022-12-06T16:40:39.168Z",
                "StartTime": "2022-12-06T16:40:39.168Z",
                "EndTime": "2022-12-06T17:23:10.224Z",
                "Status": "COMPLETED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1670341239168,
                "StartTimeEpoch": 1670341239168,
                "EndTimeEpoch": 1670343790224,
                "Running": false,
                "Completed": true,
                "Duration": "00:42:31"
            },
            {
                "Moid": "638f7083696f6e2d308a2d24",
                "Name": "Operating System Install",
                "Progress": 100,
                "CreateTime": "2022-12-06T16:40:35.914Z",
                "StartTime": "2022-12-06T16:40:36.549Z",
                "EndTime": "2022-12-06T17:23:11.42Z",
                "Status": "COMPLETED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1670341235914,
                "StartTimeEpoch": 1670341236549,
                "EndTimeEpoch": 1670343791420,
                "Running": false,
                "Completed": true,
                "Duration": "00:42:35"
            },
            {
                "Moid": "638f6ecb696f6e2d3089fd01",
                "Name": "InstallOS",
                "Progress": 23.076923,
                "CreateTime": "2022-12-06T16:33:15.946Z",
                "StartTime": "2022-12-06T16:33:15.946Z",
                "EndTime": "2022-12-06T16:33:52.692Z",
                "Status": "FAILED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1670340795946,
                "StartTimeEpoch": 1670340795946,
                "EndTimeEpoch": 1670340832692,
                "Running": false,
                "Completed": true,
                "Duration": "00:00:37"
            },
            {
                "Moid": "638f6ec6696f6e2d3089fc3d",
                "Name": "Operating System Install",
                "Progress": 33.333336,
                "CreateTime": "2022-12-06T16:33:11.184Z",
                "StartTime": "2022-12-06T16:33:12.042Z",
                "EndTime": "2022-12-06T16:33:53.281Z",
                "Status": "FAILED",
                "Type": "UserDefined",
                "CreateTimeEpoch": 1670340791184,
                "StartTimeEpoch": 1670340792042,
                "EndTimeEpoch": 1670340833281,
                "Running": false,
                "Completed": true,
                "Duration": "00:00:41"
            }
        ]
    },
    "Groups": "p2b,pod2b,power",
    "Redfish": {
        "Capable": true,
        "Enabled": true
    },
    "UCSM": {
        "Capable": false,
        "Enabled": false
    },
    "IMC": {
        "Capable": true,
        "Enabled": false
    },
    "Power": {
        "Data": {
            "PowerControl": {
                "PowerConsumedWatts": 324,
                "LimitException": "NoAction",
                "MinConsumedWatts": 176,
                "AverageConsumedWatts": 330,
                "MaxConsumedWatts": 435
            },
            "Voltage": [
                {
                    "Name": "PSU1_VOUT",
                    "ReadingVolts": 12,
                    "UpperThresholdCritical": 14,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                },
                {
                    "Name": "PSU2_VOUT",
                    "ReadingVolts": 12.2,
                    "UpperThresholdCritical": 14,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                },
                {
                    "Name": "P12V",
                    "ReadingVolts": 11.89,
                    "UpperThresholdCritical": 13.166,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                },
                {
                    "Name": "P3V_BAT_SCALED",
                    "ReadingVolts": 3.011,
                    "UpperThresholdCritical": 3.588,
                    "PhysicalContext": "PowerSupply",
                    "State": "Enabled",
                    "Health": "OK"
                }
            ],
            "PowerSupply": [
                {
                    "Name": "PSU1",
                    "Model": "PS-2112-9S-LF",
                    "SerialNumber": "LIT241244MU",
                    "PartNumber": "341-0638-03",
                    "SparePartNumber": "341-0638-03",
                    "Manufacturer": "Cisco Systems Inc",
                    "FirmwareVersion": "10062019",
                    "PowerOutputWatts": 142,
                    "LastPowerOutputWatts": 142,
                    "PowerInputWatts": 163,
                    "PowerSupplyType": "AC",
                    "State": "Enabled",
                    "Health": "OK",
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050,
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47
                },
                {
                    "Name": "PSU2",
                    "Model": "PS-2112-9S-LF",
                    "SerialNumber": "LIT241244Z5",
                    "PartNumber": "341-0638-03",
                    "SparePartNumber": "341-0638-03",
                    "Manufacturer": "Cisco Systems Inc",
                    "FirmwareVersion": "10062019",
                    "PowerOutputWatts": 148,
                    "LastPowerOutputWatts": 148,
                    "PowerInputWatts": 163,
                    "PowerSupplyType": "AC",
                    "State": "Enabled",
                    "Health": "OK",
                    "MinimumVoltage": 180,
                    "OutputWattage": 1050,
                    "MaximumFrequencyHz": 63,
                    "MaximumVoltage": 264,
                    "MinimumFrequencyHz": 47
                }
            ]
        },
        "Summary": {
            "Source": "Redfish",
            "PowerNow": 324,
            "PowerMin": 176,
            "PowerAvg": 330,
            "PowerMax": 435
        }
    },
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C240-M5SN",
    "LocatorLedOn": false,
    "FlagState": "P+ H",
    "FlagManagement": "CRi",
    "FlagWorkflow": "4"
}
```

Developer output

```
# iserver get server --ip 10.58.50.41 --power

Developer output

{
    "duration": 16926,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 10183
    },
    "redfish": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "path": 4,
        "connect_time": 1730,
        "disconnect_time": 0,
        "path_time": 1109,
        "total_time": 2839
    },
    "ucsm": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "mo": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "mo_time": 0,
        "total_time": 0
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 727
    }
}

Log: debug
-----------

[2022-12-08 23:27:42.699616]	[computes_info.get]	Get servers settings: {
    "rack": true,
    "blade": true,
    "server_setting_id": false,
    "workflow": null,
    "registration": false,
    "id": false,
    "cpu": false,
    "memory": false,
    "fw": false,
    "pci": false,
    "fan": false,
    "psu": false,
    "group": false,
    "storage": false,
    "locator": false,
    "power": false,
    "thermal": false
}
[2022-12-08 23:27:42.701611]	[computes_info.get]	Get servers match rules: {
    "name": "",
    "ip": [
        {
            "type": "address",
            "value": "10.58.50.41"
        }
    ],
    "serials": [],
    "model": "",
    "locator": false,
    "power_off": false,
    "alarms": false,
    "ucsm": false,
    "disconnected": false,
    "standalone": false,
    "cpu": "",
    "memory": "",
    "pci": "",
    "fan": false,
    "psu": false
}
[2022-12-08 23:27:47.627583]	[computes_info.get]	All 103 servers base information in 4912 ms
[2022-12-08 23:27:47.629578]	[computes_info.get]	Base filter 1 servers in 0 ms
[2022-12-08 23:27:51.006425]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9bf46176752d35e4426e",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9bf46176752d35e4426e"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c886176752d35e477e4",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477e4"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c886176752d35e477ea",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477ea"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c886176752d35e477f0",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477f0"
        }
    ],
    "AdminPowerState": "policy",
    "AlarmSummary": {
        "ClassId": "compute.AlarmSummary",
        "Critical": 0,
        "Health": "Healthy",
        "Info": 0,
        "ObjectType": "compute.AlarmSummary",
        "Warning": 0
    },
    "Alerts": [],
    "Ancestors": [],
    "AssetTag": "022C2F4",
    "AvailableMemory": 393216,
    "BiosBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9bff6176752d35e4471c",
        "ObjectType": "bios.BootMode",
        "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdf9bff6176752d35e4471c"
    },
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "60d5fbe96176752d35a30aa7",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5fbe96176752d35a30aa7"
    },
    "Biosunits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9bfe6176752d35e446cf",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/5fdf9bfe6176752d35e446cf"
        }
    ],
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c416176752d35e45e43",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/5fdf9c416176752d35e45e43"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c056176752d35e44930",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/5fdf9c056176752d35e44930"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c2d6176752d35e45801",
        "ObjectType": "boot.DeviceBootSecurity",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9c2d6176752d35e45801"
    },
    "BootDeviceBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c2d6176752d35e457e2",
        "ObjectType": "boot.DeviceBootMode",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9c2d6176752d35e457e2"
    },
    "BootHddDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000c0b6176752d35b76e3e",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000c0b6176752d35b76e3e"
        }
    ],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000c046176752d35b76bb3",
            "ObjectType": "boot.PxeDevice",
            "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000c046176752d35b76bb3"
        }
    ],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6013f1496176752d35458e49",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1496176752d35458e49"
        }
    ],
    "ClassId": "compute.RackUnit",
    "ComputePersonality": [],
    "ConnectionStatus": "",
    "CreateTime": "2020-12-20T18:46:25.383Z",
    "DeviceMoId": "5fdf9be76f72612d300a8d81",
    "Dn": "sys/rack-unit-1",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "Fanmodules": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d71",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d71"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d73",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d73"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d75",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d75"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d77",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d77"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d79",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d79"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d7b",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d7b"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d7d",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d7d"
        }
    ],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c7f6176752d35e473d9",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9c7f6176752d35e473d9"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.50.41",
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
    "Lifecycle": "None",
    "LocatorLed": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c146176752d35e44eca",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdf9c146176752d35e44eca"
    },
    "ManagementMode": "IntersightStandalone",
    "MemoryArrays": [],
    "MemorySpeed": "2933",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.50.41",
    "ModTime": "2022-12-06T18:50:05.578Z",
    "Model": "UCSC-C240-M5SN",
    "Moid": "5fdf9c016176752d35e44795",
    "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "NumAdaptors": 1,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 4,
    "NumFcHostInterfaces": 4,
    "NumThreads": 80,
    "ObjectType": "compute.RackUnit",
    "OperPowerState": "on",
    "OperReason": [],
    "OperState": "",
    "Operability": "",
    "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "5fdf9be76f72612d300a8d81"
    ],
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465cd",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465cd"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465cf",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465cf"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465d1",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d1"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465d3",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d3"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465d9",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d9"
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
            "Moid": "5fdf9c0d6176752d35e44cf7",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c0d6176752d35e44cf7"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c0d6176752d35e44cf9",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c0d6176752d35e44cf9"
        }
    ],
    "RackEnclosureSlot": null,
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9be76f72612d300a8d81",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9be76f72612d300a8d81"
    },
    "Revision": "",
    "Rn": "",
    "SasExpanders": [],
    "Serial": "WZP23400AJW",
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
        "Moid": "5fdf9c526176752d35e46529",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/5fdf9c526176752d35e46529"
    },
    "TopologyScanStatus": "",
    "TotalMemory": 393216,
    "TunneledKvm": false,
    "UnitPersonality": [],
    "UserLabel": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "Uuid": "488930EF-5754-434B-B570-C2BD8359E739",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 23:27:51.010374]	[computes_info.get_server_info]	Thread result: 5fdf9c016176752d35e44795
[2022-12-08 23:27:51.078865]	[computes_info.get]	Selected 1 servers with requested details in 3448 ms
[2022-12-08 23:27:51.080820]	[computes_info.get]	Total time 8380 ms
[2022-12-08 23:27:51.089076]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9bf46176752d35e4426e",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9bf46176752d35e4426e"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c886176752d35e477e4",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477e4"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c886176752d35e477ea",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477ea"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c886176752d35e477f0",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477f0"
        }
    ],
    "AdminPowerState": "policy",
    "AlarmSummary": {
        "ClassId": "compute.AlarmSummary",
        "Critical": 0,
        "Health": "Healthy",
        "Info": 0,
        "ObjectType": "compute.AlarmSummary",
        "Warning": 0
    },
    "Alerts": [],
    "Ancestors": [],
    "AssetTag": "022C2F4",
    "AvailableMemory": 393216,
    "BiosBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9bff6176752d35e4471c",
        "ObjectType": "bios.BootMode",
        "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdf9bff6176752d35e4471c"
    },
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "60d5fbe96176752d35a30aa7",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5fbe96176752d35a30aa7"
    },
    "Biosunits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9bfe6176752d35e446cf",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/5fdf9bfe6176752d35e446cf"
        }
    ],
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c416176752d35e45e43",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/5fdf9c416176752d35e45e43"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c056176752d35e44930",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/5fdf9c056176752d35e44930"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c2d6176752d35e45801",
        "ObjectType": "boot.DeviceBootSecurity",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9c2d6176752d35e45801"
    },
    "BootDeviceBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c2d6176752d35e457e2",
        "ObjectType": "boot.DeviceBootMode",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9c2d6176752d35e457e2"
    },
    "BootHddDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000c0b6176752d35b76e3e",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000c0b6176752d35b76e3e"
        }
    ],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000c046176752d35b76bb3",
            "ObjectType": "boot.PxeDevice",
            "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000c046176752d35b76bb3"
        }
    ],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6013f1496176752d35458e49",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1496176752d35458e49"
        }
    ],
    "ClassId": "compute.RackUnit",
    "ComputePersonality": [],
    "ConnectionStatus": "",
    "CreateTime": "2020-12-20T18:46:25.383Z",
    "DeviceMoId": "5fdf9be76f72612d300a8d81",
    "Dn": "sys/rack-unit-1",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "Fanmodules": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d71",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d71"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d73",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d73"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d75",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d75"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d77",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d77"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d79",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d79"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d7b",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d7b"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c106176752d35e44d7d",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d7d"
        }
    ],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c7f6176752d35e473d9",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9c7f6176752d35e473d9"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.50.41",
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
    "Lifecycle": "None",
    "LocatorLed": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c146176752d35e44eca",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdf9c146176752d35e44eca"
    },
    "ManagementMode": "IntersightStandalone",
    "MemoryArrays": [],
    "MemorySpeed": "2933",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.50.41",
    "ModTime": "2022-12-06T18:50:05.578Z",
    "Model": "UCSC-C240-M5SN",
    "Moid": "5fdf9c016176752d35e44795",
    "Name": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "NumAdaptors": 1,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 4,
    "NumFcHostInterfaces": 4,
    "NumThreads": 80,
    "ObjectType": "compute.RackUnit",
    "OperPowerState": "on",
    "OperReason": [],
    "OperState": "",
    "Operability": "",
    "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "5fdf9be76f72612d300a8d81"
    ],
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465cd",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465cd"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465cf",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465cf"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465d1",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d1"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465d3",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d3"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c546176752d35e465d9",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d9"
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
            "Moid": "5fdf9c0d6176752d35e44cf7",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c0d6176752d35e44cf7"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c0d6176752d35e44cf9",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c0d6176752d35e44cf9"
        }
    ],
    "RackEnclosureSlot": null,
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9be76f72612d300a8d81",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9be76f72612d300a8d81"
    },
    "Revision": "",
    "Rn": "",
    "SasExpanders": [],
    "Serial": "WZP23400AJW",
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
        "Moid": "5fdf9c526176752d35e46529",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/5fdf9c526176752d35e46529"
    },
    "TopologyScanStatus": "",
    "TotalMemory": 393216,
    "TunneledKvm": false,
    "UnitPersonality": [],
    "UserLabel": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "Uuid": "488930EF-5754-434B-B570-C2BD8359E739",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}


Log: isctl
-----------

2022-12-08 23:27:46.004628	True	3193	93	isctl get compute rackunit   -o json --top 100
2022-12-08 23:27:47.625591	True	1606	10	isctl get compute blade   -o json --top 100
2022-12-08 23:27:52.498683	True	1408	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2022-12-08 23:27:54.845575	True	2341	42	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-01T23:27:52.000Z"  -o json --top 100
2022-12-08 23:27:59.401506	True	1635	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100


Log: redfish
-------------

2022-12-08 23:27:56.603135	True	1730	connect 10.58.50.41
2022-12-08 23:27:56.667842	True	59	10.58.50.41:/redfish/v1/Systems
2022-12-08 23:27:56.742964	True	63	10.58.50.41:/redfish/v1/Chassis
2022-12-08 23:27:56.940833	True	187	10.58.50.41:/redfish/v1/Chassis/1
2022-12-08 23:27:57.760984	True	800	10.58.50.41:/redfish/v1/Chassis/1/Power
```

