# Filter by PCI device name

Use --pci option to select servers with PCI device model name matching provided value. Select based on case-insensite loose match rule.

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --pci 710

+--------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+------------------------------------------------------------------+
| SF     | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    | PCI                                                              |
+--------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+------------------------------------------------------------------+
| P- H   | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 
|        |     |    |                                |                    |             |             |            |           | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 
|        |     |    |                                |                    |             |             |            |           | Cisco UCS VIC 1457 MLOM                                          | 
|        |     |    |                                |                    |             |             |            |           | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 
|        |     |    |                                |                    |             |             |            |           | Intel X550 LOM                                                   | 
| P+ H L | cri |    | core-p5g-eu-spdc-WZP23440N02   | (R) UCSC-C220-M5SX | WZP23440N02 | 10.58.29.50 | 2S 48C 96T | 512 [GiB] | Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC               | 
|        |     |    |                                |                    |             |             |            |           | Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC               | 
|        |     |    |                                |                    |             |             |            |           | Cisco UCS VIC 1387 MLOM                                          | 
|        |     |    |                                |                    |             |             |            |           | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 
|        |     |    |                                |                    |             |             |            |           | Intel X550 LOM                                                   | 
+--------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+------------------------------------------------------------------+
```
