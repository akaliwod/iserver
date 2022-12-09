# Filter by fans state

Use --fan option to select servers with fans reporting unhealthy state.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --fan

+---------+-----+----+--------------------------------+--------------------+-------------+---------------+-------------+-----------+-----+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP            | CPU         | Memory    | Fan |
+---------+-----+----+--------------------------------+--------------------+-------------+---------------+-------------+-----------+-----+
| P+ H    | Cri |    | C240-WZP232102PH               | (R) UCSC-C240-M5SX | WZP232102PH | 10.58.244.236 | 2S 56C 112T | 512 [GiB] | 6/7 | 
| P+ H    | Cri |    | POD-4A-AIO-1-WZP23400AK9       | (R) UCSC-C240-M5SN | WZP23400AK9 | 10.58.29.55   | 2S 40C 80T  | 384 [GiB] | 6/7 | 
| P+ H    | Cri |    | POD-4A-AIO-2-WZP23400AK7       | (R) UCSC-C240-M5SN | WZP23400AK7 | 10.58.29.56   | 2S 40C 80T  | 384 [GiB] | 6/7 | 
| P+ H    | Cri |    | POD-4A-AIO-3-WZP23400AM2       | (R) UCSC-C240-M5SN | WZP23400AM2 | 10.58.29.57   | 2S 40C 80T  | 384 [GiB] | 6/7 | 
| P- H    | cri |    | aio1-p5g-eu-spdc-WZP23450C7D   | (R) UCSC-C240-M5SX | WZP23450C7D | 10.58.25.41   | 2S 48C 96T  | 512 [GiB] | 0/7 | 
| P- H    | cri |    | aio2-p5g-eu-spdc-WZP23450C8M   | (R) UCSC-C240-M5SX | WZP23450C8M | 10.58.25.42   | 2S 48C 96T  | 512 [GiB] | 0/7 | 
| P+ H    | CRi |    | aio3-p5g-eu-spdc-WZP23450C8K   | (R) UCSC-C240-M5SX | WZP23450C8K | 10.58.50.51   | 2S 48C 96T  | 384 [GiB] | 6/7 | 
| P+ H    | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41   | 2S 40C 80T  | 384 [GiB] | 6/7 | 
| P+ H    | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42   | 2S 40C 80T  | 384 [GiB] | 6/7 | 
| P- H    | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43   | 2S 40C 80T  | 384 [GiB] | 0/7 | 
| P- C(1) | Cri |    | comp1-p2a-eu-spdc-WZP22511E6V  | (R) UCSC-C240-M5SX | WZP22511E6V | 10.58.28.51   | 2S 24C 48T  | 192 [GiB] | 0/7 | 
| P- H    | CRi |    | comp1-p3b-eu-spdc-FCH2017V1J7  | (R) UCSC-C240-M4SX | FCH2017V1J7 | 10.58.50.48   | 2S 16C 32T  | 128 [GiB] | 0/6 | 
| P- H    | Cri |    | comp2-p2a-eu-spdc-WZP22511E6G  | (R) UCSC-C240-M5SX | WZP22511E6G | 10.58.28.52   | 2S 24C 48T  | 192 [GiB] | 0/7 | 
| P- H    | Cri |    | comp2-p3b-eu-spdc-FCH2017V1J8  | (R) UCSC-C240-M4SX | FCH2017V1J8 | 10.58.50.49   | 2S 16C 32T  | 128 [GiB] | 0/6 | 
| P- C(1) | cri |    | comp3-p2a-eu-spdc-WZP2335149W  | (R) UCSC-C220-M5SX | WZP2335149W | 10.58.28.53   | 2S 16C 32T  | 192 [GiB] | 0/7 | 
| P- H    | Cri |    | comp3-p3b-eu-spdc-FCH2017V1J5  | (R) UCSC-C240-M4SX | FCH2017V1J5 | 10.58.50.50   | 2S 16C 32T  | 128 [GiB] | 0/6 | 
| P+ H    | Cri |    | comp3-p4b-eu-spdc-WZP262207UM  | (R) UCSC-C225-M6S  | WZP262207UM | 10.58.53.35   | 1S 64C 128T | 512 [GiB] | 6/8 | 
| P+ H    | cri |    | comp4-p1-eu-spdc-FCH2016V23J   | (R) UCSC-C220-M4S  | FCH2016V23J | 10.58.28.47   | 2S 28C 56T  | 256 [GiB] | 0/6 | 
| P- H    | Cri |    | comp4-p2a-eu-spdc-WZP22520Y8W  | (R) UCSC-C220-M5SX | WZP22520Y8W | 10.58.28.54   | 2S 24C 48T  | 192 [GiB] | 0/7 | 
| P- H    | Cri |    | comp4-p3b-eu-spdc-FCH2108V1FC  | (R) UCSC-C220-M4S  | FCH2108V1FC | 10.58.50.57   | 2S 28C 56T  | 256 [GiB] | 0/6 | 
| P+ H    | Cri |    | comp4-p4b-eu-spdc-WZP262207VP  | (R) UCSC-C225-M6S  | WZP262207VP | 10.58.53.36   | 1S 32C 64T  | 512 [GiB] | 6/8 | 
| P+ H    | cri |    | comp5-p1-eu-spdc-FCH2017V0TN   | (R) UCSC-C220-M4S  | FCH2017V0TN | 10.58.28.48   | 2S 28C 56T  | 256 [GiB] | 0/6 | 
| P- H    | Cri |    | comp5-p3b-eu-spdc-FCH2017V1Y6  | (R) UCSC-C220-M4S  | FCH2017V1Y6 | 10.58.50.58   | 2S 28C 56T  | 256 [GiB] | 0/6 | 
| P- H    | CRi |    | comp6-p3b-eu-spdc-FCH2017V24J  | (R) UCSC-C220-M4S  | FCH2017V24J | 10.58.50.59   | 2S 28C 56T  | 256 [GiB] | 0/6 | 
| P+ H    | Cri |    | du-p5g-eu-spdc-WZP2526088F     | (R) UCSC-C240-M5SX | WZP2526088F | 10.58.29.48   | 2S 48C 48T  | 384 [GiB] | 6/7 | 
| P- H    | CRi |    | esx22-eu-spdc-WZP2343171Y      | (R) UCSC-C220-M5SX | WZP2343171Y | 10.58.50.39   | 2S 48C 96T  | 512 [GiB] | 0/7 | 
| P+ H    | Cri |    | esx91-eu-spdc-WZP234411LW      | (R) UCSC-C240-M5SX | WZP234411LW | 10.58.25.33   | 2S 28C 56T  | 256 [GiB] | 6/7 | 
| P- W(2) | Cri |    | esx94-eu-spdc-FCH2017V2AH      | (R) UCSC-C220-M4S  | FCH2017V2AH | 10.58.25.36   | 2S 28C 56T  | 256 [GiB] | 0/6 | 
| P- H    | Cri |    | esx95-eu-spdc-FCH2017V241      | (R) UCSC-C220-M4S  | FCH2017V241 | 10.58.25.37   | 2S 16C 32T  | 256 [GiB] | 0/6 | 
| P+ H    | Cri |    | tnas-eu-spdc-WZP22511E68       | (R) UCSC-C240-M5SX | WZP22511E68 | 10.58.25.52   | 2S 28C 56T  | 256 [GiB] | 6/7 | 
| P+ H    | cri |    | znas-eu-spdc-WZP22511E3P       | (R) UCSC-C240-M5SX | WZP22511E3P | 10.58.28.56   | 2S 24C 48T  | 256 [GiB] | 6/7 | 
+---------+-----+----+--------------------------------+--------------------+-------------+---------------+-------------+-----------+-----+
```
