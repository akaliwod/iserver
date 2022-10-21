# Filter by server name

Define --name value for case-insensite loose match of server's name.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers
    --name p2b
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
