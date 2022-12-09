# Filter by memory capacity

Use --memory option to select servers based on total available memory. Supported values by example:
- "--memory 128" will select servers with 128 [GiB] of memory
- "--memory gt128" will select servers with >128 [GiB] of memory
- "--memory ge128" will select servers with >=128 [GiB] of memory
- "--memory le128" will select servers with <=128 [GiB] of memory
- "--memory lt128" will select servers with <128 [GiB] of memory
- "--memory ne128" will select servers with !=128 [GiB] of memory

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

## Equal

```
# iserver get servers --memory 512

+---------+-----+----+-------------------------------+--------------------+-------------+---------------+--------------+-----------+
| SF      | MF  | WF | Name                          | Model              | Serial      | IP            | CPU          | Memory    |
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+--------------+-----------+
| P+ H    | Cri |    | C240-WZP232102PH              | (R) UCSC-C240-M5SX | WZP232102PH | 10.58.244.236 | 2S 56C 112T  | 512 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-1          | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33   | 2S 24C 48T   | 512 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-2          | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34   | 2S 24C 48T   | 512 [GiB] | 
| P- H    | cri |    | aio1-p5g-eu-spdc-WZP23450C7D  | (R) UCSC-C240-M5SX | WZP23450C7D | 10.58.25.41   | 2S 48C 96T   | 512 [GiB] | 
| P- H    | cri |    | aio2-p5g-eu-spdc-WZP23450C8M  | (R) UCSC-C240-M5SX | WZP23450C8M | 10.58.25.42   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | comp1-p4b-eu-spdc-WZP26360D36 | (R) UCSC-C245-M6SX | WZP26360D36 | 10.58.53.33   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | comp2-p4b-eu-spdc-WZP26360D3D | (R) UCSC-C245-M6SX | WZP26360D3D | 10.58.53.34   | 2S 128C 256T | 512 [GiB] | 
| P+ H    | Cri |    | comp3-p4b-eu-spdc-WZP262207UM | (R) UCSC-C225-M6S  | WZP262207UM | 10.58.53.35   | 1S 64C 128T  | 512 [GiB] | 
| P+ H    | Cri |    | comp4-p4b-eu-spdc-WZP262207VP | (R) UCSC-C225-M6S  | WZP262207VP | 10.58.53.36   | 1S 32C 64T   | 512 [GiB] | 
| P+ H L  | cri |    | core-p5g-eu-spdc-WZP23440N02  | (R) UCSC-C220-M5SX | WZP23440N02 | 10.58.29.50   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | esx00-eu-spdc-WZP22520AXQ     | (R) UCSC-C220-M5SX | WZP22520AXQ | 10.58.29.36   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | CRi |    | esx21-eu-spdc-WZP23440N1P     | (R) UCSC-C220-M5SX | WZP23440N1P | 10.58.50.38   | 2S 48C 96T   | 512 [GiB] | 
| P- H    | CRi |    | esx22-eu-spdc-WZP2343171Y     | (R) UCSC-C220-M5SX | WZP2343171Y | 10.58.50.39   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | esx4-eu-spdc-FCH2016V2BE      | (R) UCSC-C220-M4S  | FCH2016V2BE | 10.58.28.36   | 2S 36C 72T   | 512 [GiB] | 
| P+ H    | Cri |    | esx5-eu-spdc-FCH2017V024      | (R) UCSC-C220-M4S  | FCH2017V024 | 10.58.28.50   | 2S 36C 72T   | 512 [GiB] | 
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+--------------+-----------+
```

## Lower or Equal

