# Filter by location led

Use --loc option to select servers with location led turned on.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --loc

+---------+-------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags   | Name                          | Model           | Serial       | IP           | CPU         | Memory     |
+---------+-------------------------------+-----------------+--------------+--------------+-------------+------------+
| P+HRSL  | core-p5g-eu-spdc-WZP23440N02  | UCSC-C220-M5SX  | WZP23440N02  | 10.58.29.50  | 2S 48C 96T  | 512 [GiB]  | 
+---------+-------------------------------+-----------------+--------------+--------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
