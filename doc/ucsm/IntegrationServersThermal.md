# Get Intersight Servers with Thermal Information

```
# iserver get servers --group ucsm -c thermal

+---------+----+----+----------------------+------------------+-------------+-------------+------+---------+-------------+-------------+----------------+
| SF      | MF | WF | Name                 | Model            | Serial      | IP          | Fans | Sensors | Highest (C) | Min Gap (C) | Over Threshold |
+---------+----+----+----------------------+------------------+-------------+-------------+------+---------+-------------+-------------+----------------+
| P+ C(9) | CU |    | FI-ucsb1-eu-spdc-1-1 | (B) UCSB-B200-M4 | FCH205371PZ | 10.58.52.33 | N/A  | True    | 37.5        | N/A         | N/A            | 
| P+ C(9) | CU |    | FI-ucsb1-eu-spdc-1-2 | (B) UCSB-B200-M4 | FCH20527XXD | 10.58.52.34 | N/A  | True    | 38.0        | N/A         | N/A            | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-1-3 | (B) UCSB-B200-M4 | FCH20437VXH | 10.58.52.35 | N/A  | True    | 41.0        | N/A         | N/A            | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-1-4 | (B) UCSB-B200-M4 | FCH205371UU | 10.58.52.36 | N/A  | True    | 42.0        | N/A         | N/A            | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-1 | (B) UCSB-B200-M5 | FLM241501FB | 10.58.52.41 | N/A  | True    | 39.5        | N/A         | N/A            | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-2 | (B) UCSB-B200-M5 | FLM24140BJB | 10.58.52.42 | N/A  | True    | 49.0        | N/A         | N/A            | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-3 | (B) UCSB-B200-M5 | FLM241501CT | 10.58.52.43 | N/A  | True    | 37.0        | N/A         | N/A            | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-4 | (B) UCSB-B200-M5 | FLM24140B0B | 10.58.52.44 | N/A  | True    | 49.0        | N/A         | N/A            | 
+---------+----+----+----------------------+------------------+-------------+-------------+------+---------+-------------+-------------+----------------+
```

JSON Output

