# Get Intersight Server with Thermal Information

```
# iserver get server --ip 10.58.52.36 --thermal

+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+
| SF   | MF | WF | Name                 | Model            | Serial      | IP          | CPU        | Memory    |
+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+
| P+ H | CU |    | FI-ucsb1-eu-spdc-1-4 | (B) UCSB-B200-M4 | FCH205371UU | 10.58.52.36 | 2S 24C 48T | 256 [GiB] | 
+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+

+--------------------+-------+------+-------+------+
| Thermal Statistics | Value | Min  | Avg   | Max  |
+--------------------+-------+------+-------+------+
| Motherboard Front  | 25.0  | 25.0 | 25.0  | 25.0 | 
| Motherboard Rear   | 36.0  | 36.0 | 36.0  | 36.0 | 
| CPU-1              | 39.0  | 39.0 | 39.0  | 39.0 | 
| CPU-2              | 41.5  | 41.5 | 41.5  | 41.5 | 
| MEM-1              | 28.0  | 28.0 | 28.0  | 28.0 | 
| MEM-10             | 29.0  | 28.0 | 28.73 | 29.0 | 
| MEM-13             | 29.0  | 29.0 | 29.0  | 29.0 | 
| MEM-16             | 31.0  | 31.0 | 31.0  | 31.0 | 
| MEM-19             | 28.0  | 27.0 | 27.4  | 28.0 | 
| MEM-22             | 30.0  | 30.0 | 30.0  | 30.0 | 
| MEM-4              | 27.0  | 27.0 | 27.0  | 27.0 | 
| MEM-7              | 30.0  | 30.0 | 30.0  | 30.0 | 
+--------------------+-------+------+-------+------+
```

JSON Output

```
# iserver get server --ip 10.58.52.36 --thermal

{
    "Moid": "63371c9176752d3139f7da74",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Name": "FI-ucsb1-eu-spdc-1-4",
    "Model": "UCSB-B200-M4",
    "Serial": "FCH205371UU",
    "ManagementMode": "UCSM",
    "OperPowerState": "on",
    "NumCpus": 2,
    "NumCpuCores": 24,
    "NumThreads": 48,
    "Cpu": "2S 24C 48T",
    "AvailableMemory": 262144,
    "TotalMemory": 262144,
    "UsedMemory": 0,
    "TotalMemoryUnit": "256 [GiB]",
    "TotalMemoryGB": 256,
    "AvailableMemoryUnit": "256 [GiB]",
    "AvailableMemoryGB": 256,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "ManagementIp": "10.58.52.36",
    "AlarmSummary": {
        "Critical": 0,
        "Warning": 0,
        "Info": 0
    },
    "Health": "Healthy",
    "Connected": true,
    "Workflow": {
        "Running": null,
        "LatestMoid": null,
        "Last": []
    },
    "Groups": "power,ucsm",
    "Redfish": {
        "Capable": false,
        "Enabled": false
    },
    "UCSM": {
        "Capable": true,
        "Enabled": true
    },
    "IMC": {
        "Capable": false,
        "Enabled": false
    },
    "Thermal": {
        "Data": [
            {
                "dn": "sys/chassis-1/blade-4/board/temp-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "name": "Motherboard Front",
                "type": "motherboard",
                "temperature": 25.0,
                "fm_temp_sen_rear": 36.0,
                "temperature_avg": 25.0,
                "fm_temp_sen_rear_avg": 36.0,
                "temperature_min": 25.0,
                "fm_temp_sen_rear_min": 36.0,
                "temperature_max": 25.0,
                "fm_temp_sen_rear_max": 36.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/temp-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "name": "Motherboard Rear",
                "type": "motherboard",
                "temperature": 36.0,
                "temperature_avg": 36.0,
                "temperature_min": 36.0,
                "temperature_max": 36.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/cpu-1/env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "cpu_rn": "cpu-1",
                "name": "CPU-1",
                "type": "cpu",
                "temperature": 39.0,
                "temperature_avg": 39.0,
                "temperature_min": 39.0,
                "temperature_max": 39.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "cpu_rn": "cpu-2",
                "name": "CPU-2",
                "type": "cpu",
                "temperature": 41.5,
                "temperature_avg": 41.5,
                "temperature_min": 41.5,
                "temperature_max": 41.5
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-1",
                "name": "MEM-1",
                "type": "memory",
                "temperature": 28.0,
                "temperature_avg": 28.0,
                "temperature_min": 28.0,
                "temperature_max": 28.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-10/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-10",
                "name": "MEM-10",
                "type": "memory",
                "temperature": 29.0,
                "temperature_avg": 28.73,
                "temperature_min": 28.0,
                "temperature_max": 29.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-13",
                "name": "MEM-13",
                "type": "memory",
                "temperature": 29.0,
                "temperature_avg": 29.0,
                "temperature_min": 29.0,
                "temperature_max": 29.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-16/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-16",
                "name": "MEM-16",
                "type": "memory",
                "temperature": 31.0,
                "temperature_avg": 31.0,
                "temperature_min": 31.0,
                "temperature_max": 31.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-19/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-19",
                "name": "MEM-19",
                "type": "memory",
                "temperature": 28.0,
                "temperature_avg": 27.4,
                "temperature_min": 27.0,
                "temperature_max": 28.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-22/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-22",
                "name": "MEM-22",
                "type": "memory",
                "temperature": 30.0,
                "temperature_avg": 30.0,
                "temperature_min": 30.0,
                "temperature_max": 30.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-4/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-4",
                "name": "MEM-4",
                "type": "memory",
                "temperature": 27.0,
                "temperature_avg": 27.0,
                "temperature_min": 27.0,
                "temperature_max": 27.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-7/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-7",
                "name": "MEM-7",
                "type": "memory",
                "temperature": 30.0,
                "temperature_avg": 30.0,
                "temperature_min": 30.0,
                "temperature_max": 30.0
            }
        ],
        "Summary": {
            "Source": "UCSM",
            "FanHealth": "N/A",
            "SensorHealth": true,
            "HighestTemperature": 41.5,
            "SmallestGap": "N/A",
            "OverThreshold": "N/A"
        }
    },
    "Type": "Blade",
    "TypeModel": "(B) UCSB-B200-M4",
    "LocatorLedOn": false,
    "FlagState": "P+ H",
    "FlagManagement": "CU",
    "FlagWorkflow": ""
}
```

