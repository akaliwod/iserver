# Get Intersight Server with Environmental Information

Environmental = Power + Thermal

```
# iserver get server --ip 10.58.52.36 --env

+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+
| SF   | MF | WF | Name                 | Model            | Serial      | IP          | CPU        | Memory    |
+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+
| P+ H | CU |    | FI-ucsb1-eu-spdc-1-4 | (B) UCSB-B200-M4 | FCH205371UU | 10.58.52.36 | 2S 24C 48T | 256 [GiB] | 
+------+----+----+----------------------+------------------+-------------+-------------+------------+-----------+

+--------------------+-------+-------+-------+-------+
| Power Statistics   | Value | Min   | Avg   | Max   |
+--------------------+-------+-------+-------+-------+
| Consumed Power (W) | 126.0 | 126.0 | 126.0 | 126.0 | 
| Input Current (A)  | 10.52 | 10.52 | 10.52 | 10.52 | 
| Input Voltage (V)  | 11.98 | 11.98 | 11.98 | 11.98 | 
+--------------------+-------+-------+-------+-------+

+--------------------+-------+------+-------+------+
| Thermal Statistics | Value | Min  | Avg   | Max  |
+--------------------+-------+------+-------+------+
| Motherboard Front  | 25.0  | 25.0 | 25.0  | 25.0 | 
| Motherboard Rear   | 36.0  | 36.0 | 36.0  | 36.0 | 
| CPU-1              | 39.0  | 39.0 | 39.0  | 39.0 | 
| CPU-2              | 41.5  | 41.5 | 41.5  | 41.5 | 
| MEM-1              | 28.0  | 28.0 | 28.0  | 28.0 | 
| MEM-10             | 29.0  | 28.0 | 28.73 | 29.0 | 
| MEM-13             | 29.0  | 29.0 | 29.0  | 29.0 | 
| MEM-16             | 31.0  | 31.0 | 31.0  | 31.0 | 
| MEM-19             | 28.0  | 27.0 | 27.4  | 28.0 | 
| MEM-22             | 30.0  | 30.0 | 30.0  | 30.0 | 
| MEM-4              | 27.0  | 27.0 | 27.0  | 27.0 | 
| MEM-7              | 30.0  | 30.0 | 30.0  | 30.0 | 
+--------------------+-------+------+-------+------+
```

JSON Output

```
# iserver get server --ip 10.58.52.36 --env

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
            "time_collected": "2022-12-08T23:26:42.856",
            "chassis_rn": "chassis-1",
            "blade_rn": "blade-4",
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
                "dn": "sys/chassis-1/blade-4/board/temp-stats",
                "time_collected": "2022-12-08T23:26:42.856",
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
                "time_collected": "2022-12-08T23:26:42.856",
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
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "cpu_rn": "cpu-1",
                "name": "CPU-1",
                "type": "cpu",
                "temperature": 39.0,
                "temperature_avg": 39.0,
                "temperature_min": 39.0,
                "temperature_max": 39.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/cpu-2/env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "cpu_rn": "cpu-2",
                "name": "CPU-2",
                "type": "cpu",
                "temperature": 41.5,
                "temperature_avg": 41.5,
                "temperature_min": 41.5,
                "temperature_max": 41.5
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-1/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
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
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-10",
                "name": "MEM-10",
                "type": "memory",
                "temperature": 29.0,
                "temperature_avg": 28.73,
                "temperature_min": 28.0,
                "temperature_max": 29.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-13/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
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
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-16/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-16",
                "name": "MEM-16",
                "type": "memory",
                "temperature": 31.0,
                "temperature_avg": 31.0,
                "temperature_min": 31.0,
                "temperature_max": 31.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-19/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-19",
                "name": "MEM-19",
                "type": "memory",
                "temperature": 28.0,
                "temperature_avg": 27.4,
                "temperature_min": 27.0,
                "temperature_max": 28.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-22/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "array_rn": "memarray-1",
                "dimm_rn": "mem-22",
                "name": "MEM-22",
                "type": "memory",
                "temperature": 30.0,
                "temperature_avg": 30.0,
                "temperature_min": 30.0,
                "temperature_max": 30.0
            },
            {
                "dn": "sys/chassis-1/blade-4/board/memarray-1/mem-4/dimm-env-stats",
                "time_collected": "2022-12-08T23:26:42.856",
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
                "time_collected": "2022-12-08T23:26:42.856",
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
}
```