```
# iserver get servers --memory 128

+------+-----+----+------------------------------------+--------------------+----------------+--------------+-------------+-----------+
| SF   | MF  | WF | Name                               | Model              | Serial         | IP           | CPU         | Memory    |
+------+-----+----+------------------------------------+--------------------+----------------+--------------+-------------+-----------+
| P+ H | Cri |    | Dell-PowerEdge R650-YGFCBTJSO8WOMR | (R) PowerEdge R650 | YGFCBTJSO8WOMR | 10.44.182.90 | 2S 56C 112T | 128 [GiB] | 
| P- H | CRi |    | comp1-p3b-eu-spdc-FCH2017V1J7      | (R) UCSC-C240-M4SX | FCH2017V1J7    | 10.58.50.48  | 2S 16C 32T  | 128 [GiB] | 
| P- H | Cri |    | comp2-p3b-eu-spdc-FCH2017V1J8      | (R) UCSC-C240-M4SX | FCH2017V1J8    | 10.58.50.49  | 2S 16C 32T  | 128 [GiB] | 
| P- H | Cri |    | comp3-p3b-eu-spdc-FCH2017V1J5      | (R) UCSC-C240-M4SX | FCH2017V1J5    | 10.58.50.50  | 2S 16C 32T  | 128 [GiB] | 
+------+-----+----+------------------------------------+--------------------+----------------+--------------+-------------+-----------+
```

## Greater or Equal

```
# iserver get servers --memory 512

+---------+-----+----+-------------------------------+--------------------+-------------+---------------+--------------+-----------+
| SF      | MF  | WF | Name                          | Model              | Serial      | IP            | CPU          | Memory    |
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+--------------+-----------+
| P+ H    | Cri |    | C240-WZP232102PH              | (R) UCSC-C240-M5SX | WZP232102PH | 10.58.244.236 | 2S 56C 112T  | 512 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-1          | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33   | 2S 24C 48T   | 512 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-2          | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34   | 2S 24C 48T   | 512 [GiB] | 
| P- H    | cri |    | aio1-p5g-eu-spdc-WZP23450C7D  | (R) UCSC-C240-M5SX | WZP23450C7D | 10.58.25.41   | 2S 48C 96T   | 512 [GiB] | 
| P- H    | cri |    | aio2-p5g-eu-spdc-WZP23450C8M  | (R) UCSC-C240-M5SX | WZP23450C8M | 10.58.25.42   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | comp1-p4b-eu-spdc-WZP26360D36 | (R) UCSC-C245-M6SX | WZP26360D36 | 10.58.53.33   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | comp2-p4b-eu-spdc-WZP26360D3D | (R) UCSC-C245-M6SX | WZP26360D3D | 10.58.53.34   | 2S 128C 256T | 512 [GiB] | 
| P+ H    | Cri |    | comp3-p4b-eu-spdc-WZP262207UM | (R) UCSC-C225-M6S  | WZP262207UM | 10.58.53.35   | 1S 64C 128T  | 512 [GiB] | 
| P+ H    | Cri |    | comp4-p4b-eu-spdc-WZP262207VP | (R) UCSC-C225-M6S  | WZP262207VP | 10.58.53.36   | 1S 32C 64T   | 512 [GiB] | 
| P+ H L  | cri |    | core-p5g-eu-spdc-WZP23440N02  | (R) UCSC-C220-M5SX | WZP23440N02 | 10.58.29.50   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | esx00-eu-spdc-WZP22520AXQ     | (R) UCSC-C220-M5SX | WZP22520AXQ | 10.58.29.36   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | CRi |    | esx21-eu-spdc-WZP23440N1P     | (R) UCSC-C220-M5SX | WZP23440N1P | 10.58.50.38   | 2S 48C 96T   | 512 [GiB] | 
| P- H    | CRi |    | esx22-eu-spdc-WZP2343171Y     | (R) UCSC-C220-M5SX | WZP2343171Y | 10.58.50.39   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | esx4-eu-spdc-FCH2016V2BE      | (R) UCSC-C220-M4S  | FCH2016V2BE | 10.58.28.36   | 2S 36C 72T   | 512 [GiB] | 
| P+ H    | Cri |    | esx5-eu-spdc-FCH2017V024      | (R) UCSC-C220-M4S  | FCH2017V024 | 10.58.28.50   | 2S 36C 72T   | 512 [GiB] | 
+---------+-----+----+-------------------------------+--------------------+-------------+---------------+--------------+-----------+
```
