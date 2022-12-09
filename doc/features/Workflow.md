# Workflow

Get workflow's detail selected by Moid in table, json or yaml formats.

```
# iserver get workflow --help

Usage: iserver.py get workflow [OPTIONS] WORKFLOW_ID

  Get workflow

Options:
  --iaccount TEXT                 Intersight account  [default: isctl]
  -o, --output [default|json|yaml]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.
```

Default output

```
# iserver get workflow 638fe4e7696f6e2d308cdd5b

Get server workflow info...

Server
- Name: comp-4-p2b-eu-spdc-WMP240400FM
- Model: UCSC-C220-M5SX
- Serial: WMP240400FM
- IP: 10.58.50.44


Workflow
- Workflow ID: 638fe4e7696f6e2d308cdd5b
- Name: Power On
- Status: COMPLETED
- Create Time: 2022-12-07T00:57:11.666Z
- Start Time: 2022-12-07T00:57:11.811Z
- End Time: 2022-12-07T00:57:16.472Z
- Duration: 00:00:05


+--------------------------+---------------------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| Task Moid                | Description                                       | Create Time              | Status    | Duration | Details                                                                      |
+--------------------------+---------------------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
| 638fe4e7696f6e2d308cdd6b | workflow.StartWorkflowTask                        | 2022-12-07T00:57:11.922Z | COMPLETED | 00:00:00 |                                                                              | 
| 638fe4e8696f6e2d308cdd75 | Validate the platform type                        | 2022-12-07T00:57:12.01Z  | COMPLETED | 00:00:00 | Physical Summary for Server Moid 5fdfa1806176752d35e678c2 found successfully | 
| 638fe4e9696f6e2d308cdda7 | Invoke tasks based on the platform type           | 2022-12-07T00:57:13.061Z | COMPLETED | 00:00:00 | The task evaluated to case IMCM5                                             | 
| 638fe4e9696f6e2d308cddb9 | Check and Execute Set One Time Boot Configuration | 2022-12-07T00:57:13.279Z | COMPLETED | 00:00:00 | The task evaluated to case false                                             | 
| 638fe4e9696f6e2d308cddcb | Invoke Server Power On                            | 2022-12-07T00:57:13.492Z | COMPLETED | 00:00:02 | Server power on is initiated                                                 | 
| 638fe4eb696f6e2d308cddd7 | Invoke the Server Power On                        | 2022-12-07T00:57:15.603Z | NO_OP     | 00:00:00 |                                                                              | 
| 638fe4ec696f6e2d308cdde1 | Update Server Inventory                           | 2022-12-07T00:57:16.03Z  | COMPLETED | 00:00:00 | State synchronized.                                                          | 
| 638fe4ec696f6e2d308cddeb | workflow.SuccessEndWorkflowTask                   | 2022-12-07T00:57:16.391Z | COMPLETED | 00:00:00 |                                                                              | 
+--------------------------+---------------------------------------------------+--------------------------+-----------+----------+------------------------------------------------------------------------------+
```

JSON output

