# Get Intersight Server with Thermal Information

```
# iserver get server --ip 10.58.50.41 --thermal

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | 4  | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+

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
| PCIE_SWITCH_TMP  | Enabled | OK     | SystemBoard      | 39              | 100                       | 
| PSU1_TEMP        | Enabled | OK     | PowerSupply      | 21              | 65                        | 
| PSU2_TEMP        | Enabled | OK     | PowerSupply      | 19              | 65                        | 
| RISER1_INLET_TMP | Enabled | OK     | SystemBoard      | 32              | 70                        | 
| RISER1_TEMP      | Enabled | OK     | SystemBoard      | 24              | 70                        | 
| RISER2_INLET_TMP | Enabled | OK     | SystemBoard      | 32              | 70                        | 
| RISER2_TEMP      | Enabled | OK     | SystemBoard      | 27              | 70                        | 
| TEMP_SENS_FRONT  | Enabled | OK     | SystemBoard      | 25              | 45                        | 
+------------------+---------+--------+------------------+-----------------+---------------------------+

+-----------------+---------+--------+----------+
| Fan Name        | State   | Health | Value    |
+-----------------+---------+--------+----------+
| MOD1_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD1_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD2_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD2_FAN2_SPEED | Enabled | OK     | 7350 RPM | 
| MOD3_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD3_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD4_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD4_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD5_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD5_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD6_FAN1_SPEED | Enabled | OK     | 6868 RPM | 
| MOD6_FAN2_SPEED | Enabled | OK     | 7056 RPM | 
| MOD7_FAN1_SPEED | Absent  |        |          | 
+-----------------+---------+--------+----------+
```

JSON Output

```
# iserver get server --ip 10.58.50.41 --thermal

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
                    "ReadingCelsius": 39,
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
                    "ReadingCelsius": 19,
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
                    "ReadingCelsius": 27,
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
                    "Reading": 7350,
                    "Value": "7350 RPM"
                },
                {
                    "Name": "MOD3_FAN1_SPEED",
                    "State": "Enabled",
                    "Health": "OK",
                    "PhysicalContext": "Fan",
                    "ReadingUnits": "RPM",
                    "Reading": 6868,
                    "Value": "6868 RPM"
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
                    "Reading": 7056,
                    "Value": "7056 RPM"
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
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C240-M5SN",
    "LocatorLedOn": false,
    "FlagState": "P+ H",
    "FlagManagement": "CRi",
    "FlagWorkflow": "4"
}
```