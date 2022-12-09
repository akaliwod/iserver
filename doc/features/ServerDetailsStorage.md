# Server Details - Storage Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --storage

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | 4  | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+

Storage Controller
- Model                : Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)
- Vendor               : LSI Logic
- Serial               : SK00188839
- Presence             : equipped
- Pci Slot             : MRAID
- Controller Id        : MRAID
- Dn                   : sys/rack-unit-1/board/storage-SAS-MRAID
- Raid Support         : yes


Storage Controller
- Model                : 
- Vendor               : Cisco Systems Inc
- Serial               : 
- Presence             : equipped
- Pci Slot             : PCIe-Switch
- Controller Id        : PCIe-Switch
- Dn                   : sys/rack-unit-1/board/storage-NVMe-PCIe-Switch
- Raid Support         : N/A


+------------------+-------+------------+----------+----------------+---------+------+------------+----+-----------------------------------------------+
| Physical Disk Id | State | Size       | Presence | Model          | Vendor  | Type | Controller | VD | Dn                                            |
+------------------+-------+------------+----------+----------------+---------+------+------------+----+-----------------------------------------------+
| 10               | Good  | 914573 MB  | equipped | SSDSC2KB960G7K | ATA     | SSD  | MRAID      |    | sys/rack-unit-1/board/storage-SAS-MRAID/pd-10 | 
| 11               | Good  | 914573 MB  | equipped | SSDSC2KB960G7K | ATA     | SSD  | MRAID      |    | sys/rack-unit-1/board/storage-SAS-MRAID/pd-11 | 
| 12               | Good  | 914573 MB  | equipped | SSDSC2KB960G7K | ATA     | SSD  | MRAID      |    | sys/rack-unit-1/board/storage-SAS-MRAID/pd-12 | 
| 13               | Good  | 1143455 MB | equipped | ST1200MM0009   | SEAGATE | HDD  | MRAID      |    | sys/rack-unit-1/board/storage-SAS-MRAID/pd-13 | 
| 14               | Good  | 1143455 MB | equipped | ST1200MM0009   | SEAGATE | HDD  | MRAID      |    | sys/rack-unit-1/board/storage-SAS-MRAID/pd-14 | 
| 15               | Good  | 1143455 MB | equipped | ST1200MM0009   | SEAGATE | HDD  | MRAID      |    | sys/rack-unit-1/board/storage-SAS-MRAID/pd-15 | 
| 16               | Good  | 1143455 MB | equipped | ST1200MM0009   | SEAGATE | HDD  | MRAID      |    | sys/rack-unit-1/board/storage-SAS-MRAID/pd-16 | 
| 17               | Good  | 1143455 MB | equipped | ST1200MM0009   | SEAGATE | HDD  | MRAID      | 0  | sys/rack-unit-1/board/storage-SAS-MRAID/pd-17 | 
| 18               | Good  | 1143455 MB | equipped | AL15SEB120N    | TOSHIBA | HDD  | MRAID      | 0  | sys/rack-unit-1/board/storage-SAS-MRAID/pd-18 | 
| 9                | Good  | 914573 MB  | equipped | SSDSC2KB960G7K | ATA     | SSD  | MRAID      |    | sys/rack-unit-1/board/storage-SAS-MRAID/pd-9  | 
+------------------+-------+------------+----------+----------------+---------+------+------------+----+-----------------------------------------------+

