# Filter by location led

Use --loc option to select servers with location led turned on.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --loc

+--------+-----+----+------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF     | MF  | WF | Name                         | Model              | Serial      | IP          | CPU        | Memory    |
+--------+-----+----+------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H L | cri |    | core-p5g-eu-spdc-WZP23440N02 | (R) UCSC-C220-M5SX | WZP23440N02 | 10.58.29.50 | 2S 48C 96T | 512 [GiB] | 
+--------+-----+----+------------------------------+--------------------+-------------+-------------+------------+-----------+
```