```
# iserver get workflow 638fe4e7696f6e2d308cdd5b -o json

{
    "workflow": {
        "Moid": "638fe4e7696f6e2d308cdd5b",
        "Name": "Power On",
        "Progress": 100,
        "CreateTime": "2022-12-07T00:57:11.666Z",
        "StartTime": "2022-12-07T00:57:11.811Z",
        "EndTime": "2022-12-07T00:57:16.472Z",
        "Status": "COMPLETED",
        "Type": "UserDefined",
        "CreateTimeEpoch": 1670371031666,
        "StartTimeEpoch": 1670371031811,
        "EndTimeEpoch": 1670371036472,
        "Running": false,
        "Completed": true,
        "Duration": "00:00:05"
    },
    "tasks": [
        {
            "Moid": "638fe4e7696f6e2d308cdd6b",
            "Name": "workflow.StartWorkflowTask",
            "Label": "",
            "CreateTime": "2022-12-07T00:57:11.922Z",
            "StartTime": "2022-12-07T00:57:11.913Z",
            "EndTime": "2022-12-07T00:57:11.924Z",
            "Status": "COMPLETED",
            "FailureReason": "",
            "Description": "workflow.StartWorkflowTask",
            "CreateTimeEpoch": 1670371031922,
            "StartTimeEpoch": 1670371031913,
            "EndTimeEpoch": 1670371031924,
            "Duration": "00:00:00"
        },
        {
            "Moid": "638fe4e8696f6e2d308cdd75",
            "Name": "GetServerPlatformType",
            "Label": "Validate the platform type",
            "CreateTime": "2022-12-07T00:57:12.01Z",
            "StartTime": "2022-12-07T00:57:12.003Z",
            "EndTime": "2022-12-07T00:57:12.926Z",
            "Status": "COMPLETED",
            "FailureReason": "Physical Summary for Server Moid 5fdfa1806176752d35e678c2 found successfully",
            "Description": "Validate the platform type",
            "CreateTimeEpoch": 1670371032010,
            "StartTimeEpoch": 1670371032003,
            "EndTimeEpoch": 1670371032926,
            "Duration": "00:00:00"
        },
        {
            "Moid": "638fe4e9696f6e2d308cdda7",
            "Name": "workflow.DecisionWorkflowTask",
            "Label": "Invoke tasks based on the platform type",
            "CreateTime": "2022-12-07T00:57:13.061Z",
            "StartTime": "2022-12-07T00:57:13.054Z",
            "EndTime": "2022-12-07T00:57:13.161Z",
            "Status": "COMPLETED",
            "FailureReason": "The task evaluated to case IMCM5",
            "Description": "Invoke tasks based on the platform type",
            "CreateTimeEpoch": 1670371033061,
            "StartTimeEpoch": 1670371033054,
            "EndTimeEpoch": 1670371033161,
            "Duration": "00:00:00"
        },
        {
            "Moid": "638fe4e9696f6e2d308cddb9",
            "Name": "workflow.DecisionWorkflowTask",
            "Label": "Check and Execute Set One Time Boot Configuration",
            "CreateTime": "2022-12-07T00:57:13.279Z",
            "StartTime": "2022-12-07T00:57:13.269Z",
            "EndTime": "2022-12-07T00:57:13.393Z",
            "Status": "COMPLETED",
            "FailureReason": "The task evaluated to case false",
            "Description": "Check and Execute Set One Time Boot Configuration",
            "CreateTimeEpoch": 1670371033279,
            "StartTimeEpoch": 1670371033269,
            "EndTimeEpoch": 1670371033393,
            "Duration": "00:00:00"
        },
        {
            "Moid": "638fe4e9696f6e2d308cddcb",
            "Name": "compute.ServerOperationTask",
            "Label": "Invoke Server Power On",
            "CreateTime": "2022-12-07T00:57:13.492Z",
            "StartTime": "2022-12-07T00:57:13.482Z",
            "EndTime": "2022-12-07T00:57:15.459Z",
            "Status": "COMPLETED",
            "FailureReason": "Server power on is initiated",
            "Description": "Invoke Server Power On",
            "CreateTimeEpoch": 1670371033492,
            "StartTimeEpoch": 1670371033482,
            "EndTimeEpoch": 1670371035459,
            "Duration": "00:00:02"
        },
        {
            "Moid": "638fe4eb696f6e2d308cddd7",
            "Name": "compute.ServerRedfishOperationTask",
            "Label": "Invoke the Server Power On",
            "CreateTime": "2022-12-07T00:57:15.603Z",
            "StartTime": "2022-12-07T00:57:15.593Z",
            "EndTime": "2022-12-07T00:57:15.918Z",
            "Status": "NO_OP",
            "FailureReason": "",
            "Description": "Invoke the Server Power On",
            "CreateTimeEpoch": 1670371035603,
            "StartTimeEpoch": 1670371035593,
            "EndTimeEpoch": 1670371035918,
            "Duration": "00:00:00"
        },
        {
            "Moid": "638fe4ec696f6e2d308cdde1",
            "Name": "UpdateServerInventoryTask",
            "Label": "Update Server Inventory",
            "CreateTime": "2022-12-07T00:57:16.03Z",
            "StartTime": "2022-12-07T00:57:16.018Z",
            "EndTime": "2022-12-07T00:57:16.275Z",
            "Status": "COMPLETED",
            "FailureReason": "State synchronized.",
            "Description": "Update Server Inventory",
            "CreateTimeEpoch": 1670371036030,
            "StartTimeEpoch": 1670371036018,
            "EndTimeEpoch": 1670371036275,
            "Duration": "00:00:00"
        },
        {
            "Moid": "638fe4ec696f6e2d308cddeb",
            "Name": "workflow.SuccessEndWorkflowTask",
            "Label": "",
            "CreateTime": "2022-12-07T00:57:16.391Z",
            "StartTime": "2022-12-07T00:57:16.382Z",
            "EndTime": "2022-12-07T00:57:16.395Z",
            "Status": "COMPLETED",
            "FailureReason": "",
            "Description": "workflow.SuccessEndWorkflowTask",
            "CreateTimeEpoch": 1670371036391,
            "StartTimeEpoch": 1670371036382,
            "EndTimeEpoch": 1670371036395,
            "Duration": "00:00:00"
        }
    ],
    "server": {
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
        "Connected": false,
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
        "Type": "Rack",
        "TypeModel": "(R) UCSC-C220-M5SX",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "cRi",
        "FlagWorkflow": ""
    }
}
```

