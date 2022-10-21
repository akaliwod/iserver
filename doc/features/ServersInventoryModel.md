# Filter by server model

Define --model value for case-insensite loose match of server's model.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers
    --model m5sx
+------------+---------------------------------+-----------------+--------------+----------------+--------------+------------+
| Flags      | Name                            | Model           | Serial       | IP             | CPU          | Memory     |
+------------+---------------------------------+-----------------+--------------+----------------+--------------+------------+
| P+HRS      |  C220-WZP23350ZAQ               | UCSC-C220-M5SX  | WZP23350ZAQ  | 10.58.244.186  | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      |  C220-WZP23360FH9               | UCSC-C220-M5SX  | WZP23360FH9  | 10.58.244.70   | 2S 40C 80T   | 384 [GiB]  | 
| P+CRS      | C220-231                        | UCSC-C220-M5SX  | WZP23240NNZ  | 10.58.250.241  | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | C240-WZP232102PH                | UCSC-C240-M5SX  | WZP232102PH  | 10.58.244.236  | 2S 56C 112T  | 512 [GiB]  | 
| P-HRU      | HX1-eu-spdc-5                   | HXAF240C-M5SX   | WMP250901B0  | 10.58.24.58    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRU      | HX1-eu-spdc-6                   | HXAF240C-M5SX   | WMP250901AY  | 10.58.24.59    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRU      | HX1-eu-spdc-7                   | HXAF240C-M5SX   | WMP2509019D  | 10.58.24.54    | 2S 52C 104T  | 768 [GiB]  | 
| P+HRS      | aio-1-p1-eu-spdc-WZP22490ZCU    | UCSC-C220-M5SX  | WZP22490ZCU  | 10.58.28.41    | 2S 44C 88T   | 256 [GiB]  | 
| P-HRS      | aio-2-p1-eu-spdc-WZP22520Y69    | UCSC-C220-M5SX  | WZP22520Y69  | 10.58.28.42    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | aio-3-p1-eu-spdc-WZP22520Y54    | UCSC-C220-M5SX  | WZP22520Y54  | 10.58.28.43    | 2S 44C 88T   | 256 [GiB]  | 
| P-HRS      | aio1-p5g-eu-spdc-WZP23450C7D    | UCSC-C240-M5SX  | WZP23450C7D  | 10.58.25.41    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS      | aio2-p5g-eu-spdc-WZP23450C8M    | UCSC-C240-M5SX  | WZP23450C8M  | 10.58.25.42    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS      | aio3-p5g-eu-spdc-WZP23450C8K    | UCSC-C240-M5SX  | WZP23450C8K  | 10.58.50.51    | 2S 48C 96T   | 384 [GiB]  | 
| P-HRU      | berlin-ucsm-1                   | UCSC-C240-M5SX  | WZP21490417  | 10.49.234.199  | 2S 28C 56T   | 704 [GiB]  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRS      | comp1-p1-eu-spdc-WZP22520Y9J    | UCSC-C220-M5SX  | WZP22520Y9J  | 10.58.28.44    | 2S 48C 96T   | 256 [GiB]  | 
| P-CRS      | comp1-p2a-eu-spdc-WZP22511E6V   | UCSC-C240-M5SX  | WZP22511E6V  | 10.58.28.51    | 2S 24C 48T   | 192 [GiB]  | 
| P+HRS      | comp1-p4A-eu-spdc               | UCSC-C220-M5SX  | WMP24040045  | 10.58.29.54    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | comp2-p1-spdc-WZP22520Y95       | UCSC-C220-M5SX  | WZP22520Y95  | 10.58.28.45    | 2S 48C 96T   | 256 [GiB]  | 
| P-HRS      | comp2-p2a-eu-spdc-WZP22511E6G   | UCSC-C240-M5SX  | WZP22511E6G  | 10.58.28.52    | 2S 24C 48T   | 192 [GiB]  | 
| P+HRS      | comp2-p4a-eu-spdc-WZP22520B04   | UCSC-C220-M5SX  | WZP22520B04  | 10.58.29.58    | 2S 48C 96T   | 256 [GiB]  | 
| P-CRS      | comp3-p2a-eu-spdc-WZP2335149W   | UCSC-C220-M5SX  | WZP2335149W  | 10.58.28.53    | 2S 16C 32T   | 192 [GiB]  | 
| P-HRS      | comp3-p4a-eu-spdc-WZP22520Y8X   | UCSC-C220-M5SX  | WZP22520Y8X  | 10.58.29.59    | 2S 24C 48T   | 256 [GiB]  | 
| P-HRS      | comp4-p2a-eu-spdc-WZP22520Y8W   | UCSC-C220-M5SX  | WZP22520Y8W  | 10.58.28.54    | 2S 24C 48T   | 192 [GiB]  | 
| P+HRSL     | core-p5g-eu-spdc-WZP23440N02    | UCSC-C220-M5SX  | WZP23440N02  | 10.58.29.50    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS      | cu-p5g-eu-spdc-WZP23440N11      | UCSC-C220-M5SX  | WZP23440N11  | 10.58.29.49    | 2S 48C 96T   | 384 [GiB]  | 
| P+HRS      | du-p5g-eu-spdc-WZP2526088F      | UCSC-C240-M5SX  | WZP2526088F  | 10.58.29.48    | 2S 48C 48T   | 384 [GiB]  | 
| P+HRS      | esx00-eu-spdc-WZP22520AXQ       | UCSC-C220-M5SX  | WZP22520AXQ  | 10.58.29.36    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS      | esx01-eu-spdc-WZP22520Y99       | UCSC-C220-M5SX  | WZP22520Y99  | 10.58.29.37    | 2S 24C 48T   | 384 [GiB]  | 
| P+HRS      | esx20-eu-spdc-WMP24040053       | UCSC-C220-M5SX  | WMP24040053  | 10.58.50.40    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | esx21-eu-spdc-WZP23440N1P       | UCSC-C220-M5SX  | WZP23440N1P  | 10.58.50.38    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS      | esx22-eu-spdc-WZP2343171Y       | UCSC-C220-M5SX  | WZP2343171Y  | 10.58.50.39    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS      | esx91-eu-spdc-WZP234411LW       | UCSC-C240-M5SX  | WZP234411LW  | 10.58.25.33    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | mgmt-p1-eu-spdc-WZP2252176Z     | UCSC-C220-M5SX  | WZP2252176Z  | 10.58.28.40    | 2S 48C 96T   | 256 [GiB]  | 
| P+HRS      | mgmt-p4a-eu-spdc-WZP22520Y9D    | UCSC-C220-M5SX  | WZP22520Y9D  | 10.58.29.60    | 2S 48C 96T   | 256 [GiB]  | 
| P+HRS      | tnas-eu-spdc-WZP22511E68        | UCSC-C240-M5SX  | WZP22511E68  | 10.58.25.52    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | znas-eu-spdc-WZP22511E3P        | UCSC-C240-M5SX  | WZP22511E3P  | 10.58.28.56    | 2S 24C 48T   | 256 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+----------------+--------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
