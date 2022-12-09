# Filter UCSM managed server

Use --ucsm option to select UCSM managed servers.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --ucsm

+---------+----+----+----------------------+--------------------+-------------+---------------+-------------+-----------+
| SF      | MF | WF | Name                 | Model              | Serial      | IP            | CPU         | Memory    |
+---------+----+----+----------------------+--------------------+-------------+---------------+-------------+-----------+
| P+ C(9) | CU |    | FI-ucsb1-eu-spdc-1-1 | (B) UCSB-B200-M4   | FCH205371PZ | 10.58.52.33   | 2S 24C 48T  | 512 [GiB] | 
| P+ C(9) | CU |    | FI-ucsb1-eu-spdc-1-2 | (B) UCSB-B200-M4   | FCH20527XXD | 10.58.52.34   | 2S 24C 48T  | 512 [GiB] | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-1-3 | (B) UCSB-B200-M4   | FCH20437VXH | 10.58.52.35   | 2S 24C 48T  | 256 [GiB] | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-1-4 | (B) UCSB-B200-M4   | FCH205371UU | 10.58.52.36   | 2S 24C 48T  | 256 [GiB] | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-1 | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41   | 2S 40C 80T  | 384 [GiB] | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-2 | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42   | 2S 40C 80T  | 384 [GiB] | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-3 | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43   | 2S 40C 80T  | 192 [GiB] | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-4 | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44   | 2S 40C 80T  | 192 [GiB] | 
| P- C(2) | Cu |    | HX1-eu-spdc-1        | (R) HXAF220C-M5SN  | WZP24100SMV | 10.58.24.56   | 2S 40C 80T  | 384 [GiB] | 
| P- H    | Cu |    | HX1-eu-spdc-2        | (R) HXAF220C-M5SN  | WZP24100SN0 | 10.58.24.55   | 2S 40C 80T  | 384 [GiB] | 
| P- H    | Cu |    | HX1-eu-spdc-3        | (R) HXAF220C-M5SN  | WZP24100SML | 10.58.24.53   | 2S 40C 80T  | 384 [GiB] | 
| P+ C(3) | Cu |    | HX1-eu-spdc-4        | (R) HXAF220C-M5SN  | WZP24100SMP | 10.58.24.57   | 2S 40C 80T  | 384 [GiB] | 
| P- H    | Cu |    | HX1-eu-spdc-5        | (R) HXAF240C-M5SX  | WMP250901B0 | 10.58.24.58   | 2S 52C 104T | 768 [GiB] | 
| P- H    | Cu |    | HX1-eu-spdc-6        | (R) HXAF240C-M5SX  | WMP250901AY | 10.58.24.59   | 2S 52C 104T | 768 [GiB] | 
| P- H    | Cu |    | HX1-eu-spdc-7        | (R) HXAF240C-M5SX  | WMP2509019D | 10.58.24.54   | 2S 52C 104T | 768 [GiB] | 
| P- H    | Cu |    | berlin-ucsm-1        | (R) UCSC-C240-M5SX | WZP21490417 | 10.49.234.199 | 2S 28C 56T  | 704 [GiB] | 
| P+ W(1) | Cu |    | berlin-ucsm-2        | (R) UCSC-C240-M4S  | FCH1930V0PH | 10.49.234.198 | 2S 24C 48T  | 384 [GiB] | 
| P+ W(1) | Cu |    | berlin-ucsm-3        | (R) UCSC-C220-M4S  | FCH2031V0YM | 10.49.234.196 | 2S 28C 56T  | 672 [GiB] | 
| P- W(1) | Cu |    | berlin-ucsm-4        | (R) UCSC-C240-M4SX | FCH1916V1CT | 10.49.234.197 | 2S 24C 48T  | 256 [GiB] | 
| P+ W(2) | Cu |    | berlin-ucsm-5        | (R) UCSC-C240-M4SX | FCH1916V0UY | 10.49.234.206 | 2S 24C 48T  | 256 [GiB] | 
| P+ W(1) | Cu |    | berlin-ucsm-6        | (R) UCSC-C240-M4S  | FCH1930V0KM | 10.49.234.195 | 2S 24C 48T  | 384 [GiB] | 
| P- W(1) | Cu |    | berlin-ucsm-7        | (R) UCSC-C240-M4S  | FCH1930V1LA | 10.49.234.205 | 2S 28C 56T  | 768 [GiB] | 
| P+ W(1) | Cu |    | berlin-ucsm-8        | (R) UCSC-C220-M4S  | FCH1849V26H | 10.49.234.194 | 2S 24C 48T  | 256 [GiB] | 
+---------+----+----+----------------------+--------------------+-------------+---------------+-------------+-----------+
```
