# Filter by power supply state

Use --psu option to select servers with power supply reporting unhealthy state.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers
    --psu
+--------+--------------------------------+-----------------+--------------+----------------+-------------+------------+------+
| Flags  | Name                           | Model           | Serial       | IP             | CPU         | Memory     | Psu  |
+--------+--------------------------------+-----------------+--------------+----------------+-------------+------------+------+
| P-HRS  | aio-2-p1-eu-spdc-WZP22520Y69   | UCSC-C220-M5SX  | WZP22520Y69  | 10.58.28.42    | 2S 28C 56T  | 256 [GiB]  | 0/2  | 
| P-HRS  | aio1-p3b-eu-spdc-FCH2017V1J7   | UCSC-C240-M4SX  | FCH2017V1J7  | 10.58.50.48    | 2S 16C 32T  | 128 [GiB]  | 0/2  | 
| P-HRS  | aio2-p3b-eu-spdc-FCH2017V1J8   | UCSC-C240-M4SX  | FCH2017V1J8  | 10.58.50.49    | 2S 16C 32T  | 128 [GiB]  | 0/2  | 
| P-HRS  | aio3-p3b-eu-spdc-FCH2017V1J5   | UCSC-C240-M4SX  | FCH2017V1J5  | 10.58.50.50    | 2S 16C 32T  | 128 [GiB]  | 0/2  | 
| P-CRU  | berlin-ucsm-5                  | UCSC-C240-M4SX  | FCH1916V0UY  | 10.49.234.206  | 2S 24C 48T  | 256 [GiB]  | 1/2  | 
| P-HRS  | comp1-p3b-eu-spdc-FCH2108V1FC  | UCSC-C220-M4S   | FCH2108V1FC  | 10.58.50.57    | 2S 28C 56T  | 256 [GiB]  | 0/2  | 
| P-HRS  | comp2-p3b-eu-spdc-FCH2017V1Y6  | UCSC-C220-M4S   | FCH2017V1Y6  | 10.58.50.58    | 2S 28C 56T  | 256 [GiB]  | 0/2  | 
| P-HRS  | comp3-p3b-eu-spdc-FCH2017V24J  | UCSC-C220-M4S   | FCH2017V24J  | 10.58.50.59    | 2S 28C 56T  | 256 [GiB]  | 0/2  | 
| P+HRS  | comp4-p1-eu-spdc-FCH2016V23J   | UCSC-C220-M4S   | FCH2016V23J  | 10.58.28.47    | 2S 28C 56T  | 256 [GiB]  | 1/2  | 
| P+HRS  | comp5-p1-eu-spdc-FCH2017V0TN   | UCSC-C220-M4S   | FCH2017V0TN  | 10.58.28.48    | 2S 28C 56T  | 256 [GiB]  | 1/2  | 
| P-HRS  | esx4-eu-spdc-FCH2016V2BB       | UCSC-C220-M4S   | FCH2016V2BB  | 10.58.28.36    | 2S 36C 72T  | 512 [GiB]  | 0/2  | 
| P-WRS  | esx94-eu-spdc-FCH2017V2AH      | UCSC-C220-M4S   | FCH2017V2AH  | 10.58.25.36    | 2S 28C 56T  | 256 [GiB]  | 0/2  | 
| P-HRS  | esx95-eu-spdc-FCH2017V241      | UCSC-C220-M4S   | FCH2017V241  | 10.58.25.37    | 2S 16C 32T  | 256 [GiB]  | 0/2  | 
+--------+--------------------------------+-----------------+--------------+----------------+-------------+------------+------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
