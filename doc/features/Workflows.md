# Workflows

Get selected workflows' information in table, json or yaml formats.

Use command options for workflows' filtering.

```
# iserver get workflows --help

Usage: iserver.py get workflows [OPTIONS]

  Get workflows

Options:
  --iaccount TEXT                 Intersight account  [default: isctl]
  --group TEXT                    Group name
  --type [all|blade|rack]         [default: rack]
  --ip TEXT                       Management IP address or subnet filter
  --name TEXT                     Name loose match filter
  --model TEXT                    Model loose match filter
  --serial TEXT                   Serial strict match filter
  --failed                        Filter failed
  --completed                     Filter completed
  --power                         Filter power related
  --os                            Filter OS related
  --fw                            Filter firmware related
  --count INTEGER                 Last <n> count  [default: -1]
  --days INTEGER                  Last <n> days
  --order [server|workflow|date]  [default: date]
  -o, --output [default|json|yaml]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.
```

## Example: failed workflows

```
# iserver get workflows --group p2b --failed --days 7 --count 5 --order workflow

Get servers info...
Get workflows info...

+-------+--------------------------------+-------------+-------------+--------------------------+--------------------------+--------------------------+--------+
| Flags | Name                           | IP          | Serial      | Workflow ID              | Name                     | Create Time              | Status |
+-------+--------------------------------+-------------+-------------+--------------------------+--------------------------+--------------------------+--------+
| P+ H  | comp-1-p2b-eu-spdc-WZP23400AJW | 10.58.50.41 | WZP23400AJW | 638f6ecb696f6e2d3089fd01 | InstallOS                | 2022-12-06T16:33:15.946Z | FAILED | 
| P+ H  | comp-5-p2b-eu-spdc-WMP2404000R | 10.58.50.45 | WMP2404000R | 638a26db696f6e2d307d3de1 | InstallOS                | 2022-12-02T16:24:59.767Z | FAILED | 
| P+ H  | comp-5-p2b-eu-spdc-WMP2404000R | 10.58.50.45 | WMP2404000R | 6389c7f0696f6e2d307adbc0 | InstallOS                | 2022-12-02T09:40:00.303Z | FAILED | 
| P+ H  | comp-5-p2b-eu-spdc-WMP2404000R | 10.58.50.45 | WMP2404000R | 6389bb76696f6e2d307aa2ea | InstallOS                | 2022-12-02T08:46:47.275Z | FAILED | 
| P+ H  | comp-1-p2b-eu-spdc-WZP23400AJW | 10.58.50.41 | WZP23400AJW | 638f6ec6696f6e2d3089fc3d | Operating System Install | 2022-12-06T16:33:11.184Z | FAILED | 
| P+ H  | comp-5-p2b-eu-spdc-WMP2404000R | 10.58.50.45 | WMP2404000R | 638a26da696f6e2d307d3d82 | Operating System Install | 2022-12-02T16:24:58.48Z  | FAILED | 
| P+ H  | comp-5-p2b-eu-spdc-WMP2404000R | 10.58.50.45 | WMP2404000R | 6389c7ee696f6e2d307adb61 | Operating System Install | 2022-12-02T09:39:58.444Z | FAILED | 
+-------+--------------------------------+-------------+-------------+--------------------------+--------------------------+--------------------------+--------+
```

## Example: power related in last 7 days

```
# iserver get workflows --group p2b --power --order workflow --days 7 --count 5

Get servers info...
Get workflows info...

+-------+--------------------------------+-------------+-------------+--------------------------+-------------+--------------------------+-----------+
| Flags | Name                           | IP          | Serial      | Workflow ID              | Name        | Create Time              | Status    |
+-------+--------------------------------+-------------+-------------+--------------------------+-------------+--------------------------+-----------+
| P+ H  | comp-5-p2b-eu-spdc-WMP2404000R | 10.58.50.45 | WMP2404000R | 638fe537696f6e2d308cde40 | Power Cycle | 2022-12-07T00:58:31.937Z | COMPLETED | 
| P+ H  | comp-7-p2b-eu-spdc-WMP24040061 | 10.58.50.47 | WMP24040061 | 638fe9af696f6e2d308cedc0 | Power On    | 2022-12-07T01:17:35.634Z | COMPLETED | 
| P+ H  | comp-2-p2b-eu-spdc-WZP23400AK4 | 10.58.50.42 | WZP23400AK4 | 638fe680696f6e2d308ce756 | Power On    | 2022-12-07T01:04:00.147Z | COMPLETED | 
| P+ H  | comp-6-p2b-eu-spdc-WMP24040059 | 10.58.50.46 | WMP24040059 | 638fe553696f6e2d308cdef5 | Power On    | 2022-12-07T00:58:59.531Z | COMPLETED | 
| P+ H  | comp-4-p2b-eu-spdc-WMP240400FM | 10.58.50.44 | WMP240400FM | 638fe4e7696f6e2d308cdd5b | Power On    | 2022-12-07T00:57:11.666Z | COMPLETED | 
+-------+--------------------------------+-------------+-------------+--------------------------+-------------+--------------------------+-----------+
```

## Example: JSON output

```
# iserver get workflows
    --group p2b
    --power
    --order workflow
    --days 7
    --count 5 -o json

[
    {
        "server_id": "5fdfdc3b6176752d35fce0a9",
        "server_state": "P+ H",
        "server_name": "comp-5-p2b-eu-spdc-WMP2404000R",
        "server_ip": "10.58.50.45",
        "server_serial": "WMP2404000R",
        "workflow_id": "638fe537696f6e2d308cde40",
        "name": "Power Cycle",
        "created": "2022-12-07T00:58:31.937Z",
        "created_epoch": 1670371111937,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfe80d6176752d3502b008",
        "server_state": "P+ H",
        "server_name": "comp-7-p2b-eu-spdc-WMP24040061",
        "server_ip": "10.58.50.47",
        "server_serial": "WMP24040061",
        "workflow_id": "638fe9af696f6e2d308cedc0",
        "name": "Power On",
        "created": "2022-12-07T01:17:35.634Z",
        "created_epoch": 1670372255634,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdf9c786176752d35e47110",
        "server_state": "P+ H",
        "server_name": "comp-2-p2b-eu-spdc-WZP23400AK4",
        "server_ip": "10.58.50.42",
        "server_serial": "WZP23400AK4",
        "workflow_id": "638fe680696f6e2d308ce756",
        "name": "Power On",
        "created": "2022-12-07T01:04:00.147Z",
        "created_epoch": 1670371440147,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfe47f6176752d35001995",
        "server_state": "P+ H",
        "server_name": "comp-6-p2b-eu-spdc-WMP24040059",
        "server_ip": "10.58.50.46",
        "server_serial": "WMP24040059",
        "workflow_id": "638fe553696f6e2d308cdef5",
        "name": "Power On",
        "created": "2022-12-07T00:58:59.531Z",
        "created_epoch": 1670371139531,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfa1806176752d35e678c2",
        "server_state": "P+ H",
        "server_name": "comp-4-p2b-eu-spdc-WMP240400FM",
        "server_ip": "10.58.50.44",
        "server_serial": "WMP240400FM",
        "workflow_id": "638fe4e7696f6e2d308cdd5b",
        "name": "Power On",
        "created": "2022-12-07T00:57:11.666Z",
        "created_epoch": 1670371031666,
        "status": "COMPLETED"
    }
]
```
