# Get Intersight Servers with Thermal Information

```
# iserver get servers --group p2b -c thermal

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------+---------+-------------+-------------+----------------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | Fans | Sensors | Highest (C) | Min Gap (C) | Over Threshold |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------+---------+-------------+-------------+----------------+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | True | True    | 54          | 20          | 0              | 
| P+ H | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | True | True    | 56          | 19          | 0              | 
| P- H | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 |      |         |             |             |                | 
| P+ H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | True | True    | 63          | 24          | 0              | 
| P+ H | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | True | True    | 65          | 24          | 0              | 
| P+ H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | True | True    | 64          | 23          | 0              | 
| P+ H | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | True | True    | 57          | 24          | 0              | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------+---------+-------------+-------------+----------------+
```

JSON Output

```
# iserver get servers --group p2b -c thermal

[
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
        "Thermal": null,
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
        "LocatorLedOn": false,
        "FlagState": "P- H",
        "FlagManagement": "CRi",
        "FlagWorkflow": ""
    },
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
                        "ReadingCelsius": 40,
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
                        "Reading": 7350,
                        "Value": "7350 RPM"
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
                        "Reading": 7350,
                        "Value": "7350 RPM"
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
                        "Reading": 7070,
                        "Value": "7070 RPM"
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
                        "Reading": 7070,
                        "Value": "7070 RPM"
                    },
                    {
                        "Name": "MOD6_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 7350,
                        "Value": "7350 RPM"
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
        "Thermal": {
            "Data": {
                "Temperature": [
                    {
                        "Name": "DDR4_P1_A1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 84,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_B1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 90,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_C1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 96,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_D1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 102,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_E1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 108,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_F1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 114,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_G1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 120,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 29,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_H1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 126,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 30,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_J1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 132,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 30,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_K1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 138,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 28,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_L1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 144,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 29,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_M1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 150,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 29,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "MLOM_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 57,
                        "PhysicalContext": "NetworkingDevice",
                        "ReadingCelsius": 63,
                        "UpperThresholdCritical": 90
                    },
                    {
                        "Name": "P1_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 164,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 38.5,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "PCH_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 201,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 39,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "PSU1_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 199,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 28,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "PSU2_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 200,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 23,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "RISER1_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 242,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "RISER2_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 241,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 39,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "TEMP_SENS_FRONT",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 68,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 21,
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
                        "Reading": 8085,
                        "Value": "8085 RPM"
                    },
                    {
                        "Name": "MOD1_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8240,
                        "Value": "8240 RPM"
                    },
                    {
                        "Name": "MOD2_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8085,
                        "Value": "8085 RPM"
                    },
                    {
                        "Name": "MOD2_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8446,
                        "Value": "8446 RPM"
                    },
                    {
                        "Name": "MOD3_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8085,
                        "Value": "8085 RPM"
                    },
                    {
                        "Name": "MOD3_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8446,
                        "Value": "8446 RPM"
                    },
                    {
                        "Name": "MOD4_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8085,
                        "Value": "8085 RPM"
                    },
                    {
                        "Name": "MOD4_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8446,
                        "Value": "8446 RPM"
                    },
                    {
                        "Name": "MOD5_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8085,
                        "Value": "8085 RPM"
                    },
                    {
                        "Name": "MOD5_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8240,
                        "Value": "8240 RPM"
                    },
                    {
                        "Name": "MOD6_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8085,
                        "Value": "8085 RPM"
                    },
                    {
                        "Name": "MOD6_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8446,
                        "Value": "8446 RPM"
                    },
                    {
                        "Name": "MOD7_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 7875,
                        "Value": "7875 RPM"
                    },
                    {
                        "Name": "MOD7_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8240,
                        "Value": "8240 RPM"
                    }
                ]
            },
            "Summary": {
                "FanHealth": true,
                "SensorHealth": true,
                "HighestTemperature": 63,
                "SmallestGap": 24,
                "OverThreshold": 0
            }
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
        "Thermal": {
            "Data": {
                "Temperature": [
                    {
                        "Name": "DDR4_P1_A1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 84,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 37,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_B1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 90,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 37,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_C1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 96,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 37,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_D1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 102,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 36,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_E1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 108,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 37,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_F1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 114,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 39,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_G1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 120,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_H1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 126,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_J1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 132,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 37,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_K1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 138,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_L1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 144,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_M1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 150,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "MLOM_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 57,
                        "PhysicalContext": "NetworkingDevice",
                        "ReadingCelsius": 64,
                        "UpperThresholdCritical": 90
                    },
                    {
                        "Name": "P1_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 164,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 47,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 42,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "PCH_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 201,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 37,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "PSU1_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 199,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 29,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "PSU2_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 200,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 27,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "RISER1_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 242,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 36,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "RISER2_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 241,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 39,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "TEMP_SENS_FRONT",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 68,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 22,
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
                        "Reading": 3255,
                        "Value": "3255 RPM"
                    },
                    {
                        "Name": "MOD1_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3296,
                        "Value": "3296 RPM"
                    },
                    {
                        "Name": "MOD2_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3255,
                        "Value": "3255 RPM"
                    },
                    {
                        "Name": "MOD2_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3296,
                        "Value": "3296 RPM"
                    },
                    {
                        "Name": "MOD3_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3255,
                        "Value": "3255 RPM"
                    },
                    {
                        "Name": "MOD3_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3296,
                        "Value": "3296 RPM"
                    },
                    {
                        "Name": "MOD4_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3255,
                        "Value": "3255 RPM"
                    },
                    {
                        "Name": "MOD4_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3296,
                        "Value": "3296 RPM"
                    },
                    {
                        "Name": "MOD5_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3255,
                        "Value": "3255 RPM"
                    },
                    {
                        "Name": "MOD5_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3296,
                        "Value": "3296 RPM"
                    },
                    {
                        "Name": "MOD6_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3255,
                        "Value": "3255 RPM"
                    },
                    {
                        "Name": "MOD6_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3296,
                        "Value": "3296 RPM"
                    },
                    {
                        "Name": "MOD7_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3360,
                        "Value": "3360 RPM"
                    },
                    {
                        "Name": "MOD7_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3296,
                        "Value": "3296 RPM"
                    }
                ]
            },
            "Summary": {
                "FanHealth": true,
                "SensorHealth": true,
                "HighestTemperature": 64,
                "SmallestGap": 23,
                "OverThreshold": 0
            }
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
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
        "Thermal": {
            "Data": {
                "Temperature": [
                    {
                        "Name": "DDR4_P1_A1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 114,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 29,
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
                        "ReadingCelsius": 29,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_D1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 132,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 30,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_E1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 138,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 30,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_F1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 144,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 29,
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
                        "ReadingCelsius": 28,
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
                        "ReadingCelsius": 56,
                        "UpperThresholdCritical": 90
                    },
                    {
                        "Name": "P1_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 196,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 40,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 197,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 38.5,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "PCH_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 209,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 34,
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
                        "ReadingCelsius": 22,
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
                        "ReadingCelsius": 34,
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
                        "ReadingCelsius": 33,
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
                        "ReadingCelsius": 26,
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
                        "Reading": 7350,
                        "Value": "7350 RPM"
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
                        "Reading": 7350,
                        "Value": "7350 RPM"
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
                "HighestTemperature": 56,
                "SmallestGap": 19,
                "OverThreshold": 0
            }
        },
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C240-M5SN",
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
        "Thermal": {
            "Data": {
                "Temperature": [
                    {
                        "Name": "DDR4_P1_A1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 84,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_B1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 90,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_C1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 96,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_D1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 102,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_E1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 108,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_F1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 114,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_G1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 120,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_H1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 126,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 31,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_J1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 132,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_K1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 138,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 30,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_L1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 144,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 30,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_M1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 150,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 31,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "MLOM_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 57,
                        "PhysicalContext": "NetworkingDevice",
                        "ReadingCelsius": 65,
                        "UpperThresholdCritical": 90
                    },
                    {
                        "Name": "P1_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 164,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 47,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 41.5,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "PCH_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 201,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 42,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "PSU1_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 199,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "PSU2_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 200,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 26,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "RISER1_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 242,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "RISER2_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 241,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 40,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "TEMP_SENS_FRONT",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 68,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 21,
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
                        "Reading": 11445,
                        "Value": "11445 RPM"
                    },
                    {
                        "Name": "MOD1_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 12360,
                        "Value": "12360 RPM"
                    },
                    {
                        "Name": "MOD2_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11445,
                        "Value": "11445 RPM"
                    },
                    {
                        "Name": "MOD2_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11742,
                        "Value": "11742 RPM"
                    },
                    {
                        "Name": "MOD3_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11445,
                        "Value": "11445 RPM"
                    },
                    {
                        "Name": "MOD3_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11742,
                        "Value": "11742 RPM"
                    },
                    {
                        "Name": "MOD4_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11445,
                        "Value": "11445 RPM"
                    },
                    {
                        "Name": "MOD4_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 12360,
                        "Value": "12360 RPM"
                    },
                    {
                        "Name": "MOD5_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10920,
                        "Value": "10920 RPM"
                    },
                    {
                        "Name": "MOD5_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 12360,
                        "Value": "12360 RPM"
                    },
                    {
                        "Name": "MOD6_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11445,
                        "Value": "11445 RPM"
                    },
                    {
                        "Name": "MOD6_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11742,
                        "Value": "11742 RPM"
                    },
                    {
                        "Name": "MOD7_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11445,
                        "Value": "11445 RPM"
                    },
                    {
                        "Name": "MOD7_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 12360,
                        "Value": "12360 RPM"
                    }
                ]
            },
            "Summary": {
                "FanHealth": true,
                "SensorHealth": true,
                "HighestTemperature": 65,
                "SmallestGap": 24,
                "OverThreshold": 0
            }
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
        "Thermal": {
            "Data": {
                "Temperature": [
                    {
                        "Name": "DDR4_P1_A1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 84,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_B1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 90,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_C1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 96,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_D1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 102,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_E1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 108,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_F1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 114,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_G1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 120,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 31,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_H1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 126,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 31,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_J1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 132,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_K1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 138,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 29,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_L1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 144,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 30,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_M1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 150,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 31,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "MLOM_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 57,
                        "PhysicalContext": "NetworkingDevice",
                        "ReadingCelsius": 57,
                        "UpperThresholdCritical": 90
                    },
                    {
                        "Name": "P1_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 164,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 39,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "PCH_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 201,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 36,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "PSU1_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 199,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 27,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "PSU2_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 200,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 23,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "RISER1_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 242,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 31,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "RISER2_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 241,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "TEMP_SENS_FRONT",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 68,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 21,
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
                        "Reading": 6405,
                        "Value": "6405 RPM"
                    },
                    {
                        "Name": "MOD1_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6489,
                        "Value": "6489 RPM"
                    },
                    {
                        "Name": "MOD2_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6405,
                        "Value": "6405 RPM"
                    },
                    {
                        "Name": "MOD2_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6592,
                        "Value": "6592 RPM"
                    },
                    {
                        "Name": "MOD3_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6300,
                        "Value": "6300 RPM"
                    },
                    {
                        "Name": "MOD3_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6489,
                        "Value": "6489 RPM"
                    },
                    {
                        "Name": "MOD4_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6405,
                        "Value": "6405 RPM"
                    },
                    {
                        "Name": "MOD4_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6592,
                        "Value": "6592 RPM"
                    },
                    {
                        "Name": "MOD5_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6405,
                        "Value": "6405 RPM"
                    },
                    {
                        "Name": "MOD5_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6592,
                        "Value": "6592 RPM"
                    },
                    {
                        "Name": "MOD6_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6405,
                        "Value": "6405 RPM"
                    },
                    {
                        "Name": "MOD6_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6489,
                        "Value": "6489 RPM"
                    },
                    {
                        "Name": "MOD7_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6405,
                        "Value": "6405 RPM"
                    },
                    {
                        "Name": "MOD7_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6489,
                        "Value": "6489 RPM"
                    }
                ]
            },
            "Summary": {
                "FanHealth": true,
                "SensorHealth": true,
                "HighestTemperature": 57,
                "SmallestGap": 24,
                "OverThreshold": 0
            }
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