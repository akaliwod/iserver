# Filter by power state

Use --off option to select servers with power turned off.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --off

+---------+-----+----+--------------------------------+--------------------+-------------+---------------+-------------+-----------+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP            | CPU         | Memory    |
+---------+-----+----+--------------------------------+--------------------+-------------+---------------+-------------+-----------+
| P- H    | cri |    | C3X60M4-FCH21067808            | (B) UCSC-C3K-M4SRB | FCH21067808 |               | 2S 24C 48T  | 256 [GiB] | 
| P- C(2) | Cu  |    | HX1-eu-spdc-1                  | (R) HXAF220C-M5SN  | WZP24100SMV | 10.58.24.56   | 2S 40C 80T  | 384 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-2                  | (R) HXAF220C-M5SN  | WZP24100SN0 | 10.58.24.55   | 2S 40C 80T  | 384 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-3                  | (R) HXAF220C-M5SN  | WZP24100SML | 10.58.24.53   | 2S 40C 80T  | 384 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-5                  | (R) HXAF240C-M5SX  | WMP250901B0 | 10.58.24.58   | 2S 52C 104T | 768 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-6                  | (R) HXAF240C-M5SX  | WMP250901AY | 10.58.24.59   | 2S 52C 104T | 768 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-7                  | (R) HXAF240C-M5SX  | WMP2509019D | 10.58.24.54   | 2S 52C 104T | 768 [GiB] | 
| P- H    | cri |    | aio1-p5g-eu-spdc-WZP23450C7D   | (R) UCSC-C240-M5SX | WZP23450C7D | 10.58.25.41   | 2S 48C 96T  | 512 [GiB] | 
| P- H    | cri |    | aio2-p5g-eu-spdc-WZP23450C8M   | (R) UCSC-C240-M5SX | WZP23450C8M | 10.58.25.42   | 2S 48C 96T  | 512 [GiB] | 
| P- H    | Cu  |    | berlin-ucsm-1                  | (R) UCSC-C240-M5SX | WZP21490417 | 10.49.234.199 | 2S 28C 56T  | 704 [GiB] | 
| P- W(1) | Cu  |    | berlin-ucsm-4                  | (R) UCSC-C240-M4SX | FCH1916V1CT | 10.49.234.197 | 2S 24C 48T  | 256 [GiB] | 
| P- W(1) | Cu  |    | berlin-ucsm-7                  | (R) UCSC-C240-M4S  | FCH1930V1LA | 10.49.234.205 | 2S 28C 56T  | 768 [GiB] | 
| P- H    | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43   | 2S 40C 80T  | 384 [GiB] | 
| P- C(1) | Cri |    | comp1-p2a-eu-spdc-WZP22511E6V  | (R) UCSC-C240-M5SX | WZP22511E6V | 10.58.28.51   | 2S 24C 48T  | 192 [GiB] | 
| P- H    | CRi |    | comp1-p3b-eu-spdc-FCH2017V1J7  | (R) UCSC-C240-M4SX | FCH2017V1J7 | 10.58.50.48   | 2S 16C 32T  | 128 [GiB] | 
| P- H    | Cri |    | comp2-p2a-eu-spdc-WZP22511E6G  | (R) UCSC-C240-M5SX | WZP22511E6G | 10.58.28.52   | 2S 24C 48T  | 192 [GiB] | 
| P- H    | Cri |    | comp2-p3b-eu-spdc-FCH2017V1J8  | (R) UCSC-C240-M4SX | FCH2017V1J8 | 10.58.50.49   | 2S 16C 32T  | 128 [GiB] | 
| P- C(1) | cri |    | comp3-p2a-eu-spdc-WZP2335149W  | (R) UCSC-C220-M5SX | WZP2335149W | 10.58.28.53   | 2S 16C 32T  | 192 [GiB] | 
| P- H    | Cri |    | comp3-p3b-eu-spdc-FCH2017V1J5  | (R) UCSC-C240-M4SX | FCH2017V1J5 | 10.58.50.50   | 2S 16C 32T  | 128 [GiB] | 
| P- H    | Cri |    | comp4-p2a-eu-spdc-WZP22520Y8W  | (R) UCSC-C220-M5SX | WZP22520Y8W | 10.58.28.54   | 2S 24C 48T  | 192 [GiB] | 
| P- H    | Cri |    | comp4-p3b-eu-spdc-FCH2108V1FC  | (R) UCSC-C220-M4S  | FCH2108V1FC | 10.58.50.57   | 2S 28C 56T  | 256 [GiB] | 
| P- H    | Cri |    | comp5-p3b-eu-spdc-FCH2017V1Y6  | (R) UCSC-C220-M4S  | FCH2017V1Y6 | 10.58.50.58   | 2S 28C 56T  | 256 [GiB] | 
| P- H    | CRi |    | comp6-p3b-eu-spdc-FCH2017V24J  | (R) UCSC-C220-M4S  | FCH2017V24J | 10.58.50.59   | 2S 28C 56T  | 256 [GiB] | 
| P- H    | CRi |    | esx22-eu-spdc-WZP2343171Y      | (R) UCSC-C220-M5SX | WZP2343171Y | 10.58.50.39   | 2S 48C 96T  | 512 [GiB] | 
| P- W(2) | Cri |    | esx94-eu-spdc-FCH2017V2AH      | (R) UCSC-C220-M4S  | FCH2017V2AH | 10.58.25.36   | 2S 28C 56T  | 256 [GiB] | 
| P- H    | Cri |    | esx95-eu-spdc-FCH2017V241      | (R) UCSC-C220-M4S  | FCH2017V241 | 10.58.25.37   | 2S 16C 32T  | 256 [GiB] | 
+---------+-----+----+--------------------------------+--------------------+-------------+---------------+-------------+-----------+
```
