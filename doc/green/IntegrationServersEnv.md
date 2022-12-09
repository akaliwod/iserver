# Get Intersight Servers with Environmental Information

Environmental = Power + Thermal

```
# iserver get servers --group power -c env

+---------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+------+---------+-------------+-------------+----------------+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP          | Consumed [W] | Min [W] | Avg [W] | Max [W] | Fans | Sensors | Highest (C) | Min Gap (C) | Over Threshold |
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+------+---------+-------------+-------------+----------------+
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-1           | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33 | 138.0        | 138.0   | 138.0   | 138.0   | N/A  | True    | 36.5        | N/A         | N/A            | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-2           | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34 | 138.0        | 138.0   | 138.0   | 138.0   | N/A  | True    | 38.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-3           | (B) UCSB-B200-M4   | FCH20437VXH | 10.58.52.35 | 126.0        | 126.0   | 126.0   | 126.0   | N/A  | True    | 40.0        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-4           | (B) UCSB-B200-M4   | FCH205371UU | 10.58.52.36 | 126.0        | 120.0   | 126.0   | 132.0   | N/A  | True    | 41.5        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-1           | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41 | 210.6        | 206.7   | 209.62  | 210.6   | N/A  | True    | 39.0        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-2           | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42 | 241.8        | 234.0   | 237.9   | 241.8   | N/A  | True    | 48.0        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-3           | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43 | 195.0        | 191.1   | 193.7   | 195.0   | N/A  | True    | 37.0        | N/A         | N/A            | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-4           | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44 | 237.9        | 234.0   | 239.85  | 245.7   | N/A  | True    | 50.0        | N/A         | N/A            | 
| P+ H    | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 324          | 176     | 330     | 435     | True | True    | 54          | 20          | 0              | 
| P+ H    | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 288          | 52      | 315     | 798     | True | True    | 56          | 19          | 0              | 
| P- H    | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 0            | 0       | 0       | 0       |      |         |             |             |                | 
| P+ H    | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 180          | 15      | 203     | 759     | True | True    | 63          | 24          | 0              | 
| P+ H    | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 252          | 127     | 268     | 750     | True | True    | 60          | 24          | 0              | 
| P+ H    | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 216          | 181     | 226     | 699     | True | True    | 72          | 18          | 0              | 
| P+ H    | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 180          | 10      | 208     | 706     | True | True    | 61          | 23          | 0              | 
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+--------------+---------+---------+---------+------+---------+-------------+-------------+----------------+
```

JSON Output

