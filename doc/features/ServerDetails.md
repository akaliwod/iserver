# Server Details

Get server's information in table, json or yaml formats.

Select server by serial, IP or name. If more than one server matches the selection criteria, an error is thrown.

Use flags to control amount of details collected from Intersight and shown on the screen. Use --all to get all details.

Note: The more details you request, the longer it takes to prepare the data.

```
# iserver get server --help
Usage: iserver.py get server [OPTIONS]

  Get server details

Options:
  --iaccount TEXT                 Intersight account  [default: isctl]
  --ip TEXT                       Management IP address
  --name TEXT                     Name loose match filter
  --serial TEXT                   Serial number
  --cpu                           Show processor units
  --memory                        Show memory units
  --fw                            Show fw info
  --fan                           Show fan units
  --psu                           Show psu units
  --storage                       Show storage details
  --pci                           Show pci details
  --all                           Show all details
  --days INTEGER                  Last <n> days workflows
  -o, --output [default|json|yaml]
                                  [default: default]
  --flat                          Flat output
  --devel                         Developer output
  --help                          Show this message and exit.
```

## Basic output

```
# iserver get server
    --name aio-2-p2b-eu-spdc-WZP23400AK4
    --flat
Identity
- Server ID : 5fdf9c786176752d35e47110
- Name      : aio-2-p2b-eu-spdc-WZP23400AK4
- Type      : Rack
- Model     : UCSC-C240-M5SN
- Serial    : WZP23400AK4
- IP        : 10.58.50.42


State
- Power    : on
- Health   : Healthy
- Mode     : IntersightStandalone


CPU and Memory
- CPU Sockets   : 2
- Threads       : 80
- Cores         : 40
- Enabled Cores : 40
- Memory        : 384 [GiB]


No workflows
```

## All details

