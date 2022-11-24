# Filter by management (CIMC) IP address

Use --ip option to select servers by IP address or IP subnet.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

## IP Address

```
# iserver get servers --ip 10.58.50.41

+--------+--------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags  | Name                           | Model           | Serial       | IP           | CPU         | Memory     |
+--------+--------------------------------+-----------------+--------------+--------------+-------------+------------+
| P-HRS  | aio-1-p2b-eu-spdc-WZP23400AJW  | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 
+--------+--------------------------------+-----------------+--------------+--------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## IP Subnet

```
# iserver get servers --ip 10.58.50.0/24

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | 
| P-HRS      | aio1-p3b-eu-spdc-FCH2017V1J7    | UCSC-C240-M4SX  | FCH2017V1J7  | 10.58.50.48  | 2S 16C 32T  | 128 [GiB]  | 
| P-HRS      | aio2-p3b-eu-spdc-FCH2017V1J8    | UCSC-C240-M4SX  | FCH2017V1J8  | 10.58.50.49  | 2S 16C 32T  | 128 [GiB]  | 
| P-HRS      | aio3-p3b-eu-spdc-FCH2017V1J5    | UCSC-C240-M4SX  | FCH2017V1J5  | 10.58.50.50  | 2S 16C 32T  | 128 [GiB]  | 
| P+HRS      | aio3-p5g-eu-spdc-WZP23450C8K    | UCSC-C240-M5SX  | WZP23450C8K  | 10.58.50.51  | 2S 48C 96T  | 384 [GiB]  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | 
| P-HRS      | comp1-p3b-eu-spdc-FCH2108V1FC   | UCSC-C220-M4S   | FCH2108V1FC  | 10.58.50.57  | 2S 28C 56T  | 256 [GiB]  | 
| P-HRS      | comp2-p3b-eu-spdc-FCH2017V1Y6   | UCSC-C220-M4S   | FCH2017V1Y6  | 10.58.50.58  | 2S 28C 56T  | 256 [GiB]  | 
| P-HRS      | comp3-p3b-eu-spdc-FCH2017V24J   | UCSC-C220-M4S   | FCH2017V24J  | 10.58.50.59  | 2S 28C 56T  | 256 [GiB]  | 
| P+HRS      | esx20-eu-spdc-WMP24040053       | UCSC-C220-M5SX  | WMP24040053  | 10.58.50.40  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | esx21-eu-spdc-WZP23440N1P       | UCSC-C220-M5SX  | WZP23440N1P  | 10.58.50.38  | 2S 48C 96T  | 512 [GiB]  | 
| P-HRS      | esx22-eu-spdc-WZP2343171Y       | UCSC-C220-M5SX  | WZP2343171Y  | 10.58.50.39  | 2S 48C 96T  | 512 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
