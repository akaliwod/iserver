# Server Details - All Information

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --all

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

+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
| PCI Device Model                                                 | Pid               | SlotId | Vendor | Firmware           | Dn                                  |
+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+
| Cisco(R) Ethernet Converged NIC XXV710-DA2                       | UCSC-PCIE-ID25GF  | 3      | 0x8086 | 0x8000B900-1.826.0 | sys/rack-unit-1/equipped-slot-3     | 
| Cisco(R) Ethernet Converged NIC XXV710-DA2                       | UCSC-PCIE-ID25GF  | 6      | 0x8086 | 0x8000B900-1.826.0 | sys/rack-unit-1/equipped-slot-6     | 
| Intel X550 LOM                                                   | UNKNOWN           | L      | 0x8086 | 0x800016F9-1.826.0 | sys/rack-unit-1/equipped-slot-L     | 
| Cisco UCS VIC 1457 MLOM                                          | UCSC-MLOM-C25Q-04 | MLOM   | 0x1137 | 5.2(2b)            | sys/rack-unit-1/equipped-slot-MLOM  | 
| Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | UCSC-RAID-M5      | MRAID  | 0x1000 | N/A                | sys/rack-unit-1/equipped-slot-MRAID | 
+------------------------------------------------------------------+-------------------+--------+--------+--------------------+-------------------------------------+

+---------------+-----------+----------+--------------------------------+
| Fan Module Id | OperState | Presence | Dn                             |
+---------------+-----------+----------+--------------------------------+
| 1             | operable  | equipped | sys/rack-unit-1/fan-module-1-1 | 
| 2             | operable  | equipped | sys/rack-unit-1/fan-module-1-2 | 
| 3             | operable  | equipped | sys/rack-unit-1/fan-module-1-3 | 
| 4             | operable  | equipped | sys/rack-unit-1/fan-module-1-4 | 
| 5             | operable  | equipped | sys/rack-unit-1/fan-module-1-5 | 
| 6             | operable  | equipped | sys/rack-unit-1/fan-module-1-6 | 
| 7             | unknown   | missing  | sys/rack-unit-1/fan-module-1-7 | 
+---------------+-----------+----------+--------------------------------+

+---------------+-------------+-------------------+-----------------------+
| PSU Model     | Serial      | Vendor            | Dn                    |
+---------------+-------------+-------------------+-----------------------+
| PS-2112-9S-LF | LIT241244MU | Cisco Systems Inc | sys/rack-unit-1/psu-1 | 
| PS-2112-9S-LF | LIT241244Z5 | Cisco Systems Inc | sys/rack-unit-1/psu-2 | 
+---------------+-------------+-------------------+-----------------------+

Power Consumption (Watt)
------------------------
- Current      : 324
- Min          : 176
- Average      : 330
- Max          : 435
- Limit action : NoAction


+----------------+---------+--------+--------+-----------------+
| Sensor Name    | State   | Health | Volts  | Upper Threshold |
+----------------+---------+--------+--------+-----------------+
| PSU1_VOUT      | Enabled | OK     | 12     | 14              | 
| PSU2_VOUT      | Enabled | OK     | 12.2   | 14              | 
| P12V           | Enabled | OK     | 11.832 | 13.166          | 
| P3V_BAT_SCALED | Enabled | OK     | 3.011  | 3.588           | 
+----------------+---------+--------+--------+-----------------+

+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU Name | State   | Health | Serial      | Firmware | Output (Watt) | Input (Watt) | Max (V) | Min (V) | Max (Hz) | Min (Hz) |
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU1     | Enabled | OK     | LIT241244MU | 10062019 | 141           | 164          | 264     | 180     | 63       | 47       | 
| PSU2     | Enabled | OK     | LIT241244Z5 | 10062019 | 146           | 165          | 264     | 180     | 63       | 47       | 
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+

Thermal Summary
---------------
- Sensors Health   : True
- Highest (C)      : 54
- Smallest Gap (C) : 20
- Over Threshold   : 0
- Fans Health      : True


