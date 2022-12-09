# Filter by management (CIMC) IP address

Use --ip option to select servers by IP address or IP subnet.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

## IP Address

```
# iserver get servers --ip 10.58.50.41

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
```

## IP Subnet

```
# iserver get servers --ip 10.58.50.0/24

+---------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H    | CRi |    | aio3-p5g-eu-spdc-WZP23450C8K   | (R) UCSC-C240-M5SX | WZP23450C8K | 10.58.50.51 | 2S 48C 96T | 384 [GiB] | 
| P+ H    | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] | 
| P- H    | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 2S 40C 80T | 384 [GiB] | 
| P- H    | CRi |    | comp1-p3b-eu-spdc-FCH2017V1J7  | (R) UCSC-C240-M4SX | FCH2017V1J7 | 10.58.50.48 | 2S 16C 32T | 128 [GiB] | 
| P- H    | Cri |    | comp2-p3b-eu-spdc-FCH2017V1J8  | (R) UCSC-C240-M4SX | FCH2017V1J8 | 10.58.50.49 | 2S 16C 32T | 128 [GiB] | 
| P- H    | Cri |    | comp3-p3b-eu-spdc-FCH2017V1J5  | (R) UCSC-C240-M4SX | FCH2017V1J5 | 10.58.50.50 | 2S 16C 32T | 128 [GiB] | 
| P- H    | Cri |    | comp4-p3b-eu-spdc-FCH2108V1FC  | (R) UCSC-C220-M4S  | FCH2108V1FC | 10.58.50.57 | 2S 28C 56T | 256 [GiB] | 
| P- H    | Cri |    | comp5-p3b-eu-spdc-FCH2017V1Y6  | (R) UCSC-C220-M4S  | FCH2017V1Y6 | 10.58.50.58 | 2S 28C 56T | 256 [GiB] | 
| P- H    | CRi |    | comp6-p3b-eu-spdc-FCH2017V24J  | (R) UCSC-C220-M4S  | FCH2017V24J | 10.58.50.59 | 2S 28C 56T | 256 [GiB] | 
| P+ C(1) | CRi |    | comp7-p3b-eu-spdc-FCH2023V2A4  | (R) UCSC-C220-M4S  | FCH2023V2A4 | 10.58.50.60 | 2S 28C 56T | 256 [GiB] | 
| P+ H    | CRi |    | esx20-eu-spdc-WMP24040053      | (R) UCSC-C220-M5SX | WMP24040053 | 10.58.50.40 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | esx21-eu-spdc-WZP23440N1P      | (R) UCSC-C220-M5SX | WZP23440N1P | 10.58.50.38 | 2S 48C 96T | 512 [GiB] | 
| P- H    | CRi |    | esx22-eu-spdc-WZP2343171Y      | (R) UCSC-C220-M5SX | WZP2343171Y | 10.58.50.39 | 2S 48C 96T | 512 [GiB] | 
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
```
