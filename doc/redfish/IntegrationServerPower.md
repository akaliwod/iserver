# Get Intersight Server with Power Information

```
# iserver get server --ip 10.58.50.41 --power

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | 4  | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+

Power Consumption (Watt)
------------------------
- Current      : 324
- Min          : 176
- Average      : 330
- Max          : 435
- Limit action : NoAction


+----------------+---------+--------+-------+-----------------+
| Sensor Name    | State   | Health | Volts | Upper Threshold |
+----------------+---------+--------+-------+-----------------+
| PSU1_VOUT      | Enabled | OK     | 12    | 14              | 
| PSU2_VOUT      | Enabled | OK     | 12.2  | 14              | 
| P12V           | Enabled | OK     | 11.89 | 13.166          | 
| P3V_BAT_SCALED | Enabled | OK     | 3.011 | 3.588           | 
+----------------+---------+--------+-------+-----------------+

+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU Name | State   | Health | Serial      | Firmware | Output (Watt) | Input (Watt) | Max (V) | Min (V) | Max (Hz) | Min (Hz) |
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| PSU1     | Enabled | OK     | LIT241244MU | 10062019 | 142           | 163          | 264     | 180     | 63       | 47       | 
| PSU2     | Enabled | OK     | LIT241244Z5 | 10062019 | 148           | 163          | 264     | 180     | 63       | 47       | 
+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
```

JSON Output

```
# iserver get server --ip 10.58.50.41 --power

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
                    "PowerInputWatts": 163,
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
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C240-M5SN",
    "LocatorLedOn": false,
    "FlagState": "P+ H",
    "FlagManagement": "CRi",
    "FlagWorkflow": "4"
}
```