+------------------+---------+--------+------------------+-----------------+---------------------------+
| Sensor Name      | State   | Health | Location         | Value (Celcius) | Upper Threshold (Celcius) |
+------------------+---------+--------+------------------+-----------------+---------------------------+
| DDR4_P1_A1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P1_B1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P1_C1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P1_D1_TMP   | Enabled | OK     | Memory           | 29              | 85                        | 
| DDR4_P1_E1_TMP   | Enabled | OK     | Memory           | 29              | 85                        | 
| DDR4_P1_F1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P2_G1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_H1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_J1_TMP   | Enabled | OK     | Memory           | 28              | 85                        | 
| DDR4_P2_K1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_L1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| DDR4_P2_M1_TMP   | Enabled | OK     | Memory           | 27              | 85                        | 
| MLOM_TEMP        | Enabled | OK     | NetworkingDevice | 54              | 90                        | 
| P1_TEMP_SENS     | Enabled | OK     | CPU              | 39              | 100                       | 
| P2_TEMP_SENS     | Enabled | OK     | CPU              | 39.5            | 100                       | 
| PCH_TEMP_SENS    | Enabled | OK     | SystemBoard      | 33              | 85                        | 
| PCIE_SWITCH_TMP  | Enabled | OK     | SystemBoard      | 40              | 100                       | 
| PSU1_TEMP        | Enabled | OK     | PowerSupply      | 21              | 65                        | 
| PSU2_TEMP        | Enabled | OK     | PowerSupply      | 20              | 65                        | 
| RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 32              | 70                        | 
| RISER1_TEMP      | Enabled | OK     | SystemBoard      | 24              | 70                        | 
| RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 32              | 70                        | 
| RISER2_TEMP      | Enabled | OK     | SystemBoard      | 28              | 70                        | 
| TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 25              | 45                        | 
+------------------+---------+--------+------------------+-----------------+---------------------------+