YAML output

```
# iserver get workflow 638fe4e7696f6e2d308cdd5b -o yaml

server:
  AlarmSummary:
    Critical: 0
    Info: 0
    Warning: 0
  AvailableMemory: 393216
  AvailableMemoryGB: 384
  AvailableMemoryUnit: 384 [GiB]
  Connected: false
  Cpu: 2S 40C 80T
  DeviceMoId: 5fdfa1686f72612d300b383f
  FlagManagement: cRi
  FlagState: P+ H
  FlagWorkflow: ''
  Groups: p2b,pod2b,test,self-test-power,power
  Health: Healthy
  IMC:
    Capable: true
    Enabled: false
  LocatorLedOn: false
  ManagementIp: 10.58.50.44
  ManagementMode: IntersightStandalone
  Model: UCSC-C220-M5SX
  Moid: 5fdfa1806176752d35e678c2
  Name: comp-4-p2b-eu-spdc-WMP240400FM
  NumCpuCores: 40
  NumCpus: 2
  NumThreads: 80
  OperPowerState: 'on'
  Redfish:
    Capable: true
    Enabled: true
  Serial: WMP240400FM
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  Type: Rack
  TypeModel: (R) UCSC-C220-M5SX
  UCSM:
    Capable: false
    Enabled: false
  UsedMemory: 0
  UsedMemoryGB: 0
  UsedMemoryPct: 0
  UsedMemoryPctUnit: 0%
  UsedMemoryUnit: 0 [KiB]
tasks:
- CreateTime: '2022-12-07T00:57:11.922Z'
  CreateTimeEpoch: 1670371031922
  Description: workflow.StartWorkflowTask
  Duration: 00:00:00
  EndTime: '2022-12-07T00:57:11.924Z'
  EndTimeEpoch: 1670371031924
  FailureReason: ''
  Label: ''
  Moid: 638fe4e7696f6e2d308cdd6b
  Name: workflow.StartWorkflowTask
  StartTime: '2022-12-07T00:57:11.913Z'
  StartTimeEpoch: 1670371031913
  Status: COMPLETED
- CreateTime: '2022-12-07T00:57:12.01Z'
  CreateTimeEpoch: 1670371032010
  Description: Validate the platform type
  Duration: 00:00:00
  EndTime: '2022-12-07T00:57:12.926Z'
  EndTimeEpoch: 1670371032926
  FailureReason: Physical Summary for Server Moid 5fdfa1806176752d35e678c2 found successfully
  Label: Validate the platform type
  Moid: 638fe4e8696f6e2d308cdd75
  Name: GetServerPlatformType
  StartTime: '2022-12-07T00:57:12.003Z'
  StartTimeEpoch: 1670371032003
  Status: COMPLETED
- CreateTime: '2022-12-07T00:57:13.061Z'
  CreateTimeEpoch: 1670371033061
  Description: Invoke tasks based on the platform type
  Duration: 00:00:00
  EndTime: '2022-12-07T00:57:13.161Z'
  EndTimeEpoch: 1670371033161
  FailureReason: The task evaluated to case IMCM5
  Label: Invoke tasks based on the platform type
  Moid: 638fe4e9696f6e2d308cdda7
  Name: workflow.DecisionWorkflowTask
  StartTime: '2022-12-07T00:57:13.054Z'
  StartTimeEpoch: 1670371033054
  Status: COMPLETED
- CreateTime: '2022-12-07T00:57:13.279Z'
  CreateTimeEpoch: 1670371033279
  Description: Check and Execute Set One Time Boot Configuration
  Duration: 00:00:00
  EndTime: '2022-12-07T00:57:13.393Z'
  EndTimeEpoch: 1670371033393
  FailureReason: The task evaluated to case false
  Label: Check and Execute Set One Time Boot Configuration
  Moid: 638fe4e9696f6e2d308cddb9
  Name: workflow.DecisionWorkflowTask
  StartTime: '2022-12-07T00:57:13.269Z'
  StartTimeEpoch: 1670371033269
  Status: COMPLETED
- CreateTime: '2022-12-07T00:57:13.492Z'
  CreateTimeEpoch: 1670371033492
  Description: Invoke Server Power On
  Duration: 00:00:02
  EndTime: '2022-12-07T00:57:15.459Z'
  EndTimeEpoch: 1670371035459
  FailureReason: Server power on is initiated
  Label: Invoke Server Power On
  Moid: 638fe4e9696f6e2d308cddcb
  Name: compute.ServerOperationTask
  StartTime: '2022-12-07T00:57:13.482Z'
  StartTimeEpoch: 1670371033482
  Status: COMPLETED
- CreateTime: '2022-12-07T00:57:15.603Z'
  CreateTimeEpoch: 1670371035603
  Description: Invoke the Server Power On
  Duration: 00:00:00
  EndTime: '2022-12-07T00:57:15.918Z'
  EndTimeEpoch: 1670371035918
  FailureReason: ''
  Label: Invoke the Server Power On
  Moid: 638fe4eb696f6e2d308cddd7
  Name: compute.ServerRedfishOperationTask
  StartTime: '2022-12-07T00:57:15.593Z'
  StartTimeEpoch: 1670371035593
  Status: NO_OP
- CreateTime: '2022-12-07T00:57:16.03Z'
  CreateTimeEpoch: 1670371036030
  Description: Update Server Inventory
  Duration: 00:00:00
  EndTime: '2022-12-07T00:57:16.275Z'
  EndTimeEpoch: 1670371036275
  FailureReason: State synchronized.
  Label: Update Server Inventory
  Moid: 638fe4ec696f6e2d308cdde1
  Name: UpdateServerInventoryTask
  StartTime: '2022-12-07T00:57:16.018Z'
  StartTimeEpoch: 1670371036018
  Status: COMPLETED
- CreateTime: '2022-12-07T00:57:16.391Z'
  CreateTimeEpoch: 1670371036391
  Description: workflow.SuccessEndWorkflowTask
  Duration: 00:00:00
  EndTime: '2022-12-07T00:57:16.395Z'
  EndTimeEpoch: 1670371036395
  FailureReason: ''
  Label: ''
  Moid: 638fe4ec696f6e2d308cddeb
  Name: workflow.SuccessEndWorkflowTask
  StartTime: '2022-12-07T00:57:16.382Z'
  StartTimeEpoch: 1670371036382
  Status: COMPLETED
workflow:
  Completed: true
  CreateTime: '2022-12-07T00:57:11.666Z'
  CreateTimeEpoch: 1670371031666
  Duration: 00:00:05
  EndTime: '2022-12-07T00:57:16.472Z'
  EndTimeEpoch: 1670371036472
  Moid: 638fe4e7696f6e2d308cdd5b
  Name: Power On
  Progress: 100
  Running: false
  StartTime: '2022-12-07T00:57:11.811Z'
  StartTimeEpoch: 1670371031811
  Status: COMPLETED
  Type: UserDefined
```