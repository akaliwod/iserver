# Server Details - Multiple Selected Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --cpu --memory --pci

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | 4  | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+

+--------+--------+----------------------+------+------------------------------------------+----------+-----------+-------+---------+---------+-------+----------+
| CPU Id | Socket | Vendor               | Arch | Model                                    | Presence | OperState | Cores | Enabled | Threads | Speed | Stepping |
+--------+--------+----------------------+------+------------------------------------------+----------+-----------+-------+---------+---------+-------+----------+
| 1      | CPU1   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | equipped | operable  | 20    | 20      | 40      | 2.5   | 7        | 
| 2      | CPU2   | Intel(R) Corporation | Xeon | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | equipped | operable  | 20    | 20      | 40      | 2.5   | 7        | 
+--------+--------+----------------------+------+------------------------------------------+----------+-----------+-------+---------+---------+-------+----------+

+-----------+-------+------+----------+-------------+-------------+--------------+--------------+----------------------+----------+------------+----------+
| Memory Id | Array | Bank | Location | Capacity    | Clock       | Form Factor  | Type         | Model                | Serial   | Oper State | Presence |
+-----------+-------+------+----------+-------------+-------------+--------------+--------------+----------------------+----------+------------+----------+
| 1         | 1     | 0    | DIMM_A1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73490 | operable   | equipped | 
| 2         | 1     | 0    | DIMM_A2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 3         | 1     | 0    | DIMM_B1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72CD9 | operable   | equipped | 
| 4         | 1     | 0    | DIMM_B2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 5         | 1     | 0    | DIMM_C1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348D | operable   | equipped | 
| 6         | 1     | 0    | DIMM_C2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 7         | 1     | 0    | DIMM_D1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734A7 | operable   | equipped | 
| 8         | 1     | 0    | DIMM_D2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 9         | 1     | 0    | DIMM_E1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73492 | operable   | equipped | 
| 10        | 1     | 0    | DIMM_E2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 11        | 1     | 0    | DIMM_F1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73498 | operable   | equipped | 
| 12        | 1     | 0    | DIMM_F2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 13        | 1     | 0    | DIMM_G1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F7348E | operable   | equipped | 
| 14        | 1     | 0    | DIMM_G2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 15        | 1     | 0    | DIMM_H1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73495 | operable   | equipped | 
| 16        | 1     | 0    | DIMM_H2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 17        | 1     | 0    | DIMM_J1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F72CCC | operable   | equipped | 
| 18        | 1     | 0    | DIMM_J2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 19        | 1     | 0    | DIMM_K1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73493 | operable   | equipped | 
| 20        | 1     | 0    | DIMM_K2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 21        | 1     | 0    | DIMM_L1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F73494 | operable   | equipped | 
| 22        | 1     | 0    | DIMM_L2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
| 23        | 1     | 0    | DIMM_M1  | 32768       | 2933        | DIMM         | DDR4         | 36ASF4G72PZ-2G9E2    | F0F734AD | operable   | equipped | 
| 24        | 1     | 0    | DIMM_M2  | unspecified | unspecified | undiscovered | undiscovered |                      |          | removed    | missing  | 
+-----------+-------+------+----------+-------------+-------------+--------------+--------------+----------------------+----------+------------+----------+

