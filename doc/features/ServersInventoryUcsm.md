# Filter UCSM managed server

Use --ucsm option to select UCSM managed servers.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers
    --ucsm
+--------+-----------------------+-----------------+--------------+----------------+--------------+------------+
| Flags  | Name                  | Model           | Serial       | IP             | CPU          | Memory     |
+--------+-----------------------+-----------------+--------------+----------------+--------------+------------+
| P-CBU  | FI-ucsb1-eu-spdc-1-1  | UCSB-B200-M4    | FCH205371PZ  | 10.58.26.1     | 2S 24C 48T   | 256 [GiB]  | 
| P-CBU  | FI-ucsb1-eu-spdc-1-2  | UCSB-B200-M4    | FCH20527XXD  | 10.58.26.2     | 2S 24C 48T   | 256 [GiB]  | 
| P-CBU  | FI-ucsb1-eu-spdc-1-3  | UCSB-B200-M4    | FCH20437VXH  | 10.58.26.3     | 2S 24C 48T   | 256 [GiB]  | 
| P+HBU  | FI-ucsb1-eu-spdc-1-4  | UCSB-B200-M4    | FCH205371UU  | 10.58.26.4     | 2S 24C 48T   | 256 [GiB]  | 
| P-HBU  | FI-ucsb1-eu-spdc-2-1  | UCSB-B200-M5    | FLM241501FB  | 10.58.26.5     | 2S 40C 80T   | 384 [GiB]  | 
| P+HBU  | FI-ucsb1-eu-spdc-2-2  | UCSB-B200-M5    | FLM24140BJB  | 10.58.26.6     | 2S 40C 80T   | 384 [GiB]  | 
| P+HBU  | FI-ucsb1-eu-spdc-2-3  | UCSB-B200-M5    | FLM241501CT  | 10.58.26.7     | 2S 40C 80T   | 192 [GiB]  | 
| P+HBU  | FI-ucsb1-eu-spdc-2-4  | UCSB-B200-M5    | FLM24140B0B  | 10.58.26.8     | 2S 40C 80T   | 192 [GiB]  | 
| P-CRU  | HX1-eu-spdc-1         | HXAF220C-M5SN   | WZP24100SMV  | 10.58.24.56    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRU  | HX1-eu-spdc-2         | HXAF220C-M5SN   | WZP24100SN0  | 10.58.24.55    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRU  | HX1-eu-spdc-3         | HXAF220C-M5SN   | WZP24100SML  | 10.58.24.53    | 2S 40C 80T   | 384 [GiB]  | 
| P+CRU  | HX1-eu-spdc-4         | HXAF220C-M5SN   | WZP24100SMP  | 10.58.24.57    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRU  | HX1-eu-spdc-5         | HXAF240C-M5SX   | WMP250901B0  | 10.58.24.58    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRU  | HX1-eu-spdc-6         | HXAF240C-M5SX   | WMP250901AY  | 10.58.24.59    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRU  | HX1-eu-spdc-7         | HXAF240C-M5SX   | WMP2509019D  | 10.58.24.54    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRU  | berlin-ucsm-1         | UCSC-C240-M5SX  | WZP21490417  | 10.49.234.199  | 2S 28C 56T   | 704 [GiB]  | 
| P+WRU  | berlin-ucsm-2         | UCSC-C240-M4S   | FCH1930V0PH  | 10.49.234.198  | 2S 24C 48T   | 384 [GiB]  | 
| P+WRU  | berlin-ucsm-3         | UCSC-C220-M4S   | FCH2031V0YM  | 10.49.234.196  | 2S 28C 56T   | 672 [GiB]  | 
| P-CRU  | berlin-ucsm-4         | UCSC-C240-M4SX  | FCH1916V1CT  | 10.49.234.197  | 2S 24C 48T   | 256 [GiB]  | 
| P-CRU  | berlin-ucsm-5         | UCSC-C240-M4SX  | FCH1916V0UY  | 10.49.234.206  | 2S 24C 48T   | 256 [GiB]  | 
| P-WRU  | berlin-ucsm-6         | UCSC-C240-M4S   | FCH1930V0KM  | 10.49.234.195  | 2S 24C 48T   | 384 [GiB]  | 
| P+WRU  | berlin-ucsm-7         | UCSC-C240-M4S   | FCH1930V1LA  | 10.49.234.205  | 2S 28C 56T   | 768 [GiB]  | 
| P-WRU  | berlin-ucsm-8         | UCSC-C220-M4S   | FCH1849V26H  | 10.49.234.194  | 2S 24C 48T   | 256 [GiB]  | 
+--------+-----------------------+-----------------+--------------+----------------+--------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