+-----------------+---------+--------+----------+
| Fan Name        | State   | Health | Value    |
+-----------------+---------+--------+----------+
| MOD1_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD1_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD2_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD2_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD3_FAN1_SPEED | Enabled | OK     | 7070 RPM | 
| MOD3_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD4_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD4_FAN2_SPEED | Enabled | OK     | 7350 RPM | 
| MOD5_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD5_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD6_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD6_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD7_FAN1_SPEED | Absent  |        |          | 
+-----------------+---------+--------+----------+
```

JSON output

```
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --all

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
                    "ReadingVolts": 11.832,
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
                    "PowerOutputWatts": 141,
                    "LastPowerOutputWatts": 141,
                    "PowerInputWatts": 164,
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
                    "PowerOutputWatts": 146,
                    "LastPowerOutputWatts": 146,
                    "PowerInputWatts": 165,
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
    "Thermal": {
        "Data": {
            "Temperature": [
                {
                    "Name": "DDR4_P1_A1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 114,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_B1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 120,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_C1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 126,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_D1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 132,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 29,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_E1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 138,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 29,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P1_F1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 144,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_G1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 150,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_H1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 156,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_J1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 162,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_K1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 168,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_L1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 174,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "DDR4_P2_M1_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 180,
                    "PhysicalContext": "Memory",
                    "ReadingCelsius": 27,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "MLOM_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 60,
                    "PhysicalContext": "NetworkingDevice",
                    "ReadingCelsius": 54,
                    "UpperThresholdCritical": 90
                },
                {
                    "Name": "P1_TEMP_SENS",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 196,
                    "PhysicalContext": "CPU",
                    "ReadingCelsius": 39,
                    "UpperThresholdCritical": 100
                },
                {
                    "Name": "P2_TEMP_SENS",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 197,
                    "PhysicalContext": "CPU",
                    "ReadingCelsius": 39.5,
                    "UpperThresholdCritical": 100
                },
                {
                    "Name": "PCH_TEMP_SENS",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 209,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 33,
                    "UpperThresholdCritical": 85
                },
                {
                    "Name": "PCIE_SWITCH_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 239,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 40,
                    "UpperThresholdCritical": 100
                },
                {
                    "Name": "PSU1_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 207,
                    "PhysicalContext": "PowerSupply",
                    "ReadingCelsius": 21,
                    "UpperThresholdCritical": 65
                },
                {
                    "Name": "PSU2_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 208,
                    "PhysicalContext": "PowerSupply",
                    "ReadingCelsius": 20,
                    "UpperThresholdCritical": 65
                },
                {
                    "Name": "RISER1_INLET_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 250,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 32,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "RISER1_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 245,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 24,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "RISER2_INLET_TMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 249,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 32,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "RISER2_TEMP",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 246,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 28,
                    "UpperThresholdCritical": 70
                },
                {
                    "Name": "TEMP_SENS_FRONT",
                    "State": "Enabled",
                    "Health": "OK",
                    "SensorNumber": 84,
                    "PhysicalContext": "SystemBoard",
                    "ReadingCelsius": 25,
                    "UpperThresholdCritical": 45
                }
            ],
            "Fan": [
                {
                    "Name": "MOD1_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD1_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD2_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD2_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD3_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7070,
                    "Value": "7070 RPM"
                },
                {
                    "Name": "MOD3_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD4_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD4_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7350,
                    "Value": "7350 RPM"
                },
                {
                    "Name": "MOD5_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD5_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD6_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
                },
                {
                    "Name": "MOD6_FAN2_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 7056,
                    "Value": "7056 RPM"
                },
                {
                    "Name": "MOD7_FAN1_SPEED",
                    "State": "Absent",
                    "Health": "",
                    "PhysicalContext": "",
                    "ReadingUnits": "",
                    "Reading": "",
                    "Value": " "
                }
            ]
        },
        "Summary": {
            "FanHealth": true,
            "SensorHealth": true,
            "HighestTemperature": 54,
            "SmallestGap": 20,
            "OverThreshold": 0
        }
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
    "FanInfo": [
        {
            "Moid": "5fdf9c106176752d35e44d77",
            "ModuleId": 1,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-1",
            "On": true,
            "Name": "Fan Module 1",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e57",
                "5fdf9c126176752d35e44e6d"
            ]
        },
        {
            "Moid": "5fdf9c106176752d35e44d79",
            "ModuleId": 2,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-2",
            "On": true,
            "Name": "Fan Module 2",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e59",
                "5fdf9c126176752d35e44e65"
            ]
        },
        {
            "Moid": "5fdf9c106176752d35e44d7b",
            "ModuleId": 3,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-3",
            "On": true,
            "Name": "Fan Module 3",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e5f",
                "5fdf9c126176752d35e44e6f"
            ]
        },
        {
            "Moid": "5fdf9c106176752d35e44d7d",
            "ModuleId": 4,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-4",
            "On": true,
            "Name": "Fan Module 4",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e5b",
                "5fdf9c126176752d35e44e67"
            ]
        },
        {
            "Moid": "5fdf9c106176752d35e44d71",
            "ModuleId": 5,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-5",
            "On": true,
            "Name": "Fan Module 5",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e61",
                "5fdf9c126176752d35e44e69"
            ]
        },
        {
            "Moid": "5fdf9c106176752d35e44d73",
            "ModuleId": 6,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-6",
            "On": true,
            "Name": "Fan Module 6",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e5d",
                "5fdf9c126176752d35e44e63"
            ]
        },
        {
            "Moid": "5fdf9c106176752d35e44d75",
            "ModuleId": 7,
            "OperState": "unknown",
            "Presence": "missing",
            "Dn": "sys/rack-unit-1/fan-module-1-7",
            "On": false,
            "Name": "Fan Module 7",
            "FanCount": 2,
            "FanMoids": [
                "5fdf9c126176752d35e44e6b",
                "5fdf9c126176752d35e44e71"
            ]
        }
    ],
    "FanOn": 6,
    "FanCount": 7,
    "FanSummary": "6/7",
    "FanHealthy": false,
    "PsuInfo": [
        {
            "Moid": "5fdf9c0d6176752d35e44cf7",
            "Name": "",
            "Model": "PS-2112-9S-LF",
            "Serial": "LIT241244MU",
            "Vendor": "Cisco Systems Inc",
            "Dn": "sys/rack-unit-1/psu-1",
            "On": true,
            "Voltage": "ok"
        },
        {
            "Moid": "5fdf9c0d6176752d35e44cf9",
            "Name": "",
            "Model": "PS-2112-9S-LF",
            "Serial": "LIT241244Z5",
            "Vendor": "Cisco Systems Inc",
            "Dn": "sys/rack-unit-1/psu-2",
            "On": true,
            "Voltage": "ok"
        }
    ],
    "PsuOn": 2,
    "PsuCount": 2,
    "PsuSummary": "2/2",
    "PsuHealthy": true,
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
    "Fw": "4.2(2a)",
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
# iserver get server --name comp-1-p2b-eu-spdc-WZP23400AJW --all