+------------------+------------+----------------+--------+------+------------+----------------------------------------------+
| Virtual Drive Id | Size       | Physical Disks | Type   | Name | Controller | Dn                                           |
+------------------+------------+----------------+--------+------+------------+----------------------------------------------+
| 0                | 1143455 MB | 2              | RAID 1 | vd-0 | MRAID      | sys/rack-unit-1/board/storage-SAS-MRAID/vd-0 | 
+------------------+------------+----------------+--------+------+------------+----------------------------------------------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --storage

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
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C240-M5SN",
    "LocatorLedOn": false,
    "StorageControllersInfo": [
        {
            "Model": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "Moid": "635840e076752d31399d9215",
            "Vendor": "LSI Logic",
            "Serial": "SK00188839",
            "Presence": "equipped",
            "PciSlot": "MRAID",
            "ControllerId": "MRAID",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID",
            "RaidSupport": "yes",
            "PhysicalDiskCount": 10,
            "PhysicalDiskIds": [
                "635840e576752d31399d9373",
                "635840e576752d31399d9375",
                "635840e576752d31399d9377",
                "635840e576752d31399d9379",
                "635840e576752d31399d937b",
                "635840e676752d31399d937d",
                "635840e676752d31399d937f",
                "635840e676752d31399d9381",
                "635840e676752d31399d9383",
                "635840e676752d31399d9385"
            ],
            "VirtualDriveCount": 1,
            "VirtualDriveIds": [
                "638f666f76752d3139f6cc14"
            ]
        },
        {
            "Model": "",
            "Moid": "636ddf1876752d3139c8d4f5",
            "Vendor": "Cisco Systems Inc",
            "Serial": "",
            "Presence": "equipped",
            "PciSlot": "PCIe-Switch",
            "ControllerId": "PCIe-Switch",
            "Dn": "sys/rack-unit-1/board/storage-NVMe-PCIe-Switch",
            "RaidSupport": "N/A",
            "PhysicalDiskCount": 0,
            "PhysicalDiskIds": [],
            "VirtualDriveCount": 0,
            "VirtualDriveIds": []
        }
    ],
    "StorageControllersCount": 2,
    "VirtualDisks": [
        {
            "Moid": "638f666f76752d3139f6cc14",
            "Name": "vd-0",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/vd-0",
            "Size": "1143455 MB",
            "Type": "RAID 1",
            "VirtualDriveId": "0",
            "PhysicalDiskCount": 2,
            "StorageControllerId": "MRAID",
            "PhysicalDiskIds": [
                "17",
                "18"
            ]
        }
    ],
    "VirtualDiskCount": 1,
    "VirtualDiskCapacity": 1198999470080,
    "VirtualDiskCapacityUnit": "1.2 [TB]",
    "HddDisks": [
        {
            "Moid": "635840e576752d31399d937b",
            "DiskId": "13",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-13",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK654680000C024C6NE",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d937d",
            "DiskId": "14",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-14",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65J9T0000C025976H",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d937f",
            "DiskId": "15",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-15",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65HVV0000C024KK59",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d9381",
            "DiskId": "16",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-16",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65M390000C024KKSN",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d9383",
            "DiskId": "17",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-17",
            "DriveFirmware": "CN03",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK654FJ0000C024KKCC",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d9385",
            "DiskId": "18",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-18",
            "DriveFirmware": "5703",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "AL15SEB120N",
            "Pid": "AL15SEB120N",
            "Presence": "equipped",
            "Serial": "Y9G0A06DFJMF",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "TOSHIBA",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID"
        }
    ],
    "HddDiskCount": 6,
    "HddDiskCapacity": 7193996820480,
    "HddDiskCapacityUnit": "7.19 [TB]",
    "SsdDisks": [
        {
            "Moid": "635840e576752d31399d9375",
            "DiskId": "10",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-10",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002XE960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e576752d31399d9377",
            "DiskId": "11",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-11",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002VN960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e576752d31399d9379",
            "DiskId": "12",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-12",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS74610194960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e576752d31399d9373",
            "DiskId": "9",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-9",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002YU960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        }
    ],
    "SsdDiskCount": 4,
    "SsdDiskCapacity": 3835997192192,
    "SsdDiskCapacityUnit": "3.84 [TB]",
    "PhysicalDisks": [
        {
            "Moid": "635840e576752d31399d9375",
            "DiskId": "10",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-10",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002XE960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e576752d31399d9377",
            "DiskId": "11",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-11",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002VN960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e576752d31399d9379",
            "DiskId": "12",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-12",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS74610194960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e576752d31399d937b",
            "DiskId": "13",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-13",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK654680000C024C6NE",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d937d",
            "DiskId": "14",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-14",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65J9T0000C025976H",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d937f",
            "DiskId": "15",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-15",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65HVV0000C024KK59",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d9381",
            "DiskId": "16",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-16",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65M390000C024KKSN",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d9383",
            "DiskId": "17",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-17",
            "DriveFirmware": "CN03",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK654FJ0000C024KKCC",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e676752d31399d9385",
            "DiskId": "18",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-18",
            "DriveFirmware": "5703",
            "DriveState": "Online",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "AL15SEB120N",
            "Pid": "AL15SEB120N",
            "Presence": "equipped",
            "Serial": "Y9G0A06DFJMF",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "TOSHIBA",
            "VirtualDriveMoid": "638f666f76752d3139f6cc14",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "635840e576752d31399d9373",
            "DiskId": "9",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-9",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002YU960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        }
    ],
    "PhysicalDiskCount": 10,
    "PhysicalDiskCapacity": 11029994012672,
    "PhysicalDiskCapacityUnit": "11.03 [TB]",
    "StorageDrives": "2C 6H 4S 1VD",
    "StorageCapacity": "R 11.03 [TB] , VD 1.2 [TB]",
    "StorageSummary": "2C 6H 4S 1VD R11.03 [TB] L1.2 [TB]",
    "FlagState": "P+ H",
    "FlagManagement": "CRi",
    "FlagWorkflow": "4"
}
```

Developer output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --storage

Developer output

{
    "duration": 22890,
    "isctl": {
        "read": true,
        "calls": 8,
        "success": 8,
        "failed": 0,
        "total_time": 15914
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
        "lines": 722
    }
}

Log: debug
-----------

[2022-12-08 23:10:16.556520]	[computes_info.get]	Get servers settings: {
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
[2022-12-08 23:10:16.558534]	[computes_info.get]	Get servers match rules: {
    "name": "comp-1-p2b-eu-spdc-WZP23400AJW",
    "ip": [],
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
[2022-12-08 23:10:22.245403]	[computes_info.get]	All 103 servers base information in 5682 ms
[2022-12-08 23:10:22.247399]	[computes_info.get]	Base filter 1 servers in 0 ms
[2022-12-08 23:10:27.288960]	[compute_info.get]	{
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
[2022-12-08 23:10:27.292947]	[computes_info.get_server_info]	Thread result: 5fdf9c016176752d35e44795
[2022-12-08 23:10:27.359901]	[computes_info.get]	Selected 1 servers with requested details in 5111 ms
[2022-12-08 23:10:27.361097]	[computes_info.get]	Total time 10803 ms
[2022-12-08 23:10:27.372057]	[compute_info.get]	{
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

2022-12-08 23:10:20.392702	True	3750	93	isctl get compute rackunit   -o json --top 100
2022-12-08 23:10:22.243446	True	1839	10	isctl get compute blade   -o json --top 100
2022-12-08 23:10:28.863632	True	1489	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2022-12-08 23:10:31.196792	True	2326	42	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-01T23:10:28.000Z"  -o json --top 100
2022-12-08 23:10:32.934175	True	1706	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-08 23:10:34.513315	True	1557	2	isctl get storage controller --filter "Parent/Moid eq '5fdf9c056176752d35e44930'"  -o json --top 100
2022-12-08 23:10:36.047674	True	1509	1	isctl get storage virtualdrive --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-08 23:10:39.222692	True	1738	10	isctl get storage physicaldisk --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
```
