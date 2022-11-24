# Servers Inventory

Get servers' information in table, json or yaml formats.

Use command options for servers' filtering and information shown in output.

Multiple server filtering rules follow logical AND.

Intent | Command | Documentation
--- | --- | ---
Get servers summary information | iserver get servers summary | [example](ServersInventorySummary.md)
Get all servers in table format | iserver get servers list | [example](ServersInventoryAllDefault.md)
Get all servers in json format | iserver get servers list -o json | [example](ServersInventoryAllJson.md)
Get all servers in yaml format | iserver get servers list -o yaml | [example](ServersInventoryAllYaml.md)
Add extra server information | iserver get servers list -c value | [example](ServersInventoryColumns.md)
Select servers by type | iserver get servers list --type value | [example](ServersInventoryType.md)
Select servers by name | iserver get servers list --name value | [example](ServersInventoryName.md)
Select servers by model | iserver get servers list --model value | [example](ServersInventoryModel.md)
Select servers by serial numbers | iserver get servers list --serial value | [example](ServersInventorySerials.md)
Select servers by CIMC Management IP | iserver get servers list --ip value | [example](ServersInventoryIp.md)
Select servers with location led on | iserver get servers list --loc | [example](ServersInventoryLed.md)
Select servers powered off | iserver get servers list --off | [example](ServersInventoryOff.md)
Select servers with health warnings | iserver get servers list --health | [example](ServersInventoryHealth.md)
Select servers with unhealthy fans | iserver get servers list --fans | [example](ServersInventoryFans.md)
Select servers with unhealthy psu | iserver get servers list --psu | [example](ServersInventoryPsu.md)
Select USCM managed servers | iserver get servers list --ucsm | [example](ServersInventoryUcsm.md)
Select Intersight Managed servers| iserver get servers list --standalone | [example](ServersInventoryStandalone.md)
Select servers with PCI device | iserver get servers list --pci value | [example](ServersInventoryPci.md)
CPU-based filtering | iserver get servers list --cpu value | [example](ServersInventoryCpu.md)
Memory-based filtering | iserver get servers list --memory value | [example](ServersInventoryMemory.md)
Servers group management | iserver get servers list --set value | [example](ServersInventoryGroups.md)

```
# iserver get servers --help

Usage: iserver.py get servers [OPTIONS]

  Get servers list

Options:
  --iaccount TEXT                 Intersight account  [default: isctl]
  --group TEXT                    Group name
  --type [all|blade|rack]         [default: all]
  -c, --column TEXT               Extra columns:
                                  id,fw,pci,fan,psu,group,storage
  --loc                           Locator LED on
  --off                           Filter powered off
  --health                        Filter unhealthy
  --fan                           Filter unhealthy fans
  --psu                           Filter unhealthy psu
  --ucsm                          Filter UCSM managed
  --standalone                    Filter standalone servers
  --ip TEXT                       Management IP address or subnet filter
  --name TEXT                     Name loose match filter
  --model TEXT                    Model loose match filter
  --pci TEXT                      Pci model loose match filter
  --serial TEXT                   Serial strict match filter
  --cpu TEXT                      CPU cores filter
  --memory TEXT                   Memory [GiB] filter
  --set TEXT                      Set as group
  -o, --output [default|json|yaml]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.
```
