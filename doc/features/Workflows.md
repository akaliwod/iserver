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
  --devel                         Developer output  [default: False]
  --help                          Show this message and exit.
```

## Example: failed workflows

```
# iserver get workflows
    --group p2b
    --failed
    --days 7
    --count 5
    --order workflow
Get servers info...
Get workflows info...

+-------------+---------------------------------+--------------+--------------+---------------------------+---------------------------+---------------------------+---------+
| Flags       | Name                            | IP           | Serial       | Workflow ID               | Name                      | Create Time               | Status  |
+-------------+---------------------------------+--------------+--------------+---------------------------+---------------------------+---------------------------+---------+
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 63458de8696f6e2d30f6fbe9  | InstallOS                 | 2022-10-11T15:38:16.158Z  | FAILED  | 
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 63455e03696f6e2d30f6763f  | InstallOS                 | 2022-10-11T12:13:55.583Z  | FAILED  | 
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 63458de5696f6e2d30f6fb89  | Operating System Install  | 2022-10-11T15:38:14.299Z  | FAILED  | 
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 6346855b696f6e2d30f910b2  | Power Cycle               | 2022-10-12T09:14:04.059Z  | FAILED  | 
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 63468551696f6e2d30f91032  | Power Cycle               | 2022-10-12T09:13:54.033Z  | FAILED  | 
+-------------+---------------------------------+--------------+--------------+---------------------------+---------------------------+---------------------------+---------+
```

## Example: power related in last 7 days

```
# iserver get workflows
    --group p2b
    --power
    --order workflow
    --days 7
    --count 5
Get servers info...
Get workflows info...

