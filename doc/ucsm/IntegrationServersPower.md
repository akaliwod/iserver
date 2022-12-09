# Get Intersight Servers with Power Information

```
# iserver get servers --group ucsm -c power

+---------+----+----+----------------------+------------------+-------------+-------------+--------------+---------+---------+---------+
| SF      | MF | WF | Name                 | Model            | Serial      | IP          | Consumed [W] | Min [W] | Avg [W] | Max [W] |
+---------+----+----+----------------------+------------------+-------------+-------------+--------------+---------+---------+---------+
| P+ C(9) | CU |    | FI-ucsb1-eu-spdc-1-1 | (B) UCSB-B200-M4 | FCH205371PZ | 10.58.52.33 | 138.0        | 138.0   | 138.0   | 138.0   | 
| P+ C(9) | CU |    | FI-ucsb1-eu-spdc-1-2 | (B) UCSB-B200-M4 | FCH20527XXD | 10.58.52.34 | 138.0        | 138.0   | 138.0   | 138.0   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-1-3 | (B) UCSB-B200-M4 | FCH20437VXH | 10.58.52.35 | 126.0        | 126.0   | 127.2   | 138.0   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-1-4 | (B) UCSB-B200-M4 | FCH205371UU | 10.58.52.36 | 126.0        | 120.0   | 126.0   | 132.0   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-1 | (B) UCSB-B200-M5 | FLM241501FB | 10.58.52.41 | 206.7        | 206.7   | 206.7   | 206.7   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-2 | (B) UCSB-B200-M5 | FLM24140BJB | 10.58.52.42 | 234.0        | 234.0   | 234.98  | 237.9   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-3 | (B) UCSB-B200-M5 | FLM241501CT | 10.58.52.43 | 195.0        | 195.0   | 195.78  | 198.9   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-4 | (B) UCSB-B200-M5 | FLM24140B0B | 10.58.52.44 | 237.9        | 234.0   | 240.24  | 245.7   | 
+---------+----+----+----------------------+------------------+-------------+-------------+--------------+---------+---------+---------+
```

JSON Output

```
# iserver get servers --group ucsm -c power

[
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
                "time_collected": "2022-12-08T22:32:59.891",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-2",
                "consumed_power": 234.0,
                "input_current": 19.25,
                "input_voltage": 12.15,
                "consumed_power_avg": 234.98,
                "input_current_avg": 19.33,
                "input_voltage_avg": 12.15,
                "consumed_power_min": 234.0,
                "input_current_min": 19.25,
                "input_voltage_min": 12.15,
                "consumed_power_max": 237.9,
                "input_current_max": 19.57,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 234.0,
                "PowerMin": 234.0,
                "PowerAvg": 234.98,
                "PowerMax": 237.9
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
                "time_collected": "2022-12-08T22:32:15.562",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-3",
                "consumed_power": 126.0,
                "input_current": 10.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 127.2,
                "input_current_avg": 10.62,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 126.0,
                "input_current_min": 10.52,
                "input_voltage_min": 11.98,
                "consumed_power_max": 138.0,
                "input_current_max": 11.52,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 126.0,
                "PowerMin": 126.0,
                "PowerAvg": 127.2,
                "PowerMax": 138.0
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
                "time_collected": "2022-12-08T22:32:41.884",
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
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
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
                "time_collected": "2022-12-08T22:32:33.481",
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
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ C(9)",
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
                "time_collected": "2022-12-08T22:32:51.813",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-4",
                "consumed_power": 237.9,
                "input_current": 19.67,
                "input_voltage": 12.1,
                "consumed_power_avg": 240.24,
                "input_current_avg": 19.86,
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
                "PowerAvg": 240.24,
                "PowerMax": 245.7
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
                "time_collected": "2022-12-08T22:32:54.869",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-3",
                "consumed_power": 195.0,
                "input_current": 16.04,
                "input_voltage": 12.15,
                "consumed_power_avg": 195.78,
                "input_current_avg": 16.16,
                "input_voltage_avg": 12.11,
                "consumed_power_min": 195.0,
                "input_current_min": 16.04,
                "input_voltage_min": 12.1,
                "consumed_power_max": 198.9,
                "input_current_max": 16.44,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 195.0,
                "PowerMin": 195.0,
                "PowerAvg": 195.78,
                "PowerMax": 198.9
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
                "time_collected": "2022-12-08T22:32:43.789",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-1",
                "consumed_power": 206.7,
                "input_current": 17.09,
                "input_voltage": 12.1,
                "consumed_power_avg": 206.7,
                "input_current_avg": 17.09,
                "input_voltage_avg": 12.1,
                "consumed_power_min": 206.7,
                "input_current_min": 17.09,
                "input_voltage_min": 12.1,
                "consumed_power_max": 206.7,
                "input_current_max": 17.09,
                "input_voltage_max": 12.1
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 206.7,
                "PowerMin": 206.7,
                "PowerAvg": 206.7,
                "PowerMax": 206.7
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
                "time_collected": "2022-12-08T22:32:49.993",
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
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ C(9)",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    }
]
```