```
# iserver get server
    --name aio-2-p2b-eu-spdc-WZP23400AK4
    --flat
    --all
Identity
- Server ID : 5fdf9c786176752d35e47110
- Name      : aio-2-p2b-eu-spdc-WZP23400AK4
- Type      : Rack
- Model     : UCSC-C240-M5SN
- Serial    : WZP23400AK4
- IP        : 10.58.50.42


State
- Power    : on
- Health   : Healthy
- Mode     : IntersightStandalone
- Firmware : 4.1(3d)
- PSU      : 2/2
- Fan      : 6/7


CPU and Memory
- CPU Sockets   : 2
- Threads       : 80
- Cores         : 40
- Enabled Cores : 40
- Memory        : 384 [GiB]


Storage
- Controllers    : 1
- Disks count    : 10
- Disks capacity : 11.03 [TB]
- HDD count      : 6
- HDD capacity   : 7.19 [TB]
- SSD count      : 4
- SSD capacity   : 3.84 [TB]
- Virtual Disks  : 1


+---------------+---------+-----------------------+-------+-------------------------------------------+-----------+------------+--------+----------------+----------+--------+-----------+
| Processor Id  | Socket  | Vendor                | Arch  | Model                                     | Presence  | OperState  | Cores  | Cores Enabled  | Threads  | Speed  | Stepping  |
+---------------+---------+-----------------------+-------+-------------------------------------------+-----------+------------+--------+----------------+----------+--------+-----------+
| 1             | CPU1    | Intel(R) Corporation  | Xeon  | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz  | equipped  | operable   | 20     | 20             | 40       | 2.5    | 7         | 
| 2             | CPU2    | Intel(R) Corporation  | Xeon  | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz  | equipped  | operable   | 20     | 20             | 40       | 2.5    | 7         | 
+---------------+---------+-----------------------+-------+-------------------------------------------+-----------+------------+--------+----------------+----------+--------+-----------+

+------------+--------+-------+-----------+--------------+--------------+---------------+---------------+-----------------------+-----------+-------------+-----------+
| Memory Id  | Array  | Bank  | Location  | Capacity     | Clock        | Form Factor   | Type          | Model                 | Serial    | Oper State  | Presence  |
+------------+--------+-------+-----------+--------------+--------------+---------------+---------------+-----------------------+-----------+-------------+-----------+
| 1          | 1      | 0     | DIMM_A1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F736F1  | operable    | equipped  | 
| 2          | 1      | 0     | DIMM_A2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 3          | 1      | 0     | DIMM_B1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F7370D  | operable    | equipped  | 
| 4          | 1      | 0     | DIMM_B2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 5          | 1      | 0     | DIMM_C1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F736F9  | operable    | equipped  | 
| 6          | 1      | 0     | DIMM_C2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 7          | 1      | 0     | DIMM_D1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F73709  | operable    | equipped  | 
| 8          | 1      | 0     | DIMM_D2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 9          | 1      | 0     | DIMM_E1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F736F7  | operable    | equipped  | 
| 10         | 1      | 0     | DIMM_E2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 11         | 1      | 0     | DIMM_F1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F7370A  | operable    | equipped  | 
| 12         | 1      | 0     | DIMM_F2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 13         | 1      | 0     | DIMM_G1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F736F8  | operable    | equipped  | 
| 14         | 1      | 0     | DIMM_G2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 15         | 1      | 0     | DIMM_H1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F736ED  | operable    | equipped  | 
| 16         | 1      | 0     | DIMM_H2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 17         | 1      | 0     | DIMM_J1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F736F6  | operable    | equipped  | 
| 18         | 1      | 0     | DIMM_J2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 19         | 1      | 0     | DIMM_K1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0EFB85E  | operable    | equipped  | 
| 20         | 1      | 0     | DIMM_K2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 21         | 1      | 0     | DIMM_L1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F72BFA  | operable    | equipped  | 
| 22         | 1      | 0     | DIMM_L2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
| 23         | 1      | 0     | DIMM_M1   | 32768        | 2933         | DIMM          | DDR4          | 36ASF4G72PZ-2G9E2     | F0F72BFE  | operable    | equipped  | 
| 24         | 1      | 0     | DIMM_M2   | unspecified  | unspecified  | undiscovered  | undiscovered  |                       |           | removed     | missing   | 
+------------+--------+-------+-----------+--------------+--------------+---------------+---------------+-----------------------+-----------+-------------+-----------+

Storage Controller
- Model                : Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)
- Vendor               : LSI Logic
- Serial               : SK00481450
- Presence             : equipped
- Pci Slot             : MRAID
- Controller Id        : MRAID
- Dn                   : sys/rack-unit-1/board/storage-SAS-MRAID
- Raid Support         : yes


+-------------------+--------+-------------+-----------+-----------------+----------+-------+-------------+-----+------------------------------------------------+
| Physical Disk Id  | State  | Size        | Presence  | Model           | Vendor   | Type  | Controller  | VD  | Dn                                             |
+-------------------+--------+-------------+-----------+-----------------+----------+-------+-------------+-----+------------------------------------------------+
| 10                | Good   | 914573 MB   | equipped  | SSDSC2KB960G7K  | ATA      | SSD   | MRAID       | 0   | sys/rack-unit-1/board/storage-SAS-MRAID/pd-10  | 
| 11                | Good   | 914573 MB   | equipped  | SSDSC2KB960G7K  | ATA      | SSD   | MRAID       |     | sys/rack-unit-1/board/storage-SAS-MRAID/pd-11  | 
| 12                | Good   | 914573 MB   | equipped  | SSDSC2KB960G7K  | ATA      | SSD   | MRAID       |     | sys/rack-unit-1/board/storage-SAS-MRAID/pd-12  | 
| 13                | Good   | 1143455 MB  | equipped  | ST1200MM0009    | SEAGATE  | HDD   | MRAID       |     | sys/rack-unit-1/board/storage-SAS-MRAID/pd-13  | 
| 14                | Good   | 1143455 MB  | equipped  | ST1200MM0009    | SEAGATE  | HDD   | MRAID       |     | sys/rack-unit-1/board/storage-SAS-MRAID/pd-14  | 
| 15                | Good   | 1143455 MB  | equipped  | ST1200MM0009    | SEAGATE  | HDD   | MRAID       |     | sys/rack-unit-1/board/storage-SAS-MRAID/pd-15  | 
| 16                | Good   | 1143455 MB  | equipped  | ST1200MM0009    | SEAGATE  | HDD   | MRAID       |     | sys/rack-unit-1/board/storage-SAS-MRAID/pd-16  | 
| 17                | Good   | 1143455 MB  | equipped  | ST1200MM0009    | SEAGATE  | HDD   | MRAID       |     | sys/rack-unit-1/board/storage-SAS-MRAID/pd-17  | 
| 18                | Good   | 1143455 MB  | equipped  | ST1200MM0088    | SEAGATE  | HDD   | MRAID       |     | sys/rack-unit-1/board/storage-SAS-MRAID/pd-18  | 
| 9                 | Good   | 914573 MB   | equipped  | SSDSC2KB960G7K  | ATA      | SSD   | MRAID       | 0   | sys/rack-unit-1/board/storage-SAS-MRAID/pd-9   | 
+-------------------+--------+-------------+-----------+-----------------+----------+-------+-------------+-----+------------------------------------------------+

+-------------------+-------------+-----------------+---------+------------+-------------+-----------------------------------------------+
| Virtual Drive Id  | Size        | Physical Disks  | Type    | Name       | Controller  | Dn                                            |
+-------------------+-------------+-----------------+---------+------------+-------------+-----------------------------------------------+
| 0                 | 1829146 MB  | 2               | RAID 0  | RAID0_910  | MRAID       | sys/rack-unit-1/board/storage-SAS-MRAID/vd-0  | 
+-------------------+-------------+-----------------+---------+------------+-------------+-----------------------------------------------+

+-------------------------------------------------------------------+--------------------+---------+---------+---------------------+--------------------------------------+
| PCI Device Model                                                  | Pid                | SlotId  | Vendor  | Firmware            | Dn                                   |
+-------------------------------------------------------------------+--------------------+---------+---------+---------------------+--------------------------------------+
| Cisco(R) Ethernet Converged NIC XXV710-DA2                        | UCSC-PCIE-ID25GF   | 3       | 0x8086  | 0x80009E5D-1.823.2  | sys/rack-unit-1/equipped-slot-3      | 
| Cisco(R) Ethernet Converged NIC XXV710-DA2                        | UCSC-PCIE-ID25GF   | 6       | 0x8086  | 0x80009E5D-1.823.2  | sys/rack-unit-1/equipped-slot-6      | 
| Intel X550 LOM                                                    | UNKNOWN            | L       | 0x8086  | 0x80001516-1.823.2  | sys/rack-unit-1/equipped-slot-L      | 
| Cisco UCS VIC 1457 MLOM                                           | UCSC-MLOM-C25Q-04  | MLOM    | 0x1137  | 5.1(3d)             | sys/rack-unit-1/equipped-slot-MLOM   | 
| Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)  | UCSC-RAID-M5       | MRAID   | 0x1000  | 51.10.0-3612        | sys/rack-unit-1/equipped-slot-MRAID  | 
+-------------------------------------------------------------------+--------------------+---------+---------+---------------------+--------------------------------------+

+----------------+------------+-----------+---------------------------------+
| Fan Module Id  | OperState  | Presence  | Dn                              |
+----------------+------------+-----------+---------------------------------+
| 1              | operable   | equipped  | sys/rack-unit-1/fan-module-1-1  | 
| 2              | operable   | equipped  | sys/rack-unit-1/fan-module-1-2  | 
| 3              | operable   | equipped  | sys/rack-unit-1/fan-module-1-3  | 
| 4              | operable   | equipped  | sys/rack-unit-1/fan-module-1-4  | 
| 5              | operable   | equipped  | sys/rack-unit-1/fan-module-1-5  | 
| 6              | operable   | equipped  | sys/rack-unit-1/fan-module-1-6  | 
| 7              | unknown    | missing   | sys/rack-unit-1/fan-module-1-7  | 
+----------------+------------+-----------+---------------------------------+

+----------------+--------------+--------------------+------------------------+
| PSU Model      | Serial       | Vendor             | Dn                     |
+----------------+--------------+--------------------+------------------------+
| PS-2112-9S-LF  | LIT241244RQ  | Cisco Systems Inc  | sys/rack-unit-1/psu-1  | 
| PS-2112-9S-LF  | LIT241242TS  | Cisco Systems Inc  | sys/rack-unit-1/psu-2  | 
+----------------+--------------+--------------------+------------------------+

No workflows
```

## JSON output