+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
| PCI Device Model                                                 | Pid               | SlotId | Vendor | Firmware           | Dn                                  |
+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
| Cisco(R) Ethernet Converged NIC XXV710-DA2                       | UCSC-PCIE-ID25GF  | 3      | 0x8086 | 0x8000B900-1.826.0 | sys/rack-unit-1/equipped-slot-3     | 
| Cisco(R) Ethernet Converged NIC XXV710-DA2                       | UCSC-PCIE-ID25GF  | 6      | 0x8086 | 0x8000B900-1.826.0 | sys/rack-unit-1/equipped-slot-6     | 
| Intel X550 LOM                                                   | UNKNOWN           | L      | 0x8086 | 0x800016F9-1.826.0 | sys/rack-unit-1/equipped-slot-L     | 
| Cisco UCS VIC 1457 MLOM                                          | UCSC-MLOM-C25Q-04 | MLOM   | 0x1137 | 5.2(2b)            | sys/rack-unit-1/equipped-slot-MLOM  | 
| Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | UCSC-RAID-M5      | MRAID  | 0x1000 | N/A                | sys/rack-unit-1/equipped-slot-MRAID | 
+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --cpu --memory --pci

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
    "CpuInfo": [
        {
            "Architecture": "Xeon",
            "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
            "NumCores": 20,
            "NumCoresEnabled": "20",
            "NumThreads": "40",
            "OperState": "operable",
            "Presence": "equipped",
            "ProcessorId": 1,
            "SocketDesignation": "CPU1",
            "Speed": 2.5,
            "Stepping": "7",
            "Vendor": "Intel(R) Corporation"
        },
        {
            "Architecture": "Xeon",
            "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
            "NumCores": 20,
            "NumCoresEnabled": "20",
            "NumThreads": "40",
            "OperState": "operable",
            "Presence": "equipped",
            "ProcessorId": 2,
            "SocketDesignation": "CPU2",
            "Speed": 2.5,
            "Stepping": "7",
            "Vendor": "Intel(R) Corporation"
        }
    ],
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C240-M5SN",
    "LocatorLedOn": false,
    "MemoryInfo": [
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-1",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_A1",
            "MemoryId": 1,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73490",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-2",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_A2",
            "MemoryId": 2,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-3",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_B1",
            "MemoryId": 3,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F72CD9",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-4",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_B2",
            "MemoryId": 4,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-5",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_C1",
            "MemoryId": 5,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F7348D",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-6",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_C2",
            "MemoryId": 6,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-7",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_D1",
            "MemoryId": 7,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F734A7",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-8",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_D2",
            "MemoryId": 8,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-9",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_E1",
            "MemoryId": 9,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73492",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-10",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_E2",
            "MemoryId": 10,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-11",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_F1",
            "MemoryId": 11,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73498",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-12",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_F2",
            "MemoryId": 12,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-13",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_G1",
            "MemoryId": 13,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F7348E",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-14",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_G2",
            "MemoryId": 14,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-15",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_H1",
            "MemoryId": 15,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73495",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-16",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_H2",
            "MemoryId": 16,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-17",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_J1",
            "MemoryId": 17,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F72CCC",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-18",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_J2",
            "MemoryId": 18,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-19",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_K1",
            "MemoryId": 19,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73493",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-20",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_K2",
            "MemoryId": 20,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-21",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_L1",
            "MemoryId": 21,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73494",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-22",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_L2",
            "MemoryId": 22,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-23",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_M1",
            "MemoryId": 23,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F734AD",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-24",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_M2",
            "MemoryId": 24,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": "",
            "MemoryArrayId": "5fdf9c416176752d35e45e6f",
            "ChassisId": null,
            "ServerId": "5fdf9c016176752d35e44795",
            "BoardId": "5fdf9c056176752d35e44930"
        }
    ],
    "PciDevicesInfo": [
        {
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "Pid": "UCSC-PCIE-ID25GF",
            "SlotId": "3",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x8000B900-1.826.0",
            "Dn": "sys/rack-unit-1/equipped-slot-3"
        },
        {
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "Pid": "UCSC-PCIE-ID25GF",
            "SlotId": "6",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x8000B900-1.826.0",
            "Dn": "sys/rack-unit-1/equipped-slot-6"
        },
        {
            "Model": "Intel X550 LOM",
            "Pid": "UNKNOWN",
            "SlotId": "L",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x800016F9-1.826.0",
            "Dn": "sys/rack-unit-1/equipped-slot-L"
        },
        {
            "Model": "Cisco UCS VIC 1457 MLOM",
            "Pid": "UCSC-MLOM-C25Q-04",
            "SlotId": "MLOM",
            "Vendor": "0x1137",
            "FirmwareVersion": "5.2(2b)",
            "Dn": "sys/rack-unit-1/equipped-slot-MLOM"
        },
        {
            "Model": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "Pid": "UCSC-RAID-M5",
            "SlotId": "MRAID",
            "Vendor": "0x1000",
            "FirmwareVersion": "N/A",
            "Dn": "sys/rack-unit-1/equipped-slot-MRAID"
        }
    ],
    "PciModels": [
        "UCSC-MLOM-C25Q-04",
        "UCSC-RAID-M5",
        "Intel X550 LOM",
        "UCSC-PCIE-ID25GF",
        "UCSC-PCIE-ID25GF"
    ],
    "FlagState": "P+ H",
    "FlagManagement": "CRi",
    "FlagWorkflow": "4"
}
```

Developer output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --cpu --memory --pci

Developer output

{
    "duration": 19772,
    "isctl": {
        "read": true,
        "calls": 8,
        "success": 8,
        "failed": 0,
        "total_time": 14952
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

[2022-12-08 23:12:19.881734]	[computes_info.get]	Get servers settings: {
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
[2022-12-08 23:12:19.883728]	[computes_info.get]	Get servers match rules: {
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
[2022-12-08 23:12:25.076544]	[computes_info.get]	All 103 servers base information in 5181 ms
[2022-12-08 23:12:25.078539]	[computes_info.get]	Base filter 1 servers in 0 ms
[2022-12-08 23:12:29.351553]	[compute_info.get]	{
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
[2022-12-08 23:12:29.354546]	[computes_info.get_server_info]	Thread result: 5fdf9c016176752d35e44795
[2022-12-08 23:12:29.414650]	[computes_info.get]	Selected 1 servers with requested details in 4335 ms
[2022-12-08 23:12:29.416644]	[computes_info.get]	Total time 9534 ms
[2022-12-08 23:12:29.425792]	[compute_info.get]	{
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

2022-12-08 23:12:23.290933	True	3338	93	isctl get compute rackunit   -o json --top 100
2022-12-08 23:12:25.074549	True	1781	10	isctl get compute blade   -o json --top 100
2022-12-08 23:12:31.070680	True	1642	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2022-12-08 23:12:33.240688	True	2164	42	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-01T23:12:31.000Z"  -o json --top 100
2022-12-08 23:12:34.719925	True	1456	2	isctl get processor unit --filter "ComputeBoard/Moid eq '5fdf9c056176752d35e44930'"  -o json --top 100
2022-12-08 23:12:36.126700	True	1383	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-08 23:12:37.891701	True	1738	24	isctl get memory unit --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-08 23:12:39.387022	True	1450	5	isctl get pci device --filter "Parent/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
```