```
# iserver get servers --group ucsm -c thermal

[
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-1/board/temp-stats",
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 36.0,
                    "temperature_avg": 36.0,
                    "temperature_min": 36.0,
                    "temperature_max": 36.0
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:32:43.789",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 39.5,
                    "temperature_avg": 39.5,
                    "temperature_min": 39.5,
                    "temperature_max": 39.5
                },
                {
                    "dn": "sys/chassis-2/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                    "time_collected": "2022-12-08T22:32:43.789",
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
                "HighestTemperature": 39.5,
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-2/board/temp-stats",
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 42.0,
                    "temperature_avg": 42.17,
                    "temperature_min": 42.0,
                    "temperature_max": 42.5
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:32:59.891",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 49.0,
                    "temperature_avg": 48.83,
                    "temperature_min": 48.0,
                    "temperature_max": 49.5
                },
                {
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
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
                    "time_collected": "2022-12-08T22:32:59.891",
                    "chassis_rn": "chassis-2",
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
                    "dn": "sys/chassis-2/blade-2/board/memarray-1/mem-9/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:59.891",
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
                "HighestTemperature": 49.0,
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-1/board/temp-stats",
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 35.0,
                    "temperature_avg": 35.0,
                    "temperature_min": 34.5,
                    "temperature_max": 35.5
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:32:49.993",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 37.5,
                    "temperature_avg": 37.38,
                    "temperature_min": 37.0,
                    "temperature_max": 37.5
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:49.993",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
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
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-10/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-13",
                    "name": "MEM-13",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.5,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:49.993",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-14",
                    "name": "MEM-14",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
                    "chassis_rn": "chassis-1",
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
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-2/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-20",
                    "name": "MEM-20",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.5,
                    "temperature_min": 28.0,
                    "temperature_max": 29.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:49.993",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-1",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 27.0,
                    "temperature_avg": 27.0,
                    "temperature_min": 27.0,
                    "temperature_max": 27.0
                },
                {
                    "dn": "sys/chassis-1/blade-1/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
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
                    "time_collected": "2022-12-08T22:32:49.993",
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
                "HighestTemperature": 37.5,
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-2/board/temp-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
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
                    "time_collected": "2022-12-08T22:32:33.481",
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
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 35.0,
                    "temperature_avg": 34.75,
                    "temperature_min": 34.5,
                    "temperature_max": 35.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 38.0,
                    "temperature_avg": 38.0,
                    "temperature_min": 38.0,
                    "temperature_max": 38.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
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
                    "time_collected": "2022-12-08T22:32:33.481",
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
                    "time_collected": "2022-12-08T22:32:33.481",
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
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
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
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-14/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-14",
                    "name": "MEM-14",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-16",
                    "name": "MEM-16",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 32.0,
                    "temperature_min": 32.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-17/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-17",
                    "name": "MEM-17",
                    "type": "memory",
                    "temperature": 31.0,
                    "temperature_avg": 31.0,
                    "temperature_min": 31.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-19/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
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
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-2/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
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
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-20",
                    "name": "MEM-20",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.0,
                    "temperature_min": 30.0,
                    "temperature_max": 30.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-2",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-22",
                    "name": "MEM-22",
                    "type": "memory",
                    "temperature": 32.0,
                    "temperature_avg": 31.5,
                    "temperature_min": 31.0,
                    "temperature_max": 32.0
                },
                {
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-23/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
                    "chassis_rn": "chassis-1",
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
                    "dn": "sys/chassis-1/blade-2/board/memarray-1/mem-4/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:33.481",
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
                    "time_collected": "2022-12-08T22:32:33.481",
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
                    "time_collected": "2022-12-08T22:32:33.481",
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
                    "time_collected": "2022-12-08T22:32:33.481",
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
                "HighestTemperature": 38.0,
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-3/board/temp-stats",
                    "time_collected": "2022-12-08T22:33:15.487",
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
                    "time_collected": "2022-12-08T22:33:15.487",
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
                    "time_collected": "2022-12-08T22:33:15.487",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 36.5,
                    "temperature_avg": 36.5,
                    "temperature_min": 36.5,
                    "temperature_max": 36.5
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:33:15.487",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 41.0,
                    "temperature_avg": 41.0,
                    "temperature_min": 41.0,
                    "temperature_max": 41.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:33:15.487",
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
                    "time_collected": "2022-12-08T22:33:15.487",
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
                    "time_collected": "2022-12-08T22:33:15.487",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
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
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-16/dimm-env-stats",
                    "time_collected": "2022-12-08T22:33:15.487",
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
                    "time_collected": "2022-12-08T22:33:15.487",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 28.0,
                    "temperature_avg": 28.0,
                    "temperature_min": 28.0,
                    "temperature_max": 28.0
                },
                {
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T22:33:15.487",
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
                    "time_collected": "2022-12-08T22:33:15.487",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-3",
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
                    "dn": "sys/chassis-1/blade-3/board/memarray-1/mem-7/dimm-env-stats",
                    "time_collected": "2022-12-08T22:33:15.487",
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
                "HighestTemperature": 41.0,
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-1/blade-4/board/temp-stats",
                    "time_collected": "2022-12-08T22:32:41.884",
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
                    "time_collected": "2022-12-08T22:32:41.884",
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
                    "time_collected": "2022-12-08T22:32:41.884",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 38.5,
                    "temperature_avg": 38.5,
                    "temperature_min": 38.5,
                    "temperature_max": 38.5
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                    "time_collected": "2022-12-08T22:32:41.884",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 42.0,
                    "temperature_avg": 41.5,
                    "temperature_min": 41.0,
                    "temperature_max": 42.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:41.884",
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
                    "time_collected": "2022-12-08T22:32:41.884",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
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
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:41.884",
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
                    "time_collected": "2022-12-08T22:32:41.884",
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
                    "time_collected": "2022-12-08T22:32:41.884",
                    "chassis_rn": "chassis-1",
                    "blade_rn": "blade-4",
                    "array_rn": "memarray-1",
                    "dimm_rn": "mem-19",
                    "name": "MEM-19",
                    "type": "memory",
                    "temperature": 30.0,
                    "temperature_avg": 30.17,
                    "temperature_min": 30.0,
                    "temperature_max": 31.0
                },
                {
                    "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-22/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:41.884",
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
                    "time_collected": "2022-12-08T22:32:41.884",
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
                    "time_collected": "2022-12-08T22:32:41.884",
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
                "HighestTemperature": 42.0,
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-4/board/temp-stats",
                    "time_collected": "2022-12-08T22:32:51.813",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "name": "Motherboard Front",
                    "type": "motherboard",
                    "temperature": 21.0,
                    "fm_temp_sen_rear": 38.0,
                    "temperature_avg": 21.2,
                    "fm_temp_sen_rear_avg": 38.0,
                    "temperature_min": 21.0,
                    "fm_temp_sen_rear_min": 38.0,
                    "temperature_max": 22.0,
                    "fm_temp_sen_rear_max": 38.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/temp-stats",
                    "time_collected": "2022-12-08T22:32:51.813",
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
                    "time_collected": "2022-12-08T22:32:51.813",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 49.0,
                    "temperature_avg": 49.6,
                    "temperature_min": 48.0,
                    "temperature_max": 51.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/cpu-1/env-stats",
                    "time_collected": "2022-12-08T22:32:51.813",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-4",
                    "cpu_rn": "cpu-1",
                    "name": "CPU-1",
                    "type": "cpu",
                    "temperature": 42.0,
                    "temperature_avg": 41.6,
                    "temperature_min": 41.0,
                    "temperature_max": 42.0
                },
                {
                    "dn": "sys/chassis-2/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:51.813",
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
                    "time_collected": "2022-12-08T22:32:51.813",
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
                    "time_collected": "2022-12-08T22:32:51.813",
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
                    "time_collected": "2022-12-08T22:32:51.813",
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
                    "time_collected": "2022-12-08T22:32:51.813",
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
                    "time_collected": "2022-12-08T22:32:51.813",
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
                "HighestTemperature": 49.0,
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
        "Thermal": {
            "Data": [
                {
                    "dn": "sys/chassis-2/blade-3/board/temp-stats",
                    "time_collected": "2022-12-08T22:32:54.869",
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
                    "time_collected": "2022-12-08T22:32:54.869",
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
                    "time_collected": "2022-12-08T22:32:54.869",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
                    "cpu_rn": "cpu-2",
                    "name": "CPU-2",
                    "type": "cpu",
                    "temperature": 36.0,
                    "temperature_avg": 36.17,
                    "temperature_min": 36.0,
                    "temperature_max": 36.5
                },
                {
                    "dn": "sys/chassis-2/blade-3/board/cpu-1/env-stats",
                    "time_collected": "2022-12-08T22:32:54.869",
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
                    "time_collected": "2022-12-08T22:32:54.869",
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
                    "time_collected": "2022-12-08T22:32:54.869",
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
                    "time_collected": "2022-12-08T22:32:54.869",
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
                    "time_collected": "2022-12-08T22:32:54.869",
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
                    "time_collected": "2022-12-08T22:32:54.869",
                    "chassis_rn": "chassis-2",
                    "blade_rn": "blade-3",
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
                    "dn": "sys/chassis-2/blade-3/board/memarray-1/mem-5/dimm-env-stats",
                    "time_collected": "2022-12-08T22:32:54.869",
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
# iserver get servers --group ucsm -c thermal

Developer output

{
    "duration": 19804,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 11485
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
        "success": 56,
        "failed": 0,
        "connect": 16,
        "disconnect": 0,
        "mo": 40,
        "connect_time": 22686,
        "disconnect_time": 0,
        "mo_time": 19155,
        "total_time": 41841
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

[2022-12-08 22:33:09.360815]	[computes_info.get]	Get servers settings: {
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
    "power": false,
    "thermal": true,
    "env": false
}
[2022-12-08 22:33:09.363046]	[computes_info.get]	Get servers match rules: {
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
[2022-12-08 22:33:14.425946]	[computes_info.get]	All 103 servers base information in 5048 ms
[2022-12-08 22:33:14.427930]	[computes_info.get]	Base filter 8 servers in 1 ms
[2022-12-08 22:33:21.951133]	[compute_info.get]	{
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
[2022-12-08 22:33:22.050191]	[compute_info.get]	{
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
[2022-12-08 22:33:22.140669]	[compute_info.get]	{
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
[2022-12-08 22:33:22.214976]	[compute_info.get]	{
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
[2022-12-08 22:33:22.261479]	[compute_info.get]	{
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
[2022-12-08 22:33:22.368695]	[compute_info.get]	{
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
[2022-12-08 22:33:22.458648]	[compute_info.get]	{
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
[2022-12-08 22:33:22.750438]	[compute_info.get]	{
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
[2022-12-08 22:33:26.368843]	[computes_info.get_server_info]	Thread result: 6335c26e76752d3139b9694c
[2022-12-08 22:33:26.694560]	[computes_info.get_server_info]	Thread result: 6335c45976752d3139b9bf94
[2022-12-08 22:33:26.996228]	[computes_info.get_server_info]	Thread result: 6335e1f376752d3139bf12b8
[2022-12-08 22:33:27.425859]	[computes_info.get_server_info]	Thread result: 6337014c76752d3139f2f459
[2022-12-08 22:33:27.741733]	[computes_info.get_server_info]	Thread result: 6337063276752d3139f3cc83
[2022-12-08 22:33:28.068138]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da74
[2022-12-08 22:33:28.320012]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da78
[2022-12-08 22:33:28.641850]	[computes_info.get_server_info]	Thread result: 63371c9176752d3139f7da82
[2022-12-08 22:33:28.976438]	[computes_info.get]	Selected 8 servers with requested details in 14547 ms
[2022-12-08 22:33:28.978941]	[computes_info.get]	Total time 19616 ms


Log: isctl
-----------

2022-12-08 22:33:12.800416	True	3352	93	isctl get compute rackunit   -o json --top 100
2022-12-08 22:33:14.423908	True	1609	10	isctl get compute blade   -o json --top 100
2022-12-08 22:33:18.819583	True	2365	1	isctl get asset deviceregistration --filter "Moid in ('618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1')"  -o json --top 100
2022-12-08 22:33:19.118875	True	1929	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-08 22:33:19.438024	True	2230	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-07T22:33:17.000Z"  -o json --top 100


Log: ucsm
----------

2022-12-08 22:33:23.557750	True	1600	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:23.890055	True	1834	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:24.016268	True	457	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:24.199583	True	2053	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:24.343526	True	452	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:24.521959	True	503	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:24.554180	True	2333	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:24.656315	True	455	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:24.854897	True	509	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:24.859198	True	2591	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:24.958164	True	435	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:33:25.078145	True	523	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:25.164430	True	506	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:25.194207	True	2821	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:25.284574	True	428	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:33:25.344937	True	483	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:25.401883	True	442	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:33:25.516503	True	3052	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:25.583892	True	418	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:33:25.593864	True	513	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:25.669188	True	473	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:25.721983	True	436	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:33:25.828470	True	3074	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:25.851117	True	506	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:25.949691	True	546	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:33:25.971980	True	454	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:26.013608	True	429	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:33:26.030453	True	435	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:33:26.165638	True	495	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:26.261522	True	538	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:33:26.285412	True	433	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:33:26.296383	True	466	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 22:33:26.366037	True	406	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:26.445865	True	472	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:26.461702	True	429	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:33:26.565780	True	550	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:33:26.661467	True	494	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:33:26.692512	True	416	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:26.749098	True	463	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:33:26.819899	True	521	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 22:33:26.870237	True	422	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:33:26.993888	True	418	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:27.003211	True	541	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:33:27.101979	True	438	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:33:27.249795	True	428	vip-ucsb1.emea-sp.cisco.com:ComputeMbTempStats
2022-12-08 22:33:27.286072	True	535	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:33:27.306058	True	435	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:33:27.422545	True	410	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:27.635030	True	532	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:33:27.693350	True	442	vip-ucsb1.emea-sp.cisco.com:ProcessorEnvStats
2022-12-08 22:33:27.739736	True	440	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:27.894636	True	586	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:33:28.065538	True	421	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:28.226712	True	532	vip-ucsb1.emea-sp.cisco.com:MemoryUnitEnvStats
2022-12-08 22:33:28.317020	True	413	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-08 22:33:28.639895	True	404	disconnect vip-ucsb1.emea-sp.cisco.com
```
