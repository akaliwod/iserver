# Servers Inventory Summary

Get servers' summary information.

Use command options for servers' filtering and information shown in summary.

Use -o|--output for desired output format.

## Base output

```
# iserver get summary

Selected servers count: 103

Type
- Rack  : 93
- Blade : 10

Models
- HXAF220C-M5SN             : 4
- HXAF240C-M5SX             : 3
- PowerEdge R650            : 1
- ProLiant DL360 Gen10 Plus : 1
- SE-NODE-G2                : 3
- UCSB-B200-M4              : 4
- UCSB-B200-M5              : 4
- UCSC-C220-M4S             : 26
- UCSC-C220-M5SX            : 26
- UCSC-C225-M6S             : 2
- UCSC-C240-M4S             : 3
- UCSC-C240-M4SX            : 5
- UCSC-C240-M5SN            : 6
- UCSC-C240-M5SX            : 11
- UCSC-C245-M6SX            : 2
- UCSC-C3K-M4SRB            : 2

Power
- On  : 77
- Off : 26

Maximum
- CpuSockets : 2
- CpuCores   : 128
- CpuThreads : 256
- Memory     : 768

Health
- Healthy  : 83
- Warning  : 10
- Critical : 10

Locator
- On  : 1
- Off : 102

Management Mode
- Standalone : 80
- UCSM       : 23

Last Workflows Summary
- Running                   : 0
- Success                   : 0
- Failed                    : 0
- Servers with workflows    : 0
- Servers with no workflows : 103

Workflow Names
```

## Extended output

```
# iserver get summary -c all

Selected servers count: 103

Type
- Rack  : 93
- Blade : 10

Models
- HXAF220C-M5SN             : 4
- HXAF240C-M5SX             : 3
- PowerEdge R650            : 1
- ProLiant DL360 Gen10 Plus : 1
- SE-NODE-G2                : 3
- UCSB-B200-M4              : 4
- UCSB-B200-M5              : 4
- UCSC-C220-M4S             : 26
- UCSC-C220-M5SX            : 26
- UCSC-C225-M6S             : 2
- UCSC-C240-M4S             : 3
- UCSC-C240-M4SX            : 5
- UCSC-C240-M5SN            : 6
- UCSC-C240-M5SX            : 11
- UCSC-C245-M6SX            : 2
- UCSC-C3K-M4SRB            : 2

Power
- On  : 77
- Off : 26

Maximum
- CpuSockets          : 2
- CpuCores            : 128
- CpuThreads          : 256
- Memory              : 768
- Storage Controllers : 12
- Total Disk Capacity : 31.58 [TB]
- HDD Count           : 21
- HDD Capacity        : 25.18 [TB]
- SSD Count           : 11
- SSD Capacity        : 31.58 [TB]
- PCI Devices         : 11

Health
- Healthy  : 83
- Warning  : 10
- Critical : 10

Locator
- On  : 1
- Off : 102

Management Mode
- Standalone : 80
- UCSM       : 23

Server Fans
- All up    : 72
- Some down : 31

Server Psus
- All up    : 91
- Some down : 12

PCI Models
-                                                                  : 6
- 00MNMV                                                           : 2
- 04TRD3                                                           : 1
- 0FGNRW                                                           : 1
- 0MHFHK                                                           : 1
- Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) : 2
- Cisco UCS VIC 1387 MLOM                                          : 1
- Cisco UCS VIC 1457 MLOM                                          : 1
- Cisco(R) Ethernet Converged NIC XXV710-DA2                       : 2
- Intel Unknown Device                                             : 1
- Intel X550 LOM                                                   : 45
- Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC               : 2
- Intel(R) I350 1 Gbps Network Controller                          : 27
- K53978-004                                                       : 1
- LSI MegaRAID SAS 3108                                            : 7
- N2XX-AIPCI01                                                     : 16
- P26463-B21                                                       : 1
- SSDPE21K375GAW                                                   : 7
- SSDPE2KX010T8K                                                   : 36
- UCS-C3K-M4RAID                                                   : 2
- UCS-M2-HWRAID                                                    : 4
- UCS-NVMEI4-I1920                                                 : 8
- UCSB-MRAID12G                                                    : 4
- UCSB-MRAID12G-HE                                                 : 4
- UCSC-C3260-SIOC                                                  : 2
- UCSC-GPU-A16                                                     : 1
- UCSC-GPU-T4-16                                                   : 1
- UCSC-M-V100-04                                                   : 4
- UCSC-MLOM-C100-04                                                : 1
- UCSC-MLOM-C25Q-04                                                : 26
- UCSC-MLOM-C40Q-03                                                : 8
- UCSC-MLOM-CSC-02                                                 : 31
- UCSC-MRAID12G                                                    : 27
- UCSC-NVMEHW-H1600                                                : 3
- UCSC-PCIE-C25Q-04                                                : 7
- UCSC-PCIE-CSC-02                                                 : 3
- UCSC-PCIE-ID10GF                                                 : 1
- UCSC-PCIE-ID25GF                                                 : 28
- UCSC-PCIE-ID40GF                                                 : 12
- UCSC-PCIE-IQ10GF                                                 : 69
- UCSC-RAID-M5                                                     : 33
- UCSC-RAID-M5HD                                                   : 11
- UCSC-RAID-M6SD                                                   : 2
- UCSC-RAID-M6T                                                    : 2
- UCSC-SAS-M5HD                                                    : 3

Firmware
- 2.55       : 1
- 4.0(4b)    : 3
- 4.0(4e)    : 1
- 4.1(1f)    : 1
- 4.1(2f)    : 20
- 4.1(2g)    : 10
- 4.1(2k)    : 8
- 4.1(3b)    : 2
- 4.1(3c)    : 1
- 4.1(3d)    : 28
- 4.1(3f)    : 7
- 4.2(1c)    : 8
- 4.2(2a)    : 11
- 4.2(2f)    : 1
- 5.10.00.00 : 1

Last Workflows Summary
- Running                   : 0
- Success                   : 0
- Failed                    : 0
- Servers with workflows    : 0
- Servers with no workflows : 103

Workflow Names
```
