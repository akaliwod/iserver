# Filter by server's health

Use --health option to select servers with any warnings or critical alarms.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --health

+--------+--------------------------------+-----------------+--------------+----------------+-------------+------------+
| Flags  | Name                           | Model           | Serial       | IP             | CPU         | Memory     |
+--------+--------------------------------+-----------------+--------------+----------------+-------------+------------+
| P+CRS  | C220-231                       | UCSC-C220-M5SX  | WZP23240NNZ  | 10.58.250.241  | 2S 40C 80T  | 384 [GiB]  | 
| P-CBU  | FI-ucsb1-eu-spdc-1-1           | UCSB-B200-M4    | FCH205371PZ  | 10.58.26.1     | 2S 24C 48T  | 256 [GiB]  | 
| P-CBU  | FI-ucsb1-eu-spdc-1-2           | UCSB-B200-M4    | FCH20527XXD  | 10.58.26.2     | 2S 24C 48T  | 256 [GiB]  | 
| P-CBU  | FI-ucsb1-eu-spdc-1-3           | UCSB-B200-M4    | FCH20437VXH  | 10.58.26.3     | 2S 24C 48T  | 256 [GiB]  | 
| P-CRU  | HX1-eu-spdc-1                  | HXAF220C-M5SN   | WZP24100SMV  | 10.58.24.56    | 2S 40C 80T  | 384 [GiB]  | 
| P+CRU  | HX1-eu-spdc-4                  | HXAF220C-M5SN   | WZP24100SMP  | 10.58.24.57    | 2S 40C 80T  | 384 [GiB]  | 
| P+WRU  | berlin-ucsm-2                  | UCSC-C240-M4S   | FCH1930V0PH  | 10.49.234.198  | 2S 24C 48T  | 384 [GiB]  | 
| P+WRU  | berlin-ucsm-3                  | UCSC-C220-M4S   | FCH2031V0YM  | 10.49.234.196  | 2S 28C 56T  | 672 [GiB]  | 
| P-CRU  | berlin-ucsm-4                  | UCSC-C240-M4SX  | FCH1916V1CT  | 10.49.234.197  | 2S 24C 48T  | 256 [GiB]  | 
| P-CRU  | berlin-ucsm-5                  | UCSC-C240-M4SX  | FCH1916V0UY  | 10.49.234.206  | 2S 24C 48T  | 256 [GiB]  | 
| P-WRU  | berlin-ucsm-6                  | UCSC-C240-M4S   | FCH1930V0KM  | 10.49.234.195  | 2S 24C 48T  | 384 [GiB]  | 
| P+WRU  | berlin-ucsm-7                  | UCSC-C240-M4S   | FCH1930V1LA  | 10.49.234.205  | 2S 28C 56T  | 768 [GiB]  | 
| P-WRU  | berlin-ucsm-8                  | UCSC-C220-M4S   | FCH1849V26H  | 10.49.234.194  | 2S 24C 48T  | 256 [GiB]  | 
| P-CRS  | comp1-p2a-eu-spdc-WZP22511E6V  | UCSC-C240-M5SX  | WZP22511E6V  | 10.58.28.51    | 2S 24C 48T  | 192 [GiB]  | 
| P-CRS  | comp3-p2a-eu-spdc-WZP2335149W  | UCSC-C220-M5SX  | WZP2335149W  | 10.58.28.53    | 2S 16C 32T  | 192 [GiB]  | 
| P+CRS  | esx7-eu-spdc-FCH2004V0M6       | UCSC-C220-M4S   | FCH2004V0M6  | 10.58.28.58    | 2S 16C 32T  | 256 [GiB]  | 
| P+WRS  | esx92-eu-spdc-FCH2017V2AF      | UCSC-C220-M4S   | FCH2017V2AF  | 10.58.25.34    | 2S 28C 56T  | 256 [GiB]  | 
| P-WRS  | esx94-eu-spdc-FCH2017V2AH      | UCSC-C220-M4S   | FCH2017V2AH  | 10.58.25.36    | 2S 28C 56T  | 256 [GiB]  | 
| P+CRS  | sn13-eu-spdc-WZP234301R9       | SE-NODE-G2      | WZP234301R9  | 10.58.29.35    | 2S 20C 40T  | 256 [GiB]  | 
+--------+--------------------------------+-----------------+--------------+----------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
