# Extra server information - Server ID

```
# iserver get servers --column id --group p2b

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+--------------------------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    | Moid                     |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+--------------------------+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 5fdf9c016176752d35e44795 | 
| P+ H | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] | 5fdf9c786176752d35e47110 | 
| P- H | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] | 5fdf9d026176752d35e4ac4e | 
| P+ H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] | 5fdfa1806176752d35e678c2 | 
| P+ H | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 2S 40C 80T | 384 [GiB] | 5fdfdc3b6176752d35fce0a9 | 
| P+ H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] | 5fdfe47f6176752d35001995 | 
| P+ H | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 2S 40C 80T | 384 [GiB] | 5fdfe80d6176752d3502b008 | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+--------------------------+
```

JSON output

```
# iserver get servers --column id --group p2b

[
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
            "LatestMoid": null,
            "Last": []
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "Moid": "5fdf9c786176752d35e47110",
        "DeviceMoId": "5fdf9c676f72612d300a9c8d",
        "Name": "comp-2-p2b-eu-spdc-WZP23400AK4",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AK4",
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
        "ManagementIp": "10.58.50.42",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "Moid": "5fdf9d026176752d35e4ac4e",
        "DeviceMoId": "5fdf9cf26f72612d300aaca0",
        "Name": "comp-3-p2b-eu-spdc-WZP23400AKL",
        "Model": "UCSC-C240-M5SN",
        "Serial": "WZP23400AKL",
        "ManagementMode": "IntersightStandalone",
        "OperPowerState": "off",
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
        "ManagementIp": "10.58.50.43",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "Moid": "5fdfa1806176752d35e678c2",
        "DeviceMoId": "5fdfa1686f72612d300b383f",
        "Name": "comp-4-p2b-eu-spdc-WMP240400FM",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP240400FM",
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
        "ManagementIp": "10.58.50.44",
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
        "Groups": "p2b,pod2b,test,self-test-power,power",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "Moid": "5fdfe47f6176752d35001995",
        "DeviceMoId": "5fdfe4666f72612d30130510",
        "Name": "comp-6-p2b-eu-spdc-WMP24040059",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP24040059",
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
        "ManagementIp": "10.58.50.46",
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
        "Groups": "p2b,pod2b,test,self-test-power,self-test-locator,power",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "Moid": "5fdfe80d6176752d3502b008",
        "DeviceMoId": "5fdfe7d86f72612d30136fed",
        "Name": "comp-7-p2b-eu-spdc-WMP24040061",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP24040061",
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
        "ManagementIp": "10.58.50.47",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
    {
        "Moid": "5fdfdc3b6176752d35fce0a9",
        "DeviceMoId": "5fdfdc206f72612d30120ab4",
        "Name": "comp-5-p2b-eu-spdc-WMP2404000R",
        "Model": "UCSC-C220-M5SX",
        "Serial": "WMP2404000R",
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
        "ManagementIp": "10.58.50.45",
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    }
]
```

Developer output

