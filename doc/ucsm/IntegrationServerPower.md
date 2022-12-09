# Get Intersight Server with Power Information

```
# iserver get server --ip 10.58.52.36 --power

+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+
| SF   | MF | WF | Name                 | Model            | Serial      | IP          | CPU        | Memory    |
+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+
| P+ H | CU |    | FI-ucsb1-eu-spdc-1-4 | (B) UCSB-B200-M4 | FCH205371UU | 10.58.52.36 | 2S 24C 48T | 256 [GiB] | 
+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+

+--------------------+-------+-------+-------+-------+
| Power Statistics   | Value | Min   | Avg   | Max   |
+--------------------+-------+-------+-------+-------+
| Consumed Power (W) | 126.0 | 126.0 | 126.0 | 126.0 | 
| Input Current (A)  | 10.52 | 10.52 | 10.52 | 10.52 | 
| Input Voltage (V)  | 11.98 | 11.98 | 11.98 | 11.98 | 
+--------------------+-------+-------+-------+-------+
```

JSON Output

```
# iserver get server --ip 10.58.52.36 --power

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
    "Power": {
        "Data": {
            "dn": "sys/chassis-1/blade-4/board/power-stats",
            "time_collected": "2022-12-08T23:25:42.939",
            "chassis_rn": "chassis-1",
            "blade_rn": "blade-4",
            "consumed_power": 126.0,
            "input_current": 10.52,
            "input_voltage": 11.98,
            "consumed_power_avg": 126.0,
            "input_current_avg": 10.52,
            "input_voltage_avg": 11.98,
            "consumed_power_min": 126.0,
            "input_current_min": 10.52,
            "input_voltage_min": 11.98,
            "consumed_power_max": 126.0,
            "input_current_max": 10.52,
            "input_voltage_max": 11.98
        },
        "Summary": {
            "Source": "UCSM",
            "PowerNow": 126.0,
            "PowerMin": 126.0,
            "PowerAvg": 126.0,
            "PowerMax": 126.0
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
# iserver get server --ip 10.58.52.36 --power

Developer output

{
    "duration": 16123,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 8697
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
        "success": 5,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 2090,
        "disconnect_time": 0,
        "mo_time": 1511,
        "total_time": 3601
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

[2022-12-08 23:26:23.415616]	[computes_info.get]	Get servers settings: {
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
[2022-12-08 23:26:23.417615]	[computes_info.get]	Get servers match rules: {
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
[2022-12-08 23:26:28.491114]	[computes_info.get]	All 103 servers base information in 5058 ms
[2022-12-08 23:26:28.493108]	[computes_info.get]	Base filter 1 servers in 0 ms
[2022-12-08 23:26:31.689986]	[compute_info.get]	{
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
[2022-12-08 23:26:31.691946]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da74
[2022-12-08 23:26:31.777748]	[computes_info.get]	Selected 1 servers with requested details in 3283 ms
[2022-12-08 23:26:31.779727]	[computes_info.get]	Total time 8362 ms
[2022-12-08 23:26:31.789228]	[compute_info.get]	{
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

2022-12-08 23:26:26.753135	True	3215	93	isctl get compute rackunit   -o json --top 100
2022-12-08 23:26:28.490147	True	1720	10	isctl get compute blade   -o json --top 100
2022-12-08 23:26:33.328468	True	1536	1	isctl get asset deviceregistration  moid 618942976f72612d309dfbe1 -o json
2022-12-08 23:26:35.561003	True	2226	42	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-01T23:26:33.000Z"  -o json --top 100


Log: ucsm
----------

2022-12-08 23:26:37.239494	True	1653	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 23:26:37.763283	True	517	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 23:26:38.311722	True	544	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 23:26:38.762434	True	450	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 23:26:39.204103	True	437	disconnect vip-ucsb1.emea-sp.cisco.com
```
