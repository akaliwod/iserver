# Servers Inventory Summary

Get servers' summary information in default, json or yaml formats.

Use command options for servers' filtering and information shown in summary.

## Base output

```
# iserver get summary
Selected servers count: 92

Type
- Rack  : 82
- Blade : 10

Models
- HXAF220C-M5SN  : 4
- HXAF240C-M5SX  : 3
- SE-NODE-G2     : 3
- UCSB-B200-M4   : 4
- UCSB-B200-M5   : 4
- UCSC-C220-M4S  : 21
- UCSC-C220-M5SX : 26
- UCSC-C240-M4S  : 3
- UCSC-C240-M4SX : 5
- UCSC-C240-M5SN : 6
- UCSC-C240-M5SX : 11
- UCSC-C3K-M4SRB : 2

Power
- On  : 56
- Off : 36

Maximum
- CpuSockets : 2
- CpuCores   : 56
- CpuThreads : 112
- Memory     : 768

Health
- Healthy  : 73
- Warning  : 7
- Critical : 12

Locator
- On  : 1
- Off : 91

Management Mode
- Standalone : 69
- UCSM       : 23

Last Workflows Summary
- Running                   : 1
- Success                   : 37
- Failed                    : 0
- Servers with workflows    : 1
- Servers with no workflows : 91

Workflow Names
- InstallOS                : 12
- Power Cycle              : 11
- Operating System Install : 11
- Turn Off Locator         : 2
- Turn On Locator          : 2
```

## Extended output

```
# iserver get summary -c all
Selected servers count: 92

Type
- Rack  : 82
- Blade : 10

Models
- HXAF220C-M5SN  : 4
- HXAF240C-M5SX  : 3
- SE-NODE-G2     : 3
- UCSB-B200-M4   : 4
- UCSB-B200-M5   : 4
- UCSC-C220-M4S  : 21
- UCSC-C220-M5SX : 26
- UCSC-C240-M4S  : 3
- UCSC-C240-M4SX : 5
- UCSC-C240-M5SN : 6
- UCSC-C240-M5SX : 11
- UCSC-C3K-M4SRB : 2

Power
- On  : 56
- Off : 36

Maximum
- CpuSockets          : 2
- CpuCores            : 56
- CpuThreads          : 112
- Memory              : 768
- Storage Controllers : 12
- Total Disk Capacity : 31.58 [TB]
- HDD Count           : 21
- HDD Capacity        : 25.18 [TB]
- SSD Count           : 11
- SSD Capacity        : 31.58 [TB]
- PCI Devices         : 11

Health
- Healthy  : 73
- Warning  : 7
- Critical : 12

Locator
- On  : 1
- Off : 91

Management Mode
- Standalone : 69
- UCSM       : 23

Server Fans
- All up    : 58
- Some down : 34

Server Psus
- All up    : 79
- Some down : 13

PCI Models
- Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) : 2
- Cisco UCS VIC 1457 MLOM                                          : 2
- Cisco(R) Ethernet Converged NIC XXV710-DA2                       : 4
- Intel Unknown Device                                             : 1
- Intel X550 LOM                                                   : 45
- Intel(R) I350 1 Gbps Network Controller                          : 22
- LSI MegaRAID SAS 3108                                            : 7
- N2XX-AIPCI01                                                     : 15
- SSDPE21K375GAW                                                   : 7
- SSDPE2KX010T8K                                                   : 36
- UCSC-MLOM-C100-04                                                : 1
- UCSC-MLOM-C25Q-04                                                : 25
- UCSC-MLOM-C40Q-03                                                : 9
- UCSC-MLOM-CSC-02                                                 : 26
- UCSC-MRAID12G                                                    : 22
- UCSC-NVMEHW-H1600                                                : 3
- UCSC-PCIE-C25Q-04                                                : 3
- UCSC-PCIE-CSC-02                                                 : 3
- UCSC-PCIE-ID10GF                                                 : 1
- UCSC-PCIE-ID25GF                                                 : 26
- UCSC-PCIE-ID40GF                                                 : 14
- UCSC-PCIE-IQ10GF                                                 : 60
- UCSC-RAID-M5                                                     : 33
- UCSC-RAID-M5HD                                                   : 11
- UCSC-SAS-M5HD                                                    : 3

Firmware
- 4.0(4b) : 3
- 4.0(4e) : 1
- 4.1(1f) : 1
- 4.1(2f) : 19
- 4.1(2g) : 6
- 4.1(2k) : 8
- 4.1(3b) : 2
- 4.1(3c) : 1
- 4.1(3d) : 34
- 4.1(3f) : 7
- 4.2(1c) : 8
- 4.2(2a) : 2

Last Workflows Summary
- Running                   : 1
- Success                   : 37
- Failed                    : 0
- Servers with workflows    : 1
- Servers with no workflows : 91

Workflow Names
- InstallOS                : 12
- Power Cycle              : 11
- Operating System Install : 11
- Turn Off Locator         : 2
- Turn On Locator          : 2
```
