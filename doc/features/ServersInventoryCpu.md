# Filter by CPU cores

Use --cpu option to select servers based on CPU cores count. Supported values by example:
- "--cpu 28" will select servers with 28 CPU cores
- "--cpu gt28" will select servers with >28 CPU cores
- "--cpu ge28" will select servers with >=28 CPU cores
- "--cpu le28" will select servers with <=28 CPU cores
- "--cpu lt28" will select servers with <28 CPU cores
- "--cpu ne28" will select servers with !=28 CPU cores

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

## Equal

```
# iserver get servers --cpu 40

+------------+---------------------------------+-----------------+--------------+----------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP             | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+----------------+-------------+------------+
| P+HRS      |  C220-WZP23350ZAQ               | UCSC-C220-M5SX  | WZP23350ZAQ  | 10.58.244.186  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      |  C220-WZP23360FH9               | UCSC-C220-M5SX  | WZP23360FH9  | 10.58.244.70   | 2S 40C 80T  | 384 [GiB]  | 
| P+CRS      | C220-231                        | UCSC-C220-M5SX  | WZP23240NNZ  | 10.58.250.241  | 2S 40C 80T  | 384 [GiB]  | 
| P-HBU      | FI-ucsb1-eu-spdc-2-1            | UCSB-B200-M5    | FLM241501FB  | 10.58.26.5     | 2S 40C 80T  | 384 [GiB]  | 
| P+HBU      | FI-ucsb1-eu-spdc-2-2            | UCSB-B200-M5    | FLM24140BJB  | 10.58.26.6     | 2S 40C 80T  | 384 [GiB]  | 
| P+HBU      | FI-ucsb1-eu-spdc-2-3            | UCSB-B200-M5    | FLM241501CT  | 10.58.26.7     | 2S 40C 80T  | 192 [GiB]  | 
| P+HBU      | FI-ucsb1-eu-spdc-2-4            | UCSB-B200-M5    | FLM24140B0B  | 10.58.26.8     | 2S 40C 80T  | 192 [GiB]  | 
| P-CRU      | HX1-eu-spdc-1                   | HXAF220C-M5SN   | WZP24100SMV  | 10.58.24.56    | 2S 40C 80T  | 384 [GiB]  | 
| P-HRU      | HX1-eu-spdc-2                   | HXAF220C-M5SN   | WZP24100SN0  | 10.58.24.55    | 2S 40C 80T  | 384 [GiB]  | 
| P-HRU      | HX1-eu-spdc-3                   | HXAF220C-M5SN   | WZP24100SML  | 10.58.24.53    | 2S 40C 80T  | 384 [GiB]  | 
| P+CRU      | HX1-eu-spdc-4                   | HXAF220C-M5SN   | WZP24100SMP  | 10.58.24.57    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | POD-4A-AIO-1-WZP23400AK9        | UCSC-C240-M5SN  | WZP23400AK9  | 10.58.29.55    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | POD-4A-AIO-2-WZP23400AK7        | UCSC-C240-M5SN  | WZP23400AK7  | 10.58.29.56    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | POD-4A-AIO-3-WZP23400AM2        | UCSC-C240-M5SN  | WZP23400AM2  | 10.58.29.57    | 2S 40C 80T  | 384 [GiB]  | 
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | comp1-p4A-eu-spdc               | UCSC-C220-M5SX  | WMP24040045  | 10.58.29.54    | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | esx20-eu-spdc-WMP24040053       | UCSC-C220-M5SX  | WMP24040053  | 10.58.50.40    | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+----------------+-------------+------------+

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
# iserver get servers --cpu 30

+--------+-------+--------+---------+-----+------+---------+
| Flags  | Name  | Model  | Serial  | IP  | CPU  | Memory  |
+--------+-------+--------+---------+-----+------+---------+
+--------+-------+--------+---------+-----+------+---------+

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
# iserver get servers --cpu 100

+--------+-------+--------+---------+-----+------+---------+
| Flags  | Name  | Model  | Serial  | IP  | CPU  | Memory  |
+--------+-------+--------+---------+-----+------+---------+
+--------+-------+--------+---------+-----+------+---------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