Developer Output

```
# iserver get server --ip 10.58.52.36 --thermal

Developer output

{
    "duration": 18101,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 9260
    },
    "redfish": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "path": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 0
    },
    "ucsm": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 2151,
        "disconnect_time": 0,
        "mo_time": 2519,
        "total_time": 4670
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
        "lines": 521
    }
}

Log: debug
-----------

[2022-12-08 23:26:44.261144]	[computes_info.get]	Get servers settings: {
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
[2022-12-08 23:26:44.263144]	[computes_info.get]	Get servers match rules: {
    "name": "",
    "ip": [
        {
            "type": "address",
            "value": "10.58.52.36"
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
[2022-12-08 23:26:50.093757]	[computes_info.get]	All 103 servers base information in 5818 ms
[2022-12-08 23:26:50.095777]	[computes_info.get]	Base filter 1 servers in 0 ms
[2022-12-08 23:26:53.809567]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f64f76752d31391e780a",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6337f64f76752d31391e780a"
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
    "Ancestors": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "619d058176752d313994941f",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f"
        }
    ],
    "AssetTag": "",
    "AvailableMemory": 262144,
    "BiosBootmode": null,
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosUnits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f68b76752d31391e85ae",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/6337f68b76752d31391e85ae"
        }
    ],
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e85bc",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6337f68b76752d31391e85bc"
    },
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e85cc",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/6337f68b76752d31391e85cc"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e85da",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6337f68b76752d31391e85da"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": null,
    "BootDeviceBootmode": null,
    "BootHddDevices": [],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [],
    "ChassisId": "1",
    "ClassId": "compute.Blade",
    "ComputePersonality": null,
    "CreateTime": "2022-09-30T16:42:57.259Z",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Dn": "sys/chassis-1/blade-4",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "EquipmentChassis": {
        "ClassId": "mo.MoRef",
        "Moid": "619d058176752d313994941f",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f"
    },
    "EquipmentIoExpanders": [],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "63371c9176752d3139f7da8e",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/63371c9176752d3139f7da8e"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.52.36",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.52.62",
            "Dn": "sys/chassis-1/blade-4/mgmt/ipv4-static-addr",
            "HttpPort": 80,
            "HttpsPort": 443,
            "KvmPort": 2068,
            "KvmVlan": 0,
            "Name": "Outband",
            "ObjectType": "compute.IpAddress",
            "Subnet": "255.255.255.224",
            "Type": "VnicIpV4StaticAddr"
        },
        {
            "Address": "10.58.26.4",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.26.62",
            "Dn": "sys/chassis-1/blade-4/mgmt/ipv4-prof-addr",
            "HttpPort": 80,
            "HttpsPort": 443,
            "KvmPort": 2068,
            "KvmVlan": 0,
            "Name": "Outband",
            "ObjectType": "compute.IpAddress",
            "Subnet": "255.255.255.192",
            "Type": "VnicIpV4ProfDerivedAddr"
        }
    ],
    "KvmServerStateEnabled": false,
    "KvmVendor": "",
    "Lifecycle": "None",
    "LocatorLed": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f6cc76752d31391e9345",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f6cc76752d31391e9345"
    },
    "ManagementMode": "UCSM",
    "MemoryArrays": [],
    "MemorySpeed": "2133",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.52.36, 10.58.26.4",
    "ModTime": "2022-11-09T11:54:30.279Z",
    "Model": "UCSB-B200-M4",
    "Moid": "63371c9176752d3139f7da74",
    "Name": "FI-ucsb1-eu-spdc-1-4",
    "NumAdaptors": 1,
    "NumCpuCores": 24,
    "NumCpuCoresEnabled": 24,
    "NumCpus": 2,
    "NumEthHostInterfaces": 8,
    "NumFcHostInterfaces": 0,
    "NumThreads": 48,
    "ObjectType": "compute.Blade",
    "OperPowerState": "on",
    "OperReason": [],
    "OperState": "ok",
    "Operability": "operable",
    "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "618942976f72612d309dfbe1"
    ],
    "Parent": {
        "ClassId": "mo.MoRef",
        "Moid": "619d058176752d313994941f",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f"
    },
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f68b76752d31391e859a",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/6337f68b76752d31391e859a"
        }
    ],
    "PciNodes": [],
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
    "PlatformType": "UCSFI",
    "Presence": "equipped",
    "PreviousFru": null,
    "Processors": [],
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "618942976f72612d309dfbe1",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1"
    },
    "Revision": "0",
    "Rn": "",
    "ScaledMode": "none",
    "Serial": "FCH205371UU",
    "ServiceProfile": "org-root/org-EU-SPN/ls-esx44-eu-spdc",
    "SharedScope": "",
    "SlotId": 4,
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
        "Moid": "618942be76752d3139ace73b",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b"
    },
    "TotalMemory": 262144,
    "TunneledKvm": false,
    "UserLabel": "",
    "Uuid": "315220a5-2121-4e5b-0101-e1dc0000013f",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 23:26:53.812939]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da74
[2022-12-08 23:26:53.878701]	[computes_info.get]	Selected 1 servers with requested details in 3781 ms
[2022-12-08 23:26:53.879620]	[computes_info.get]	Total time 9618 ms
[2022-12-08 23:26:53.887598]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f64f76752d31391e780a",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6337f64f76752d31391e780a"
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
    "Ancestors": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "619d058176752d313994941f",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f"
        }
    ],
    "AssetTag": "",
    "AvailableMemory": 262144,
    "BiosBootmode": null,
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosUnits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f68b76752d31391e85ae",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/6337f68b76752d31391e85ae"
        }
    ],
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e85bc",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6337f68b76752d31391e85bc"
    },
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e85cc",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/6337f68b76752d31391e85cc"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e85da",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6337f68b76752d31391e85da"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": null,
    "BootDeviceBootmode": null,
    "BootHddDevices": [],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [],
    "ChassisId": "1",
    "ClassId": "compute.Blade",
    "ComputePersonality": null,
    "CreateTime": "2022-09-30T16:42:57.259Z",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Dn": "sys/chassis-1/blade-4",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "EquipmentChassis": {
        "ClassId": "mo.MoRef",
        "Moid": "619d058176752d313994941f",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f"
    },
    "EquipmentIoExpanders": [],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "63371c9176752d3139f7da8e",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/63371c9176752d3139f7da8e"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.52.36",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.52.62",
            "Dn": "sys/chassis-1/blade-4/mgmt/ipv4-static-addr",
            "HttpPort": 80,
            "HttpsPort": 443,
            "KvmPort": 2068,
            "KvmVlan": 0,
            "Name": "Outband",
            "ObjectType": "compute.IpAddress",
            "Subnet": "255.255.255.224",
            "Type": "VnicIpV4StaticAddr"
        },
        {
            "Address": "10.58.26.4",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.26.62",
            "Dn": "sys/chassis-1/blade-4/mgmt/ipv4-prof-addr",
            "HttpPort": 80,
            "HttpsPort": 443,
            "KvmPort": 2068,
            "KvmVlan": 0,
            "Name": "Outband",
            "ObjectType": "compute.IpAddress",
            "Subnet": "255.255.255.192",
            "Type": "VnicIpV4ProfDerivedAddr"
        }
    ],
    "KvmServerStateEnabled": false,
    "KvmVendor": "",
    "Lifecycle": "None",
    "LocatorLed": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f6cc76752d31391e9345",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f6cc76752d31391e9345"
    },
    "ManagementMode": "UCSM",
    "MemoryArrays": [],
    "MemorySpeed": "2133",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.52.36, 10.58.26.4",
    "ModTime": "2022-11-09T11:54:30.279Z",
    "Model": "UCSB-B200-M4",
    "Moid": "63371c9176752d3139f7da74",
    "Name": "FI-ucsb1-eu-spdc-1-4",
    "NumAdaptors": 1,
    "NumCpuCores": 24,
    "NumCpuCoresEnabled": 24,
    "NumCpus": 2,
    "NumEthHostInterfaces": 8,
    "NumFcHostInterfaces": 0,
    "NumThreads": 48,
    "ObjectType": "compute.Blade",
    "OperPowerState": "on",
    "OperReason": [],
    "OperState": "ok",
    "Operability": "operable",
    "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "618942976f72612d309dfbe1"
    ],
    "Parent": {
        "ClassId": "mo.MoRef",
        "Moid": "619d058176752d313994941f",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f"
    },
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f68b76752d31391e859a",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/6337f68b76752d31391e859a"
        }
    ],
    "PciNodes": [],
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
    "PlatformType": "UCSFI",
    "Presence": "equipped",
    "PreviousFru": null,
    "Processors": [],
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "618942976f72612d309dfbe1",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1"
    },
    "Revision": "0",
    "Rn": "",
    "ScaledMode": "none",
    "Serial": "FCH205371UU",
    "ServiceProfile": "org-root/org-EU-SPN/ls-esx44-eu-spdc",
    "SharedScope": "",
    "SlotId": 4,
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
        "Moid": "618942be76752d3139ace73b",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b"
    },
    "TotalMemory": 262144,
    "TunneledKvm": false,
    "UserLabel": "",
    "Uuid": "315220a5-2121-4e5b-0101-e1dc0000013f",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}


Log: isctl
-----------

2022-12-08 23:26:47.940226	True	3582	93	isctl get compute rackunit   -o json --top 100
2022-12-08 23:26:50.092760	True	2136	10	isctl get compute blade   -o json --top 100
2022-12-08 23:26:55.424617	True	1535	1	isctl get asset deviceregistration  moid 618942976f72612d309dfbe1 -o json
2022-12-08 23:26:57.439886	True	2007	42	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-01T23:26:55.000Z"  -o json --top 100


Log: ucsm
----------

2022-12-08 23:26:59.185012	True	1725	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 23:26:59.699692	True	508	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 23:27:00.242571	True	538	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 23:27:00.704825	True	460	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 23:27:01.167277	True	460	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 23:27:01.722104	True	553	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 23:27:02.159104	True	426	disconnect vip-ucsb1.emea-sp.cisco.com
```
