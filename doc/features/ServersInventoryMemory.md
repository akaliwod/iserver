# Filter by memory capacity

Use --memory option to select servers based on total available memory. Supported values by example:
- "--memory 128" will select servers with 128 [GiB] of memory
- "--memory gt128" will select servers with >128 [GiB] of memory
- "--memory ge128" will select servers with >=128 [GiB] of memory
- "--memory le128" will select servers with <=128 [GiB] of memory
- "--memory lt128" will select servers with <128 [GiB] of memory
- "--memory ne128" will select servers with !=128 [GiB] of memory

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

## Equal

```
# iserver get servers --memory 512

+---------+-------------------------------+-----------------+--------------+----------------+--------------+------------+
| Flags   | Name                          | Model           | Serial       | IP             | CPU          | Memory     |
+---------+-------------------------------+-----------------+--------------+----------------+--------------+------------+
| P+HRS   | C240-WZP232102PH              | UCSC-C240-M5SX  | WZP232102PH  | 10.58.244.236  | 2S 56C 112T  | 512 [GiB]  | 
| P-HRS   | aio1-p5g-eu-spdc-WZP23450C7D  | UCSC-C240-M5SX  | WZP23450C7D  | 10.58.25.41    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS   | aio2-p5g-eu-spdc-WZP23450C8M  | UCSC-C240-M5SX  | WZP23450C8M  | 10.58.25.42    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRSL  | core-p5g-eu-spdc-WZP23440N02  | UCSC-C220-M5SX  | WZP23440N02  | 10.58.29.50    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS   | esx00-eu-spdc-WZP22520AXQ     | UCSC-C220-M5SX  | WZP22520AXQ  | 10.58.29.36    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS   | esx21-eu-spdc-WZP23440N1P     | UCSC-C220-M5SX  | WZP23440N1P  | 10.58.50.38    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS   | esx22-eu-spdc-WZP2343171Y     | UCSC-C220-M5SX  | WZP2343171Y  | 10.58.50.39    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS   | esx4-eu-spdc-FCH2016V2BB      | UCSC-C220-M4S   | FCH2016V2BB  | 10.58.28.36    | 2S 36C 72T   | 512 [GiB]  | 
| P+HRS   | esx5-eu-spdc-FCH2017V024      | UCSC-C220-M4S   | FCH2017V024  | 10.58.28.50    | 2S 36C 72T   | 512 [GiB]  | 
+---------+-------------------------------+-----------------+--------------+----------------+--------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## Lower or Equal

```
# iserver get servers --memory 128

+--------+-------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags  | Name                          | Model           | Serial       | IP           | CPU         | Memory     |
+--------+-------------------------------+-----------------+--------------+--------------+-------------+------------+
| P-HRS  | aio1-p3b-eu-spdc-FCH2017V1J7  | UCSC-C240-M4SX  | FCH2017V1J7  | 10.58.50.48  | 2S 16C 32T  | 128 [GiB]  | 
| P-HRS  | aio2-p3b-eu-spdc-FCH2017V1J8  | UCSC-C240-M4SX  | FCH2017V1J8  | 10.58.50.49  | 2S 16C 32T  | 128 [GiB]  | 
| P-HRS  | aio3-p3b-eu-spdc-FCH2017V1J5  | UCSC-C240-M4SX  | FCH2017V1J5  | 10.58.50.50  | 2S 16C 32T  | 128 [GiB]  | 
+--------+-------------------------------+-----------------+--------------+--------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## Greater or Equal

```
# iserver get servers --memory 512

+---------+-------------------------------+-----------------+--------------+----------------+--------------+------------+
| Flags   | Name                          | Model           | Serial       | IP             | CPU          | Memory     |
+---------+-------------------------------+-----------------+--------------+----------------+--------------+------------+
| P+HRS   | C240-WZP232102PH              | UCSC-C240-M5SX  | WZP232102PH  | 10.58.244.236  | 2S 56C 112T  | 512 [GiB]  | 
| P-HRS   | aio1-p5g-eu-spdc-WZP23450C7D  | UCSC-C240-M5SX  | WZP23450C7D  | 10.58.25.41    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS   | aio2-p5g-eu-spdc-WZP23450C8M  | UCSC-C240-M5SX  | WZP23450C8M  | 10.58.25.42    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRSL  | core-p5g-eu-spdc-WZP23440N02  | UCSC-C220-M5SX  | WZP23440N02  | 10.58.29.50    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS   | esx00-eu-spdc-WZP22520AXQ     | UCSC-C220-M5SX  | WZP22520AXQ  | 10.58.29.36    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS   | esx21-eu-spdc-WZP23440N1P     | UCSC-C220-M5SX  | WZP23440N1P  | 10.58.50.38    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS   | esx22-eu-spdc-WZP2343171Y     | UCSC-C220-M5SX  | WZP2343171Y  | 10.58.50.39    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS   | esx4-eu-spdc-FCH2016V2BB      | UCSC-C220-M4S   | FCH2016V2BB  | 10.58.28.36    | 2S 36C 72T   | 512 [GiB]  | 
| P+HRS   | esx5-eu-spdc-FCH2017V024      | UCSC-C220-M4S   | FCH2017V024  | 10.58.28.50    | 2S 36C 72T   | 512 [GiB]  | 
+---------+-------------------------------+-----------------+--------------+----------------+--------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