```
# iserver get servers --group power -c env

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
                        "PowerInputWatts": 17,
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
                        "SerialNumber": "APS240201EL",
                        "PartNumber": "341-0638-03",
                        "SparePartNumber": "341-0638-03",
                        "Manufacturer": "Cisco Systems Inc",
                        "FirmwareVersion": "10252046",
                        "PowerOutputWatts": 88,
                        "LastPowerOutputWatts": 88,
                        "PowerInputWatts": 100,
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
                        "PowerInputWatts": 97,
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
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_F1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 114,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
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
                        "ReadingCelsius": 32,
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
                        "ReadingCelsius": 40.5,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 36.5,
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
                        "ReadingCelsius": 29,
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
                        "Reading": 3885,
                        "Value": "3885 RPM"
                    },
                    {
                        "Name": "MOD1_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3811,
                        "Value": "3811 RPM"
                    },
                    {
                        "Name": "MOD2_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 4095,
                        "Value": "4095 RPM"
                    },
                    {
                        "Name": "MOD2_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3811,
                        "Value": "3811 RPM"
                    },
                    {
                        "Name": "MOD3_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3990,
                        "Value": "3990 RPM"
                    },
                    {
                        "Name": "MOD3_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3811,
                        "Value": "3811 RPM"
                    },
                    {
                        "Name": "MOD4_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3990,
                        "Value": "3990 RPM"
                    },
                    {
                        "Name": "MOD4_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3914,
                        "Value": "3914 RPM"
                    },
                    {
                        "Name": "MOD5_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3990,
                        "Value": "3990 RPM"
                    },
                    {
                        "Name": "MOD5_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3914,
                        "Value": "3914 RPM"
                    },
                    {
                        "Name": "MOD6_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 4095,
                        "Value": "4095 RPM"
                    },
                    {
                        "Name": "MOD6_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3914,
                        "Value": "3914 RPM"
                    },
                    {
                        "Name": "MOD7_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3990,
                        "Value": "3990 RPM"
                    },
                    {
                        "Name": "MOD7_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3914,
                        "Value": "3914 RPM"
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
                        "PowerOutputWatts": 100,
                        "LastPowerOutputWatts": 100,
                        "PowerInputWatts": 113,
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
                        "PowerOutputWatts": 96,
                        "LastPowerOutputWatts": 96,
                        "PowerInputWatts": 113,
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
                        "ReadingCelsius": 39,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_B1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 90,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 39,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_C1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 96,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 38,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_D1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 102,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 38,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_E1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 108,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 39,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_F1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 114,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 40,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_G1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 120,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 36,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_H1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 126,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 36,
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
                        "ReadingCelsius": 34,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_M1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 150,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "MLOM_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 57,
                        "PhysicalContext": "NetworkingDevice",
                        "ReadingCelsius": 72,
                        "UpperThresholdCritical": 90
                    },
                    {
                        "Name": "P1_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 164,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 52,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 46,
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
                        "ReadingCelsius": 31,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "PSU2_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 200,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 30,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "RISER1_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 242,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 38,
                        "UpperThresholdCritical": 70
                    },
                    {
                        "Name": "RISER2_INLET_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 241,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 41,
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
                        "Reading": 5565,
                        "Value": "5565 RPM"
                    },
                    {
                        "Name": "MOD1_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5562,
                        "Value": "5562 RPM"
                    },
                    {
                        "Name": "MOD2_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5565,
                        "Value": "5565 RPM"
                    },
                    {
                        "Name": "MOD2_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5665,
                        "Value": "5665 RPM"
                    },
                    {
                        "Name": "MOD3_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5565,
                        "Value": "5565 RPM"
                    },
                    {
                        "Name": "MOD3_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5562,
                        "Value": "5562 RPM"
                    },
                    {
                        "Name": "MOD4_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5565,
                        "Value": "5565 RPM"
                    },
                    {
                        "Name": "MOD4_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5459,
                        "Value": "5459 RPM"
                    },
                    {
                        "Name": "MOD5_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5565,
                        "Value": "5565 RPM"
                    },
                    {
                        "Name": "MOD5_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5871,
                        "Value": "5871 RPM"
                    },
                    {
                        "Name": "MOD6_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5565,
                        "Value": "5565 RPM"
                    },
                    {
                        "Name": "MOD6_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5562,
                        "Value": "5562 RPM"
                    },
                    {
                        "Name": "MOD7_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5775,
                        "Value": "5775 RPM"
                    },
                    {
                        "Name": "MOD7_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 5562,
                        "Value": "5562 RPM"
                    }
                ]
            },
            "Summary": {
                "FanHealth": true,
                "SensorHealth": true,
                "HighestTemperature": 72,
                "SmallestGap": 18,
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
                        "PowerOutputWatts": 144,
                        "LastPowerOutputWatts": 144,
                        "PowerInputWatts": 158,
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
                        "PowerOutputWatts": 141,
                        "LastPowerOutputWatts": 141,
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
                        "ReadingCelsius": 28,
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
                        "ReadingCelsius": 39.5,
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
                        "ReadingCelsius": 35,
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
                        "Reading": 7056,
                        "Value": "7056 RPM"
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
                        "ReadingVolts": 12.1,
                        "UpperThresholdCritical": 14,
                        "PhysicalContext": "PowerSupply",
                        "State": "Enabled",
                        "Health": "OK"
                    },
                    {
                        "Name": "PSU2_VOUT",
                        "ReadingVolts": 12.1,
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
                        "Reading": 7056,
                        "Value": "7056 RPM"
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
                        "PowerOutputWatts": 85,
                        "LastPowerOutputWatts": 85,
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
                        "PowerOutputWatts": 92,
                        "LastPowerOutputWatts": 92,
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
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_B1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 90,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 36,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_C1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 96,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_D1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 102,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 35,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_E1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 108,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 36,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P1_F1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 114,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 37,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_G1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 120,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_H1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 126,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 33,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_J1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 132,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 36,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_K1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 138,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 31,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_L1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 144,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "DDR4_P2_M1_TMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 150,
                        "PhysicalContext": "Memory",
                        "ReadingCelsius": 32,
                        "UpperThresholdCritical": 85
                    },
                    {
                        "Name": "MLOM_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 57,
                        "PhysicalContext": "NetworkingDevice",
                        "ReadingCelsius": 61,
                        "UpperThresholdCritical": 90
                    },
                    {
                        "Name": "P1_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 164,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 43.5,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "P2_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 165,
                        "PhysicalContext": "CPU",
                        "ReadingCelsius": 36.5,
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
                        "ReadingCelsius": 28,
                        "UpperThresholdCritical": 65
                    },
                    {
                        "Name": "PSU2_TEMP",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 200,
                        "PhysicalContext": "PowerSupply",
                        "ReadingCelsius": 25,
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
                        "ReadingCelsius": 36,
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
                        "Reading": 3885,
                        "Value": "3885 RPM"
                    },
                    {
                        "Name": "MOD1_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3708,
                        "Value": "3708 RPM"
                    },
                    {
                        "Name": "MOD2_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3990,
                        "Value": "3990 RPM"
                    },
                    {
                        "Name": "MOD2_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3708,
                        "Value": "3708 RPM"
                    },
                    {
                        "Name": "MOD3_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3990,
                        "Value": "3990 RPM"
                    },
                    {
                        "Name": "MOD3_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3708,
                        "Value": "3708 RPM"
                    },
                    {
                        "Name": "MOD4_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3885,
                        "Value": "3885 RPM"
                    },
                    {
                        "Name": "MOD4_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3811,
                        "Value": "3811 RPM"
                    },
                    {
                        "Name": "MOD5_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3885,
                        "Value": "3885 RPM"
                    },
                    {
                        "Name": "MOD5_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3811,
                        "Value": "3811 RPM"
                    },
                    {
                        "Name": "MOD6_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3885,
                        "Value": "3885 RPM"
                    },
                    {
                        "Name": "MOD6_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3914,
                        "Value": "3914 RPM"
                    },
                    {
                        "Name": "MOD7_FAN1_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3990,
                        "Value": "3990 RPM"
                    },
                    {
                        "Name": "MOD7_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 3708,
                        "Value": "3708 RPM"
                    }
                ]
            },
            "Summary": {
                "FanHealth": true,
                "SensorHealth": true,
                "HighestTemperature": 61,
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
        "Moid": "6335c26e76752d3139b9694c",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-1",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM241501FB",
        "ManagementMode": "UCSM",
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
        "ManagementIp": "10.58.52.41",
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
                "dn": "sys/chassis-2/blade-1/board/power-stats",
                "time_collected": "2022-12-08T22:35:44.244",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-1",
                "consumed_power": 210.6,
                "input_current": 17.5,
                "input_voltage": 12.04,
                "consumed_power_avg": 209.62,
                "input_current_avg": 17.35,
                "input_voltage_avg": 12.08,
                "consumed_power_min": 206.7,
                "input_current_min": 17.09,
                "input_voltage_min": 12.04,
                "consumed_power_max": 210.6,
                "input_current_max": 17.5,
                "input_voltage_max": 12.1
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 210.6,
                "PowerMin": 206.7,
                "PowerAvg": 209.62,
                "PowerMax": 210.6
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-1/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 20.0,
                    "fm_temp_sen_rear": 33.0,
                    "temperature_avg": 20.0,
                    "fm_temp_sen_rear_avg": 33.0,
                    "temperature_min": 20.0,
                    "fm_temp_sen_rear_min": 33.0,
                    "temperature_max": 20.0,
                    "fm_temp_sen_rear_max": 33.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 33.0,
                    "temperature_avg": 33.0,
                    "temperature_min": 33.0,
                    "temperature_max": 33.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/cpu-1/env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 35.5,
                    "temperature_avg": 35.9,
                    "temperature_min": 35.5,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 39.0,
                    "temperature_avg": 39.6,
                    "temperature_min": 39.0,
                    "temperature_max": 40.5
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-11/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-11",
                    "name": "MEM-11",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-15/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-15",
                    "name": "MEM-15",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-21/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-21",
                    "name": "MEM-21",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-3/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-3",
                    "name": "MEM-3",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 26.0,
                    "temperature_min": 26.0,
                    "temperature_max": 26.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-9/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:44.244",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-9",
                    "name": "MEM-9",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 39.0,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
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
                        "PowerOutputWatts": 120,
                        "LastPowerOutputWatts": 120,
                        "PowerInputWatts": 135,
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
                        "PowerOutputWatts": 112,
                        "LastPowerOutputWatts": 112,
                        "PowerInputWatts": 129,
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
                        "ReadingCelsius": 60,
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
                        "ReadingCelsius": 41.5,
                        "UpperThresholdCritical": 100
                    },
                    {
                        "Name": "PCH_TEMP_SENS",
                        "State": "Enabled",
                        "Health": "OK",
                        "SensorNumber": 201,
                        "PhysicalContext": "SystemBoard",
                        "ReadingCelsius": 41,
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
                        "ReadingCelsius": 24,
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
                        "ReadingCelsius": 38,
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
                        "Reading": 8446,
                        "Value": "8446 RPM"
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
                        "Reading": 8240,
                        "Value": "8240 RPM"
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
                        "Reading": 7875,
                        "Value": "7875 RPM"
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
                        "Reading": 8400,
                        "Value": "8400 RPM"
                    },
                    {
                        "Name": "MOD7_FAN2_SPEED",
                        "State": "Enabled",
                        "Health": "OK",
                        "PhysicalContext": "Fan",
                        "ReadingUnits": "RPM",
                        "Reading": 8446,
                        "Value": "8446 RPM"
                    }
                ]
            },
            "Summary": {
                "FanHealth": true,
                "SensorHealth": true,
                "HighestTemperature": 60,
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
        "Moid": "6335c45976752d3139b9bf94",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-2",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM24140BJB",
        "ManagementMode": "UCSM",
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
        "ManagementIp": "10.58.52.42",
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
                "dn": "sys/chassis-2/blade-2/board/power-stats",
                "time_collected": "2022-12-08T22:35:59.344",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-2",
                "consumed_power": 241.8,
                "input_current": 19.89,
                "input_voltage": 12.15,
                "consumed_power_avg": 237.9,
                "input_current_avg": 19.57,
                "input_voltage_avg": 12.15,
                "consumed_power_min": 234.0,
                "input_current_min": 19.25,
                "input_voltage_min": 12.15,
                "consumed_power_max": 241.8,
                "input_current_max": 19.89,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 241.8,
                "PowerMin": 234.0,
                "PowerAvg": 237.9,
                "PowerMax": 241.8
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-2/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 21.0,
                    "fm_temp_sen_rear": 37.0,
                    "temperature_avg": 21.0,
                    "fm_temp_sen_rear_avg": 37.0,
                    "temperature_min": 21.0,
                    "fm_temp_sen_rear_min": 37.0,
                    "temperature_max": 21.0,
                    "fm_temp_sen_rear_max": 37.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 37.0,
                    "temperature_avg": 37.0,
                    "temperature_min": 37.0,
                    "temperature_max": 37.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/cpu-1/env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 42.0,
                    "temperature_avg": 42.25,
                    "temperature_min": 42.0,
                    "temperature_max": 42.5
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 48.0,
                    "temperature_avg": 48.58,
                    "temperature_min": 48.0,
                    "temperature_max": 49.5
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-11/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-11",
                    "name": "MEM-11",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 33.0,
                    "temperature_avg": 33.0,
                    "temperature_min": 33.0,
                    "temperature_max": 33.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-15/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-15",
                    "name": "MEM-15",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.0,
                    "temperature_min": 31.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 34.0,
                    "temperature_avg": 34.0,
                    "temperature_min": 34.0,
                    "temperature_max": 34.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-21/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-21",
                    "name": "MEM-21",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 32.0,
                    "temperature_min": 32.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.0,
                    "temperature_min": 31.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-3/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-3",
                    "name": "MEM-3",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.0,
                    "temperature_min": 31.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.8,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-9/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:59.344",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-9",
                    "name": "MEM-9",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 48.0,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "Moid": "6335e1f376752d3139bf12b8",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-1",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH205371PZ",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
        "AvailableMemory": 524288,
        "TotalMemory": 524288,
        "UsedMemory": 0,
        "TotalMemoryUnit": "512 [GiB]",
        "TotalMemoryGB": 512,
        "AvailableMemoryUnit": "512 [GiB]",
        "AvailableMemoryGB": 512,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.33",
        "AlarmSummary": {
            "Critical": 9,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Critical (9)",
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
                "dn": "sys/chassis-1/blade-1/board/power-stats",
                "time_collected": "2022-12-08T22:35:50.267",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "consumed_power": 138.0,
                "input_current": 11.47,
                "input_voltage": 12.04,
                "consumed_power_avg": 138.0,
                "input_current_avg": 11.47,
                "input_voltage_avg": 12.04,
                "consumed_power_min": 138.0,
                "input_current_min": 11.47,
                "input_voltage_min": 12.04,
                "consumed_power_max": 138.0,
                "input_current_max": 11.47,
                "input_voltage_max": 12.04
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 138.0,
                "PowerMin": 138.0,
                "PowerAvg": 138.0,
                "PowerMax": 138.0
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-1/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 23.0,
                    "fm_temp_sen_rear": 36.0,
                    "temperature_avg": 23.0,
                    "fm_temp_sen_rear_avg": 36.0,
                    "temperature_min": 23.0,
                    "fm_temp_sen_rear_min": 36.0,
                    "temperature_max": 23.0,
                    "fm_temp_sen_rear_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 36.0,
                    "temperature_avg": 36.0,
                    "temperature_min": 36.0,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/cpu-1/env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 34.5,
                    "temperature_avg": 34.79,
                    "temperature_min": 34.0,
                    "temperature_max": 35.5
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 36.5,
                    "temperature_avg": 37.07,
                    "temperature_min": 36.5,
                    "temperature_max": 37.5
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.4,
                    "temperature_min": 27.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-10/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-10",
                    "name": "MEM-10",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-11/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-11",
                    "name": "MEM-11",
                    "type": "memory",
                    "temperature": 25.0,
                    "temperature_avg": 25.0,
                    "temperature_min": 25.0,
                    "temperature_max": 25.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.2,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-14",
                    "name": "MEM-14",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.4,
                    "temperature_min": 29.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 25.0,
                    "temperature_avg": 25.0,
                    "temperature_min": 25.0,
                    "temperature_max": 25.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.4,
                    "temperature_min": 29.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-2/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-2",
                    "name": "MEM-2",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 26.0,
                    "temperature_min": 26.0,
                    "temperature_max": 26.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-20/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-20",
                    "name": "MEM-20",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.2,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 26.4,
                    "temperature_min": 26.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
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
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-8/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:50.267",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-8",
                    "name": "MEM-8",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 36.5,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ C(9)",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "Moid": "6337014c76752d3139f2f459",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-2",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH20527XXD",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
        "AvailableMemory": 524288,
        "TotalMemory": 524288,
        "UsedMemory": 0,
        "TotalMemoryUnit": "512 [GiB]",
        "TotalMemoryGB": 512,
        "AvailableMemoryUnit": "512 [GiB]",
        "AvailableMemoryGB": 512,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.34",
        "AlarmSummary": {
            "Critical": 9,
            "Warning": 0,
            "Info": 1
        },
        "Health": "Critical (9)",
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
                "dn": "sys/chassis-1/blade-2/board/power-stats",
                "time_collected": "2022-12-08T22:35:33.451",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-2",
                "consumed_power": 138.0,
                "input_current": 11.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 138.0,
                "input_current_avg": 11.52,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 138.0,
                "input_current_min": 11.52,
                "input_voltage_min": 11.98,
                "consumed_power_max": 138.0,
                "input_current_max": 11.52,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 138.0,
                "PowerMin": 138.0,
                "PowerAvg": 138.0,
                "PowerMax": 138.0
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-2/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:33.451",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 24.0,
                    "fm_temp_sen_rear": 36.0,
                    "temperature_avg": 24.0,
                    "fm_temp_sen_rear_avg": 36.0,
                    "temperature_min": 24.0,
                    "fm_temp_sen_rear_min": 36.0,
                    "temperature_max": 24.0,
                    "fm_temp_sen_rear_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:33.451",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 36.0,
                    "temperature_avg": 36.0,
                    "temperature_min": 36.0,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/cpu-1/env-stats",
                    "time_collected": "2022-12-08T22:35:33.451",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 35.0,
                    "temperature_avg": 34.68,
                    "temperature_min": 34.0,
                    "temperature_max": 35.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:35:33.451",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 38.5,
                    "temperature_avg": 38.0,
                    "temperature_min": 37.5,
                    "temperature_max": 38.5
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-10/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-10",
                    "name": "MEM-10",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-11/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-11",
                    "name": "MEM-11",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 26.0,
                    "temperature_min": 26.0,
                    "temperature_max": 26.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 33.0,
                    "temperature_avg": 30.44,
                    "temperature_min": 30.0,
                    "temperature_max": 33.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-14",
                    "name": "MEM-14",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 28.33,
                    "temperature_min": 28.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 31.44,
                    "temperature_min": 29.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 30.67,
                    "temperature_min": 29.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 30.44,
                    "temperature_min": 30.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-2/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-2",
                    "name": "MEM-2",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-20/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-20",
                    "name": "MEM-20",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 30.33,
                    "temperature_min": 30.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.451",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 31.11,
                    "temperature_min": 29.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.451",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-23",
                    "name": "MEM-23",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 30.78,
                    "temperature_min": 29.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-4",
                    "name": "MEM-4",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-8/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:33.452",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-8",
                    "name": "MEM-8",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 38.5,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ C(9)",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "Moid": "6337063276752d3139f3cc83",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-3",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH20437VXH",
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
        "ManagementIp": "10.58.52.35",
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
                "dn": "sys/chassis-1/blade-3/board/power-stats",
                "time_collected": "2022-12-08T22:36:15.364",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-3",
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-3/board/temp-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
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
                    "dn": "sys/chassis-1/blade-3/board/temp-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 36.0,
                    "temperature_avg": 36.0,
                    "temperature_min": 36.0,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/cpu-1/env-stats",
                    "time_collected": "2022-12-08T22:36:15.363",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 36.0,
                    "temperature_avg": 36.0,
                    "temperature_min": 35.5,
                    "temperature_max": 36.5
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 40.0,
                    "temperature_avg": 40.12,
                    "temperature_min": 39.5,
                    "temperature_max": 41.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
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
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-10/dimm-env-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-10",
                    "name": "MEM-10",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.25,
                    "temperature_min": 30.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 26.0,
                    "temperature_min": 26.0,
                    "temperature_max": 26.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.25,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 25.0,
                    "temperature_avg": 25.0,
                    "temperature_min": 25.0,
                    "temperature_max": 25.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-4",
                    "name": "MEM-4",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 26.25,
                    "temperature_min": 26.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-08T22:36:15.364",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-7",
                    "name": "MEM-7",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 40.0,
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
    },
    {
        "Moid": "63371c9176752d3139f7da78",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-4",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM24140B0B",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
        "AvailableMemory": 196608,
        "TotalMemory": 196608,
        "UsedMemory": 0,
        "TotalMemoryUnit": "192 [GiB]",
        "TotalMemoryGB": 192,
        "AvailableMemoryUnit": "192 [GiB]",
        "AvailableMemoryGB": 192,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.44",
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
                "dn": "sys/chassis-2/blade-4/board/power-stats",
                "time_collected": "2022-12-08T22:35:52.296",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-4",
                "consumed_power": 237.9,
                "input_current": 19.67,
                "input_voltage": 12.1,
                "consumed_power_avg": 239.85,
                "input_current_avg": 19.83,
                "input_voltage_avg": 12.1,
                "consumed_power_min": 234.0,
                "input_current_min": 19.35,
                "input_voltage_min": 12.1,
                "consumed_power_max": 245.7,
                "input_current_max": 20.31,
                "input_voltage_max": 12.1
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 237.9,
                "PowerMin": 234.0,
                "PowerAvg": 239.85,
                "PowerMax": 245.7
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-4/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 21.0,
                    "fm_temp_sen_rear": 38.0,
                    "temperature_avg": 21.13,
                    "fm_temp_sen_rear_avg": 38.0,
                    "temperature_min": 21.0,
                    "fm_temp_sen_rear_min": 38.0,
                    "temperature_max": 22.0,
                    "fm_temp_sen_rear_max": 38.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 38.0,
                    "temperature_avg": 38.0,
                    "temperature_min": 38.0,
                    "temperature_max": 38.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 50.0,
                    "temperature_avg": 49.69,
                    "temperature_min": 48.0,
                    "temperature_max": 51.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/cpu-1/env-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 40.5,
                    "temperature_avg": 41.44,
                    "temperature_min": 40.5,
                    "temperature_max": 42.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 32.0,
                    "temperature_min": 32.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-15/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-15",
                    "name": "MEM-15",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 29.0,
                    "temperature_min": 29.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-3/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-3",
                    "name": "MEM-3",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:52.296",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
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
                "HighestTemperature": 50.0,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
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
                "time_collected": "2022-12-08T22:35:41.778",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "consumed_power": 126.0,
                "input_current": 10.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 126.0,
                "input_current_avg": 10.52,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 120.0,
                "input_current_min": 10.02,
                "input_voltage_min": 11.98,
                "consumed_power_max": 132.0,
                "input_current_max": 11.02,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 126.0,
                "PowerMin": 120.0,
                "PowerAvg": 126.0,
                "PowerMax": 132.0
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-4/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:41.778",
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
                    "time_collected": "2022-12-08T22:35:41.778",
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
                    "time_collected": "2022-12-08T22:35:41.778",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 38.5,
                    "temperature_avg": 38.45,
                    "temperature_min": 38.0,
                    "temperature_max": 38.5
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:35:41.778",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 41.5,
                    "temperature_avg": 41.6,
                    "temperature_min": 41.0,
                    "temperature_max": 42.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:41.778",
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
                    "time_collected": "2022-12-08T22:35:41.778",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-10",
                    "name": "MEM-10",
                    "type": "memory",
                    "temperature": 29.0,
                    "temperature_avg": 28.78,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:41.778",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 32.0,
                    "temperature_min": 32.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:41.778",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:41.778",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.22,
                    "temperature_min": 30.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:41.778",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:41.778",
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
                    "time_collected": "2022-12-08T22:35:41.778",
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
    },
    {
        "Moid": "63371c9176752d3139f7da82",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-3",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM241501CT",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
        "AvailableMemory": 196608,
        "TotalMemory": 196608,
        "UsedMemory": 0,
        "TotalMemoryUnit": "192 [GiB]",
        "TotalMemoryGB": 192,
        "AvailableMemoryUnit": "192 [GiB]",
        "AvailableMemoryGB": 192,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.43",
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
                "dn": "sys/chassis-2/blade-3/board/power-stats",
                "time_collected": "2022-12-08T22:35:55.340",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-3",
                "consumed_power": 195.0,
                "input_current": 16.04,
                "input_voltage": 12.15,
                "consumed_power_avg": 193.7,
                "input_current_avg": 15.96,
                "input_voltage_avg": 12.13,
                "consumed_power_min": 191.1,
                "input_current_min": 15.8,
                "input_voltage_min": 12.1,
                "consumed_power_max": 195.0,
                "input_current_max": 16.04,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 195.0,
                "PowerMin": 191.1,
                "PowerAvg": 193.7,
                "PowerMax": 195.0
            }
        },
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-3/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 20.0,
                    "fm_temp_sen_rear": 32.0,
                    "temperature_avg": 20.0,
                    "fm_temp_sen_rear_avg": 32.0,
                    "temperature_min": 20.0,
                    "fm_temp_sen_rear_min": 32.0,
                    "temperature_max": 20.0,
                    "fm_temp_sen_rear_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/temp-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "name": "Motherboard Rear",
                    "type": "motherboard",
                    "temperature": 32.0,
                    "temperature_avg": 32.0,
                    "temperature_min": 32.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 36.0,
                    "temperature_avg": 36.08,
                    "temperature_min": 36.0,
                    "temperature_max": 36.5
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/cpu-1/env-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 37.0,
                    "temperature_avg": 37.0,
                    "temperature_min": 37.0,
                    "temperature_max": 37.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-1",
                    "name": "MEM-1",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
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
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-15/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-15",
                    "name": "MEM-15",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-3/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-3",
                    "name": "MEM-3",
                    "type": "memory",
                    "temperature": 26.0,
                    "temperature_avg": 26.75,
                    "temperature_min": 26.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-08T22:35:55.340",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-5",
                    "name": "MEM-5",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                }
            ],
            "Summary": {
                "Source": "UCSM",
                "FanHealth": "N/A",
                "SensorHealth": true,
                "HighestTemperature": 37.0,
                "SmallestGap": "N/A",
                "OverThreshold": "N/A"
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    }
]
```

