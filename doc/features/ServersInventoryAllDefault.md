# Servers inventory in table mode

Use default output (-o) format.

```
# iserver get servers
+------------+---------------------------------+-----------------+--------------+----------------+--------------+------------+
| Flags      | Name                            | Model           | Serial       | IP             | CPU          | Memory     |
+------------+---------------------------------+-----------------+--------------+----------------+--------------+------------+
| P+HRS      |  C220-WZP23350ZAQ               | UCSC-C220-M5SX  | WZP23350ZAQ  | 10.58.244.186  | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      |  C220-WZP23360FH9               | UCSC-C220-M5SX  | WZP23360FH9  | 10.58.244.70   | 2S 40C 80T   | 384 [GiB]  | 
| P+CRS      | C220-231                        | UCSC-C220-M5SX  | WZP23240NNZ  | 10.58.250.241  | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | C240-WZP232102PH                | UCSC-C240-M5SX  | WZP232102PH  | 10.58.244.236  | 2S 56C 112T  | 512 [GiB]  | 
| P-HBS      | C3X60M4-FCH21067808             | UCSC-C3K-M4SRB  | FCH21067808  |                | 2S 24C 48T   | 256 [GiB]  | 
| P-CBU      | FI-ucsb1-eu-spdc-1-1            | UCSB-B200-M4    | FCH205371PZ  | 10.58.26.1     | 2S 24C 48T   | 256 [GiB]  | 
| P-CBU      | FI-ucsb1-eu-spdc-1-2            | UCSB-B200-M4    | FCH20527XXD  | 10.58.26.2     | 2S 24C 48T   | 256 [GiB]  | 
| P-CBU      | FI-ucsb1-eu-spdc-1-3            | UCSB-B200-M4    | FCH20437VXH  | 10.58.26.3     | 2S 24C 48T   | 256 [GiB]  | 
| P+HBU      | FI-ucsb1-eu-spdc-1-4            | UCSB-B200-M4    | FCH205371UU  | 10.58.26.4     | 2S 24C 48T   | 256 [GiB]  | 
| P-HBU      | FI-ucsb1-eu-spdc-2-1            | UCSB-B200-M5    | FLM241501FB  | 10.58.26.5     | 2S 40C 80T   | 384 [GiB]  | 
| P+HBU      | FI-ucsb1-eu-spdc-2-2            | UCSB-B200-M5    | FLM24140BJB  | 10.58.26.6     | 2S 40C 80T   | 384 [GiB]  | 
| P+HBU      | FI-ucsb1-eu-spdc-2-3            | UCSB-B200-M5    | FLM241501CT  | 10.58.26.7     | 2S 40C 80T   | 192 [GiB]  | 
| P+HBU      | FI-ucsb1-eu-spdc-2-4            | UCSB-B200-M5    | FLM24140B0B  | 10.58.26.8     | 2S 40C 80T   | 192 [GiB]  | 
| P-CRU      | HX1-eu-spdc-1                   | HXAF220C-M5SN   | WZP24100SMV  | 10.58.24.56    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRU      | HX1-eu-spdc-2                   | HXAF220C-M5SN   | WZP24100SN0  | 10.58.24.55    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRU      | HX1-eu-spdc-3                   | HXAF220C-M5SN   | WZP24100SML  | 10.58.24.53    | 2S 40C 80T   | 384 [GiB]  | 
| P+CRU      | HX1-eu-spdc-4                   | HXAF220C-M5SN   | WZP24100SMP  | 10.58.24.57    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRU      | HX1-eu-spdc-5                   | HXAF240C-M5SX   | WMP250901B0  | 10.58.24.58    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRU      | HX1-eu-spdc-6                   | HXAF240C-M5SX   | WMP250901AY  | 10.58.24.59    | 2S 52C 104T  | 768 [GiB]  | 
| P-HRU      | HX1-eu-spdc-7                   | HXAF240C-M5SX   | WMP2509019D  | 10.58.24.54    | 2S 52C 104T  | 768 [GiB]  | 
| P+HRS      | POD-4A-AIO-1-WZP23400AK9        | UCSC-C240-M5SN  | WZP23400AK9  | 10.58.29.55    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | POD-4A-AIO-2-WZP23400AK7        | UCSC-C240-M5SN  | WZP23400AK7  | 10.58.29.56    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | POD-4A-AIO-3-WZP23400AM2        | UCSC-C240-M5SN  | WZP23400AM2  | 10.58.29.57    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | aio-1-p1-eu-spdc-WZP22490ZCU    | UCSC-C220-M5SX  | WZP22490ZCU  | 10.58.28.41    | 2S 44C 88T   | 256 [GiB]  | 
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRS      | aio-2-p1-eu-spdc-WZP22520Y69    | UCSC-C220-M5SX  | WZP22520Y69  | 10.58.28.42    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | aio-3-p1-eu-spdc-WZP22520Y54    | UCSC-C220-M5SX  | WZP22520Y54  | 10.58.28.43    | 2S 44C 88T   | 256 [GiB]  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRS      | aio1-p3b-eu-spdc-FCH2017V1J7    | UCSC-C240-M4SX  | FCH2017V1J7  | 10.58.50.48    | 2S 16C 32T   | 128 [GiB]  | 
| P-HRS      | aio1-p5g-eu-spdc-WZP23450C7D    | UCSC-C240-M5SX  | WZP23450C7D  | 10.58.25.41    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS      | aio2-p3b-eu-spdc-FCH2017V1J8    | UCSC-C240-M4SX  | FCH2017V1J8  | 10.58.50.49    | 2S 16C 32T   | 128 [GiB]  | 
| P-HRS      | aio2-p5g-eu-spdc-WZP23450C8M    | UCSC-C240-M5SX  | WZP23450C8M  | 10.58.25.42    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS      | aio3-p3b-eu-spdc-FCH2017V1J5    | UCSC-C240-M4SX  | FCH2017V1J5  | 10.58.50.50    | 2S 16C 32T   | 128 [GiB]  | 
| P+HRS      | aio3-p5g-eu-spdc-WZP23450C8K    | UCSC-C240-M5SX  | WZP23450C8K  | 10.58.50.51    | 2S 48C 96T   | 384 [GiB]  | 
| P-HRU      | berlin-ucsm-1                   | UCSC-C240-M5SX  | WZP21490417  | 10.49.234.199  | 2S 28C 56T   | 704 [GiB]  | 
| P+WRU      | berlin-ucsm-2                   | UCSC-C240-M4S   | FCH1930V0PH  | 10.49.234.198  | 2S 24C 48T   | 384 [GiB]  | 
| P+WRU      | berlin-ucsm-3                   | UCSC-C220-M4S   | FCH2031V0YM  | 10.49.234.196  | 2S 28C 56T   | 672 [GiB]  | 
| P-CRU      | berlin-ucsm-4                   | UCSC-C240-M4SX  | FCH1916V1CT  | 10.49.234.197  | 2S 24C 48T   | 256 [GiB]  | 
| P-CRU      | berlin-ucsm-5                   | UCSC-C240-M4SX  | FCH1916V0UY  | 10.49.234.206  | 2S 24C 48T   | 256 [GiB]  | 
| P-WRU      | berlin-ucsm-6                   | UCSC-C240-M4S   | FCH1930V0KM  | 10.49.234.195  | 2S 24C 48T   | 384 [GiB]  | 
| P+WRU      | berlin-ucsm-7                   | UCSC-C240-M4S   | FCH1930V1LA  | 10.49.234.205  | 2S 28C 56T   | 768 [GiB]  | 
| P-WRU      | berlin-ucsm-8                   | UCSC-C220-M4S   | FCH1849V26H  | 10.49.234.194  | 2S 24C 48T   | 256 [GiB]  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47    | 2S 40C 80T   | 384 [GiB]  | 
| P-HRS      | comp1-p1-eu-spdc-WZP22520Y9J    | UCSC-C220-M5SX  | WZP22520Y9J  | 10.58.28.44    | 2S 48C 96T   | 256 [GiB]  | 
| P-CRS      | comp1-p2a-eu-spdc-WZP22511E6V   | UCSC-C240-M5SX  | WZP22511E6V  | 10.58.28.51    | 2S 24C 48T   | 192 [GiB]  | 
| P-HRS      | comp1-p3b-eu-spdc-FCH2108V1FC   | UCSC-C220-M4S   | FCH2108V1FC  | 10.58.50.57    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | comp1-p4A-eu-spdc               | UCSC-C220-M5SX  | WMP24040045  | 10.58.29.54    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | comp2-p1-spdc-WZP22520Y95       | UCSC-C220-M5SX  | WZP22520Y95  | 10.58.28.45    | 2S 48C 96T   | 256 [GiB]  | 
| P-HRS      | comp2-p2a-eu-spdc-WZP22511E6G   | UCSC-C240-M5SX  | WZP22511E6G  | 10.58.28.52    | 2S 24C 48T   | 192 [GiB]  | 
| P-HRS      | comp2-p3b-eu-spdc-FCH2017V1Y6   | UCSC-C220-M4S   | FCH2017V1Y6  | 10.58.50.58    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | comp2-p4a-eu-spdc-WZP22520B04   | UCSC-C220-M5SX  | WZP22520B04  | 10.58.29.58    | 2S 48C 96T   | 256 [GiB]  | 
| P-CRS      | comp3-p2a-eu-spdc-WZP2335149W   | UCSC-C220-M5SX  | WZP2335149W  | 10.58.28.53    | 2S 16C 32T   | 192 [GiB]  | 
| P-HRS      | comp3-p3b-eu-spdc-FCH2017V24J   | UCSC-C220-M4S   | FCH2017V24J  | 10.58.50.59    | 2S 28C 56T   | 256 [GiB]  | 
| P-HRS      | comp3-p4a-eu-spdc-WZP22520Y8X   | UCSC-C220-M5SX  | WZP22520Y8X  | 10.58.29.59    | 2S 24C 48T   | 256 [GiB]  | 
| P+HRS      | comp4-p1-eu-spdc-FCH2016V23J    | UCSC-C220-M4S   | FCH2016V23J  | 10.58.28.47    | 2S 28C 56T   | 256 [GiB]  | 
| P-HRS      | comp4-p2a-eu-spdc-WZP22520Y8W   | UCSC-C220-M5SX  | WZP22520Y8W  | 10.58.28.54    | 2S 24C 48T   | 192 [GiB]  | 
| P+HRS      | comp5-p1-eu-spdc-FCH2017V0TN    | UCSC-C220-M4S   | FCH2017V0TN  | 10.58.28.48    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRSL     | core-p5g-eu-spdc-WZP23440N02    | UCSC-C220-M5SX  | WZP23440N02  | 10.58.29.50    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS      | cu-p5g-eu-spdc-WZP23440N11      | UCSC-C220-M5SX  | WZP23440N11  | 10.58.29.49    | 2S 48C 96T   | 384 [GiB]  | 
| P+HRS      | du-p5g-eu-spdc-WZP2526088F      | UCSC-C240-M5SX  | WZP2526088F  | 10.58.29.48    | 2S 48C 48T   | 384 [GiB]  | 
| P+HRS      | esx00-eu-spdc-WZP22520AXQ       | UCSC-C220-M5SX  | WZP22520AXQ  | 10.58.29.36    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS      | esx01-eu-spdc-WZP22520Y99       | UCSC-C220-M5SX  | WZP22520Y99  | 10.58.29.37    | 2S 24C 48T   | 384 [GiB]  | 
| P+HRS      | esx10-eu-spdc-FCH2017V0TN       | UCSC-C220-M4S   | FCH2017V0TN  | 10.58.28.61    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | esx11-eu-spdc-FCH2050V125       | UCSC-C220-M4S   | FCH2050V125  | 10.58.29.51    | 2S 24C 48T   | 256 [GiB]  | 
| P+HRS      | esx2-eu-spdc-FCH2004V1PV        | UCSC-C220-M4S   | FCH2004V1PV  | 10.58.28.34    | 2S 16C 32T   | 256 [GiB]  | 
| P+HRS      | esx20-eu-spdc-WMP24040053       | UCSC-C220-M5SX  | WMP24040053  | 10.58.50.40    | 2S 40C 80T   | 384 [GiB]  | 
| P+HRS      | esx21-eu-spdc-WZP23440N1P       | UCSC-C220-M5SX  | WZP23440N1P  | 10.58.50.38    | 2S 48C 96T   | 512 [GiB]  | 
| P-HRS      | esx22-eu-spdc-WZP2343171Y       | UCSC-C220-M5SX  | WZP2343171Y  | 10.58.50.39    | 2S 48C 96T   | 512 [GiB]  | 
| P+HRS      | esx3-eu-spdc-FCH2004V0RW        | UCSC-C220-M4S   | FCH2004V0RW  | 10.58.28.35    | 2S 16C 32T   | 256 [GiB]  | 
| P-HRS      | esx4-eu-spdc-FCH2016V2BB        | UCSC-C220-M4S   | FCH2016V2BB  | 10.58.28.36    | 2S 36C 72T   | 512 [GiB]  | 
| P+HRS      | esx5-eu-spdc-FCH2017V024        | UCSC-C220-M4S   | FCH2017V024  | 10.58.28.50    | 2S 36C 72T   | 512 [GiB]  | 
| P+HRS      | esx6-eu-spdc-FCH2006V04E        | UCSC-C220-M4S   | FCH2006V04E  | 10.58.28.57    | 2S 16C 32T   | 256 [GiB]  | 
| P+CRS      | esx7-eu-spdc-FCH2004V0M6        | UCSC-C220-M4S   | FCH2004V0M6  | 10.58.28.58    | 2S 16C 32T   | 256 [GiB]  | 
| P+HRS      | esx8-eu-spdc-FCH2017V0T1        | UCSC-C220-M4S   | FCH2017V0T1  | 10.58.28.59    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | esx9-eu-spdc-FCH2016V23J        | UCSC-C220-M4S   | FCH2016V23J  | 10.58.28.60    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | esx91-eu-spdc-WZP234411LW       | UCSC-C240-M5SX  | WZP234411LW  | 10.58.25.33    | 2S 28C 56T   | 256 [GiB]  | 
| P+WRS      | esx92-eu-spdc-FCH2017V2AF       | UCSC-C220-M4S   | FCH2017V2AF  | 10.58.25.34    | 2S 28C 56T   | 256 [GiB]  | 
| P+HRS      | esx93-eu-spdc-FCH2108V1HE       | UCSC-C220-M4S   | FCH2108V1HE  | 10.58.25.35    | 2S 28C 56T   | 256 [GiB]  | 
| P-WRS      | esx94-eu-spdc-FCH2017V2AH       | UCSC-C220-M4S   | FCH2017V2AH  | 10.58.25.36    | 2S 28C 56T   | 256 [GiB]  | 
| P-HRS      | esx95-eu-spdc-FCH2017V241       | UCSC-C220-M4S   | FCH2017V241  | 10.58.25.37    | 2S 16C 32T   | 256 [GiB]  | 
| P+HRS      | mgmt-p1-eu-spdc-WZP2252176Z     | UCSC-C220-M5SX  | WZP2252176Z  | 10.58.28.40    | 2S 48C 96T   | 256 [GiB]  | 
| P+HRS      | mgmt-p4a-eu-spdc-WZP22520Y9D    | UCSC-C220-M5SX  | WZP22520Y9D  | 10.58.29.60    | 2S 48C 96T   | 256 [GiB]  | 
| P+HRS      | sn11-eu-spdc-WZP23430C4N        | SE-NODE-G2      | WZP23430C4N  | 10.58.29.33    | 2S 20C 40T   | 256 [GiB]  | 
| P+HRS      | sn12-eu-spdc-WZP23430C4D        | SE-NODE-G2      | WZP23430C4D  | 10.58.29.34    | 2S 20C 40T   | 256 [GiB]  | 
| P+CRS      | sn13-eu-spdc-WZP234301R9        | SE-NODE-G2      | WZP234301R9  | 10.58.29.35    | 2S 20C 40T   | 256 [GiB]  | 
| P+HRS      | tnas-eu-spdc-WZP22511E68        | UCSC-C240-M5SX  | WZP22511E68  | 10.58.25.52    | 2S 28C 56T   | 256 [GiB]  | 
| P+HBS      | ynasc1-eu-spdc-FCH20487P5X-1    | UCSC-C3K-M4SRB  | FCH21067808  |                | 2S 24C 48T   | 256 [GiB]  | 
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