```
# iserver get server
    --name aio-2-p2b-eu-spdc-WZP23400AK4
    --all -o json
{
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Adapters": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c6b6176752d35e46d1c",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9c6b6176752d35e46d1c"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cfe6176752d35e4aa7f",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa7f"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cfe6176752d35e4aa85",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa85"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cfe6176752d35e4aa8b",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa8b"
        }
    ],
    "AdminPowerState": "policy",
    "AlarmSummary": {
        "ClassId": "compute.AlarmSummary",
        "Critical": 0,
        "ObjectType": "compute.AlarmSummary",
        "Warning": 0
    },
    "Alerts": [],
    "Ancestors": [],
    "AssetTag": "022C2F7",
    "AvailableMemory": 393216,
    "BiosBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c756176752d35e4704d",
        "ObjectType": "bios.BootMode",
        "link": "https://www.intersight.com/api/v1/bios/BootModes/5fdf9c756176752d35e4704d"
    },
    "BiosPostComplete": false,
    "BiosTokenSettings": null,
    "BiosVfSelectMemoryRasConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "60d5ee256176752d359b9914",
        "ObjectType": "bios.VfSelectMemoryRasConfiguration",
        "link": "https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5ee256176752d359b9914"
    },
    "Biosunits": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c736176752d35e46f8c",
            "ObjectType": "bios.Unit",
            "link": "https://www.intersight.com/api/v1/bios/Units/5fdf9c736176752d35e46f8c"
        }
    ],
    "Bmc": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9cb86176752d35e48ebd",
        "ObjectType": "management.Controller",
        "link": "https://www.intersight.com/api/v1/management/Controllers/5fdf9cb86176752d35e48ebd"
    },
    "Board": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c7c6176752d35e472bd",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/5fdf9c7c6176752d35e472bd"
    },
    "BootCddDevices": [],
    "BootDeviceBootSecurity": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9ca56176752d35e4844f",
        "ObjectType": "boot.DeviceBootSecurity",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9ca56176752d35e4844f"
    },
    "BootDeviceBootmode": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9ca46176752d35e483e0",
        "ObjectType": "boot.DeviceBootMode",
        "link": "https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9ca46176752d35e483e0"
    },
    "BootHddDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000c066176752d35b76c32",
            "ObjectType": "boot.HddDevice",
            "link": "https://www.intersight.com/api/v1/boot/HddDevices/60000c066176752d35b76c32"
        }
    ],
    "BootIscsiDevices": [],
    "BootNvmeDevices": [],
    "BootPchStorageDevices": [],
    "BootPxeDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "60000bff6176752d35b769c9",
            "ObjectType": "boot.PxeDevice",
            "link": "https://www.intersight.com/api/v1/boot/PxeDevices/60000bff6176752d35b769c9"
        }
    ],
    "BootSanDevices": [],
    "BootSdDevices": [],
    "BootUefiShellDevices": [],
    "BootUsbDevices": [],
    "BootVmediaDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "6013f1466176752d35458cdb",
            "ObjectType": "boot.VmediaDevice",
            "link": "https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1466176752d35458cdb"
        }
    ],
    "ClassId": "compute.RackUnit",
    "ConnectionStatus": "",
    "CreateTime": "2020-12-20T18:48:24.465Z",
    "DeviceMoId": "5fdf9c676f72612d300a9c8d",
    "Dn": "sys/rack-unit-1",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "Fanmodules": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e4777c",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e4777c"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e4777e",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e4777e"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47780",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47780"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47782",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47782"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47784",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47784"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47786",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47786"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c876176752d35e47788",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47788"
        }
    ],
    "FaultSummary": 0,
    "GenericInventoryHolders": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9cf66176752d35e4a75b",
            "ObjectType": "inventory.GenericInventoryHolder",
            "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9cf66176752d35e4a75b"
        }
    ],
    "GraphicsCards": [],
    "HardwareUuid": "",
    "InventoryDeviceInfo": null,
    "KvmIpAddresses": [
        {
            "Address": "10.58.50.42",
            "Category": "Equipment",
            "ClassId": "compute.IpAddress",
            "DefaultGateway": "10.58.50.62",
            "Dn": "sys/rack-unit-1/mgmt/if-1",
            "HttpPort": 80,
            "HttpsPort": 443,
            "KvmPort": 2068,
            "KvmVlan": 1,
            "Name": "Outband",
            "ObjectType": "compute.IpAddress",
            "Subnet": "255.255.255.224",
            "Type": "MgmtInterface"
        }
    ],
    "KvmServerStateEnabled": false,
    "KvmVendor": "Avocent",
    "LocatorLed": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c8b6176752d35e47959",
        "ObjectType": "equipment.LocatorLed",
        "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdf9c8b6176752d35e47959"
    },
    "ManagementMode": "IntersightStandalone",
    "MemoryArrays": [],
    "MemorySpeed": "2933",
    "MgmtIdentity": null,
    "MgmtIpAddress": "10.58.50.42",
    "ModTime": "2022-09-28T08:19:26.75Z",
    "Model": "UCSC-C240-M5SN",
    "Moid": "5fdf9c786176752d35e47110",
    "Name": "aio-2-p2b-eu-spdc-WZP23400AK4",
    "NumAdaptors": 1,
    "NumCpuCores": 40,
    "NumCpuCoresEnabled": 40,
    "NumCpus": 2,
    "NumEthHostInterfaces": 2,
    "NumFcHostInterfaces": 2,
    "NumThreads": 80,
    "ObjectType": "compute.RackUnit",
    "OperPowerState": "on",
    "OperReason": [],
    "OperState": "",
    "Operability": "",
    "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "5fdf9c676f72612d300a9c8d"
    ],
    "PciDevices": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496d1",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d1"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496d3",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d3"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496d5",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d5"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496d7",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d7"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9ccb6176752d35e496da",
            "ObjectType": "pci.Device",
            "link": "https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496da"
        }
    ],
    "PermissionResources": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736972652d321d26b5",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "625706a06972652d3202a8f9",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "6242d1016972652d32eda017",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
        }
    ],
    "PlatformType": "IMCM5",
    "Presence": "equipped",
    "PreviousFru": null,
    "Processors": [],
    "Psus": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c856176752d35e476b8",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c856176752d35e476b8"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c856176752d35e476ba",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/5fdf9c856176752d35e476ba"
        }
    ],
    "RackEnclosureSlot": null,
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9c676f72612d300a9c8d",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9c676f72612d300a9c8d"
    },
    "Revision": "",
    "Rn": "",
    "SasExpanders": [],
    "Serial": "WZP23400AK4",
    "ServerId": 1,
    "ServiceProfile": "",
    "SharedScope": "",
    "StorageControllers": [],
    "StorageEnclosures": [],
    "Tags": [
        {
            "Key": "Intersight.LicenseTier",
            "Value": "Premier"
        }
    ],
    "TopSystem": {
        "ClassId": "mo.MoRef",
        "Moid": "5fdf9cc96176752d35e49601",
        "ObjectType": "top.System",
        "link": "https://www.intersight.com/api/v1/top/Systems/5fdf9cc96176752d35e49601"
    },
    "TopologyScanStatus": "",
    "TotalMemory": 393216,
    "TunneledKvm": false,
    "UnitPersonality": [],
    "UserLabel": "aio-2-p2b-eu-spdc-WZP23400AK4",
    "Uuid": "B813910F-BFD2-439F-9C3B-75B376C5B160",
    "Vendor": "Cisco Systems Inc",
    "Vmedia": null,
    "ManagementIp": "10.58.50.42",
    "Cpu": "2S 40C 80T",
    "Health": "Healthy",
    "TotalMemoryUnit": "384 [GiB]",
    "TotalMemoryGB": 384,
    "Groups": "p2b,pod2b,pods",
    "WorkflowRunning": null,
    "WorkflowLast": null,
    "WorkflowsLast": [],
    "WorkflowsLastIds": [],
    "WorkflowsLastFailedIds": [],
    "Type": "Rack",
    "CpuInfo": [
        {
            "Architecture": "Xeon",
            "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
            "NumCores": 20,
            "NumCoresEnabled": "20",
            "NumThreads": "40",
            "OperState": "operable",
            "Presence": "equipped",
            "ProcessorId": 1,
            "SocketDesignation": "CPU1",
            "Speed": 2.5,
            "Stepping": "7",
            "Vendor": "Intel(R) Corporation"
        },
        {
            "Architecture": "Xeon",
            "Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
            "NumCores": 20,
            "NumCoresEnabled": "20",
            "NumThreads": "40",
            "OperState": "operable",
            "Presence": "equipped",
            "ProcessorId": 2,
            "SocketDesignation": "CPU2",
            "Speed": 2.5,
            "Stepping": "7",
            "Vendor": "Intel(R) Corporation"
        }
    ],
    "MemoryInfo": [
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-1",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_A1",
            "MemoryId": 1,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F736F1",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-2",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_A2",
            "MemoryId": 2,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-3",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_B1",
            "MemoryId": 3,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F7370D",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-4",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_B2",
            "MemoryId": 4,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-5",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_C1",
            "MemoryId": 5,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F736F9",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-6",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_C2",
            "MemoryId": 6,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-7",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_D1",
            "MemoryId": 7,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F73709",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-8",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_D2",
            "MemoryId": 8,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-9",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_E1",
            "MemoryId": 9,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F736F7",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-10",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_E2",
            "MemoryId": 10,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-11",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_F1",
            "MemoryId": 11,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F7370A",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-12",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_F2",
            "MemoryId": 12,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-13",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_G1",
            "MemoryId": 13,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F736F8",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-14",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_G2",
            "MemoryId": 14,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-15",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_H1",
            "MemoryId": 15,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F736ED",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-16",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_H2",
            "MemoryId": 16,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-17",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_J1",
            "MemoryId": 17,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F736F6",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-18",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_J2",
            "MemoryId": 18,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-19",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_K1",
            "MemoryId": 19,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0EFB85E",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-20",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_K2",
            "MemoryId": 20,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-21",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_L1",
            "MemoryId": 21,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F72BFA",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-22",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_L2",
            "MemoryId": 22,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "32768",
            "Clock": "2933",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-23",
            "FormFactor": "DIMM",
            "Latency": "",
            "Location": "DIMM_M1",
            "MemoryId": 23,
            "Model": "36ASF4G72PZ-2G9E2   ",
            "OperState": "operable",
            "Presence": "equipped",
            "Serial": "F0F72BFE",
            "Speed": "",
            "Type": "DDR4",
            "Vendor": "0x2C00"
        },
        {
            "ArrayId": 1,
            "Bank": 0,
            "Capacity": "unspecified",
            "Clock": "unspecified",
            "Dn": "sys/rack-unit-1/board/memarray-1/mem-24",
            "FormFactor": "undiscovered",
            "Latency": "",
            "Location": "DIMM_M2",
            "MemoryId": 24,
            "Model": "",
            "OperState": "removed",
            "Presence": "missing",
            "Serial": "",
            "Speed": "",
            "Type": "undiscovered",
            "Vendor": ""
        }
    ],
    "FanInfo": [
        {
            "ModuleId": 1,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-1"
        },
        {
            "ModuleId": 2,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-2"
        },
        {
            "ModuleId": 3,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-3"
        },
        {
            "ModuleId": 4,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-4"
        },
        {
            "ModuleId": 5,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-5"
        },
        {
            "ModuleId": 6,
            "OperState": "operable",
            "Presence": "equipped",
            "Dn": "sys/rack-unit-1/fan-module-1-6"
        },
        {
            "ModuleId": 7,
            "OperState": "unknown",
            "Presence": "missing",
            "Dn": "sys/rack-unit-1/fan-module-1-7"
        }
    ],
    "FanOn": 6,
    "FanCount": 7,
    "FanSummary": "6/7",
    "FanHealthy": false,
    "PsuInfo": [
        {
            "Model": "PS-2112-9S-LF",
            "Serial": "LIT241244RQ",
            "Vendor": "Cisco Systems Inc",
            "Dn": "sys/rack-unit-1/psu-1"
        },
        {
            "Model": "PS-2112-9S-LF",
            "Serial": "LIT241242TS",
            "Vendor": "Cisco Systems Inc",
            "Dn": "sys/rack-unit-1/psu-2"
        }
    ],
    "PsuOn": 2,
    "PsuCount": 2,
    "PsuSummary": "2/2",
    "PsuHealthy": true,
    "PciDevicesInfo": [
        {
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "Pid": "UCSC-PCIE-ID25GF",
            "SlotId": "3",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x80009E5D-1.823.2",
            "Dn": "sys/rack-unit-1/equipped-slot-3"
        },
        {
            "Model": "Cisco(R) Ethernet Converged NIC XXV710-DA2",
            "Pid": "UCSC-PCIE-ID25GF",
            "SlotId": "6",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x80009E5D-1.823.2",
            "Dn": "sys/rack-unit-1/equipped-slot-6"
        },
        {
            "Model": "Intel X550 LOM",
            "Pid": "UNKNOWN",
            "SlotId": "L",
            "Vendor": "0x8086",
            "FirmwareVersion": "0x80001516-1.823.2",
            "Dn": "sys/rack-unit-1/equipped-slot-L"
        },
        {
            "Model": "Cisco UCS VIC 1457 MLOM",
            "Pid": "UCSC-MLOM-C25Q-04",
            "SlotId": "MLOM",
            "Vendor": "0x1137",
            "FirmwareVersion": "5.1(3d)",
            "Dn": "sys/rack-unit-1/equipped-slot-MLOM"
        },
        {
            "Model": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "Pid": "UCSC-RAID-M5",
            "SlotId": "MRAID",
            "Vendor": "0x1000",
            "FirmwareVersion": "51.10.0-3612",
            "Dn": "sys/rack-unit-1/equipped-slot-MRAID"
        }
    ],
    "PciModels": [
        "UCSC-PCIE-ID25GF",
        "UCSC-PCIE-ID25GF",
        "UCSC-MLOM-C25Q-04",
        "UCSC-RAID-M5",
        "Intel X550 LOM"
    ],
    "Fw": "4.1(3d)",
    "StorageControllersInfo": [
        {
            "Model": "Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)",
            "Moid": "5fdf9cd46176752d35e4998e",
            "Vendor": "LSI Logic",
            "Serial": "SK00481450",
            "Presence": "equipped",
            "PciSlot": "MRAID",
            "ControllerId": "MRAID",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID",
            "RaidSupport": "yes",
            "PhysicalDiskCount": 10,
            "PhysicalDiskIds": [
                "6166890f76752d3139384892",
                "6166890f76752d31393848bd",
                "6166891076752d31393848f3",
                "6166891076752d3139384913",
                "6166891076752d3139384924",
                "6166891076752d3139384935",
                "6166891076752d3139384947",
                "6166891076752d3139384958",
                "6166891176752d313938496a",
                "6166891176752d3139384985"
            ],
            "VirtualDriveCount": 1,
            "VirtualDriveIds": [
                "6166891176752d31393849a7"
            ]
        }
    ],
    "StorageControllersCount": 1,
    "VirtualDisks": [
        {
            "Moid": "6166891176752d31393849a7",
            "Name": "RAID0_910",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/vd-0",
            "Size": "1829146 MB",
            "Type": "RAID 0",
            "VirtualDriveId": "0",
            "PhysicalDiskCount": 2,
            "StorageControllerId": "MRAID",
            "PhysicalDiskIds": [
                "9",
                "10"
            ]
        }
    ],
    "VirtualDiskCount": 1,
    "VirtualDiskCapacity": 1917998596096,
    "VirtualDiskCapacityUnit": "1.92 [TB]",
    "HddDisks": [
        {
            "Moid": "6166891076752d3139384924",
            "DiskId": "13",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-13",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65JQF0000C0259760",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d3139384935",
            "DiskId": "14",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-14",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65LZ70000C02597DN",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d3139384947",
            "DiskId": "15",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-15",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65LD10000C024KKJM",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d3139384958",
            "DiskId": "16",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-16",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK64DPD0000C0244K8B",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891176752d313938496a",
            "DiskId": "17",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-17",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK64DX60000C025BW6X",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891176752d3139384985",
            "DiskId": "18",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-18",
            "DriveFirmware": "N0A4",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0088",
            "Pid": "ST1200MM0088",
            "Presence": "equipped",
            "Serial": "Z4000FFD0000R616HPN9",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        }
    ],
    "HddDiskCount": 6,
    "HddDiskCapacity": 7193996820480,
    "HddDiskCapacityUnit": "7.19 [TB]",
    "SsdDisks": [
        {
            "Moid": "6166890f76752d31393848bd",
            "DiskId": "10",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-10",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "Online",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002M1960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": "6166891176752d31393849a7",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d31393848f3",
            "DiskId": "11",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-11",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002ME960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d3139384913",
            "DiskId": "12",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-12",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746003DM960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166890f76752d3139384892",
            "DiskId": "9",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-9",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "Online",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746100ZW960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": "6166891176752d31393849a7",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID"
        }
    ],
    "SsdDiskCount": 4,
    "SsdDiskCapacity": 3835997192192,
    "SsdDiskCapacityUnit": "3.84 [TB]",
    "PhysicalDisks": [
        {
            "Moid": "6166890f76752d31393848bd",
            "DiskId": "10",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-10",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "Online",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002M1960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": "6166891176752d31393849a7",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d31393848f3",
            "DiskId": "11",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-11",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746002ME960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d3139384913",
            "DiskId": "12",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-12",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "JBOD",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746003DM960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d3139384924",
            "DiskId": "13",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-13",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65JQF0000C0259760",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d3139384935",
            "DiskId": "14",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-14",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65LZ70000C02597DN",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d3139384947",
            "DiskId": "15",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-15",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK65LD10000C024KKJM",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891076752d3139384958",
            "DiskId": "16",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-16",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK64DPD0000C0244K8B",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891176752d313938496a",
            "DiskId": "17",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-17",
            "DriveFirmware": "CN03",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0009",
            "Pid": "ST1200MM0009",
            "Presence": "equipped",
            "Serial": "WFK64DX60000C025BW6X",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166891176752d3139384985",
            "DiskId": "18",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-18",
            "DriveFirmware": "N0A4",
            "DriveState": "JBOD",
            "LinkSpeed": "12.0 Gb/s",
            "Model": "ST1200MM0088",
            "Pid": "ST1200MM0088",
            "Presence": "equipped",
            "Serial": "Z4000FFD0000R616HPN9",
            "Size": "1143455 MB",
            "Type": "HDD",
            "Vendor": "SEAGATE",
            "VirtualDriveMoid": null,
            "VirtualDriveId": "",
            "StorageControllerId": "MRAID"
        },
        {
            "Moid": "6166890f76752d3139384892",
            "DiskId": "9",
            "DiskState": "Good",
            "Dn": "sys/rack-unit-1/board/storage-SAS-MRAID/pd-9",
            "DriveFirmware": "SCV1CS08",
            "DriveState": "Online",
            "LinkSpeed": "6.0 Gb/s",
            "Model": "SSDSC2KB960G7K",
            "Pid": "SSDSC2KB960G7K",
            "Presence": "equipped",
            "Serial": "PHYS746100ZW960CGN",
            "Size": "914573 MB",
            "Type": "SSD",
            "Vendor": "ATA",
            "VirtualDriveMoid": "6166891176752d31393849a7",
            "VirtualDriveId": "0",
            "StorageControllerId": "MRAID"
        }
    ],
    "PhysicalDiskCount": 10,
    "PhysicalDiskCapacity": 11029994012672,
    "PhysicalDiskCapacityUnit": "11.03 [TB]",
    "StorageDrives": "1C 6H 4S 1VD",
    "StorageCapacity": "R 11.03 [TB] , VD 1.92 [TB]",
    "StorageSummary": "1C 6H 4S 1VD R11.03 [TB] L1.92 [TB]",
    "State": "P+HRS"
}
```

