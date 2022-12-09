# Get Intersight Servers with Environmental Information

Environmental = Power + Thermal

```
# iserver get servers --group p2b -c env

+------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+------+---------+-------------+-------------+----------------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | Consumed [W] | Min [W] | Avg [W] | Max [W] | Fans | Sensors | Highest (C) | Min Gap (C) | Over Threshold |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+------+---------+-------------+-------------+----------------+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 324          | 176     | 330     | 435     | True | True    | 54          | 20          | 0              | 
| P+ H | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 288          | 52      | 315     | 798     | True | True    | 56          | 19          | 0              | 
| P- H | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 0            | 0       | 0       | 0       |      |         |             |             |                | 
| P+ H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 180          | 15      | 203     | 759     | True | True    | 62          | 24          | 0              | 
| P+ H | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 252          | 127     | 268     | 750     | True | True    | 63          | 24          | 0              | 
| P+ H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 216          | 181     | 226     | 699     | True | True    | 66          | 23          | 0              | 
| P+ H | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 180          | 10      | 208     | 706     | True | True    | 58          | 24          | 0              | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+------+---------+-------------+-------------+----------------+
```

JSON Output

```
# iserver get servers --group p2b -c env

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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 0,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 0,
                    "AverageConsumedWatts": 0,
                    "MaxConsumedWatts": 0
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 0,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "PSU2_VOUT",
                        "ReadingVolts": 0,
                        "UpperThresholdCritical": 14,
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
                        "SerialNumber": "LIT241244NV",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10062019",
                        "PowerOutputWatts": 0,
                        "LastPowerOutputWatts": 0,
                        "PowerInputWatts": 12,
                        "PowerSupplyType": "AC",
                        "State": "Enabled",
                        "Health": "OK",
                        "OutputWattage": 1050,
                        "MaximumFrequencyHz": 63,
                        "MaximumVoltage": 264,
                        "MinimumVoltage": 90,
                        "MinimumFrequencyHz": 47
                    },
                    {
                        "Name": "PSU2",
                        "Model": "PS-2112-9S-LF",
                        "SerialNumber": "LIT241244UN",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10062019",
                        "PowerOutputWatts": 0,
                        "LastPowerOutputWatts": 0,
                        "PowerInputWatts": 15,
                        "PowerSupplyType": "AC",
                        "State": "Enabled",
                        "Health": "OK",
                        "OutputWattage": 1050,
                        "MaximumFrequencyHz": 63,
                        "MaximumVoltage": 264,
                        "MinimumVoltage": 90,
                        "MinimumFrequencyHz": 47
                    }
                ]
            },
            "Summary": {
                "Source": "Redfish",
                "PowerNow": 0,
                "PowerMin": 0,
                "PowerAvg": 0,
                "PowerMax": 0
            }
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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 180,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 15,
                    "AverageConsumedWatts": 203,
                    "MaxConsumedWatts": 759
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 12.1,
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
                        "ReadingVolts": 3.026,
                        "UpperThresholdCritical": 3.588,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    }
                ],
                "PowerSupply": [
                    {
                        "Name": "PSU1",
                        "Model": "700-014550-0000",
                        "SerialNumber": "APS240201EL",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 88,
                        "LastPowerOutputWatts": 88,
                        "PowerInputWatts": 102,
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
                        "Model": "700-014550-0000",
                        "SerialNumber": "ART2601F4S6",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 84,
                        "LastPowerOutputWatts": 84,
                        "PowerInputWatts": 100,
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
                "PowerNow": 180,
                "PowerMin": 15,
                "PowerAvg": 203,
                "PowerMax": 759
            }
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
                        "ReadingCelsius": 32,
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
                        "ReadingCelsius": 30,
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
                        "ReadingCelsius": 31,
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
                        "ReadingCelsius": 62,
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
                        "ReadingCelsius": 34.5,
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
                        "Reading": 6489,
                        "Value": "6489 RPM"
                    },
                    {
                        "Name": "MOD3_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 6405,
                        "Value": "6405 RPM"
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
                        "Reading": 6489,
                        "Value": "6489 RPM"
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
                        "Reading": 6489,
                        "Value": "6489 RPM"
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
                "HighestTemperature": 62,
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
                        "ReadingVolts": 12,
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
                        "PowerOutputWatts": 143,
                        "LastPowerOutputWatts": 143,
                        "PowerInputWatts": 165,
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
                        "PowerOutputWatts": 147,
                        "LastPowerOutputWatts": 147,
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
                        "Reading": 7350,
                        "Value": "7350 RPM"
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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 252,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 127,
                    "AverageConsumedWatts": 268,
                    "MaxConsumedWatts": 750
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 12.2,
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
                        "ReadingVolts": 3.026,
                        "UpperThresholdCritical": 3.588,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    }
                ],
                "PowerSupply": [
                    {
                        "Name": "PSU1",
                        "Model": "700-014550-0000",
                        "SerialNumber": "APS240201ES",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 126,
                        "LastPowerOutputWatts": 126,
                        "PowerInputWatts": 139,
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
                        "Model": "700-014550-0000",
                        "SerialNumber": "ART2601F4S2",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 119,
                        "LastPowerOutputWatts": 119,
                        "PowerInputWatts": 132,
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
                "PowerNow": 252,
                "PowerMin": 127,
                "PowerAvg": 268,
                "PowerMax": 750
            }
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
                        "ReadingCelsius": 32,
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
                        "ReadingCelsius": 30,
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
                        "ReadingCelsius": 46,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 41,
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
                        "Reading": 10500,
                        "Value": "10500 RPM"
                    },
                    {
                        "Name": "MOD1_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11227,
                        "Value": "11227 RPM"
                    },
                    {
                        "Name": "MOD2_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10500,
                        "Value": "10500 RPM"
                    },
                    {
                        "Name": "MOD2_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11227,
                        "Value": "11227 RPM"
                    },
                    {
                        "Name": "MOD3_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10920,
                        "Value": "10920 RPM"
                    },
                    {
                        "Name": "MOD3_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10712,
                        "Value": "10712 RPM"
                    },
                    {
                        "Name": "MOD4_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10500,
                        "Value": "10500 RPM"
                    },
                    {
                        "Name": "MOD4_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 11227,
                        "Value": "11227 RPM"
                    },
                    {
                        "Name": "MOD5_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10500,
                        "Value": "10500 RPM"
                    },
                    {
                        "Name": "MOD5_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10712,
                        "Value": "10712 RPM"
                    },
                    {
                        "Name": "MOD6_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10500,
                        "Value": "10500 RPM"
                    },
                    {
                        "Name": "MOD6_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10712,
                        "Value": "10712 RPM"
                    },
                    {
                        "Name": "MOD7_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10920,
                        "Value": "10920 RPM"
                    },
                    {
                        "Name": "MOD7_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 10712,
                        "Value": "10712 RPM"
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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 216,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 181,
                    "AverageConsumedWatts": 226,
                    "MaxConsumedWatts": 699
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 12.1,
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
                        "ReadingVolts": 3.042,
                        "UpperThresholdCritical": 3.588,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    }
                ],
                "PowerSupply": [
                    {
                        "Name": "PSU1",
                        "Model": "700-014550-0000",
                        "SerialNumber": "APS240201EX",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252041",
                        "PowerOutputWatts": 94,
                        "LastPowerOutputWatts": 94,
                        "PowerInputWatts": 110,
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
                        "Model": "700-014550-0000",
                        "SerialNumber": "ART2601F4SS",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 91,
                        "LastPowerOutputWatts": 91,
                        "PowerInputWatts": 108,
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
                "PowerNow": 216,
                "PowerMin": 181,
                "PowerAvg": 226,
                "PowerMax": 699
            }
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
                        "ReadingCelsius": 38,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_B1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 90,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 38,
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
                        "ReadingCelsius": 37,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_E1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 108,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 38,
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
                        "ReadingCelsius": 35,
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
                        "ReadingCelsius": 38,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_K1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 138,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
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
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "MLOM_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 57,
                        "PhysicalContext": "NetworkingDevice",
                        "ReadingCelsius": 66,
                        "UpperThresholdCritical": 90
                    },
                    {
                        "Name": "P1_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 164,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 48.5,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 43.5,
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
                        "ReadingCelsius": 30,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "PSU2_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 200,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 28,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "RISER1_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 242,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 37,
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
                        "Reading": 3360,
                        "Value": "3360 RPM"
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
                        "Reading": 3360,
                        "Value": "3360 RPM"
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
                "HighestTemperature": 66,
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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 180,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 10,
                    "AverageConsumedWatts": 208,
                    "MaxConsumedWatts": 706
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 12.1,
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
                        "ReadingVolts": 3.026,
                        "UpperThresholdCritical": 3.588,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    }
                ],
                "PowerSupply": [
                    {
                        "Name": "PSU1",
                        "Model": "700-014550-0000",
                        "SerialNumber": "APS240201ER",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 87,
                        "LastPowerOutputWatts": 87,
                        "PowerInputWatts": 99,
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
                        "Model": "700-014550-0000",
                        "SerialNumber": "ART2601F4LL",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 94,
                        "LastPowerOutputWatts": 94,
                        "PowerInputWatts": 103,
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
                "PowerNow": 180,
                "PowerMin": 10,
                "PowerAvg": 208,
                "PowerMax": 706
            }
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
                        "ReadingCelsius": 34,
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
                        "ReadingCelsius": 35,
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
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_J1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 132,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 34,
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
                        "ReadingCelsius": 58,
                        "UpperThresholdCritical": 90
                    },
                    {
                        "Name": "P1_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 164,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 40,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "PCH_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 201,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 35,
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
                        "ReadingCelsius": 24,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "RISER1_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 242,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "RISER2_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 241,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 36,
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
                        "Reading": 6592,
                        "Value": "6592 RPM"
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
                        "Reading": 6592,
                        "Value": "6592 RPM"
                    }
                ]
            },
            "Summary": {
                "FanHealth": true,
                "SensorHealth": true,
                "HighestTemperature": 58,
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
        "Power": {
            "Data": {
                "PowerControl": {
                    "PowerConsumedWatts": 288,
                    "LimitException": "NoAction",
                    "MinConsumedWatts": 52,
                    "AverageConsumedWatts": 315,
                    "MaxConsumedWatts": 798
                },
                "Voltage": [
                    {
                        "Name": "PSU1_VOUT",
                        "ReadingVolts": 12.2,
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
                        "ReadingVolts": 3.026,
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
                        "SerialNumber": "LIT241244RQ",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10062019",
                        "PowerOutputWatts": 145,
                        "LastPowerOutputWatts": 145,
                        "PowerInputWatts": 159,
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
                        "SerialNumber": "LIT241242TS",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10062019",
                        "PowerOutputWatts": 139,
                        "LastPowerOutputWatts": 139,
                        "PowerInputWatts": 155,
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
                "PowerNow": 288,
                "PowerMin": 52,
                "PowerAvg": 315,
                "PowerMax": 798
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
                        "ReadingCelsius": 28,
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
                        "ReadingCelsius": 36,
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
                        "Reading": 7056,
                        "Value": "7056 RPM"
                    },
                    {
                        "Name": "MOD2_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 7070,
                        "Value": "7070 RPM"
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
                        "Reading": 7070,
                        "Value": "7070 RPM"
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
    }
]
```