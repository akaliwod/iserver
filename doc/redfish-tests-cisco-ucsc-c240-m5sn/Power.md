# Redfish Template Power

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SN

```
# iserver get redfish endpoint
    --cache ucsc-c240-m5sn-wzp23400ak4-4.1.3d-on
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --template power

Power Consumption (Watt)
------------------------
- Current      : 324
- Min          : 186
- Average      : 349
- Max          : 495
- Limit action : NoAction


+-----------------+----------+---------+--------+------------------+
| Name            | State    | Health  | Volts  | Upper Threshold  |
+-----------------+----------+---------+--------+------------------+
| PSU1_VOUT       | Enabled  | OK      | 12.2   | 14               | 
| PSU2_VOUT       | Enabled  | OK      | 12.2   | 14               | 
| P12V            | Enabled  | OK      | 11.89  | 13.166           | 
| P3V_BAT_SCALED  | Enabled  | OK      | 3.026  | 3.588            | 
+-----------------+----------+---------+--------+------------------+

+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| Name  | State    | Health  | Serial       | Firmware  | Output (Watt)  | Input (Watt)  | Max (V)  | Min (V)  | Max (Hz)  | Min (Hz)  |
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| PSU1  | Enabled  | OK      | LIT241244RQ  | 10062019  | 155            | 173           | 264      | 90       | 63        | 47        | 
| PSU2  | Enabled  | OK      | LIT241242TS  | 10062019  | 152            | 176           | 264      | 90       | 63        | 47        | 
+-------+----------+---------+--------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
```