## YAML output

```
# iserver get server
    --name aio-2-p2b-eu-spdc-WZP23400AK4
    --all -o yaml
AccountMoid: 5be4b2ce67626c6d661ca38d
Adapters:
- ClassId: mo.MoRef
  Moid: 5fdf9c6b6176752d35e46d1c
  ObjectType: adapter.Unit
  link: https://www.intersight.com/api/v1/adapter/Units/5fdf9c6b6176752d35e46d1c
- ClassId: mo.MoRef
  Moid: 5fdf9cfe6176752d35e4aa7f
  ObjectType: adapter.Unit
  link: https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa7f
- ClassId: mo.MoRef
  Moid: 5fdf9cfe6176752d35e4aa85
  ObjectType: adapter.Unit
  link: https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa85
- ClassId: mo.MoRef
  Moid: 5fdf9cfe6176752d35e4aa8b
  ObjectType: adapter.Unit
  link: https://www.intersight.com/api/v1/adapter/Units/5fdf9cfe6176752d35e4aa8b
AdminPowerState: policy
AlarmSummary:
  ClassId: compute.AlarmSummary
  Critical: 0
  ObjectType: compute.AlarmSummary
  Warning: 0
Alerts: []
Ancestors: []
AssetTag: 022C2F7
AvailableMemory: 393216
BiosBootmode:
  ClassId: mo.MoRef
  Moid: 5fdf9c756176752d35e4704d
  ObjectType: bios.BootMode
  link: https://www.intersight.com/api/v1/bios/BootModes/5fdf9c756176752d35e4704d
BiosPostComplete: false
BiosTokenSettings: null
BiosVfSelectMemoryRasConfiguration:
  ClassId: mo.MoRef
  Moid: 60d5ee256176752d359b9914
  ObjectType: bios.VfSelectMemoryRasConfiguration
  link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5ee256176752d359b9914
Biosunits:
- ClassId: mo.MoRef
  Moid: 5fdf9c736176752d35e46f8c
  ObjectType: bios.Unit
  link: https://www.intersight.com/api/v1/bios/Units/5fdf9c736176752d35e46f8c
Bmc:
  ClassId: mo.MoRef
  Moid: 5fdf9cb86176752d35e48ebd
  ObjectType: management.Controller
  link: https://www.intersight.com/api/v1/management/Controllers/5fdf9cb86176752d35e48ebd
Board:
  ClassId: mo.MoRef
  Moid: 5fdf9c7c6176752d35e472bd
  ObjectType: compute.Board
  link: https://www.intersight.com/api/v1/compute/Boards/5fdf9c7c6176752d35e472bd
BootCddDevices: []
BootDeviceBootSecurity:
  ClassId: mo.MoRef
  Moid: 5fdf9ca56176752d35e4844f
  ObjectType: boot.DeviceBootSecurity
  link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9ca56176752d35e4844f
BootDeviceBootmode:
  ClassId: mo.MoRef
  Moid: 5fdf9ca46176752d35e483e0
  ObjectType: boot.DeviceBootMode
  link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9ca46176752d35e483e0
BootHddDevices:
- ClassId: mo.MoRef
  Moid: 60000c066176752d35b76c32
  ObjectType: boot.HddDevice
  link: https://www.intersight.com/api/v1/boot/HddDevices/60000c066176752d35b76c32
BootIscsiDevices: []
BootNvmeDevices: []
BootPchStorageDevices: []
BootPxeDevices:
- ClassId: mo.MoRef
  Moid: 60000bff6176752d35b769c9
  ObjectType: boot.PxeDevice
  link: https://www.intersight.com/api/v1/boot/PxeDevices/60000bff6176752d35b769c9
BootSanDevices: []
BootSdDevices: []
BootUefiShellDevices: []
BootUsbDevices: []
BootVmediaDevices:
- ClassId: mo.MoRef
  Moid: 6013f1466176752d35458cdb
  ObjectType: boot.VmediaDevice
  link: https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1466176752d35458cdb
ClassId: compute.RackUnit
ConnectionStatus: ''
Cpu: 2S 40C 80T
CpuInfo:
- Architecture: Xeon
  Model: Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz
  NumCores: 20
  NumCoresEnabled: '20'
  NumThreads: '40'
  OperState: operable
  Presence: equipped
  ProcessorId: 1
  SocketDesignation: CPU1
  Speed: 2.5
  Stepping: '7'
  Vendor: Intel(R) Corporation
- Architecture: Xeon
  Model: Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz
  NumCores: 20
  NumCoresEnabled: '20'
  NumThreads: '40'
  OperState: operable
  Presence: equipped
  ProcessorId: 2
  SocketDesignation: CPU2
  Speed: 2.5
  Stepping: '7'
  Vendor: Intel(R) Corporation
CreateTime: '2020-12-20T18:48:24.465Z'
DeviceMoId: 5fdf9c676f72612d300a9c8d
Dn: sys/rack-unit-1
DomainGroupMoid: 5be4b2ce67626c6d661ca39c
FanCount: 7
FanHealthy: false
FanInfo:
- Dn: sys/rack-unit-1/fan-module-1-1
  ModuleId: 1
  OperState: operable
  Presence: equipped
- Dn: sys/rack-unit-1/fan-module-1-2
  ModuleId: 2
  OperState: operable
  Presence: equipped
- Dn: sys/rack-unit-1/fan-module-1-3
  ModuleId: 3
  OperState: operable
  Presence: equipped
- Dn: sys/rack-unit-1/fan-module-1-4
  ModuleId: 4
  OperState: operable
  Presence: equipped
- Dn: sys/rack-unit-1/fan-module-1-5
  ModuleId: 5
  OperState: operable
  Presence: equipped
- Dn: sys/rack-unit-1/fan-module-1-6
  ModuleId: 6
  OperState: operable
  Presence: equipped
- Dn: sys/rack-unit-1/fan-module-1-7
  ModuleId: 7
  OperState: unknown
  Presence: missing
FanOn: 6
FanSummary: 6/7
Fanmodules:
- ClassId: mo.MoRef
  Moid: 5fdf9c876176752d35e4777c
  ObjectType: equipment.FanModule
  link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e4777c
- ClassId: mo.MoRef
  Moid: 5fdf9c876176752d35e4777e
  ObjectType: equipment.FanModule
  link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e4777e
- ClassId: mo.MoRef
  Moid: 5fdf9c876176752d35e47780
  ObjectType: equipment.FanModule
  link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47780
- ClassId: mo.MoRef
  Moid: 5fdf9c876176752d35e47782
  ObjectType: equipment.FanModule
  link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47782
- ClassId: mo.MoRef
  Moid: 5fdf9c876176752d35e47784
  ObjectType: equipment.FanModule
  link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47784
- ClassId: mo.MoRef
  Moid: 5fdf9c876176752d35e47786
  ObjectType: equipment.FanModule
  link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47786
- ClassId: mo.MoRef
  Moid: 5fdf9c876176752d35e47788
  ObjectType: equipment.FanModule
  link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c876176752d35e47788
FaultSummary: 0
Fw: 4.1(3d)
GenericInventoryHolders:
- ClassId: mo.MoRef
  Moid: 5fdf9cf66176752d35e4a75b
  ObjectType: inventory.GenericInventoryHolder
  link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9cf66176752d35e4a75b
GraphicsCards: []
Groups: p2b,pod2b,pods
HardwareUuid: ''
HddDiskCapacity: 7193996820480
HddDiskCapacityUnit: 7.19 [TB]
HddDiskCount: 6
HddDisks:
- DiskId: '13'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-13
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891076752d3139384924
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK65JQF0000C0259760
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '14'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-14
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891076752d3139384935
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK65LZ70000C02597DN
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '15'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-15
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891076752d3139384947
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK65LD10000C024KKJM
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '16'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-16
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891076752d3139384958
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK64DPD0000C0244K8B
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '17'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-17
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891176752d313938496a
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK64DX60000C025BW6X
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '18'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-18
  DriveFirmware: N0A4
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0088
  Moid: 6166891176752d3139384985
  Pid: ST1200MM0088
  Presence: equipped
  Serial: Z4000FFD0000R616HPN9
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
Health: Healthy
InventoryDeviceInfo: null
KvmIpAddresses:
- Address: 10.58.50.42
  Category: Equipment
  ClassId: compute.IpAddress
  DefaultGateway: 10.58.50.62
  Dn: sys/rack-unit-1/mgmt/if-1
  HttpPort: 80
  HttpsPort: 443
  KvmPort: 2068
  KvmVlan: 1
  Name: Outband
  ObjectType: compute.IpAddress
  Subnet: 255.255.255.224
  Type: MgmtInterface
KvmServerStateEnabled: false
KvmVendor: Avocent
LocatorLed:
  ClassId: mo.MoRef
  Moid: 5fdf9c8b6176752d35e47959
  ObjectType: equipment.LocatorLed
  link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdf9c8b6176752d35e47959
ManagementIp: 10.58.50.42
ManagementMode: IntersightStandalone
MemoryArrays: []
MemoryInfo:
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-1
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_A1
  MemoryId: 1
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F736F1
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-2
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_A2
  MemoryId: 2
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-3
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_B1
  MemoryId: 3
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F7370D
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-4
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_B2
  MemoryId: 4
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-5
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_C1
  MemoryId: 5
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F736F9
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-6
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_C2
  MemoryId: 6
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-7
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_D1
  MemoryId: 7
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F73709
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-8
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_D2
  MemoryId: 8
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-9
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_E1
  MemoryId: 9
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F736F7
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-10
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_E2
  MemoryId: 10
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-11
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_F1
  MemoryId: 11
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F7370A
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-12
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_F2
  MemoryId: 12
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-13
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_G1
  MemoryId: 13
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F736F8
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-14
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_G2
  MemoryId: 14
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-15
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_H1
  MemoryId: 15
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F736ED
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-16
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_H2
  MemoryId: 16
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-17
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_J1
  MemoryId: 17
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F736F6
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-18
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_J2
  MemoryId: 18
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-19
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_K1
  MemoryId: 19
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0EFB85E
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-20
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_K2
  MemoryId: 20
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-21
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_L1
  MemoryId: 21
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F72BFA
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-22
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_L2
  MemoryId: 22
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
- ArrayId: 1
  Bank: 0
  Capacity: '32768'
  Clock: '2933'
  Dn: sys/rack-unit-1/board/memarray-1/mem-23
  FormFactor: DIMM
  Latency: ''
  Location: DIMM_M1
  MemoryId: 23
  Model: '36ASF4G72PZ-2G9E2   '
  OperState: operable
  Presence: equipped
  Serial: F0F72BFE
  Speed: ''
  Type: DDR4
  Vendor: '0x2C00'
- ArrayId: 1
  Bank: 0
  Capacity: unspecified
  Clock: unspecified
  Dn: sys/rack-unit-1/board/memarray-1/mem-24
  FormFactor: undiscovered
  Latency: ''
  Location: DIMM_M2
  MemoryId: 24
  Model: ''
  OperState: removed
  Presence: missing
  Serial: ''
  Speed: ''
  Type: undiscovered
  Vendor: ''
MemorySpeed: '2933'
MgmtIdentity: null
MgmtIpAddress: 10.58.50.42
ModTime: '2022-09-28T08:19:26.75Z'
Model: UCSC-C240-M5SN
Moid: 5fdf9c786176752d35e47110
Name: aio-2-p2b-eu-spdc-WZP23400AK4
NumAdaptors: 1
NumCpuCores: 40
NumCpuCoresEnabled: 40
NumCpus: 2
NumEthHostInterfaces: 2
NumFcHostInterfaces: 2
NumThreads: 80
ObjectType: compute.RackUnit
OperPowerState: 'on'
OperReason: []
OperState: ''
Operability: ''
Owners:
- 5be4b2ce67626c6d661ca38d
- 5fdf9c676f72612d300a9c8d
PciDevices:
- ClassId: mo.MoRef
  Moid: 5fdf9ccb6176752d35e496d1
  ObjectType: pci.Device
  link: https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d1
- ClassId: mo.MoRef
  Moid: 5fdf9ccb6176752d35e496d3
  ObjectType: pci.Device
  link: https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d3
- ClassId: mo.MoRef
  Moid: 5fdf9ccb6176752d35e496d5
  ObjectType: pci.Device
  link: https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d5
- ClassId: mo.MoRef
  Moid: 5fdf9ccb6176752d35e496d7
  ObjectType: pci.Device
  link: https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496d7
- ClassId: mo.MoRef
  Moid: 5fdf9ccb6176752d35e496da
  ObjectType: pci.Device
  link: https://www.intersight.com/api/v1/pci/Devices/5fdf9ccb6176752d35e496da
PciDevicesInfo:
- Dn: sys/rack-unit-1/equipped-slot-3
  FirmwareVersion: 0x80009E5D-1.823.2
  Model: Cisco(R) Ethernet Converged NIC XXV710-DA2
  Pid: UCSC-PCIE-ID25GF
  SlotId: '3'
  Vendor: '0x8086'
- Dn: sys/rack-unit-1/equipped-slot-6
  FirmwareVersion: 0x80009E5D-1.823.2
  Model: Cisco(R) Ethernet Converged NIC XXV710-DA2
  Pid: UCSC-PCIE-ID25GF
  SlotId: '6'
  Vendor: '0x8086'
- Dn: sys/rack-unit-1/equipped-slot-L
  FirmwareVersion: 0x80001516-1.823.2
  Model: Intel X550 LOM
  Pid: UNKNOWN
  SlotId: L
  Vendor: '0x8086'
- Dn: sys/rack-unit-1/equipped-slot-MLOM
  FirmwareVersion: 5.1(3d)
  Model: Cisco UCS VIC 1457 MLOM
  Pid: UCSC-MLOM-C25Q-04
  SlotId: MLOM
  Vendor: '0x1137'
- Dn: sys/rack-unit-1/equipped-slot-MRAID
  FirmwareVersion: 51.10.0-3612
  Model: Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)
  Pid: UCSC-RAID-M5
  SlotId: MRAID
  Vendor: '0x1000'
PciModels:
- UCSC-PCIE-ID25GF
- UCSC-PCIE-ID25GF
- UCSC-MLOM-C25Q-04
- UCSC-RAID-M5
- Intel X550 LOM
PermissionResources:
- ClassId: mo.MoRef
  Moid: 5dee1d736972652d321d26b5
  ObjectType: organization.Organization
  link: https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5
- ClassId: mo.MoRef
  Moid: 625706a06972652d3202a8f9
  ObjectType: organization.Organization
  link: https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9
- ClassId: mo.MoRef
  Moid: 6242d1016972652d32eda017
  ObjectType: organization.Organization
  link: https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017
PhysicalDiskCapacity: 11029994012672
PhysicalDiskCapacityUnit: 11.03 [TB]
PhysicalDiskCount: 10
PhysicalDisks:
- DiskId: '10'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-10
  DriveFirmware: SCV1CS08
  DriveState: Online
  LinkSpeed: 6.0 Gb/s
  Model: SSDSC2KB960G7K
  Moid: 6166890f76752d31393848bd
  Pid: SSDSC2KB960G7K
  Presence: equipped
  Serial: PHYS746002M1960CGN
  Size: 914573 MB
  StorageControllerId: MRAID
  Type: SSD
  Vendor: ATA
  VirtualDriveId: '0'
  VirtualDriveMoid: 6166891176752d31393849a7
- DiskId: '11'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-11
  DriveFirmware: SCV1CS08
  DriveState: JBOD
  LinkSpeed: 6.0 Gb/s
  Model: SSDSC2KB960G7K
  Moid: 6166891076752d31393848f3
  Pid: SSDSC2KB960G7K
  Presence: equipped
  Serial: PHYS746002ME960CGN
  Size: 914573 MB
  StorageControllerId: MRAID
  Type: SSD
  Vendor: ATA
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '12'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-12
  DriveFirmware: SCV1CS08
  DriveState: JBOD
  LinkSpeed: 6.0 Gb/s
  Model: SSDSC2KB960G7K
  Moid: 6166891076752d3139384913
  Pid: SSDSC2KB960G7K
  Presence: equipped
  Serial: PHYS746003DM960CGN
  Size: 914573 MB
  StorageControllerId: MRAID
  Type: SSD
  Vendor: ATA
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '13'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-13
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891076752d3139384924
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK65JQF0000C0259760
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '14'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-14
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891076752d3139384935
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK65LZ70000C02597DN
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '15'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-15
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891076752d3139384947
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK65LD10000C024KKJM
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '16'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-16
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891076752d3139384958
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK64DPD0000C0244K8B
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '17'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-17
  DriveFirmware: CN03
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0009
  Moid: 6166891176752d313938496a
  Pid: ST1200MM0009
  Presence: equipped
  Serial: WFK64DX60000C025BW6X
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '18'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-18
  DriveFirmware: N0A4
  DriveState: JBOD
  LinkSpeed: 12.0 Gb/s
  Model: ST1200MM0088
  Moid: 6166891176752d3139384985
  Pid: ST1200MM0088
  Presence: equipped
  Serial: Z4000FFD0000R616HPN9
  Size: 1143455 MB
  StorageControllerId: MRAID
  Type: HDD
  Vendor: SEAGATE
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '9'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-9
  DriveFirmware: SCV1CS08
  DriveState: Online
  LinkSpeed: 6.0 Gb/s
  Model: SSDSC2KB960G7K
  Moid: 6166890f76752d3139384892
  Pid: SSDSC2KB960G7K
  Presence: equipped
  Serial: PHYS746100ZW960CGN
  Size: 914573 MB
  StorageControllerId: MRAID
  Type: SSD
  Vendor: ATA
  VirtualDriveId: '0'
  VirtualDriveMoid: 6166891176752d31393849a7
PlatformType: IMCM5
Presence: equipped
PreviousFru: null
Processors: []
PsuCount: 2
PsuHealthy: true
PsuInfo:
- Dn: sys/rack-unit-1/psu-1
  Model: PS-2112-9S-LF
  Serial: LIT241244RQ
  Vendor: Cisco Systems Inc
- Dn: sys/rack-unit-1/psu-2
  Model: PS-2112-9S-LF
  Serial: LIT241242TS
  Vendor: Cisco Systems Inc
PsuOn: 2
PsuSummary: 2/2
Psus:
- ClassId: mo.MoRef
  Moid: 5fdf9c856176752d35e476b8
  ObjectType: equipment.Psu
  link: https://www.intersight.com/api/v1/equipment/Psus/5fdf9c856176752d35e476b8
- ClassId: mo.MoRef
  Moid: 5fdf9c856176752d35e476ba
  ObjectType: equipment.Psu
  link: https://www.intersight.com/api/v1/equipment/Psus/5fdf9c856176752d35e476ba
RackEnclosureSlot: null
RegisteredDevice:
  ClassId: mo.MoRef
  Moid: 5fdf9c676f72612d300a9c8d
  ObjectType: asset.DeviceRegistration
  link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9c676f72612d300a9c8d
Revision: ''
Rn: ''
SasExpanders: []
Serial: WZP23400AK4
ServerId: 1
ServiceProfile: ''
SharedScope: ''
SsdDiskCapacity: 3835997192192
SsdDiskCapacityUnit: 3.84 [TB]
SsdDiskCount: 4
SsdDisks:
- DiskId: '10'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-10
  DriveFirmware: SCV1CS08
  DriveState: Online
  LinkSpeed: 6.0 Gb/s
  Model: SSDSC2KB960G7K
  Moid: 6166890f76752d31393848bd
  Pid: SSDSC2KB960G7K
  Presence: equipped
  Serial: PHYS746002M1960CGN
  Size: 914573 MB
  StorageControllerId: MRAID
  Type: SSD
  Vendor: ATA
  VirtualDriveId: '0'
  VirtualDriveMoid: 6166891176752d31393849a7
- DiskId: '11'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-11
  DriveFirmware: SCV1CS08
  DriveState: JBOD
  LinkSpeed: 6.0 Gb/s
  Model: SSDSC2KB960G7K
  Moid: 6166891076752d31393848f3
  Pid: SSDSC2KB960G7K
  Presence: equipped
  Serial: PHYS746002ME960CGN
  Size: 914573 MB
  StorageControllerId: MRAID
  Type: SSD
  Vendor: ATA
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '12'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-12
  DriveFirmware: SCV1CS08
  DriveState: JBOD
  LinkSpeed: 6.0 Gb/s
  Model: SSDSC2KB960G7K
  Moid: 6166891076752d3139384913
  Pid: SSDSC2KB960G7K
  Presence: equipped
  Serial: PHYS746003DM960CGN
  Size: 914573 MB
  StorageControllerId: MRAID
  Type: SSD
  Vendor: ATA
  VirtualDriveId: ''
  VirtualDriveMoid: null
- DiskId: '9'
  DiskState: Good
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID/pd-9
  DriveFirmware: SCV1CS08
  DriveState: Online
  LinkSpeed: 6.0 Gb/s
  Model: SSDSC2KB960G7K
  Moid: 6166890f76752d3139384892
  Pid: SSDSC2KB960G7K
  Presence: equipped
  Serial: PHYS746100ZW960CGN
  Size: 914573 MB
  StorageControllerId: MRAID
  Type: SSD
  Vendor: ATA
  VirtualDriveId: '0'
  VirtualDriveMoid: 6166891176752d31393849a7
State: P+HRS
StorageCapacity: R 11.03 [TB] , VD 1.92 [TB]
StorageControllers: []
StorageControllersCount: 1
StorageControllersInfo:
- ControllerId: MRAID
  Dn: sys/rack-unit-1/board/storage-SAS-MRAID
  Model: Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)
  Moid: 5fdf9cd46176752d35e4998e
  PciSlot: MRAID
  PhysicalDiskCount: 10
  PhysicalDiskIds:
  - 6166890f76752d3139384892
  - 6166890f76752d31393848bd
  - 6166891076752d31393848f3
  - 6166891076752d3139384913
  - 6166891076752d3139384924
  - 6166891076752d3139384935
  - 6166891076752d3139384947
  - 6166891076752d3139384958
  - 6166891176752d313938496a
  - 6166891176752d3139384985
  Presence: equipped
  RaidSupport: 'yes'
  Serial: SK00481450
  Vendor: LSI Logic
  VirtualDriveCount: 1
  VirtualDriveIds:
  - 6166891176752d31393849a7
StorageDrives: 1C 6H 4S 1VD
StorageEnclosures: []
StorageSummary: 1C 6H 4S 1VD R11.03 [TB] L1.92 [TB]
Tags:
- Key: Intersight.LicenseTier
  Value: Premier
TopSystem:
  ClassId: mo.MoRef
  Moid: 5fdf9cc96176752d35e49601
  ObjectType: top.System
  link: https://www.intersight.com/api/v1/top/Systems/5fdf9cc96176752d35e49601
TopologyScanStatus: ''
TotalMemory: 393216
TotalMemoryGB: 384
TotalMemoryUnit: 384 [GiB]
TunneledKvm: false
Type: Rack
UnitPersonality: []
UserLabel: aio-2-p2b-eu-spdc-WZP23400AK4
Uuid: B813910F-BFD2-439F-9C3B-75B376C5B160
Vendor: Cisco Systems Inc
VirtualDiskCapacity: 1917998596096
VirtualDiskCapacityUnit: 1.92 [TB]
VirtualDiskCount: 1
VirtualDisks:
- Dn: sys/rack-unit-1/board/storage-SAS-MRAID/vd-0
  Moid: 6166891176752d31393849a7
  Name: RAID0_910
  PhysicalDiskCount: 2
  PhysicalDiskIds:
  - '9'
  - '10'
  Size: 1829146 MB
  StorageControllerId: MRAID
  Type: RAID 0
  VirtualDriveId: '0'
Vmedia: null
WorkflowLast: null
WorkflowRunning: null
WorkflowsLast: []
WorkflowsLastFailedIds: []
WorkflowsLastIds: []
```