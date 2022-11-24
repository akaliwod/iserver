# Filter by PCI device name

Use --pci option to select servers with PCI device model name matching provided value. Select based on case-insensite loose match rule.

You can add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

```
# iserver get servers --pci 710

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+-------------------------------------------------------------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     | PCI                                                               |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+-------------------------------------------------------------------+
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | Cisco(R) Ethernet Converged NIC XXV710-DA2                        | 
|            |                                 |                 |              |              |             |            | Cisco(R) Ethernet Converged NIC XXV710-DA2                        | 
|            |                                 |                 |              |              |             |            | Cisco UCS VIC 1457 MLOM                                           | 
|            |                                 |                 |              |              |             |            | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)  | 
|            |                                 |                 |              |              |             |            | Intel X550 LOM                                                    | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | Cisco(R) Ethernet Converged NIC XXV710-DA2                        | 
|            |                                 |                 |              |              |             |            | Cisco(R) Ethernet Converged NIC XXV710-DA2                        | 
|            |                                 |                 |              |              |             |            | Cisco UCS VIC 1457 MLOM                                           | 
|            |                                 |                 |              |              |             |            | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)  | 
|            |                                 |                 |              |              |             |            | Intel X550 LOM                                                    | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+-------------------------------------------------------------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