```
# iserver get servers --column id --group p2b

Developer output

{
    "duration": 11349,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 10214
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
        "lines": 2481
    }
}

Log: debug
-----------

[2022-12-08 22:10:06.550564]	[computes_info.get]	Get servers settings: {
    "locator": true,
    "workflow": 86400,
    "registration": true,
    "rack": true,
    "blade": true,
    "id": true,
    "cpu": false,
    "memory": false,
    "fw": false,
    "pci": false,
    "fan": false,
    "psu": false,
    "group": false,
    "storage": false,
    "server_setting_id": false,
    "power": false,
    "thermal": false,
    "env": false
}
[2022-12-08 22:10:06.554615]	[computes_info.get]	Get servers match rules: {
    "name": "",
    "model": "",
    "ip": [],
    "serials": [
        "WZP23400AJW",
        "WZP23400AK4",
        "WZP23400AKL",
        "WMP240400FM",
        "WMP2404000R",
        "WMP24040059",
        "WMP24040061"
    ],
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
[2022-12-08 22:10:11.944714]	[computes_info.get]	All 103 servers base information in 5386 ms
[2022-12-08 22:10:11.946709]	[computes_info.get]	Base filter 7 servers in 0 ms
[2022-12-08 22:10:17.151593]	[compute_info.get]	{
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
[2022-12-08 22:10:17.157263]	[computes_info.get_server_info]	Thread result: 5fdf9c016176752d35e44795
[2022-12-08 22:10:17.173819]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c6b6176752d35e46d1c",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c6b6176752d35e46d1c"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cfe6176752d35e4aa7f",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa7f"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cfe6176752d35e4aa85",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa85"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cfe6176752d35e4aa8b",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa8b"
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
    "AssetTag": "022C2F7",
    "AvailableMemory": 393216,
    "BiosBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c756176752d35e4704d",
        "ObjectType": "bios.BootMode",
        "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdf9c756176752d35e4704d"
    },
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "60d5ee256176752d359b9914",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5ee256176752d359b9914"
    },
    "Biosunits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c736176752d35e46f8c",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/5fdf9c736176752d35e46f8c"
        }
    ],
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9cb86176752d35e48ebd",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/5fdf9cb86176752d35e48ebd"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c7c6176752d35e472bd",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/5fdf9c7c6176752d35e472bd"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9ca56176752d35e4844f",
        "ObjectType": "boot.DeviceBootSecurity",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9ca56176752d35e4844f"
    },
    "BootDeviceBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9ca46176752d35e483e0",
        "ObjectType": "boot.DeviceBootMode",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9ca46176752d35e483e0"
    },
    "BootHddDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000c066176752d35b76c32",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000c066176752d35b76c32"
        }
    ],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000bff6176752d35b769c9",
            "ObjectType": "boot.PxeDevice",
            "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000bff6176752d35b769c9"
        }
    ],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6013f1466176752d35458cdb",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1466176752d35458cdb"
        }
    ],
    "ClassId": "compute.RackUnit",
    "ComputePersonality": [],
    "ConnectionStatus": "",
    "CreateTime": "2020-12-20T18:48:24.465Z",
    "DeviceMoId": "5fdf9c676f72612d300a9c8d",
    "Dn": "sys/rack-unit-1",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "Fanmodules": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e4777c",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e4777c"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e4777e",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e4777e"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47780",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47780"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47782",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47782"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47784",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47784"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47786",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47786"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47788",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47788"
        }
    ],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cf66176752d35e4a75b",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9cf66176752d35e4a75b"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.50.42",
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
        "Moid": "5fdf9c8b6176752d35e47959",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdf9c8b6176752d35e47959"
    },
    "ManagementMode": "IntersightStandalone",
    "MemoryArrays": [],
    "MemorySpeed": "2933",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.50.42",
    "ModTime": "2022-12-07T01:57:13.203Z",
    "Model": "UCSC-C240-M5SN",
    "Moid": "5fdf9c786176752d35e47110",
    "Name": "comp-2-p2b-eu-spdc-WZP23400AK4",
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
        "5fdf9c676f72612d300a9c8d"
    ],
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496d1",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d1"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496d3",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d3"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496d5",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d5"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496d7",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d7"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496da",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496da"
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
            "Moid": "5fdf9c856176752d35e476b8",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c856176752d35e476b8"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c856176752d35e476ba",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c856176752d35e476ba"
        }
    ],
    "RackEnclosureSlot": null,
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c676f72612d300a9c8d",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9c676f72612d300a9c8d"
    },
    "Revision": "",
    "Rn": "",
    "SasExpanders": [],
    "Serial": "WZP23400AK4",
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
        "Moid": "5fdf9cc96176752d35e49601",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/5fdf9cc96176752d35e49601"
    },
    "TopologyScanStatus": "",
    "TotalMemory": 393216,
    "TunneledKvm": false,
    "UnitPersonality": [],
    "UserLabel": "comp-2-p2b-eu-spdc-WZP23400AK4",
    "Uuid": "B813910F-BFD2-439F-9C3B-75B376C5B160",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:10:17.178824]	[computes_info.get_server_info]	Thread result: 5fdf9c786176752d35e47110
[2022-12-08 22:10:17.192037]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cf56176752d35e4a70f",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cf56176752d35e4a70f"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d896176752d35e4e0b6",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9d896176752d35e4e0b6"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d896176752d35e4e0bc",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9d896176752d35e4e0bc"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d896176752d35e4e0c2",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9d896176752d35e4e0c2"
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
    "AssetTag": "022C2CE",
    "AvailableMemory": 393216,
    "BiosBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9d006176752d35e4aae0",
        "ObjectType": "bios.BootMode",
        "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdf9d006176752d35e4aae0"
    },
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "60d5ee266176752d359b9a6f",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5ee266176752d359b9a6f"
    },
    "Biosunits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cfd6176752d35e4aa25",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/5fdf9cfd6176752d35e4aa25"
        }
    ],
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9d426176752d35e4c645",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/5fdf9d426176752d35e4c645"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9d066176752d35e4aebe",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/5fdf9d066176752d35e4aebe"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9d2f6176752d35e4bf2f",
        "ObjectType": "boot.DeviceBootSecurity",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9d2f6176752d35e4bf2f"
    },
    "BootDeviceBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9d2e6176752d35e4bef4",
        "ObjectType": "boot.DeviceBootMode",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9d2e6176752d35e4bef4"
    },
    "BootHddDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000c046176752d35b76bd5",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000c046176752d35b76bd5"
        }
    ],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000bfd6176752d35b7692a",
            "ObjectType": "boot.PxeDevice",
            "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000bfd6176752d35b7692a"
        }
    ],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6013f1486176752d35458daf",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1486176752d35458daf"
        }
    ],
    "ClassId": "compute.RackUnit",
    "ComputePersonality": [],
    "ConnectionStatus": "",
    "CreateTime": "2020-12-20T18:50:42.597Z",
    "DeviceMoId": "5fdf9cf26f72612d300aaca0",
    "Dn": "sys/rack-unit-1",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "Fanmodules": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d116176752d35e4b355",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b355"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d116176752d35e4b357",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b357"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d116176752d35e4b359",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b359"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d116176752d35e4b35b",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b35b"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d116176752d35e4b35d",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b35d"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d116176752d35e4b35f",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b35f"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d116176752d35e4b361",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b361"
        }
    ],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d806176752d35e4de4d",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9d806176752d35e4de4d"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.50.43",
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
        "Moid": "5fdf9d156176752d35e4b534",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdf9d156176752d35e4b534"
    },
    "ManagementMode": "IntersightStandalone",
    "MemoryArrays": [],
    "MemorySpeed": "2933",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.50.43",
    "ModTime": "2022-12-07T05:36:31.071Z",
    "Model": "UCSC-C240-M5SN",
    "Moid": "5fdf9d026176752d35e4ac4e",
    "Name": "comp-3-p2b-eu-spdc-WZP23400AKL",
    "NumAdaptors": 1,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 0,
    "NumFcHostInterfaces": 0,
    "NumThreads": 80,
    "ObjectType": "compute.RackUnit",
    "OperPowerState": "off",
    "OperReason": [],
    "OperState": "",
    "Operability": "",
    "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "5fdf9cf26f72612d300aaca0"
    ],
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d556176752d35e4cd3d",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd3d"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d556176752d35e4cd41",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd41"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d556176752d35e4cd43",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd43"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d556176752d35e4cd48",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd48"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d566176752d35e4cd4a",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9d566176752d35e4cd4a"
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
            "Moid": "5fdf9d0f6176752d35e4b2a3",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9d0f6176752d35e4b2a3"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9d0f6176752d35e4b2a5",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9d0f6176752d35e4b2a5"
        }
    ],
    "RackEnclosureSlot": null,
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9cf26f72612d300aaca0",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9cf26f72612d300aaca0"
    },
    "Revision": "",
    "Rn": "",
    "SasExpanders": [],
    "Serial": "WZP23400AKL",
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
        "Moid": "5fdf9d536176752d35e4cc5f",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/5fdf9d536176752d35e4cc5f"
    },
    "TopologyScanStatus": "",
    "TotalMemory": 393216,
    "TunneledKvm": false,
    "UnitPersonality": [],
    "UserLabel": "comp-3-p2b-eu-spdc-WZP23400AKL",
    "Uuid": "11942B96-9C29-4871-924F-F42877A98020",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:10:17.208515]	[compute_info.get]	{
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
        "Health": "Healthy",
        "Info": 0,
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
    "ComputePersonality": [],
    "ConnectionStatus": "",
    "CreateTime": "2020-12-20T19:09:52.345Z",
    "DeviceMoId": "5fdfa1686f72612d300b383f",
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
    "Lifecycle": "None",
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
    "ModTime": "2022-12-07T01:48:26.821Z",
    "Model": "UCSC-C220-M5SX",
    "Moid": "5fdfa1806176752d35e678c2",
    "Name": "comp-4-p2b-eu-spdc-WMP240400FM",
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
    "UserLabel": "comp-4-p2b-eu-spdc-WMP240400FM",
    "Uuid": "E6FB96C5-2DA8-465D-A83E-E1764CA90D5B",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:10:17.201531]	[computes_info.get_server_info]	Thread result: 5fdf9d026176752d35e4ac4e
[2022-12-08 22:10:17.214736]	[computes_info.get_server_info]	Thread result: 5fdfa1806176752d35e678c2
[2022-12-08 22:10:17.231520]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc830b76752d3139cb9dec",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/61dc830b76752d3139cb9dec"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc839f76752d3139cbb982",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/61dc839f76752d3139cbb982"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc839f76752d3139cbb988",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/61dc839f76752d3139cbb988"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc839f76752d3139cbb98e",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/61dc839f76752d3139cbb98e"
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
    "AssetTag": "022C2B4",
    "AvailableMemory": 393216,
    "BiosBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "61dc833676752d3139cba702",
        "ObjectType": "bios.BootMode",
        "link": "https://www.intersight.com/api/v1/bios/BootModes/61dc833676752d3139cba702"
    },
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "61dc832e76752d3139cba576",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61dc832e76752d3139cba576"
    },
    "Biosunits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc832476752d3139cba32d",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/61dc832476752d3139cba32d"
        }
    ],
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "61dc838f76752d3139cbb6f8",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/61dc838f76752d3139cbb6f8"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "61dc833176752d3139cba603",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/61dc833176752d3139cba603"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": {
        "ClassId": "mo.MoRef",
        "Moid": "61dc839176752d3139cbb771",
        "ObjectType": "boot.DeviceBootSecurity",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61dc839176752d3139cbb771"
    },
    "BootDeviceBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "61dc835076752d3139cbabc5",
        "ObjectType": "boot.DeviceBootMode",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/61dc835076752d3139cbabc5"
    },
    "BootHddDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc839076752d3139cbb71a",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/61dc839076752d3139cbb71a"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "633e7c0876752d31394170ac",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/633e7c0876752d31394170ac"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "63467f3976752d3139a03cdb",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/63467f3976752d3139a03cdb"
        }
    ],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "61e1412476752d31392f7477",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/61e1412476752d31392f7477"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "633e7c0876752d31394170ae",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/633e7c0876752d31394170ae"
        }
    ],
    "ClassId": "compute.RackUnit",
    "ComputePersonality": [],
    "ConnectionStatus": "",
    "CreateTime": "2020-12-20T23:55:43.055Z",
    "DeviceMoId": "5fdfe4666f72612d30130510",
    "Dn": "sys/rack-unit-1",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "Fanmodules": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc837776752d3139cbb2de",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/61dc837776752d3139cbb2de"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc837776752d3139cbb2e0",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/61dc837776752d3139cbb2e0"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc837776752d3139cbb2e2",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/61dc837776752d3139cbb2e2"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc837876752d3139cbb2e4",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/61dc837876752d3139cbb2e4"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc837876752d3139cbb2ea",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/61dc837876752d3139cbb2ea"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc837876752d3139cbb2ec",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/61dc837876752d3139cbb2ec"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc837876752d3139cbb2ee",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/61dc837876752d3139cbb2ee"
        }
    ],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc839d76752d3139cbb954",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61dc839d76752d3139cbb954"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.50.46",
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
        "Moid": "61dc835176752d3139cbabff",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/61dc835176752d3139cbabff"
    },
    "ManagementMode": "IntersightStandalone",
    "MemoryArrays": [],
    "MemorySpeed": "2933",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.50.46",
    "ModTime": "2022-12-07T01:49:45.457Z",
    "Model": "UCSC-C220-M5SX",
    "Moid": "5fdfe47f6176752d35001995",
    "Name": "comp-6-p2b-eu-spdc-WMP24040059",
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
        "5fdfe4666f72612d30130510"
    ],
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc838276752d3139cbb4f3",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/61dc838276752d3139cbb4f3"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc838376752d3139cbb4f9",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/61dc838376752d3139cbb4f9"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc838376752d3139cbb4fb",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/61dc838376752d3139cbb4fb"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc838376752d3139cbb4fd",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/61dc838376752d3139cbb4fd"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc838376752d3139cbb4ff",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/61dc838376752d3139cbb4ff"
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
            "Moid": "61dc832c76752d3139cba4f4",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/61dc832c76752d3139cba4f4"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "61dc832c76752d3139cba4fa",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/61dc832c76752d3139cba4fa"
        }
    ],
    "RackEnclosureSlot": null,
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfe4666f72612d30130510",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdfe4666f72612d30130510"
    },
    "Revision": "",
    "Rn": "",
    "SasExpanders": [],
    "Serial": "WMP24040059",
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
        "Moid": "5fdfe4d06176752d35003724",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/5fdfe4d06176752d35003724"
    },
    "TopologyScanStatus": "",
    "TotalMemory": 393216,
    "TunneledKvm": false,
    "UnitPersonality": [],
    "UserLabel": "comp-6-p2b-eu-spdc-WMP24040059",
    "Uuid": "0C455BAB-4534-41B2-B84F-C27E202D2D45",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:10:17.236620]	[computes_info.get_server_info]	Thread result: 5fdfe47f6176752d35001995
[2022-12-08 22:10:17.252519]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80c6176752d3502af12",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfe80c6176752d3502af12"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe8786176752d3502df2e",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfe8786176752d3502df2e"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe8786176752d3502df34",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfe8786176752d3502df34"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe8786176752d3502df3a",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfe8786176752d3502df3a"
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
    "AssetTag": "022C32A",
    "AvailableMemory": 393216,
    "BiosBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfe80d6176752d3502aff4",
        "ObjectType": "bios.BootMode",
        "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdfe80d6176752d3502aff4"
    },
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "60d591f66176752d356a9a0d",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d591f66176752d356a9a0d"
    },
    "Biosunits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80d6176752d3502afd6",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/5fdfe80d6176752d3502afd6"
        }
    ],
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfe82e6176752d3502bfe7",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/5fdfe82e6176752d3502bfe7"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfe80d6176752d3502b05b",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/5fdfe80d6176752d3502b05b"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfe8176176752d3502b687",
        "ObjectType": "boot.DeviceBootSecurity",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdfe8176176752d3502b687"
    },
    "BootDeviceBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfe8176176752d3502b656",
        "ObjectType": "boot.DeviceBootMode",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdfe8176176752d3502b656"
    },
    "BootHddDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000bfa6176752d35b7684c",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000bfa6176752d35b7684c"
        }
    ],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000bf76176752d35b76661",
            "ObjectType": "boot.PxeDevice",
            "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000bf76176752d35b76661"
        }
    ],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6013f13a6176752d354587d4",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f13a6176752d354587d4"
        }
    ],
    "ClassId": "compute.RackUnit",
    "ComputePersonality": [],
    "ConnectionStatus": "",
    "CreateTime": "2020-12-21T00:10:53.684Z",
    "DeviceMoId": "5fdfe7d86f72612d30136fed",
    "Dn": "sys/rack-unit-1",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "Fanmodules": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80e6176752d3502b139",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b139"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80e6176752d3502b13b",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b13b"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80e6176752d3502b13d",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b13d"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80e6176752d3502b13f",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b13f"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80e6176752d3502b141",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b141"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80e6176752d3502b143",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b143"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80e6176752d3502b145",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b145"
        }
    ],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe8706176752d3502dc1c",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdfe8706176752d3502dc1c"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.50.47",
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
        "Moid": "5fdfe80f6176752d3502b1ab",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdfe80f6176752d3502b1ab"
    },
    "ManagementMode": "IntersightStandalone",
    "MemoryArrays": [],
    "MemorySpeed": "2933",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.50.47",
    "ModTime": "2022-12-07T02:07:34.65Z",
    "Model": "UCSC-C220-M5SX",
    "Moid": "5fdfe80d6176752d3502b008",
    "Name": "comp-7-p2b-eu-spdc-WMP24040061",
    "NumAdaptors": 1,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 2,
    "NumFcHostInterfaces": 2,
    "NumThreads": 80,
    "ObjectType": "compute.RackUnit",
    "OperPowerState": "on",
    "OperReason": [],
    "OperState": "",
    "Operability": "",
    "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "5fdfe7d86f72612d30136fed"
    ],
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe8456176752d3502c9f4",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502c9f4"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe8456176752d3502c9f9",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502c9f9"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe8456176752d3502c9fb",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502c9fb"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe8456176752d3502c9fe",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502c9fe"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe8456176752d3502ca01",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502ca01"
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
            "Moid": "5fdfe80e6176752d3502b0f2",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdfe80e6176752d3502b0f2"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfe80e6176752d3502b0f5",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdfe80e6176752d3502b0f5"
        }
    ],
    "RackEnclosureSlot": null,
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfe7d86f72612d30136fed",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdfe7d86f72612d30136fed"
    },
    "Revision": "",
    "Rn": "",
    "SasExpanders": [],
    "Serial": "WMP24040061",
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
        "Moid": "5fdfe8436176752d3502c897",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/5fdfe8436176752d3502c897"
    },
    "TopologyScanStatus": "",
    "TotalMemory": 393216,
    "TunneledKvm": false,
    "UnitPersonality": [],
    "UserLabel": "comp-7-p2b-eu-spdc-WMP24040061",
    "Uuid": "B947D1F9-F0A0-4D6F-AF63-16A48DD0A96E",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:10:17.260013]	[computes_info.get_server_info]	Thread result: 5fdfe80d6176752d3502b008
[2022-12-08 22:10:17.216576]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc2c6176752d35fcd8af",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfdc2c6176752d35fcd8af"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdcbf6176752d35fd172c",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfdcbf6176752d35fd172c"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdcbf6176752d35fd1736",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfdcbf6176752d35fd1736"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdcbf6176752d35fd173c",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdfdcbf6176752d35fd173c"
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
    "AssetTag": "022C2C2",
    "AvailableMemory": 393216,
    "BiosBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfdc396176752d35fcdf96",
        "ObjectType": "bios.BootMode",
        "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdfdc396176752d35fcdf96"
    },
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "60d591f66176752d356a9a42",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d591f66176752d356a9a42"
    },
    "Biosunits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc346176752d35fcdd04",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/5fdfdc346176752d35fcdd04"
        }
    ],
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfdc756176752d35fcf7b3",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/5fdfdc756176752d35fcf7b3"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfdc3d6176752d35fce1ad",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/5fdfdc3d6176752d35fce1ad"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfdc5f6176752d35fcef2a",
        "ObjectType": "boot.DeviceBootSecurity",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdfdc5f6176752d35fcef2a"
    },
    "BootDeviceBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfdc5b6176752d35fcee4a",
        "ObjectType": "boot.DeviceBootMode",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdfdc5b6176752d35fcee4a"
    },
    "BootHddDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "638a273276752d3139ebca51",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/638a273276752d3139ebca51"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "638a33b576752d3139ee6e96",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/638a33b576752d3139ee6e96"
        }
    ],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "638a33b576752d3139ee6e92",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/638a33b576752d3139ee6e92"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "638a33b576752d3139ee6e94",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/638a33b576752d3139ee6e94"
        }
    ],
    "ClassId": "compute.RackUnit",
    "ComputePersonality": [],
    "ConnectionStatus": "",
    "CreateTime": "2020-12-20T23:20:27.032Z",
    "DeviceMoId": "5fdfdc206f72612d30120ab4",
    "Dn": "sys/rack-unit-1",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "Fanmodules": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc476176752d35fce724",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce724"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc476176752d35fce726",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce726"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc476176752d35fce728",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce728"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc476176752d35fce72a",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce72a"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc476176752d35fce72c",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce72c"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc476176752d35fce72e",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce72e"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc476176752d35fce730",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce730"
        }
    ],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdcb76176752d35fd1249",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdfdcb76176752d35fd1249"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.50.45",
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
        "Moid": "5fdfdc4c6176752d35fce94e",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdfdc4c6176752d35fce94e"
    },
    "ManagementMode": "IntersightStandalone",
    "MemoryArrays": [],
    "MemorySpeed": "2933",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.50.45",
    "ModTime": "2022-12-07T01:50:10.961Z",
    "Model": "UCSC-C220-M5SX",
    "Moid": "5fdfdc3b6176752d35fce0a9",
    "Name": "comp-5-p2b-eu-spdc-WMP2404000R",
    "NumAdaptors": 1,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 2,
    "NumFcHostInterfaces": 2,
    "NumThreads": 80,
    "ObjectType": "compute.RackUnit",
    "OperPowerState": "on",
    "OperReason": [],
    "OperState": "",
    "Operability": "",
    "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "5fdfdc206f72612d30120ab4"
    ],
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc8c6176752d35fd0298",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd0298"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc8c6176752d35fd029a",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd029a"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc8c6176752d35fd029c",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd029c"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc8c6176752d35fd029f",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd029f"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc8c6176752d35fd02a3",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd02a3"
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
            "Moid": "5fdfdc456176752d35fce61b",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdfdc456176752d35fce61b"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdfdc456176752d35fce620",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdfdc456176752d35fce620"
        }
    ],
    "RackEnclosureSlot": null,
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfdc206f72612d30120ab4",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdfdc206f72612d30120ab4"
    },
    "Revision": "",
    "Rn": "",
    "SasExpanders": [],
    "Serial": "WMP2404000R",
    "ServerId": 1,
    "ServiceProfile": "",
    "SharedScope": "",
    "StorageControllers": [],
    "StorageEnclosures": [],
    "Tags": [
        {
            "Key": "User",
            "Value": "vanniew"
        },
        {
            "Key": "Intersight.LicenseTier",
            "Value": "Premier"
        }
    ],
    "TopSystem": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdfdc8b6176752d35fd0207",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/5fdfdc8b6176752d35fd0207"
    },
    "TopologyScanStatus": "",
    "TotalMemory": 393216,
    "TunneledKvm": true,
    "UnitPersonality": [],
    "UserLabel": "comp-5-p2b-eu-spdc-WMP2404000R",
    "Uuid": "1419A230-1C67-48C6-AA3C-C7A27F567FD9",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:10:17.325214]	[computes_info.get_server_info]	Thread result: 5fdfdc3b6176752d35fce0a9
[2022-12-08 22:10:17.705534]	[computes_info.get]	Selected 7 servers with requested details in 5757 ms
[2022-12-08 22:10:17.707155]	[computes_info.get]	Total time 11155 ms


Log: isctl
-----------

2022-12-08 22:10:10.273268	True	3611	93	isctl get compute rackunit   -o json --top 100
2022-12-08 22:10:11.942720	True	1655	10	isctl get compute blade   -o json --top 100
2022-12-08 22:10:15.353885	True	1751	7	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '5fdfa1686f72612d300b383f', '5fdfdc206f72612d30120ab4', '5fdfe4666f72612d30130510', '5fdfe7d86f72612d30136fed')"  -o json --top 100
2022-12-08 22:10:15.429573	True	1446	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-07T22:10:13.000Z"  -o json --top 100
2022-12-08 22:10:15.435779	True	1751	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
```
