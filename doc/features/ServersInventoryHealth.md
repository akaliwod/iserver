# Filter by server's health

Use --health option to select servers with any warnings or critical alarms.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --health

+---------+-----+----+-------------------------------+--------------------+-------------+---------------+------------+-----------+
| SF      | MF  | WF | Name                          | Model              | Serial      | IP            | CPU        | Memory    |
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+------------+-----------+
| P+ C(1) | Cri |    | C220-231                      | (R) UCSC-C220-M5SX | WZP23240NNZ | 10.58.250.241 | 2S 40C 80T | 384 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-1          | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33   | 2S 24C 48T | 512 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-2          | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34   | 2S 24C 48T | 512 [GiB] | 
| P- C(2) | Cu  |    | HX1-eu-spdc-1                 | (R) HXAF220C-M5SN  | WZP24100SMV | 10.58.24.56   | 2S 40C 80T | 384 [GiB] | 
| P+ C(3) | Cu  |    | HX1-eu-spdc-4                 | (R) HXAF220C-M5SN  | WZP24100SMP | 10.58.24.57   | 2S 40C 80T | 384 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-2                 | (R) UCSC-C240-M4S  | FCH1930V0PH | 10.49.234.198 | 2S 24C 48T | 384 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-3                 | (R) UCSC-C220-M4S  | FCH2031V0YM | 10.49.234.196 | 2S 28C 56T | 672 [GiB] | 
| P- W(1) | Cu  |    | berlin-ucsm-4                 | (R) UCSC-C240-M4SX | FCH1916V1CT | 10.49.234.197 | 2S 24C 48T | 256 [GiB] | 
| P+ W(2) | Cu  |    | berlin-ucsm-5                 | (R) UCSC-C240-M4SX | FCH1916V0UY | 10.49.234.206 | 2S 24C 48T | 256 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-6                 | (R) UCSC-C240-M4S  | FCH1930V0KM | 10.49.234.195 | 2S 24C 48T | 384 [GiB] | 
| P- W(1) | Cu  |    | berlin-ucsm-7                 | (R) UCSC-C240-M4S  | FCH1930V1LA | 10.49.234.205 | 2S 28C 56T | 768 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-8                 | (R) UCSC-C220-M4S  | FCH1849V26H | 10.49.234.194 | 2S 24C 48T | 256 [GiB] | 
| P- C(1) | Cri |    | comp1-p2a-eu-spdc-WZP22511E6V | (R) UCSC-C240-M5SX | WZP22511E6V | 10.58.28.51   | 2S 24C 48T | 192 [GiB] | 
| P- C(1) | cri |    | comp3-p2a-eu-spdc-WZP2335149W | (R) UCSC-C220-M5SX | WZP2335149W | 10.58.28.53   | 2S 16C 32T | 192 [GiB] | 
| P+ C(1) | CRi |    | comp7-p3b-eu-spdc-FCH2023V2A4 | (R) UCSC-C220-M4S  | FCH2023V2A4 | 10.58.50.60   | 2S 28C 56T | 256 [GiB] | 
| P+ W(1) | Cri |    | esx13-eu-spdc-FCH2018V027     | (R) UCSC-C220-M4S  | FCH2018V027 | 10.58.29.53   | 2S 16C 32T | 256 [GiB] | 
| P+ C(1) | Cri |    | esx7-eu-spdc-FCH2004V0M6      | (R) UCSC-C220-M4S  | FCH2004V0M6 | 10.58.28.58   | 2S 16C 32T | 256 [GiB] | 
| P+ W(1) | Cri |    | esx92-eu-spdc-FCH2017V2AF     | (R) UCSC-C220-M4S  | FCH2017V2AF | 10.58.25.34   | 2S 28C 56T | 256 [GiB] | 
| P- W(2) | Cri |    | esx94-eu-spdc-FCH2017V2AH     | (R) UCSC-C220-M4S  | FCH2017V2AH | 10.58.25.36   | 2S 28C 56T | 256 [GiB] | 
| P+ C(1) | Cri |    | sn13-eu-spdc-WZP234301R9      | (R) SE-NODE-G2     | WZP234301R9 | 10.58.29.35   | 2S 20C 40T | 256 [GiB] | 
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+------------+-----------+
```
