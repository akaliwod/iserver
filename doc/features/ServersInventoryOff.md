# Filter by power state

Use --off option to select servers with power turned off.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --off

+--------+--------------------------------+-----------------+--------------+----------------+--------------+------------+
| Flags  | Name                           | Model           | Serial       | IP             | CPU          | Memory     |
+--------+--------------------------------+-----------------+--------------+----------------+--------------+------------+
| P-HBS  | C3X60M4-FCH21067808            | UCSC-C3K-M4SRB  | FCH21067808  |                | 2S 24C 48T   | 256 [GiB]  | 
| P-CBU  | FI-ucsb1-eu-spdc-1-1           | UCSB-B200-M4    | FCH205371PZ  | 10.58.26.1     | 2S 24C 48T   | 256 [GiB]  | 
| P-CBU  | FI-ucsb1-eu-spdc-1-2           | UCSB-B200-M4    | FCH20527XXD  | 10.58.26.2     | 2S 24C 48T   | 256 [GiB]  | 
| P-CBU  | FI-ucsb1-eu-spdc-1-3           | UCSB-B200-M4    | FCH20437VXH  | 10.58.26.3     | 2S 24C 48T   | 256 [GiB]  | 
| P-HBU  | FI-ucsb1-eu-spdc-2-1           | UCSB-B200-M5    | FLM241501FB  | 10.58.26.5     | 2S 40C 80T   | 384 [GiB]  | 
| P-CRU  | HX1-eu-spdc-1                  | HXAF220C-M5SN   | WZP24100SMV  | 10.58.24.56    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRU  | HX1-eu-spdc-2                  | HXAF220C-M5SN   | WZP24100SN0  | 10.58.24.55    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRU  | HX1-eu-spdc-3                  | HXAF220C-M5SN   | WZP24100SML  | 10.58.24.53    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRU  | HX1-eu-spdc-5                  | HXAF240C-M5SX   | WMP250901B0  | 10.58.24.58    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRU  | HX1-eu-spdc-6                  | HXAF240C-M5SX   | WMP250901AY  | 10.58.24.59    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRU  | HX1-eu-spdc-7                  | HXAF240C-M5SX   | WMP2509019D  | 10.58.24.54    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRS  | aio-1-p2b-eu-spdc-WZP23400AJW  | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRS  | aio-2-p1-eu-spdc-WZP22520Y69   | UCSC-C220-M5SX  | WZP22520Y69  | 10.58.28.42    | 2S 28C 56T   | 256 [GiB]  | 
| P-HRS  | aio1-p3b-eu-spdc-FCH2017V1J7   | UCSC-C240-M4SX  | FCH2017V1J7  | 10.58.50.48    | 2S 16C 32T   | 128 [GiB]  | 
| P-HRS  | aio1-p5g-eu-spdc-WZP23450C7D   | UCSC-C240-M5SX  | WZP23450C7D  | 10.58.25.41    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS  | aio2-p3b-eu-spdc-FCH2017V1J8   | UCSC-C240-M4SX  | FCH2017V1J8  | 10.58.50.49    | 2S 16C 32T   | 128 [GiB]  | 
| P-HRS  | aio2-p5g-eu-spdc-WZP23450C8M   | UCSC-C240-M5SX  | WZP23450C8M  | 10.58.25.42    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS  | aio3-p3b-eu-spdc-FCH2017V1J5   | UCSC-C240-M4SX  | FCH2017V1J5  | 10.58.50.50    | 2S 16C 32T   | 128 [GiB]  | 
| P-HRU  | berlin-ucsm-1                  | UCSC-C240-M5SX  | WZP21490417  | 10.49.234.199  | 2S 28C 56T   | 704 [GiB]  | 
| P-CRU  | berlin-ucsm-4                  | UCSC-C240-M4SX  | FCH1916V1CT  | 10.49.234.197  | 2S 24C 48T   | 256 [GiB]  | 
| P-CRU  | berlin-ucsm-5                  | UCSC-C240-M4SX  | FCH1916V0UY  | 10.49.234.206  | 2S 24C 48T   | 256 [GiB]  | 
| P-WRU  | berlin-ucsm-6                  | UCSC-C240-M4S   | FCH1930V0KM  | 10.49.234.195  | 2S 24C 48T   | 384 [GiB]  | 
| P-WRU  | berlin-ucsm-8                  | UCSC-C220-M4S   | FCH1849V26H  | 10.49.234.194  | 2S 24C 48T   | 256 [GiB]  | 
| P-HRS  | comp1-p1-eu-spdc-WZP22520Y9J   | UCSC-C220-M5SX  | WZP22520Y9J  | 10.58.28.44    | 2S 48C 96T   | 256 [GiB]  | 
| P-CRS  | comp1-p2a-eu-spdc-WZP22511E6V  | UCSC-C240-M5SX  | WZP22511E6V  | 10.58.28.51    | 2S 24C 48T   | 192 [GiB]  | 
| P-HRS  | comp1-p3b-eu-spdc-FCH2108V1FC  | UCSC-C220-M4S   | FCH2108V1FC  | 10.58.50.57    | 2S 28C 56T   | 256 [GiB]  | 
| P-HRS  | comp2-p2a-eu-spdc-WZP22511E6G  | UCSC-C240-M5SX  | WZP22511E6G  | 10.58.28.52    | 2S 24C 48T   | 192 [GiB]  | 
| P-HRS  | comp2-p3b-eu-spdc-FCH2017V1Y6  | UCSC-C220-M4S   | FCH2017V1Y6  | 10.58.50.58    | 2S 28C 56T   | 256 [GiB]  | 
| P-CRS  | comp3-p2a-eu-spdc-WZP2335149W  | UCSC-C220-M5SX  | WZP2335149W  | 10.58.28.53    | 2S 16C 32T   | 192 [GiB]  | 
| P-HRS  | comp3-p3b-eu-spdc-FCH2017V24J  | UCSC-C220-M4S   | FCH2017V24J  | 10.58.50.59    | 2S 28C 56T   | 256 [GiB]  | 
| P-HRS  | comp3-p4a-eu-spdc-WZP22520Y8X  | UCSC-C220-M5SX  | WZP22520Y8X  | 10.58.29.59    | 2S 24C 48T   | 256 [GiB]  | 
| P-HRS  | comp4-p2a-eu-spdc-WZP22520Y8W  | UCSC-C220-M5SX  | WZP22520Y8W  | 10.58.28.54    | 2S 24C 48T   | 192 [GiB]  | 
| P-HRS  | esx22-eu-spdc-WZP2343171Y      | UCSC-C220-M5SX  | WZP2343171Y  | 10.58.50.39    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS  | esx4-eu-spdc-FCH2016V2BB       | UCSC-C220-M4S   | FCH2016V2BB  | 10.58.28.36    | 2S 36C 72T   | 512 [GiB]  | 
| P-WRS  | esx94-eu-spdc-FCH2017V2AH      | UCSC-C220-M4S   | FCH2017V2AH  | 10.58.25.36    | 2S 28C 56T   | 256 [GiB]  | 
| P-HRS  | esx95-eu-spdc-FCH2017V241      | UCSC-C220-M4S   | FCH2017V241  | 10.58.25.37    | 2S 16C 32T   | 256 [GiB]  | 
+--------+--------------------------------+-----------------+--------------+----------------+--------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