Developer output

{
    "duration": 41807,
    "isctl": {
        "read": true,
        "calls": 14,
        "success": 14,
        "failed": 0,
        "total_time": 26783
    },
    "redfish": {
        "read": true,
        "success": 11,
        "failed": 0,
        "connect": 3,
        "disconnect": 0,
        "path": 8,
        "connect_time": 3867,
        "disconnect_time": 0,
        "path_time": 2565,
        "total_time": 6432
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

[2022-12-08 23:06:05.448647]	[computes_info.get]	Get servers settings: {
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
[2022-12-08 23:06:05.452637]	[computes_info.get]	Get servers match rules: {
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
[2022-12-08 23:06:11.193519]	[computes_info.get]	All 103 servers base information in 5739 ms
[2022-12-08 23:06:11.195513]	[computes_info.get]	Base filter 1 servers in 0 ms
[2022-12-08 23:06:16.482894]	[compute_info.get]	{
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
[2022-12-08 23:06:16.486838]	[computes_info.get_server_info]	Thread result: 5fdf9c016176752d35e44795
[2022-12-08 23:06:16.560939]	[computes_info.get]	Selected 1 servers with requested details in 5364 ms
[2022-12-08 23:06:16.562934]	[computes_info.get]	Total time 11112 ms
[2022-12-08 23:06:16.571746]	[compute_info.get]	{
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

2022-12-08 23:06:09.130238	True	3576	93	isctl get compute rackunit   -o json --top 100
2022-12-08 23:06:11.192521	True	2058	10	isctl get compute blade   -o json --top 100
2022-12-08 23:06:18.036437	True	1463	1	isctl get asset deviceregistration  moid 5fdf9be76f72612d300a8d81 -o json
2022-12-08 23:06:20.018699	True	1976	42	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-01T23:06:18.000Z"  -o json --top 100
2022-12-08 23:06:27.430269	True	1365	2	isctl get processor unit --filter "ComputeBoard/Moid eq '5fdf9c056176752d35e44930'"  -o json --top 100
2022-12-08 23:06:29.090991	True	1632	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-08 23:06:30.889030	True	1775	24	isctl get memory unit --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-08 23:06:32.829390	True	1893	7	isctl get equipment fanmodule --filter "Parent/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2022-12-08 23:06:34.380886	True	1519	2	isctl get equipment psu --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-08 23:06:36.323036	True	1897	5	isctl get pci device --filter "Parent/Moid eq '5fdf9c016176752d35e44795'"  -o json --top 100
2022-12-08 23:06:38.684991	True	1842	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-08 23:06:40.084240	True	1368	2	isctl get storage controller --filter "Parent/Moid eq '5fdf9c056176752d35e44930'"  -o json --top 100
2022-12-08 23:06:41.802168	True	1687	1	isctl get storage virtualdrive --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-08 23:06:46.022913	True	2732	10	isctl get storage physicaldisk --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100


Log: redfish
-------------

2022-12-08 23:06:21.745697	True	1691	connect 10.58.50.41
2022-12-08 23:06:21.809830	True	62	10.58.50.41:/redfish/v1/Systems
2022-12-08 23:06:21.873790	True	59	10.58.50.41:/redfish/v1/Chassis
2022-12-08 23:06:22.071749	True	193	10.58.50.41:/redfish/v1/Chassis/1
2022-12-08 23:06:22.916125	True	838	10.58.50.41:/redfish/v1/Chassis/1/Power
2022-12-08 23:06:24.627479	True	1699	connect 10.58.50.41
2022-12-08 23:06:24.688341	True	60	10.58.50.41:/redfish/v1/Systems
2022-12-08 23:06:24.751505	True	59	10.58.50.41:/redfish/v1/Chassis
2022-12-08 23:06:24.937700	True	180	10.58.50.41:/redfish/v1/Chassis/1
2022-12-08 23:06:26.058468	True	1114	10.58.50.41:/redfish/v1/Chassis/1/Thermal
2022-12-08 23:06:36.807317	True	477	disconnect 10.58.50.41
```