Developer Output

```
# iserver get servers --group ucsm -c power

Developer output

{
    "duration": 20531,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 12946
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
        "success": 40,
        "failed": 0,
        "connect": 16,
        "disconnect": 0,
        "mo": 24,
        "connect_time": 24406,
        "disconnect_time": 0,
        "mo_time": 11585,
        "total_time": 35991
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
        "lines": 1979
    }
}

Log: debug
-----------

[2022-12-08 22:32:44.019973]	[computes_info.get]	Get servers settings: {
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
    "thermal": false,
    "env": false
}
[2022-12-08 22:32:44.021962]	[computes_info.get]	Get servers match rules: {
    "name": "",
    "model": "",
    "ip": [],
    "serials": [
        "FLM241501FB",
        "FLM24140BJB",
        "FCH20527XXD",
        "FCH205371PZ",
        "FLM24140B0B",
        "FCH20437VXH",
        "FCH205371UU",
        "FLM241501CT"
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
[2022-12-08 22:32:49.439939]	[computes_info.get]	All 103 servers base information in 5416 ms
[2022-12-08 22:32:49.441936]	[computes_info.get]	Base filter 8 servers in 0 ms
[2022-12-08 22:32:57.682547]	[compute_info.get]	{
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
[2022-12-08 22:32:58.097707]	[compute_info.get]	{
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
[2022-12-08 22:32:58.237164]	[compute_info.get]	{
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
[2022-12-08 22:32:58.302007]	[compute_info.get]	{
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
[2022-12-08 22:32:58.364347]	[compute_info.get]	{
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
[2022-12-08 22:32:58.396357]	[compute_info.get]	{
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
[2022-12-08 22:32:58.467932]	[compute_info.get]	{
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
[2022-12-08 22:32:58.506675]	[compute_info.get]	{
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
[2022-12-08 22:33:01.694490]	[computes_info.get_server_info]	Thread result: 6335c45976752d3139b9bf94
[2022-12-08 22:33:01.982959]	[computes_info.get_server_info]	Thread result: 6337063276752d3139f3cc83
[2022-12-08 22:33:02.262330]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da74
[2022-12-08 22:33:02.500381]	[computes_info.get_server_info]	Thread result: 6337014c76752d3139f2f459
[2022-12-08 22:33:03.097005]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da78
[2022-12-08 22:33:03.248236]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da82
[2022-12-08 22:33:03.612752]	[computes_info.get_server_info]	Thread result: 6335c26e76752d3139b9694c
[2022-12-08 22:33:03.908668]	[computes_info.get_server_info]	Thread result: 6335e1f376752d3139bf12b8
[2022-12-08 22:33:04.365628]	[computes_info.get]	Selected 8 servers with requested details in 14922 ms
[2022-12-08 22:33:04.367377]	[computes_info.get]	Total time 20346 ms


Log: isctl
-----------

2022-12-08 22:32:47.639623	True	3554	93	isctl get compute rackunit   -o json --top 100
2022-12-08 22:32:49.438828	True	1785	10	isctl get compute blade   -o json --top 100
2022-12-08 22:32:54.843858	True	2574	1	isctl get asset deviceregistration --filter "Moid in ('618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1')"  -o json --top 100
2022-12-08 22:32:55.079124	True	2627	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-08 22:32:55.201097	True	2406	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-07T22:32:52.000Z"  -o json --top 100


Log: ucsm
----------

2022-12-08 22:32:59.755952	True	1650	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:00.095371	True	1724	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:00.295169	True	538	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:00.376634	True	1974	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:00.601691	True	504	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:00.683296	True	2370	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:00.810144	True	513	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:00.845049	True	468	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:01.065144	True	2593	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:01.119059	True	517	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:01.137829	True	452	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:01.265827	True	453	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:33:01.376875	True	519	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:01.391614	True	2880	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:01.544868	True	477	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:01.552847	True	432	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:33:01.641910	True	502	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:01.692496	True	424	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:01.733367	True	4045	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:01.812714	True	434	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:33:01.848406	True	456	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:01.979970	True	423	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:02.025846	True	3784	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:02.074785	True	431	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:33:02.075531	True	528	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:02.211461	True	476	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:02.259333	True	444	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:02.384829	True	534	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:02.498386	True	420	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:02.546002	True	519	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:02.682636	True	495	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:33:02.756876	True	543	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:02.814999	True	428	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:33:03.063399	True	516	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:03.095011	True	410	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:03.183783	True	426	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:33:03.245177	True	428	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:03.489369	True	424	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 22:33:03.609480	True	423	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:03.906575	True	414	disconnect vip-ucsb1.emea-sp.cisco.com
```
