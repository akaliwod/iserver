# Redfish Template Power

Vendor | Model
--- | ---
Cisco | UCSC-C220-M4S

```
# iserver get redfish endpoint
    --cache ucsc-ucs-c220-m4s-fch2017v24j-4.1.2g-off
    --type ucsc
    --ip 10.58.50.59
    --username admin
    --password ******
    --template power

Power Consumption (Watt)
------------------------
- Current      : 0
- Limit action : NoAction


+-------+--------+---------+--------+------------------+
| Name  | State  | Health  | Volts  | Upper Threshold  |
+-------+--------+---------+--------+------------------+
+-------+--------+---------+--------+------------------+

+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| Name  | State    | Health  | Serial       | Firmware  | Output (Watt)  | Input (Watt)  | Max (V)  | Min (V)  | Max (Hz)  | Min (Hz)  |
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| PSU1  | Enabled  | N/A     | LIT20100SXH  | 10052023  | 0              | 13            | 264      | 90       | 63        | 47        | 
| PSU2  | Enabled  | N/A     | LIT20100SU6  | 10052023  | 0              | 14            | 264      | 90       | 63        | 47        | 
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
```