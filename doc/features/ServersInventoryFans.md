# Filter by fans state

Use --fan option to select servers with fans reporting unhealthy state.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers
    --fan
+--------+--------------------------------+-----------------+--------------+----------------+--------------+------------+------+
| Flags  | Name                           | Model           | Serial       | IP             | CPU          | Memory     | Fan  |
+--------+--------------------------------+-----------------+--------------+----------------+--------------+------------+------+
| P+HRS  | C240-WZP232102PH               | UCSC-C240-M5SX  | WZP232102PH  | 10.58.244.236  | 2S 56C 112T  | 512 [GiB]  | 6/7  | 
| P+HRS  | POD-4A-AIO-1-WZP23400AK9       | UCSC-C240-M5SN  | WZP23400AK9  | 10.58.29.55    | 2S 40C 80T   | 384 [GiB]  | 6/7  | 
| P+HRS  | POD-4A-AIO-2-WZP23400AK7       | UCSC-C240-M5SN  | WZP23400AK7  | 10.58.29.56    | 2S 40C 80T   | 384 [GiB]  | 6/7  | 
| P+HRS  | POD-4A-AIO-3-WZP23400AM2       | UCSC-C240-M5SN  | WZP23400AM2  | 10.58.29.57    | 2S 40C 80T   | 384 [GiB]  | 6/7  | 
| P-HRS  | aio-1-p2b-eu-spdc-WZP23400AJW  | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41    | 2S 40C 80T   | 384 [GiB]  | 0/7  | 
| P-HRS  | aio-2-p1-eu-spdc-WZP22520Y69   | UCSC-C220-M5SX  | WZP22520Y69  | 10.58.28.42    | 2S 28C 56T   | 256 [GiB]  | 0/7  | 
| P+HRS  | aio-2-p2b-eu-spdc-WZP23400AK4  | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42    | 2S 40C 80T   | 384 [GiB]  | 6/7  | 
| P+HRS  | aio-3-p2b-eu-spdc-WZP23400AKL  | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43    | 2S 40C 80T   | 384 [GiB]  | 6/7  | 
| P-HRS  | aio1-p3b-eu-spdc-FCH2017V1J7   | UCSC-C240-M4SX  | FCH2017V1J7  | 10.58.50.48    | 2S 16C 32T   | 128 [GiB]  | 0/6  | 
| P-HRS  | aio1-p5g-eu-spdc-WZP23450C7D   | UCSC-C240-M5SX  | WZP23450C7D  | 10.58.25.41    | 2S 48C 96T   | 512 [GiB]  | 0/7  | 
| P-HRS  | aio2-p3b-eu-spdc-FCH2017V1J8   | UCSC-C240-M4SX  | FCH2017V1J8  | 10.58.50.49    | 2S 16C 32T   | 128 [GiB]  | 0/6  | 
| P-HRS  | aio2-p5g-eu-spdc-WZP23450C8M   | UCSC-C240-M5SX  | WZP23450C8M  | 10.58.25.42    | 2S 48C 96T   | 512 [GiB]  | 0/7  | 
| P-HRS  | aio3-p3b-eu-spdc-FCH2017V1J5   | UCSC-C240-M4SX  | FCH2017V1J5  | 10.58.50.50    | 2S 16C 32T   | 128 [GiB]  | 0/6  | 
| P+HRS  | aio3-p5g-eu-spdc-WZP23450C8K   | UCSC-C240-M5SX  | WZP23450C8K  | 10.58.50.51    | 2S 48C 96T   | 384 [GiB]  | 6/7  | 
| P-HRS  | comp1-p1-eu-spdc-WZP22520Y9J   | UCSC-C220-M5SX  | WZP22520Y9J  | 10.58.28.44    | 2S 48C 96T   | 256 [GiB]  | 0/7  | 
| P-CRS  | comp1-p2a-eu-spdc-WZP22511E6V  | UCSC-C240-M5SX  | WZP22511E6V  | 10.58.28.51    | 2S 24C 48T   | 192 [GiB]  | 0/7  | 
| P-HRS  | comp1-p3b-eu-spdc-FCH2108V1FC  | UCSC-C220-M4S   | FCH2108V1FC  | 10.58.50.57    | 2S 28C 56T   | 256 [GiB]  | 0/6  | 
| P-HRS  | comp2-p2a-eu-spdc-WZP22511E6G  | UCSC-C240-M5SX  | WZP22511E6G  | 10.58.28.52    | 2S 24C 48T   | 192 [GiB]  | 0/7  | 
| P-HRS  | comp2-p3b-eu-spdc-FCH2017V1Y6  | UCSC-C220-M4S   | FCH2017V1Y6  | 10.58.50.58    | 2S 28C 56T   | 256 [GiB]  | 0/6  | 
| P-CRS  | comp3-p2a-eu-spdc-WZP2335149W  | UCSC-C220-M5SX  | WZP2335149W  | 10.58.28.53    | 2S 16C 32T   | 192 [GiB]  | 0/7  | 
| P-HRS  | comp3-p3b-eu-spdc-FCH2017V24J  | UCSC-C220-M4S   | FCH2017V24J  | 10.58.50.59    | 2S 28C 56T   | 256 [GiB]  | 0/6  | 
| P-HRS  | comp3-p4a-eu-spdc-WZP22520Y8X  | UCSC-C220-M5SX  | WZP22520Y8X  | 10.58.29.59    | 2S 24C 48T   | 256 [GiB]  | 0/7  | 
| P+HRS  | comp4-p1-eu-spdc-FCH2016V23J   | UCSC-C220-M4S   | FCH2016V23J  | 10.58.28.47    | 2S 28C 56T   | 256 [GiB]  | 0/6  | 
| P-HRS  | comp4-p2a-eu-spdc-WZP22520Y8W  | UCSC-C220-M5SX  | WZP22520Y8W  | 10.58.28.54    | 2S 24C 48T   | 192 [GiB]  | 0/7  | 
| P+HRS  | comp5-p1-eu-spdc-FCH2017V0TN   | UCSC-C220-M4S   | FCH2017V0TN  | 10.58.28.48    | 2S 28C 56T   | 256 [GiB]  | 0/6  | 
| P+HRS  | du-p5g-eu-spdc-WZP2526088F     | UCSC-C240-M5SX  | WZP2526088F  | 10.58.29.48    | 2S 48C 48T   | 384 [GiB]  | 6/7  | 
| P-HRS  | esx22-eu-spdc-WZP2343171Y      | UCSC-C220-M5SX  | WZP2343171Y  | 10.58.50.39    | 2S 48C 96T   | 512 [GiB]  | 0/7  | 
| P-HRS  | esx4-eu-spdc-FCH2016V2BB       | UCSC-C220-M4S   | FCH2016V2BB  | 10.58.28.36    | 2S 36C 72T   | 512 [GiB]  | 0/6  | 
| P+HRS  | esx91-eu-spdc-WZP234411LW      | UCSC-C240-M5SX  | WZP234411LW  | 10.58.25.33    | 2S 28C 56T   | 256 [GiB]  | 6/7  | 
| P-WRS  | esx94-eu-spdc-FCH2017V2AH      | UCSC-C220-M4S   | FCH2017V2AH  | 10.58.25.36    | 2S 28C 56T   | 256 [GiB]  | 0/6  | 
| P-HRS  | esx95-eu-spdc-FCH2017V241      | UCSC-C220-M4S   | FCH2017V241  | 10.58.25.37    | 2S 16C 32T   | 256 [GiB]  | 0/6  | 
| P+HRS  | tnas-eu-spdc-WZP22511E68       | UCSC-C240-M5SX  | WZP22511E68  | 10.58.25.52    | 2S 28C 56T   | 256 [GiB]  | 6/7  | 
| P+HRS  | znas-eu-spdc-WZP22511E3P       | UCSC-C240-M5SX  | WZP22511E3P  | 10.58.28.56    | 2S 24C 48T   | 256 [GiB]  | 6/7  | 
+--------+--------------------------------+-----------------+--------------+----------------+--------------+------------+------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
