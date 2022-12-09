# Servers filtering by serial number

Use --serial option to provide comma (,) separated list of serial numbers you want to get.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --serial WMP24040059,WMP240400FM

+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] | 
| P+ H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] | 
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
```