Developer Output

```
# iserver get servers --group power -c env

Developer output

{
    "duration": 29741,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 10832
    },
    "redfish": {
        "read": true,
        "success": 78,
        "failed": 0,
        "connect": 26,
        "disconnect": 0,
        "path": 52,
        "connect_time": 27290,
        "disconnect_time": 0,
        "path_time": 18856,
        "total_time": 46146
    },
    "ucsm": {
        "read": true,
        "success": 96,
        "failed": 0,
        "connect": 32,
        "disconnect": 0,
        "mo": 64,
        "connect_time": 35584,
        "disconnect_time": 0,
        "mo_time": 32514,
        "total_time": 68098
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
        "lines": 4417
    }
}

Log: debug
-----------

[2022-12-08 22:36:03.379719]	[computes_info.get]	Get servers settings: {
    "locator": true,
    "workflow": 86400,
    "registration": true,
    "rack": true,
    "blade": true,
    "id": false,
    "cpu": false,
    "memory": false,
    "fw": false,
    "pci": false,
    "fan": false,
    "psu": false,
    "group": false,
    "storage": false,
    "server_setting_id": false,
    "power": true,
    "thermal": true,
    "env": true
}
[2022-12-08 22:36:03.381590]	[computes_info.get]	Get servers match rules: {
    "name": "",
    "model": "",
    "ip": [],
    "serials": [
        "FLM241501FB",
        "FCH205371PZ",
        "FLM24140BJB",
        "FLM24140B0B",
        "FLM241501CT",
        "FCH205371UU",
        "FCH20437VXH",
        "FCH20527XXD",
        "WZP23400AK4",
        "WZP23400AJW",
        "WMP240400FM",
        "WZP23400AKL",
        "WMP24040059",
        "WMP24040061",
        "WMP2404000R"
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
[2022-12-08 22:36:08.279283]	[computes_info.get]	All 103 servers base information in 4896 ms
[2022-12-08 22:36:08.281278]	[computes_info.get]	Base filter 15 servers in 0 ms
[2022-12-08 22:36:14.521089]	[compute_info.get]	{
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
[2022-12-08 22:36:14.876812]	[compute_info.get]	{
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
[2022-12-08 22:36:14.915504]	[compute_info.get]	{
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
[2022-12-08 22:36:14.953640]	[compute_info.get]	{
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
[2022-12-08 22:36:15.008695]	[compute_info.get]	{
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
[2022-12-08 22:36:15.114226]	[compute_info.get]	{
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
[2022-12-08 22:36:15.189563]	[compute_info.get]	{
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
[2022-12-08 22:36:15.200684]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a4b276752d3139e3141c",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6336a4b276752d3139e3141c"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a50b76752d3139e32a16",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6336a50b76752d3139e32a16"
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
            "Moid": "619d05ae76752d313994a00a",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
        }
    ],
    "AssetTag": "",
    "AvailableMemory": 393216,
    "BiosBootmode": null,
    "BiosPostComplete": false,
    "BiosTokenSettings": {
        "ClassId": "mo.MoRef",
        "Moid": "6336a4b276752d3139e314c3",
        "ObjectType": "bios.TokenSettings",
        "link": "https://www.intersight.com/api/v1/bios/TokenSettings/6336a4b276752d3139e314c3"
    },
    "BiosUnits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a4b276752d3139e3143f",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/6336a4b276752d3139e3143f"
        }
    ],
    "BiosVfSelectMemoryRasConfiguration": null,
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "6335c26e76752d3139b9694e",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/6335c26e76752d3139b9694e"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "6336a4b276752d3139e31423",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6336a4b276752d3139e31423"
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
    "ChassisId": "2",
    "ClassId": "compute.Blade",
    "ComputePersonality": null,
    "CreateTime": "2022-09-29T16:06:06.567Z",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Dn": "sys/chassis-2/blade-1",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "EquipmentChassis": {
        "ClassId": "mo.MoRef",
        "Moid": "619d05ae76752d313994a00a",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
    },
    "EquipmentIoExpanders": [],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6335c40f76752d3139b9b32a",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6335c40f76752d3139b9b32a"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.52.41",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.52.62",
            "Dn": "sys/chassis-2/blade-1/mgmt/ipv4-static-addr",
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
            "Address": "10.58.26.5",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.26.62",
            "Dn": "sys/chassis-2/blade-1/mgmt/ipv4-prof-addr",
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
        "Moid": "6336a4b276752d3139e31447",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6336a4b276752d3139e31447"
    },
    "ManagementMode": "UCSM",
    "MemoryArrays": [],
    "MemorySpeed": "2666",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.52.41, 10.58.26.5",
    "ModTime": "2022-11-09T11:54:30.339Z",
    "Model": "UCSB-B200-M5",
    "Moid": "6335c26e76752d3139b9694c",
    "Name": "FI-ucsb1-eu-spdc-2-1",
    "NumAdaptors": 2,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 8,
    "NumFcHostInterfaces": 0,
    "NumThreads": 80,
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
        "Moid": "619d05ae76752d313994a00a",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
    },
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a4b276752d3139e3143b",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/6336a4b276752d3139e3143b"
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
    "Serial": "FLM241501FB",
    "ServiceProfile": "org-root/org-EU-SPN/ls-esx51-eu-spdc",
    "SharedScope": "",
    "SlotId": 1,
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
    "TotalMemory": 393216,
    "TunneledKvm": false,
    "UserLabel": "",
    "Uuid": "315220a5-2121-4e5b-0101-e1dc0000010f",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:36:17.459451]	[computes_info.get_server_info]	Thread result: 5fdf9d026176752d35e4ac4e
[2022-12-08 22:36:17.975014]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a4b276752d3139e31487",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6336a4b276752d3139e31487"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a4b276752d3139e31492",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6336a4b276752d3139e31492"
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
            "Moid": "619d05ae76752d313994a00a",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
        }
    ],
    "AssetTag": "",
    "AvailableMemory": 393216,
    "BiosBootmode": null,
    "BiosPostComplete": false,
    "BiosTokenSettings": {
        "ClassId": "mo.MoRef",
        "Moid": "6336a4b276752d3139e3143d",
        "ObjectType": "bios.TokenSettings",
        "link": "https://www.intersight.com/api/v1/bios/TokenSettings/6336a4b276752d3139e3143d"
    },
    "BiosUnits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a4b276752d3139e31437",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/6336a4b276752d3139e31437"
        }
    ],
    "BiosVfSelectMemoryRasConfiguration": null,
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "6335c53776752d3139b9e46b",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/6335c53776752d3139b9e46b"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "6336a4b276752d3139e3142a",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6336a4b276752d3139e3142a"
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
    "ChassisId": "2",
    "ClassId": "compute.Blade",
    "ComputePersonality": null,
    "CreateTime": "2022-09-29T16:14:17.973Z",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Dn": "sys/chassis-2/blade-2",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "EquipmentChassis": {
        "ClassId": "mo.MoRef",
        "Moid": "619d05ae76752d313994a00a",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
    },
    "EquipmentIoExpanders": [],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6335c4c976752d3139b9d1f2",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6335c4c976752d3139b9d1f2"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.52.42",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.52.62",
            "Dn": "sys/chassis-2/blade-2/mgmt/ipv4-static-addr",
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
            "Address": "10.58.26.6",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.26.62",
            "Dn": "sys/chassis-2/blade-2/mgmt/ipv4-prof-addr",
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
        "Moid": "6335c53776752d3139b9e46d",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6335c53776752d3139b9e46d"
    },
    "ManagementMode": "UCSM",
    "MemoryArrays": [],
    "MemorySpeed": "2666",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.52.42, 10.58.26.6",
    "ModTime": "2022-11-09T11:54:30.297Z",
    "Model": "UCSB-B200-M5",
    "Moid": "6335c45976752d3139b9bf94",
    "Name": "FI-ucsb1-eu-spdc-2-2",
    "NumAdaptors": 2,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 8,
    "NumFcHostInterfaces": 0,
    "NumThreads": 80,
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
        "Moid": "619d05ae76752d313994a00a",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
    },
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a4b276752d3139e31426",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/6336a4b276752d3139e31426"
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
    "Serial": "FLM24140BJB",
    "ServiceProfile": "org-root/org-EU-SPN/ls-esx52-eu-spdc",
    "SharedScope": "",
    "SlotId": 2,
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
    "TotalMemory": 393216,
    "TunneledKvm": false,
    "UserLabel": "",
    "Uuid": "315220a5-2121-4e5b-0101-e1dc0000011f",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:36:20.432661]	[computes_info.get_server_info]	Thread result: 5fdfa1806176752d35e678c2
[2022-12-08 22:36:20.728678]	[computes_info.get_server_info]	Thread result: 5fdfe47f6176752d35001995
[2022-12-08 22:36:20.855841]	[computes_info.get_server_info]	Thread result: 5fdf9c786176752d35e47110
[2022-12-08 22:36:20.891906]	[computes_info.get_server_info]	Thread result: 5fdf9c016176752d35e44795
[2022-12-08 22:36:20.908859]	[computes_info.get_server_info]	Thread result: 5fdfe80d6176752d3502b008
[2022-12-08 22:36:21.379684]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a4b276752d3139e31428",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6336a4b276752d3139e31428"
        }
    ],
    "AdminPowerState": "policy",
    "AlarmSummary": {
        "ClassId": "compute.AlarmSummary",
        "Critical": 9,
        "Health": "Critical",
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
    "AvailableMemory": 524288,
    "BiosBootmode": null,
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosUnits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6336a4b276752d3139e314c5",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/6336a4b276752d3139e314c5"
        }
    ],
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "6336a4b276752d3139e31443",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6336a4b276752d3139e31443"
    },
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "6336a4b276752d3139e3144d",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/6336a4b276752d3139e3144d"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "6336a4b276752d3139e31445",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6336a4b276752d3139e31445"
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
    "ComputePersonality": [],
    "CreateTime": "2022-09-29T18:20:35.079Z",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Dn": "sys/chassis-1/blade-1",
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
            "Moid": "6335e1f376752d3139bf12c7",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6335e1f376752d3139bf12c7"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.52.33",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.52.62",
            "Dn": "sys/chassis-1/blade-1/mgmt/ipv4-static-addr",
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
            "Address": "10.58.26.1",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.26.62",
            "Dn": "sys/chassis-1/blade-1/mgmt/ipv4-prof-addr",
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
        "Moid": "6336a4b276752d3139e3147f",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6336a4b276752d3139e3147f"
    },
    "ManagementMode": "UCSM",
    "MemoryArrays": [],
    "MemorySpeed": "2133",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.52.33, 10.58.26.1",
    "ModTime": "2022-12-02T22:39:58.949Z",
    "Model": "UCSB-B200-M4",
    "Moid": "6335e1f376752d3139bf12b8",
    "Name": "FI-ucsb1-eu-spdc-1-1",
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
            "Moid": "6336a4b276752d3139e31483",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/6336a4b276752d3139e31483"
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
    "Serial": "FCH205371PZ",
    "ServiceProfile": "org-root/org-EU-SPN/ls-esx41-eu-spdc",
    "SharedScope": "",
    "SlotId": 1,
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
    "TotalMemory": 524288,
    "TunneledKvm": false,
    "UserLabel": "",
    "Uuid": "315220a5-2121-4e5b-0101-e1dc0000014f",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:36:21.676332]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337063276752d3139f3cc25",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6337063276752d3139f3cc25"
        }
    ],
    "AdminPowerState": "policy",
    "AlarmSummary": {
        "ClassId": "compute.AlarmSummary",
        "Critical": 9,
        "Health": "Critical",
        "Info": 1,
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
    "AvailableMemory": 524288,
    "BiosBootmode": null,
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosUnits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f64f76752d31391e7818",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/6337f64f76752d31391e7818"
        }
    ],
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e85e8",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6337f68b76752d31391e85e8"
    },
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "6337021776752d3139f31631",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/6337021776752d3139f31631"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "6337063276752d3139f3cc64",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6337063276752d3139f3cc64"
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
    "ComputePersonality": [],
    "CreateTime": "2022-09-30T14:46:36.147Z",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Dn": "sys/chassis-1/blade-2",
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
            "Moid": "6337021776752d3139f31633",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6337021776752d3139f31633"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.52.34",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.52.62",
            "Dn": "sys/chassis-1/blade-2/mgmt/ipv4-static-addr",
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
            "Address": "10.58.26.2",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.26.62",
            "Dn": "sys/chassis-1/blade-2/mgmt/ipv4-prof-addr",
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
        "Moid": "6337f68b76752d31391e85fb",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f68b76752d31391e85fb"
    },
    "ManagementMode": "UCSM",
    "MemoryArrays": [],
    "MemorySpeed": "2133",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.52.34, 10.58.26.2",
    "ModTime": "2022-12-02T22:39:58.94Z",
    "Model": "UCSB-B200-M4",
    "Moid": "6337014c76752d3139f2f459",
    "Name": "FI-ucsb1-eu-spdc-1-2",
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
            "Moid": "6337f68b76752d31391e85d2",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/6337f68b76752d31391e85d2"
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
    "Serial": "FCH20527XXD",
    "ServiceProfile": "org-root/org-EU-SPN/ls-esx42-eu-spdc",
    "SharedScope": "",
    "SlotId": 2,
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
    "TotalMemory": 524288,
    "TunneledKvm": false,
    "UserLabel": "",
    "Uuid": "315220a5-2121-4e5b-0101-e1dc0000015f",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:36:21.871614]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337063276752d3139f3cc89",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6337063276752d3139f3cc89"
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
            "Moid": "6337f68b76752d31391e8566",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/6337f68b76752d31391e8566"
        }
    ],
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e8561",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6337f68b76752d31391e8561"
    },
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "6337063276752d3139f3ccae",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/6337063276752d3139f3ccae"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "6337063276752d3139f3ccb0",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6337063276752d3139f3ccb0"
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
    "ComputePersonality": [],
    "CreateTime": "2022-09-30T15:07:30.234Z",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Dn": "sys/chassis-1/blade-3",
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
            "Moid": "63371c9176752d3139f7dab5",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/63371c9176752d3139f7dab5"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.52.35",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.52.62",
            "Dn": "sys/chassis-1/blade-3/mgmt/ipv4-static-addr",
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
            "Address": "10.58.26.3",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.26.62",
            "Dn": "sys/chassis-1/blade-3/mgmt/ipv4-prof-addr",
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
        "Moid": "6337f68b76752d31391e85be",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f68b76752d31391e85be"
    },
    "ManagementMode": "UCSM",
    "MemoryArrays": [],
    "MemorySpeed": "2133",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.52.35, 10.58.26.3",
    "ModTime": "2022-12-02T22:39:58.963Z",
    "Model": "UCSB-B200-M4",
    "Moid": "6337063276752d3139f3cc83",
    "Name": "FI-ucsb1-eu-spdc-1-3",
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
            "Moid": "6337f64f76752d31391e780c",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/6337f64f76752d31391e780c"
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
    "Serial": "FCH20437VXH",
    "ServiceProfile": "org-root/org-EU-SPN/ls-esx43-eu-spdc",
    "SharedScope": "",
    "SlotId": 3,
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
    "Uuid": "315220a5-2121-4e5b-0101-e1dc0000012f",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:36:21.942427]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f68b76752d31391e8581",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6337f68b76752d31391e8581"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f68b76752d31391e85b2",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6337f68b76752d31391e85b2"
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
            "Moid": "619d05ae76752d313994a00a",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
        }
    ],
    "AssetTag": "",
    "AvailableMemory": 196608,
    "BiosBootmode": null,
    "BiosPostComplete": false,
    "BiosTokenSettings": {
        "ClassId": "mo.MoRef",
        "Moid": "63371d0c76752d3139f7ee4d",
        "ObjectType": "bios.TokenSettings",
        "link": "https://www.intersight.com/api/v1/bios/TokenSettings/63371d0c76752d3139f7ee4d"
    },
    "BiosUnits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f68b76752d31391e856e",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/6337f68b76752d31391e856e"
        }
    ],
    "BiosVfSelectMemoryRasConfiguration": null,
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f64f76752d31391e7812",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/6337f64f76752d31391e7812"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e8577",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6337f68b76752d31391e8577"
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
    "ChassisId": "2",
    "ClassId": "compute.Blade",
    "ComputePersonality": null,
    "CreateTime": "2022-09-30T16:42:57.291Z",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Dn": "sys/chassis-2/blade-4",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "EquipmentChassis": {
        "ClassId": "mo.MoRef",
        "Moid": "619d05ae76752d313994a00a",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
    },
    "EquipmentIoExpanders": [],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "63371c9176752d3139f7da90",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/63371c9176752d3139f7da90"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.52.44",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.52.62",
            "Dn": "sys/chassis-2/blade-4/mgmt/ipv4-static-addr",
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
            "Address": "10.58.26.8",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.26.62",
            "Dn": "sys/chassis-2/blade-4/mgmt/ipv4-prof-addr",
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
        "Moid": "6337f6cc76752d31391e931c",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f6cc76752d31391e931c"
    },
    "ManagementMode": "UCSM",
    "MemoryArrays": [],
    "MemorySpeed": "2666",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.52.44, 10.58.26.8",
    "ModTime": "2022-11-09T11:54:30.26Z",
    "Model": "UCSB-B200-M5",
    "Moid": "63371c9176752d3139f7da78",
    "Name": "FI-ucsb1-eu-spdc-2-4",
    "NumAdaptors": 2,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 8,
    "NumFcHostInterfaces": 0,
    "NumThreads": 80,
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
        "Moid": "619d05ae76752d313994a00a",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
    },
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f68b76752d31391e85a2",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/6337f68b76752d31391e85a2"
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
    "Serial": "FLM24140B0B",
    "ServiceProfile": "org-root/org-EU-SPN/ls-esx54-eu-spdc",
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
    "TotalMemory": 196608,
    "TunneledKvm": false,
    "UserLabel": "",
    "Uuid": "315220a5-2121-4e5b-0101-e1dc0000015e",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:36:22.231897]	[compute_info.get]	{
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
[2022-12-08 22:36:23.526149]	[computes_info.get_server_info]	Thread result: 6335c26e76752d3139b9694c
[2022-12-08 22:36:23.556790]	[compute_info.get]	{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f64f76752d31391e7808",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6337f64f76752d31391e7808"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f68b76752d31391e8558",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/6337f68b76752d31391e8558"
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
            "Moid": "619d05ae76752d313994a00a",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
        }
    ],
    "AssetTag": "",
    "AvailableMemory": 196608,
    "BiosBootmode": null,
    "BiosPostComplete": false,
    "BiosTokenSettings": {
        "ClassId": "mo.MoRef",
        "Moid": "63371d0c76752d3139f7ee4b",
        "ObjectType": "bios.TokenSettings",
        "link": "https://www.intersight.com/api/v1/bios/TokenSettings/63371d0c76752d3139f7ee4b"
    },
    "BiosUnits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f6cc76752d31391e934d",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/6337f6cc76752d31391e934d"
        }
    ],
    "BiosVfSelectMemoryRasConfiguration": null,
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f68b76752d31391e8588",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/6337f68b76752d31391e8588"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "6337f64f76752d31391e781c",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6337f64f76752d31391e781c"
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
    "ChassisId": "2",
    "ClassId": "compute.Blade",
    "ComputePersonality": null,
    "CreateTime": "2022-09-30T16:42:57.325Z",
    "DeviceMoId": "618942976f72612d309dfbe1",
    "Dn": "sys/chassis-2/blade-3",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "EquipmentChassis": {
        "ClassId": "mo.MoRef",
        "Moid": "619d05ae76752d313994a00a",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
    },
    "EquipmentIoExpanders": [],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "63371c9176752d3139f7da92",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/63371c9176752d3139f7da92"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.52.43",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.52.62",
            "Dn": "sys/chassis-2/blade-3/mgmt/ipv4-static-addr",
            "HttpPort": 80,
            "HttpsPort": 443,
            "KvmPort": 2068,
            "KvmVlan": 0,
            "Name": "Outband",
            "ObjectType": "compute.IpAddress",
            "Subnet": "255.255.255.0",
            "Type": "VnicIpV4StaticAddr"
        },
        {
            "Address": "10.58.26.7",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.26.62",
            "Dn": "sys/chassis-2/blade-3/mgmt/ipv4-prof-addr",
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
        "Moid": "6337f68b76752d31391e85dc",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f68b76752d31391e85dc"
    },
    "ManagementMode": "UCSM",
    "MemoryArrays": [],
    "MemorySpeed": "2666",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.52.43, 10.58.26.7",
    "ModTime": "2022-11-09T11:54:30.369Z",
    "Model": "UCSB-B200-M5",
    "Moid": "63371c9176752d3139f7da82",
    "Name": "FI-ucsb1-eu-spdc-2-3",
    "NumAdaptors": 2,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 8,
    "NumFcHostInterfaces": 0,
    "NumThreads": 80,
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
        "Moid": "619d05ae76752d313994a00a",
        "ObjectType": "equipment.Chassis",
        "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
    },
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6337f6cc76752d31391e9340",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/6337f6cc76752d31391e9340"
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
    "Serial": "FLM241501CT",
    "ServiceProfile": "org-root/org-EU-SPN/ls-esx53-eu-spdc",
    "SharedScope": "",
    "SlotId": 3,
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
    "TotalMemory": 196608,
    "TunneledKvm": false,
    "UserLabel": "",
    "Uuid": "315220a5-2121-4e5b-0101-e1dc0000014e",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null
}
[2022-12-08 22:36:23.758002]	[computes_info.get_server_info]	Thread result: 5fdfdc3b6176752d35fce0a9
[2022-12-08 22:36:26.322098]	[computes_info.get_server_info]	Thread result: 6335c45976752d3139b9bf94
[2022-12-08 22:36:29.726094]	[computes_info.get_server_info]	Thread result: 6335e1f376752d3139bf12b8
[2022-12-08 22:36:30.213297]	[computes_info.get_server_info]	Thread result: 6337014c76752d3139f2f459
[2022-12-08 22:36:30.705792]	[computes_info.get_server_info]	Thread result: 6337063276752d3139f3cc83
[2022-12-08 22:36:30.950805]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da78
[2022-12-08 22:36:31.465319]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da74
[2022-12-08 22:36:31.752138]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da82
[2022-12-08 22:36:32.919204]	[computes_info.get]	Selected 15 servers with requested details in 24637 ms
[2022-12-08 22:36:32.920629]	[computes_info.get]	Total time 29540 ms


Log: isctl
-----------

2022-12-08 22:36:06.474675	True	3035	93	isctl get compute rackunit   -o json --top 100
2022-12-08 22:36:08.277290	True	1790	10	isctl get compute blade   -o json --top 100
2022-12-08 22:36:11.962077	True	2171	8	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '5fdfa1686f72612d300b383f', '5fdfdc206f72612d30120ab4', '5fdfe4666f72612d30130510', '5fdfe7d86f72612d30136fed', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1')"  -o json --top 100
2022-12-08 22:36:12.057341	True	1796	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-07T22:36:10.000Z"  -o json --top 100
2022-12-08 22:36:12.088071	True	2040	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100


Log: redfish
-------------

2022-12-08 22:36:16.232862	True	1700	connect 10.58.50.41
2022-12-08 22:36:16.291258	True	57	10.58.50.41:/redfish/v1/Systems
2022-12-08 22:36:16.358578	True	62	10.58.50.41:/redfish/v1/Chassis
2022-12-08 22:36:16.460513	True	1537	connect 10.58.50.43
2022-12-08 22:36:16.496904	True	1602	connect 10.58.50.42
2022-12-08 22:36:16.518361	True	56	10.58.50.43:/redfish/v1/Systems
2022-12-08 22:36:16.542765	True	1579	connect 10.58.50.44
2022-12-08 22:36:16.550742	True	186	10.58.50.41:/redfish/v1/Chassis/1
2022-12-08 22:36:16.554730	True	57	10.58.50.42:/redfish/v1/Systems
2022-12-08 22:36:16.580068	True	58	10.58.50.43:/redfish/v1/Chassis
2022-12-08 22:36:16.604181	True	61	10.58.50.44:/redfish/v1/Systems
2022-12-08 22:36:16.625276	True	63	10.58.50.42:/redfish/v1/Chassis
2022-12-08 22:36:16.659001	True	1641	connect 10.58.50.45
2022-12-08 22:36:16.663773	True	54	10.58.50.44:/redfish/v1/Chassis
2022-12-08 22:36:16.698684	True	1575	connect 10.58.50.46
2022-12-08 22:36:16.721080	True	61	10.58.50.45:/redfish/v1/Systems
2022-12-08 22:36:16.724038	True	128	10.58.50.43:/redfish/v1/Chassis/1
2022-12-08 22:36:16.751763	True	121	10.58.50.42:/redfish/v1/Chassis/1
2022-12-08 22:36:16.770072	True	69	10.58.50.46:/redfish/v1/Systems
2022-12-08 22:36:16.790016	True	61	10.58.50.45:/redfish/v1/Chassis
2022-12-08 22:36:16.804177	True	125	10.58.50.44:/redfish/v1/Chassis/1
2022-12-08 22:36:16.840252	True	60	10.58.50.46:/redfish/v1/Chassis
2022-12-08 22:36:16.875683	True	1672	connect 10.58.50.47
2022-12-08 22:36:16.917466	True	121	10.58.50.45:/redfish/v1/Chassis/1
2022-12-08 22:36:16.938401	True	59	10.58.50.47:/redfish/v1/Systems
2022-12-08 22:36:16.974434	True	122	10.58.50.46:/redfish/v1/Chassis/1
2022-12-08 22:36:17.011004	True	61	10.58.50.47:/redfish/v1/Chassis
2022-12-08 22:36:17.144815	True	121	10.58.50.47:/redfish/v1/Chassis/1
2022-12-08 22:36:17.322192	True	766	10.58.50.41:/redfish/v1/Chassis/1/Power
2022-12-08 22:36:17.452367	True	719	10.58.50.43:/redfish/v1/Chassis/1/Power
2022-12-08 22:36:17.468998	True	658	10.58.50.44:/redfish/v1/Chassis/1/Power
2022-12-08 22:36:17.560068	True	795	10.58.50.42:/redfish/v1/Chassis/1/Power
2022-12-08 22:36:17.647806	True	660	10.58.50.46:/redfish/v1/Chassis/1/Power
2022-12-08 22:36:17.859170	True	703	10.58.50.47:/redfish/v1/Chassis/1/Power
2022-12-08 22:36:17.951589	True	486	disconnect 10.58.50.43
2022-12-08 22:36:18.918795	True	1578	connect 10.58.50.41
2022-12-08 22:36:18.983747	True	60	10.58.50.41:/redfish/v1/Systems
2022-12-08 22:36:19.033204	True	1555	connect 10.58.50.44
2022-12-08 22:36:19.053148	True	61	10.58.50.41:/redfish/v1/Chassis
2022-12-08 22:36:19.097051	True	59	10.58.50.44:/redfish/v1/Systems
2022-12-08 22:36:19.142854	True	1568	connect 10.58.50.42
2022-12-08 22:36:19.170992	True	61	10.58.50.44:/redfish/v1/Chassis
2022-12-08 22:36:19.192872	True	127	10.58.50.41:/redfish/v1/Chassis/1
2022-12-08 22:36:19.198553	True	1531	connect 10.58.50.46
2022-12-08 22:36:19.203648	True	59	10.58.50.42:/redfish/v1/Systems
2022-12-08 22:36:19.263239	True	61	10.58.50.46:/redfish/v1/Systems
2022-12-08 22:36:19.274746	True	61	10.58.50.42:/redfish/v1/Chassis
2022-12-08 22:36:19.308113	True	124	10.58.50.44:/redfish/v1/Chassis/1
2022-12-08 22:36:19.337461	True	60	10.58.50.46:/redfish/v1/Chassis
2022-12-08 22:36:19.465468	True	122	10.58.50.46:/redfish/v1/Chassis/1
2022-12-08 22:36:19.484415	True	193	10.58.50.42:/redfish/v1/Chassis/1
2022-12-08 22:36:19.487405	True	1605	connect 10.58.50.47
2022-12-08 22:36:19.549692	True	58	10.58.50.47:/redfish/v1/Systems
2022-12-08 22:36:19.619769	True	59	10.58.50.47:/redfish/v1/Chassis
2022-12-08 22:36:19.748935	True	123	10.58.50.47:/redfish/v1/Chassis/1
2022-12-08 22:36:20.390453	True	1076	10.58.50.44:/redfish/v1/Chassis/1/Thermal
2022-12-08 22:36:20.602592	True	3673	10.58.50.45:/redfish/v1/Chassis/1/Power
2022-12-08 22:36:20.694929	True	1215	10.58.50.46:/redfish/v1/Chassis/1/Thermal
2022-12-08 22:36:20.836533	True	1339	10.58.50.42:/redfish/v1/Chassis/1/Thermal
2022-12-08 22:36:20.878051	True	1671	10.58.50.41:/redfish/v1/Chassis/1/Thermal
2022-12-08 22:36:20.893897	True	1117	10.58.50.47:/redfish/v1/Chassis/1/Thermal
2022-12-08 22:36:20.926025	True	487	disconnect 10.58.50.44
2022-12-08 22:36:21.164556	True	431	disconnect 10.58.50.46
2022-12-08 22:36:21.279078	True	417	disconnect 10.58.50.42
2022-12-08 22:36:21.348428	True	414	disconnect 10.58.50.44
2022-12-08 22:36:21.361951	True	449	disconnect 10.58.50.47
2022-12-08 22:36:21.530612	True	630	disconnect 10.58.50.41
2022-12-08 22:36:21.635915	True	463	disconnect 10.58.50.46
2022-12-08 22:36:21.836602	True	548	disconnect 10.58.50.42
2022-12-08 22:36:21.895547	True	522	disconnect 10.58.50.47
2022-12-08 22:36:22.199959	True	656	disconnect 10.58.50.41
2022-12-08 22:36:22.265260	True	1623	connect 10.58.50.45
2022-12-08 22:36:22.335489	True	64	10.58.50.45:/redfish/v1/Systems
2022-12-08 22:36:22.417546	True	65	10.58.50.45:/redfish/v1/Chassis
2022-12-08 22:36:22.622819	True	186	10.58.50.45:/redfish/v1/Chassis/1
2022-12-08 22:36:23.747031	True	1098	10.58.50.45:/redfish/v1/Chassis/1/Thermal
2022-12-08 22:36:32.267210	True	456	disconnect 10.58.50.45
2022-12-08 22:36:32.841125	True	565	disconnect 10.58.50.45


Log: ucsm
----------

2022-12-08 22:36:16.774060	True	1567	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:17.250505	True	473	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:17.781796	True	527	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:18.237657	True	455	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:36:18.676073	True	432	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:19.558671	True	1577	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:20.064237	True	503	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:20.293378	True	1610	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:20.763846	True	695	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:20.824999	True	509	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:21.224286	True	459	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:36:21.405200	True	577	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:21.667156	True	438	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:21.930196	True	521	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:36:22.461674	True	524	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:36:23.055364	True	590	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:36:23.184073	True	1793	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:23.351677	True	1677	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:23.517901	True	452	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:23.663287	True	477	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:23.673234	True	1981	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:23.846452	True	490	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:24.002856	True	2114	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:24.226046	True	548	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:24.293863	True	627	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:24.352175	True	2400	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:24.394182	True	544	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:24.636672	True	629	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:24.685309	True	2441	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:24.733536	True	438	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:36:24.777880	True	541	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:24.837857	True	483	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:24.862261	True	466	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:36:25.104115	True	1542	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:25.157233	True	519	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:25.161189	True	425	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:25.262349	True	480	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:36:25.157233	True	470	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:25.347025	True	484	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:36:25.383715	True	543	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:25.602135	True	495	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:25.625074	True	466	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:36:25.693922	True	424	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:25.818587	True	432	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:36:25.829558	True	559	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:25.895630	True	545	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:36:26.054443	True	424	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:26.106487	True	499	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:26.268085	True	446	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:26.319613	True	413	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:26.323141	True	492	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:36:26.541628	True	433	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:36:26.747268	True	1584	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:26.750899	True	423	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:26.975852	True	430	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:27.216776	True	463	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:27.359792	True	1660	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:27.680096	True	1618	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:27.780930	True	560	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:27.844150	True	480	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:28.011838	True	1733	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:28.164819	True	478	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:28.226477	True	444	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:36:28.349770	True	502	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:28.462028	True	1593	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:28.468145	True	453	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:28.717135	True	548	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:28.739110	True	511	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:36:28.766035	True	1788	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:28.791998	True	440	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:36:28.922697	True	456	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:29.012288	True	541	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:29.186451	True	467	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:36:29.197453	True	430	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:36:29.238426	True	445	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:36:29.278005	True	537	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:36:29.459383	True	446	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:36:29.474344	True	547	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:29.634525	True	446	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:36:29.718383	True	519	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:36:29.722333	True	436	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:29.779513	True	539	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:36:29.930529	True	469	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:36:29.982206	True	506	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:36:30.210148	True	421	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:30.229277	True	593	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:36:30.262154	True	542	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:36:30.454707	True	469	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:36:30.506094	True	574	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:36:30.696843	True	458	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:30.753129	True	490	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:36:30.947783	True	431	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:31.017591	True	561	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:36:31.320910	True	565	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:36:31.462221	True	436	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:36:31.747190	True	417	disconnect vip-ucsb1.emea-sp.cisco.com
```