+-------------+---------------------------------+--------------+--------------+---------------------------+---------------+---------------------------+------------+
| Flags       | Name                            | IP           | Serial       | Workflow ID               | Name          | Create Time               | Status     |
+-------------+---------------------------------+--------------+--------------+---------------------------+---------------+---------------------------+------------+
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 6346855b696f6e2d30f910b2  | Power Cycle   | 2022-10-12T09:14:04.059Z  | FAILED     | 
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 63468551696f6e2d30f91032  | Power Cycle   | 2022-10-12T09:13:54.033Z  | FAILED     | 
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 63467c36696f6e2d30f8fb26  | Power Cycle   | 2022-10-12T08:35:02.176Z  | COMPLETED  | 
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 63467478696f6e2d30f8e329  | Power Cycle   | 2022-10-12T08:02:00.754Z  | COMPLETED  | 
| P-HRS WR90  | comp-3-p2b-eu-spdc-WMP24040059  | 10.58.50.46  | WMP24040059  | 634665ed696f6e2d30f8c99f  | Power Cycle   | 2022-10-12T06:59:57.992Z  | COMPLETED  | 
| P+HRS W16   | comp-1-p2b-eu-spdc-WMP240400FM  | 10.58.50.44  | WMP240400FM  | 63454434696f6e2d30f64065  | Power Cycle   | 2022-10-11T10:23:48.899Z  | COMPLETED  | 
| P-HRS W12   | aio-1-p2b-eu-spdc-WZP23400AJW   | 10.58.50.41  | WZP23400AJW  | 634519f0696f6e2d30f58f35  | Power Off     | 2022-10-11T07:23:28.867Z  | COMPLETED  | 
| P-HRS W12   | aio-1-p2b-eu-spdc-WZP23400AJW   | 10.58.50.41  | WZP23400AJW  | 63451717696f6e2d30f57cda  | Power Off     | 2022-10-11T07:11:19.406Z  | COMPLETED  | 
| P-HRS W12   | aio-1-p2b-eu-spdc-WZP23400AJW   | 10.58.50.41  | WZP23400AJW  | 634516e2696f6e2d30f57b74  | Power Off     | 2022-10-11T07:10:26.987Z  | COMPLETED  | 
| P-HRS W12   | aio-1-p2b-eu-spdc-WZP23400AJW   | 10.58.50.41  | WZP23400AJW  | 6345161a696f6e2d30f57630  | Power Off     | 2022-10-11T07:07:06.448Z  | COMPLETED  | 
| P-HRS W12   | aio-1-p2b-eu-spdc-WZP23400AJW   | 10.58.50.41  | WZP23400AJW  | 634515d1696f6e2d30f57505  | Power Off     | 2022-10-11T07:05:54.313Z  | COMPLETED  | 
| P+HRS W16   | comp-1-p2b-eu-spdc-WMP240400FM  | 10.58.50.44  | WMP240400FM  | 6345453f696f6e2d30f64470  | Power On      | 2022-10-11T10:28:15.896Z  | COMPLETED  | 
| P+HRS W16   | comp-1-p2b-eu-spdc-WMP240400FM  | 10.58.50.44  | WMP240400FM  | 6345448b696f6e2d30f6421a  | Power On      | 2022-10-11T10:25:15.869Z  | COMPLETED  | 
| P+HRS W16   | comp-1-p2b-eu-spdc-WMP240400FM  | 10.58.50.44  | WMP240400FM  | 6345459b696f6e2d30f645ba  | Reboot IMC    | 2022-10-11T10:29:47.275Z  | COMPLETED  | 
| P+HRS W16   | comp-1-p2b-eu-spdc-WMP240400FM  | 10.58.50.44  | WMP240400FM  | 634544e2696f6e2d30f64341  | Shut Down OS  | 2022-10-11T10:26:42.629Z  | COMPLETED  | 
+-------------+---------------------------------+--------------+--------------+---------------------------+---------------+---------------------------+------------+
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
        "server_id": "5fdfe47f6176752d35001995",
        "server_state": "P-HRS WR90",
        "server_name": "comp-3-p2b-eu-spdc-WMP24040059",
        "server_ip": "10.58.50.46",
        "server_serial": "WMP24040059",
        "workflow_id": "6346855b696f6e2d30f910b2",
        "name": "Power Cycle",
        "created": "2022-10-12T09:14:04.059Z",
        "created_epoch": 1665558844059,
        "status": "FAILED"
    },
    {
        "server_id": "5fdfe47f6176752d35001995",
        "server_state": "P-HRS WR90",
        "server_name": "comp-3-p2b-eu-spdc-WMP24040059",
        "server_ip": "10.58.50.46",
        "server_serial": "WMP24040059",
        "workflow_id": "63468551696f6e2d30f91032",
        "name": "Power Cycle",
        "created": "2022-10-12T09:13:54.033Z",
        "created_epoch": 1665558834033,
        "status": "FAILED"
    },
    {
        "server_id": "5fdfe47f6176752d35001995",
        "server_state": "P-HRS WR90",
        "server_name": "comp-3-p2b-eu-spdc-WMP24040059",
        "server_ip": "10.58.50.46",
        "server_serial": "WMP24040059",
        "workflow_id": "63467c36696f6e2d30f8fb26",
        "name": "Power Cycle",
        "created": "2022-10-12T08:35:02.176Z",
        "created_epoch": 1665556502176,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfe47f6176752d35001995",
        "server_state": "P-HRS WR90",
        "server_name": "comp-3-p2b-eu-spdc-WMP24040059",
        "server_ip": "10.58.50.46",
        "server_serial": "WMP24040059",
        "workflow_id": "63467478696f6e2d30f8e329",
        "name": "Power Cycle",
        "created": "2022-10-12T08:02:00.754Z",
        "created_epoch": 1665554520754,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfe47f6176752d35001995",
        "server_state": "P-HRS WR90",
        "server_name": "comp-3-p2b-eu-spdc-WMP24040059",
        "server_ip": "10.58.50.46",
        "server_serial": "WMP24040059",
        "workflow_id": "634665ed696f6e2d30f8c99f",
        "name": "Power Cycle",
        "created": "2022-10-12T06:59:57.992Z",
        "created_epoch": 1665550797992,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfa1806176752d35e678c2",
        "server_state": "P+HRS W16",
        "server_name": "comp-1-p2b-eu-spdc-WMP240400FM",
        "server_ip": "10.58.50.44",
        "server_serial": "WMP240400FM",
        "workflow_id": "63454434696f6e2d30f64065",
        "name": "Power Cycle",
        "created": "2022-10-11T10:23:48.899Z",
        "created_epoch": 1665476628899,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdf9c016176752d35e44795",
        "server_state": "P-HRS W12",
        "server_name": "aio-1-p2b-eu-spdc-WZP23400AJW",
        "server_ip": "10.58.50.41",
        "server_serial": "WZP23400AJW",
        "workflow_id": "634519f0696f6e2d30f58f35",
        "name": "Power Off",
        "created": "2022-10-11T07:23:28.867Z",
        "created_epoch": 1665465808867,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdf9c016176752d35e44795",
        "server_state": "P-HRS W12",
        "server_name": "aio-1-p2b-eu-spdc-WZP23400AJW",
        "server_ip": "10.58.50.41",
        "server_serial": "WZP23400AJW",
        "workflow_id": "63451717696f6e2d30f57cda",
        "name": "Power Off",
        "created": "2022-10-11T07:11:19.406Z",
        "created_epoch": 1665465079406,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdf9c016176752d35e44795",
        "server_state": "P-HRS W12",
        "server_name": "aio-1-p2b-eu-spdc-WZP23400AJW",
        "server_ip": "10.58.50.41",
        "server_serial": "WZP23400AJW",
        "workflow_id": "634516e2696f6e2d30f57b74",
        "name": "Power Off",
        "created": "2022-10-11T07:10:26.987Z",
        "created_epoch": 1665465026987,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdf9c016176752d35e44795",
        "server_state": "P-HRS W12",
        "server_name": "aio-1-p2b-eu-spdc-WZP23400AJW",
        "server_ip": "10.58.50.41",
        "server_serial": "WZP23400AJW",
        "workflow_id": "6345161a696f6e2d30f57630",
        "name": "Power Off",
        "created": "2022-10-11T07:07:06.448Z",
        "created_epoch": 1665464826448,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdf9c016176752d35e44795",
        "server_state": "P-HRS W12",
        "server_name": "aio-1-p2b-eu-spdc-WZP23400AJW",
        "server_ip": "10.58.50.41",
        "server_serial": "WZP23400AJW",
        "workflow_id": "634515d1696f6e2d30f57505",
        "name": "Power Off",
        "created": "2022-10-11T07:05:54.313Z",
        "created_epoch": 1665464754313,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfa1806176752d35e678c2",
        "server_state": "P+HRS W16",
        "server_name": "comp-1-p2b-eu-spdc-WMP240400FM",
        "server_ip": "10.58.50.44",
        "server_serial": "WMP240400FM",
        "workflow_id": "6345453f696f6e2d30f64470",
        "name": "Power On",
        "created": "2022-10-11T10:28:15.896Z",
        "created_epoch": 1665476895896,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfa1806176752d35e678c2",
        "server_state": "P+HRS W16",
        "server_name": "comp-1-p2b-eu-spdc-WMP240400FM",
        "server_ip": "10.58.50.44",
        "server_serial": "WMP240400FM",
        "workflow_id": "6345448b696f6e2d30f6421a",
        "name": "Power On",
        "created": "2022-10-11T10:25:15.869Z",
        "created_epoch": 1665476715869,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfa1806176752d35e678c2",
        "server_state": "P+HRS W16",
        "server_name": "comp-1-p2b-eu-spdc-WMP240400FM",
        "server_ip": "10.58.50.44",
        "server_serial": "WMP240400FM",
        "workflow_id": "6345459b696f6e2d30f645ba",
        "name": "Reboot IMC",
        "created": "2022-10-11T10:29:47.275Z",
        "created_epoch": 1665476987275,
        "status": "COMPLETED"
    },
    {
        "server_id": "5fdfa1806176752d35e678c2",
        "server_state": "P+HRS W16",
        "server_name": "comp-1-p2b-eu-spdc-WMP240400FM",
        "server_ip": "10.58.50.44",
        "server_serial": "WMP240400FM",
        "workflow_id": "634544e2696f6e2d30f64341",
        "name": "Shut Down OS",
        "created": "2022-10-11T10:26:42.629Z",
        "created_epoch": 1665476802629,
        "status": "COMPLETED"
    }
]
```
