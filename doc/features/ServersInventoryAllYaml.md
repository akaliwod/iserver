# Servers inventory in YAML format

Use YAML (-o yaml) output format.

```
# iserver get servers -o yaml
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5e8c4f0c6176752d32d54fd3
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5e8c4f0c6176752d32d54fd3
  - ClassId: mo.MoRef
    Moid: 5e8c50046176752d32d6446e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5e8c50046176752d32d6446e
  - ClassId: mo.MoRef
    Moid: 5e8c50046176752d32d64476
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5e8c50046176752d32d64476
  - ClassId: mo.MoRef
    Moid: 5e8c50046176752d32d64486
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5e8c50046176752d32d64486
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02209B4
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa1a35d6176752d35470524
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa1a35d6176752d35470524
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d58c806176752d3567e8b1
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d58c806176752d3567e8b1
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5e8c4f206176752d32d55fc3
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5e8c4f206176752d32d55fc3
  Bmc:
    ClassId: mo.MoRef
    Moid: 5e8c4f076176752d32d54b2a
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5e8c4f076176752d32d54b2a
  Board:
    ClassId: mo.MoRef
    Moid: 5e8c4ed96176752d32d52214
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5e8c4ed96176752d32d52214
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb326176752d35de11b9
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb326176752d35de11b9
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5e8c4fd66176752d32d61684
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5e8c4fd66176752d32d61684
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf826176752d3570bfd4
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb7cf826176752d3570bfd4
  - ClassId: mo.MoRef
    Moid: 5fb7cf826176752d3570bfd6
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb7cf826176752d3570bfd6
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf8d6176752d3570c65c
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb7cf8d6176752d3570c65c
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf806176752d3570bece
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb7cf806176752d3570bece
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 16C 32T
  CreateTime: '2020-04-07T09:58:42.039Z'
  DeviceMoId: 5e8c4ecd6f72612d302b11a6
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5e8c4ef36176752d32d5387b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5e8c4ef36176752d32d5387b
  - ClassId: mo.MoRef
    Moid: 5e8c4ef36176752d32d5387e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5e8c4ef36176752d32d5387e
  - ClassId: mo.MoRef
    Moid: 5e8c4ef36176752d32d53882
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5e8c4ef36176752d32d53882
  - ClassId: mo.MoRef
    Moid: 5e8c4ef36176752d32d53886
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5e8c4ef36176752d32d53886
  - ClassId: mo.MoRef
    Moid: 5e8c4ef36176752d32d5388c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5e8c4ef36176752d32d5388c
  - ClassId: mo.MoRef
    Moid: 5e8c4ef36176752d32d5388e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5e8c4ef36176752d32d5388e
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5e8c4ff76176752d32d63a3b
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5e8c4ff76176752d32d63a3b
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.34
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5e8c4ef86176752d32d53c1e
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5e8c4ef86176752d32d53c1e
  LocatorLedOn: false
  ManagementIp: 10.58.28.34
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.34
  ModTime: '2022-10-05T22:01:40.258Z'
  Model: UCSC-C220-M4S
  Moid: 5e8c4ed26176752d32d51c40
  Name: esx2-eu-spdc-FCH2004V1PV
  NumAdaptors: 4
  NumCpuCores: 16
  NumCpuCoresEnabled: 16
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 32
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5e8c4ecd6f72612d302b11a6
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5e8c4fe16176752d32d624f6
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5e8c4fe16176752d32d624f6
  - ClassId: mo.MoRef
    Moid: 5e8c4fe16176752d32d624fb
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5e8c4fe16176752d32d624fb
  - ClassId: mo.MoRef
    Moid: 5e8c4fe16176752d32d62501
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5e8c4fe16176752d32d62501
  - ClassId: mo.MoRef
    Moid: 5e8c4fe16176752d32d62503
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5e8c4fe16176752d32d62503
  - ClassId: mo.MoRef
    Moid: 5e8c4fe16176752d32d62508
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5e8c4fe16176752d32d62508
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5e8c4ee56176752d32d529d8
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5e8c4ee56176752d32d529d8
  - ClassId: mo.MoRef
    Moid: 5e8c4ee56176752d32d529da
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5e8c4ee56176752d32d529da
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5e8c4ecd6f72612d302b11a6
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5e8c4ecd6f72612d302b11a6
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2004V1PV
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: LAB-ID
    Value: EU-SPDC
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5e8c4fd86176752d32d61a7c
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5e8c4fd86176752d32d61a7c
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx2-eu-spdc-FCH2004V1PV
  Uuid: 319C36CB-BC94-4906-9218-CE1BD05E4737
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6153349076752d3137194aa7
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6153349076752d3137194aa7
  - ClassId: mo.MoRef
    Moid: 6153349076752d3137194aad
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6153349076752d3137194aad
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290572
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa1658b6176752d35307736
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa1658b6176752d35307736
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5fbea6176752d35a30b41
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5fbea6176752d35a30b41
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5ecf82826176752d35b7ea58
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5ecf82826176752d35b7ea58
  Bmc:
    ClassId: mo.MoRef
    Moid: 5ecf82a86176752d35b7f6ba
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5ecf82a86176752d35b7f6ba
  Board:
    ClassId: mo.MoRef
    Moid: 5ecf82886176752d35b7eb4a
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5ecf82886176752d35b7eb4a
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb426176752d35de1743
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb426176752d35de1743
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5ecf82a96176752d35b7f6fa
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5ecf82a96176752d35b7f6fa
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb844a36176752d359d9cfe
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb844a36176752d359d9cfe
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb844ae6176752d359da0ba
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb844ae6176752d359da0ba
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2020-05-28T09:21:14.322Z'
  DeviceMoId: 5ecf82676f72612d30687409
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5ecf82736176752d35b7e757
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf82736176752d35b7e757
  - ClassId: mo.MoRef
    Moid: 5ecf82736176752d35b7e759
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf82736176752d35b7e759
  - ClassId: mo.MoRef
    Moid: 5ecf82736176752d35b7e75b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf82736176752d35b7e75b
  - ClassId: mo.MoRef
    Moid: 5ecf82736176752d35b7e75d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf82736176752d35b7e75d
  - ClassId: mo.MoRef
    Moid: 5ecf82736176752d35b7e75f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf82736176752d35b7e75f
  - ClassId: mo.MoRef
    Moid: 5ecf82736176752d35b7e761
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf82736176752d35b7e761
  - ClassId: mo.MoRef
    Moid: 5ecf82736176752d35b7e763
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf82736176752d35b7e763
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5ecf82ea6176752d35b80a94
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5ecf82ea6176752d35b80a94
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.60
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 5ecf82996176752d35b7f0e0
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5ecf82996176752d35b7f0e0
  LocatorLedOn: false
  ManagementIp: 10.58.29.60
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.60
  ModTime: '2022-07-25T17:16:33.659Z'
  Model: UCSC-C220-M5SX
  Moid: 5ecf828a6176752d35b7eb9a
  Name: mgmt-p4a-eu-spdc-WZP22520Y9D
  NumAdaptors: 0
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5ecf82676f72612d30687409
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5ecf82c66176752d35b7fee5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5ecf82c66176752d35b7fee5
  - ClassId: mo.MoRef
    Moid: 5ecf82c66176752d35b7feeb
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5ecf82c66176752d35b7feeb
  - ClassId: mo.MoRef
    Moid: 5ecf82c66176752d35b7feed
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5ecf82c66176752d35b7feed
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5ecf826c6176752d35b7e5af
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5ecf826c6176752d35b7e5af
  - ClassId: mo.MoRef
    Moid: 5ecf826c6176752d35b7e5b1
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5ecf826c6176752d35b7e5b1
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5ecf82676f72612d30687409
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5ecf82676f72612d30687409
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520Y9D
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5ecf82c26176752d35b7fe21
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5ecf82c26176752d35b7fe21
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: mgmt-p4a-spdc-WZP22520Y9D
  Uuid: 051437F5-BE0E-44F3-B815-79058BD93C7A
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5ecf875e6176752d35b96534
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5ecf875e6176752d35b96534
  - ClassId: mo.MoRef
    Moid: 5ecf875e6176752d35b96548
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5ecf875e6176752d35b96548
  - ClassId: mo.MoRef
    Moid: 61a951cb76752d3139700067
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61a951cb76752d3139700067
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 1
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290574
  AvailableMemory: 196608
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5f13cb996176752d35982549
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5f13cb996176752d35982549
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d591f66176752d356a9a38
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d591f66176752d356a9a38
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5ecf86ec6176752d35b9429e
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5ecf86ec6176752d35b9429e
  Bmc:
    ClassId: mo.MoRef
    Moid: 5ecf87186176752d35b94e00
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5ecf87186176752d35b94e00
  Board:
    ClassId: mo.MoRef
    Moid: 5ecf86f56176752d35b944f9
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5ecf86f56176752d35b944f9
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdd093c6176752d35e3b8aa
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdd093c6176752d35e3b8aa
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5ecf87186176752d35b94e16
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5ecf87186176752d35b94e16
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7c16a6176752d356b807c
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb7c16a6176752d356b807c
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7c1746176752d356b8343
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb7c1746176752d356b8343
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 24C 48T
  CreateTime: '2020-05-28T09:40:01.064Z'
  DeviceMoId: 5ecf86d86f72612d3068b4bc
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5ecf87006176752d35b94805
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf87006176752d35b94805
  - ClassId: mo.MoRef
    Moid: 5ecf87006176752d35b94807
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf87006176752d35b94807
  - ClassId: mo.MoRef
    Moid: 5ecf87006176752d35b94809
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf87006176752d35b94809
  - ClassId: mo.MoRef
    Moid: 5ecf87006176752d35b9480b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf87006176752d35b9480b
  - ClassId: mo.MoRef
    Moid: 5ecf87006176752d35b9480d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf87006176752d35b9480d
  - ClassId: mo.MoRef
    Moid: 5ecf87006176752d35b9480f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf87006176752d35b9480f
  - ClassId: mo.MoRef
    Moid: 5ecf87006176752d35b94811
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf87006176752d35b94811
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5ecf87566176752d35b963cd
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5ecf87566176752d35b963cd
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.51
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5ecf87046176752d35b94908
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5ecf87046176752d35b94908
  LocatorLedOn: false
  ManagementIp: 10.58.28.51
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.51
  ModTime: '2022-09-23T04:52:52.103Z'
  Model: UCSC-C240-M5SX
  Moid: 5ecf86f16176752d35b94401
  Name: comp1-p2a-eu-spdc-WZP22511E6V
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5ecf86d86f72612d3068b4bc
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5ecf872b6176752d35b9550c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5ecf872b6176752d35b9550c
  - ClassId: mo.MoRef
    Moid: 5ecf872b6176752d35b9550e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5ecf872b6176752d35b9550e
  - ClassId: mo.MoRef
    Moid: 5ecf872b6176752d35b95513
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5ecf872b6176752d35b95513
  - ClassId: mo.MoRef
    Moid: 61e8623076752d3139a4dd98
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e8623076752d3139a4dd98
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5ecf86fd6176752d35b94789
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5ecf86fd6176752d35b94789
  - ClassId: mo.MoRef
    Moid: 5ecf86fd6176752d35b9478b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5ecf86fd6176752d35b9478b
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5ecf86d86f72612d3068b4bc
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5ecf86d86f72612d3068b4bc
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 62e8fc3676752d3139c8a590
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/62e8fc3676752d3139c8a590
  Serial: WZP22511E6V
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-CRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5ecf87296176752d35b95455
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5ecf87296176752d35b95455
  TopologyScanStatus: ''
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp1-p2a-eu-spdc-WZP22511E6V
  Uuid: 77C9F6AB-FA35-45E5-A01F-C9D630053FCC
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5ecf88796176752d35b9b678
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5ecf88796176752d35b9b678
  - ClassId: mo.MoRef
    Moid: 61a9515276752d31396fdda9
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61a9515276752d31396fdda9
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 022C208
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5f1413686176752d35b5a943
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5f1413686176752d35b5a943
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5fbe96176752d35a30a81
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5fbe96176752d35a30a81
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5ecf87c06176752d35b97e87
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5ecf87c06176752d35b97e87
  Bmc:
    ClassId: mo.MoRef
    Moid: 5ecf88376176752d35b9a14c
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5ecf88376176752d35b9a14c
  Board:
    ClassId: mo.MoRef
    Moid: 5ecf88106176752d35b997b6
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5ecf88106176752d35b997b6
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb426176752d35de175b
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb426176752d35de175b
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5ecf883a6176752d35b9a2db
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5ecf883a6176752d35b9a2db
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb739776176752d353557a0
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb739776176752d353557a0
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb739816176752d35355a76
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb739816176752d35355a76
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 24C 48T
  CreateTime: '2020-05-28T09:43:33.889Z'
  DeviceMoId: 5ecf87bc6f72612d3068c346
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5ecf881a6176752d35b999eb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf881a6176752d35b999eb
  - ClassId: mo.MoRef
    Moid: 5ecf881a6176752d35b999f0
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf881a6176752d35b999f0
  - ClassId: mo.MoRef
    Moid: 5ecf881a6176752d35b999f2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf881a6176752d35b999f2
  - ClassId: mo.MoRef
    Moid: 5ecf881a6176752d35b999f4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf881a6176752d35b999f4
  - ClassId: mo.MoRef
    Moid: 5ecf881a6176752d35b999f6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf881a6176752d35b999f6
  - ClassId: mo.MoRef
    Moid: 5ecf881a6176752d35b999f8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf881a6176752d35b999f8
  - ClassId: mo.MoRef
    Moid: 5ecf881a6176752d35b999fa
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5ecf881a6176752d35b999fa
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5ecf88706176752d35b9b369
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5ecf88706176752d35b9b369
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.56
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 5ecf881e6176752d35b99b17
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5ecf881e6176752d35b99b17
  LocatorLedOn: false
  ManagementIp: 10.58.28.56
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.56
  ModTime: '2022-05-09T13:35:25.987Z'
  Model: UCSC-C240-M5SX
  Moid: 5ecf87c56176752d35b97fa4
  Name: znas-eu-spdc-WZP22511E3P
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 4
  NumFcHostInterfaces: 4
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5ecf87bc6f72612d3068c346
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5ecf88456176752d35b9a670
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5ecf88456176752d35b9a670
  - ClassId: mo.MoRef
    Moid: 5ecf88456176752d35b9a672
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5ecf88456176752d35b9a672
  - ClassId: mo.MoRef
    Moid: 61c19d5776752d3139e3a844
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c19d5776752d3139e3a844
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 619e0d2a76752d3139d4c0e5
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/619e0d2a76752d3139d4c0e5
  - ClassId: mo.MoRef
    Moid: 619e0d2a76752d3139d4c0e7
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/619e0d2a76752d3139d4c0e7
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5ecf87bc6f72612d3068c346
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5ecf87bc6f72612d3068c346
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 61c1d99c76752d3139ef5549
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/61c1d99c76752d3139ef5549
  Serial: WZP22511E3P
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5ecf88436176752d35b9a5fa
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5ecf88436176752d35b9a5fa
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: znas-eu-spdc-WZP22511E3P
  Uuid: 4F26FDC3-A273-4054-8E13-1EB1E1F3F9AA
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa045b66176752d35c9ccbb
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa045b66176752d35c9ccbb
  - ClassId: mo.MoRef
    Moid: 5fa046ed6176752d35ca46cb
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa046ed6176752d35ca46cb
  - ClassId: mo.MoRef
    Moid: 5fa046ed6176752d35ca46d1
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa046ed6176752d35ca46d1
  - ClassId: mo.MoRef
    Moid: 5fa046ed6176752d35ca46db
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa046ed6176752d35ca46db
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02209AF
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa045ea6176752d35c9e00a
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa045ea6176752d35c9e00a
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d58c806176752d3567e896
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d58c806176752d3567e896
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa045ed6176752d35c9e15f
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa045ed6176752d35c9e15f
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa046bb6176752d35ca37dc
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa046bb6176752d35ca37dc
  Board:
    ClassId: mo.MoRef
    Moid: 5fa045d26176752d35c9d420
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa045d26176752d35c9d420
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdd09426176752d35e3bad1
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdd09426176752d35e3bad1
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa046b16176752d35ca3446
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa046b16176752d35ca3446
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734d16176752d35337a02
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb734d16176752d35337a02
  - ClassId: mo.MoRef
    Moid: 5fb734d16176752d35337a04
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb734d16176752d35337a04
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734da6176752d35337ecb
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb734da6176752d35337ecb
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734cd6176752d35337885
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb734cd6176752d35337885
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 16C 32T
  CreateTime: '2020-11-02T17:45:50.125Z'
  DeviceMoId: 5fa045b46f72612d3086c548
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa0460b6176752d35c9f071
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa0460b6176752d35c9f071
  - ClassId: mo.MoRef
    Moid: 5fa0460b6176752d35c9f073
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa0460b6176752d35c9f073
  - ClassId: mo.MoRef
    Moid: 5fa0460b6176752d35c9f076
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa0460b6176752d35c9f076
  - ClassId: mo.MoRef
    Moid: 5fa0460b6176752d35c9f078
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa0460b6176752d35c9f078
  - ClassId: mo.MoRef
    Moid: 5fa0460b6176752d35c9f07a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa0460b6176752d35c9f07a
  - ClassId: mo.MoRef
    Moid: 5fa0460b6176752d35c9f07c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa0460b6176752d35c9f07c
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa046fe6176752d35ca4c06
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa046fe6176752d35ca4c06
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.35
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fa046146176752d35c9f3ef
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa046146176752d35c9f3ef
  LocatorLedOn: false
  ManagementIp: 10.58.28.35
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.35
  ModTime: '2022-10-05T22:01:39.961Z'
  Model: UCSC-C220-M4S
  Moid: 5fa045ce6176752d35c9d2f5
  Name: esx3-eu-spdc-FCH2004V0RW
  NumAdaptors: 4
  NumCpuCores: 16
  NumCpuCoresEnabled: 16
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 32
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa045b46f72612d3086c548
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa046e16176752d35ca42b1
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa046e16176752d35ca42b1
  - ClassId: mo.MoRef
    Moid: 5fa046e16176752d35ca42b3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa046e16176752d35ca42b3
  - ClassId: mo.MoRef
    Moid: 5fa046e16176752d35ca42b5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa046e16176752d35ca42b5
  - ClassId: mo.MoRef
    Moid: 5fa046e16176752d35ca42b7
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa046e16176752d35ca42b7
  - ClassId: mo.MoRef
    Moid: 5fa046e16176752d35ca42b9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa046e16176752d35ca42b9
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa046016176752d35c9ec00
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa046016176752d35c9ec00
  - ClassId: mo.MoRef
    Moid: 5fa046016176752d35c9ec02
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa046016176752d35c9ec02
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa045b46f72612d3086c548
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa045b46f72612d3086c548
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2004V0RW
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa046c26176752d35ca3b66
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa046c26176752d35ca3b66
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx3-eu-spdc-FCH2004V0RW
  Uuid: D6BB55F7-FE8D-4401-96AE-53C4BF493EDF
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa047b56176752d35ca8505
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa047b56176752d35ca8505
  - ClassId: mo.MoRef
    Moid: 5fa048de6176752d35cafa59
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa048de6176752d35cafa59
  - ClassId: mo.MoRef
    Moid: 5fa048de6176752d35cafa5f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa048de6176752d35cafa5f
  - ClassId: mo.MoRef
    Moid: 5fa048de6176752d35cafa67
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa048de6176752d35cafa67
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 025F4DF
  AvailableMemory: 524288
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa047de6176752d35ca9661
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa047de6176752d35ca9661
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5a00c6176752d35723f70
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5a00c6176752d35723f70
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa047cc6176752d35ca8d90
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa047cc6176752d35ca8d90
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa0489e6176752d35cae227
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa0489e6176752d35cae227
  Board:
    ClassId: mo.MoRef
    Moid: 5fa047d96176752d35ca939b
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa047d96176752d35ca939b
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb336176752d35de1211
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb336176752d35de1211
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa048a66176752d35cae4b2
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa048a66176752d35cae4b2
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf836176752d3570c0b1
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb7cf836176752d3570c0b1
  - ClassId: mo.MoRef
    Moid: 5fb7cf836176752d3570c0b3
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb7cf836176752d3570c0b3
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf906176752d3570c8d3
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb7cf906176752d3570c8d3
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf806176752d3570bf28
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb7cf806176752d3570bf28
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 36C 72T
  CreateTime: '2020-11-02T17:53:41.511Z'
  DeviceMoId: 5fa0477f6f72612d30873c09
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa047f36176752d35ca9ed7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa047f36176752d35ca9ed7
  - ClassId: mo.MoRef
    Moid: 5fa047f36176752d35ca9ed9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa047f36176752d35ca9ed9
  - ClassId: mo.MoRef
    Moid: 5fa047f36176752d35ca9edb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa047f36176752d35ca9edb
  - ClassId: mo.MoRef
    Moid: 5fa047f36176752d35ca9edd
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa047f36176752d35ca9edd
  - ClassId: mo.MoRef
    Moid: 5fa047f36176752d35ca9edf
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa047f36176752d35ca9edf
  - ClassId: mo.MoRef
    Moid: 5fa047f36176752d35ca9ee1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa047f36176752d35ca9ee1
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa048d96176752d35caf931
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa048d96176752d35caf931
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.36
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fa047fc6176752d35caa1a0
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa047fc6176752d35caa1a0
  LocatorLedOn: false
  ManagementIp: 10.58.28.36
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.36
  ModTime: '2022-09-13T08:44:49.523Z'
  Model: UCSC-C220-M4S
  Moid: 5fa047a56176752d35ca8002
  Name: esx4-eu-spdc-FCH2016V2BB
  NumAdaptors: 4
  NumCpuCores: 36
  NumCpuCoresEnabled: 36
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 72
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa0477f6f72612d30873c09
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa048d56176752d35caf7f3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa048d56176752d35caf7f3
  - ClassId: mo.MoRef
    Moid: 5fa048d56176752d35caf7f5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa048d56176752d35caf7f5
  - ClassId: mo.MoRef
    Moid: 5fa048d56176752d35caf7f7
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa048d56176752d35caf7f7
  - ClassId: mo.MoRef
    Moid: 5fa048d56176752d35caf7f9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa048d56176752d35caf7f9
  - ClassId: mo.MoRef
    Moid: 5fa048d56176752d35caf7fb
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa048d56176752d35caf7fb
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa047e86176752d35ca9abb
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa047e86176752d35ca9abb
  - ClassId: mo.MoRef
    Moid: 5fa047e86176752d35ca9abd
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa047e86176752d35ca9abd
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa0477f6f72612d30873c09
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa0477f6f72612d30873c09
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2016V2BB
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa0489b6176752d35cae158
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa0489b6176752d35cae158
  TopologyScanStatus: ''
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx4c-eu-spdc-FCH2016V2BB
  Uuid: 25B803A4-FACA-4FD4-ACEB-AEFDE133E7D6
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa048f06176752d35cafffb
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa048f06176752d35cafffb
  - ClassId: mo.MoRef
    Moid: 5fa049d86176752d35cb594c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa049d86176752d35cb594c
  - ClassId: mo.MoRef
    Moid: 5fa049d86176752d35cb5952
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa049d86176752d35cb5952
  - ClassId: mo.MoRef
    Moid: 5fa049d86176752d35cb595a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa049d86176752d35cb595a
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 025F4FB
  AvailableMemory: 524288
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa048a76176752d35cae521
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa048a76176752d35cae521
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d562526176752d35509e5b
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d562526176752d35509e5b
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa048a46176752d35cae414
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa048a46176752d35cae414
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa0499b6176752d35cb4736
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa0499b6176752d35cb4736
  Board:
    ClassId: mo.MoRef
    Moid: 5fa048ab6176752d35cae6b4
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa048ab6176752d35cae6b4
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb4b6176752d35de1ae1
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb4b6176752d35de1ae1
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa049976176752d35cb45d9
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa049976176752d35cb45d9
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb741636176752d35399934
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb741636176752d35399934
  - ClassId: mo.MoRef
    Moid: 5fb741636176752d35399936
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb741636176752d35399936
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7416e6176752d3539abd1
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb7416e6176752d3539abd1
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb741606176752d35399546
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb741606176752d35399546
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 36C 72T
  CreateTime: '2020-11-02T17:58:08.507Z'
  DeviceMoId: 5fa0489f6f72612d30878741
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa048ba6176752d35caed8a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa048ba6176752d35caed8a
  - ClassId: mo.MoRef
    Moid: 5fa048ba6176752d35caed8c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa048ba6176752d35caed8c
  - ClassId: mo.MoRef
    Moid: 5fa048ba6176752d35caed8e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa048ba6176752d35caed8e
  - ClassId: mo.MoRef
    Moid: 5fa048ba6176752d35caed90
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa048ba6176752d35caed90
  - ClassId: mo.MoRef
    Moid: 5fa048ba6176752d35caed92
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa048ba6176752d35caed92
  - ClassId: mo.MoRef
    Moid: 5fa048ba6176752d35caed94
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa048ba6176752d35caed94
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa049f56176752d35cb6427
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa049f56176752d35cb6427
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.50
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fa049856176752d35cb3ce0
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa049856176752d35cb3ce0
  LocatorLedOn: false
  ManagementIp: 10.58.28.50
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.50
  ModTime: '2022-10-05T22:01:40.488Z'
  Model: UCSC-C220-M4S
  Moid: 5fa048b06176752d35cae964
  Name: esx5-eu-spdc-FCH2017V024
  NumAdaptors: 4
  NumCpuCores: 36
  NumCpuCoresEnabled: 36
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 72
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa0489f6f72612d30878741
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa049cc6176752d35cb557e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa049cc6176752d35cb557e
  - ClassId: mo.MoRef
    Moid: 5fa049cc6176752d35cb5580
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa049cc6176752d35cb5580
  - ClassId: mo.MoRef
    Moid: 5fa049cc6176752d35cb5582
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa049cc6176752d35cb5582
  - ClassId: mo.MoRef
    Moid: 5fa049cc6176752d35cb5586
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa049cc6176752d35cb5586
  - ClassId: mo.MoRef
    Moid: 5fa049cc6176752d35cb5588
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa049cc6176752d35cb5588
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa048c86176752d35caf1f0
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa048c86176752d35caf1f0
  - ClassId: mo.MoRef
    Moid: 5fa048c86176752d35caf1f2
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa048c86176752d35caf1f2
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa0489f6f72612d30878741
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa0489f6f72612d30878741
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2017V024
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa049d16176752d35cb5742
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa049d16176752d35cb5742
  TopologyScanStatus: ''
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx5-eu-spdc-FCH2017V024
  Uuid: 7107D536-4CEB-4C61-9311-F056FF45D6AA
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa04b526176752d35cbe941
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04b526176752d35cbe941
  - ClassId: mo.MoRef
    Moid: 5fa04b526176752d35cbe947
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04b526176752d35cbe947
  - ClassId: mo.MoRef
    Moid: 5fa04b526176752d35cbe951
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04b526176752d35cbe951
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290579
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04aa26176752d35cba390
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa04aa26176752d35cba390
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d59a8b6176752d356f1774
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d59a8b6176752d356f1774
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa04ae16176752d35cbbce0
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa04ae16176752d35cbbce0
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa04b166176752d35cbce96
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa04b166176752d35cbce96
  Board:
    ClassId: mo.MoRef
    Moid: 5fa04aa36176752d35cba43f
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa04aa36176752d35cba43f
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb2c6176752d35de0ea6
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb2c6176752d35de0ea6
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04b136176752d35cbcd6d
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa04b136176752d35cbcd6d
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb76d0b6176752d354c2532
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb76d0b6176752d354c2532
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb76d166176752d354c28a1
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb76d166176752d354c28a1
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices:
  - ClassId: mo.MoRef
    Moid: 5fb76d0f6176752d354c26a8
    ObjectType: boot.UefiShellDevice
    link: https://www.intersight.com/api/v1/boot/UefiShellDevices/5fb76d0f6176752d354c26a8
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2020-11-02T18:06:26.398Z'
  DeviceMoId: 5fa04a9e6f72612d30880e03
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa04af46176752d35cbc2b2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04af46176752d35cbc2b2
  - ClassId: mo.MoRef
    Moid: 5fa04af46176752d35cbc2b4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04af46176752d35cbc2b4
  - ClassId: mo.MoRef
    Moid: 5fa04af46176752d35cbc2b6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04af46176752d35cbc2b6
  - ClassId: mo.MoRef
    Moid: 5fa04af46176752d35cbc2b8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04af46176752d35cbc2b8
  - ClassId: mo.MoRef
    Moid: 5fa04af46176752d35cbc2ba
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04af46176752d35cbc2ba
  - ClassId: mo.MoRef
    Moid: 5fa04af46176752d35cbc2bc
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04af46176752d35cbc2bc
  - ClassId: mo.MoRef
    Moid: 5fa04af46176752d35cbc2be
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04af46176752d35cbc2be
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa04b496176752d35cbe5b1
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa04b496176752d35cbe5b1
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.40
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fa04af86176752d35cbc3e7
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa04af86176752d35cbc3e7
  LocatorLedOn: false
  ManagementIp: 10.58.28.40
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.40
  ModTime: '2022-07-26T03:11:06.365Z'
  Model: UCSC-C220-M5SX
  Moid: 5fa04aa26176752d35cba3c9
  Name: mgmt-p1-eu-spdc-WZP2252176Z
  NumAdaptors: 0
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa04a9e6f72612d30880e03
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa04b1f6176752d35cbd290
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04b1f6176752d35cbd290
  - ClassId: mo.MoRef
    Moid: 5fa04b1f6176752d35cbd294
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04b1f6176752d35cbd294
  - ClassId: mo.MoRef
    Moid: 5fa04b1f6176752d35cbd296
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04b1f6176752d35cbd296
  - ClassId: mo.MoRef
    Moid: 5fa04b1f6176752d35cbd298
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04b1f6176752d35cbd298
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa04af26176752d35cbc201
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04af26176752d35cbc201
  - ClassId: mo.MoRef
    Moid: 5fa04af26176752d35cbc203
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04af26176752d35cbc203
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa04a9e6f72612d30880e03
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa04a9e6f72612d30880e03
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP2252176Z
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6165853976752d3139f5065d
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6165853976752d3139f5065d
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: mgmt-p1-eu-spdc
  Uuid: 8DC4924A-215D-4C2C-B0CC-134A4895031E
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa04c176176752d35cc2a4f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04c176176752d35cc2a4f
  - ClassId: mo.MoRef
    Moid: 5fa04c176176752d35cc2a5b
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04c176176752d35cc2a5b
  - ClassId: mo.MoRef
    Moid: 5fa04c176176752d35cc2a61
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04c176176752d35cc2a61
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 029056F
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04ba86176752d35cc03e3
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa04ba86176752d35cc03e3
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d58c7b6176752d3567e5e3
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d58c7b6176752d3567e5e3
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa04b616176752d35cbee67
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa04b616176752d35cbee67
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa04bcd6176752d35cc1066
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa04bcd6176752d35cc1066
  Board:
    ClassId: mo.MoRef
    Moid: 5fa04bae6176752d35cc060d
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa04bae6176752d35cc060d
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb476176752d35de192c
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb476176752d35de192c
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04bcc6176752d35cc101f
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa04bcc6176752d35cc101f
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734cb6176752d35337837
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb734cb6176752d35337837
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734d86176752d35337dcf
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb734d86176752d35337dcf
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734c96176752d35337781
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb734c96176752d35337781
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 44C 88T
  CreateTime: '2020-11-02T18:10:50.427Z'
  DeviceMoId: 5fa04b536f72612d30883fd0
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa04bb96176752d35cc08a3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04bb96176752d35cc08a3
  - ClassId: mo.MoRef
    Moid: 5fa04bb96176752d35cc08a7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04bb96176752d35cc08a7
  - ClassId: mo.MoRef
    Moid: 5fa04bb96176752d35cc08a9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04bb96176752d35cc08a9
  - ClassId: mo.MoRef
    Moid: 5fa04bb96176752d35cc08ab
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04bb96176752d35cc08ab
  - ClassId: mo.MoRef
    Moid: 5fa04bb96176752d35cc08ad
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04bb96176752d35cc08ad
  - ClassId: mo.MoRef
    Moid: 5fa04bb96176752d35cc08af
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04bb96176752d35cc08af
  - ClassId: mo.MoRef
    Moid: 5fa04bb96176752d35cc08b1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04bb96176752d35cc08b1
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa04c0e6176752d35cc2833
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa04c0e6176752d35cc2833
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.41
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fa04bbe6176752d35cc0b73
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa04bbe6176752d35cc0b73
  LocatorLedOn: false
  ManagementIp: 10.58.28.41
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.41
  ModTime: '2022-08-03T14:56:51.595Z'
  Model: UCSC-C220-M5SX
  Moid: 5fa04baa6176752d35cc0518
  Name: aio-1-p1-eu-spdc-WZP22490ZCU
  NumAdaptors: 0
  NumCpuCores: 44
  NumCpuCoresEnabled: 44
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 88
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa04b536f72612d30883fd0
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa04be46176752d35cc18d0
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04be46176752d35cc18d0
  - ClassId: mo.MoRef
    Moid: 5fa04be46176752d35cc18d3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04be46176752d35cc18d3
  - ClassId: mo.MoRef
    Moid: 5fa04be46176752d35cc18d5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04be46176752d35cc18d5
  - ClassId: mo.MoRef
    Moid: 5fa04be46176752d35cc18d7
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04be46176752d35cc18d7
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa04bb76176752d35cc0822
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04bb76176752d35cc0822
  - ClassId: mo.MoRef
    Moid: 5fa04bb76176752d35cc0824
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04bb76176752d35cc0824
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa04b536f72612d30883fd0
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa04b536f72612d30883fd0
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22490ZCU
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa04be26176752d35cc17d7
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa04be26176752d35cc17d7
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio-1-p1-eu-spdc
  Uuid: B16A1200-1CCF-42EA-8B33-6C4D50110704
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa04ca66176752d35cc56c6
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04ca66176752d35cc56c6
  - ClassId: mo.MoRef
    Moid: 5fa04ca66176752d35cc56cc
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04ca66176752d35cc56cc
  - ClassId: mo.MoRef
    Moid: 5fa04ca66176752d35cc56d2
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04ca66176752d35cc56d2
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 029057B
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04bee6176752d35cc1c47
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa04bee6176752d35cc1c47
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d58c7b6176752d3567e5a2
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d58c7b6176752d3567e5a2
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa04bec6176752d35cc1bb2
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa04bec6176752d35cc1bb2
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa04c626176752d35cc3fb1
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa04c626176752d35cc3fb1
  Board:
    ClassId: mo.MoRef
    Moid: 5fa04c3e6176752d35cc369a
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa04c3e6176752d35cc369a
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdd093c6176752d35e3b88c
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdd093c6176752d35e3b88c
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04c626176752d35cc3fc7
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa04c626176752d35cc3fc7
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734ca6176752d353377f9
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb734ca6176752d353377f9
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734d56176752d35337b8c
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb734d56176752d35337b8c
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734c86176752d3533771d
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb734c86176752d3533771d
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2020-11-02T18:13:14.246Z'
  DeviceMoId: 5fa04be16f72612d30886344
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa04c486176752d35cc3934
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04c486176752d35cc3934
  - ClassId: mo.MoRef
    Moid: 5fa04c486176752d35cc3936
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04c486176752d35cc3936
  - ClassId: mo.MoRef
    Moid: 5fa04c486176752d35cc3938
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04c486176752d35cc3938
  - ClassId: mo.MoRef
    Moid: 5fa04c486176752d35cc393b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04c486176752d35cc393b
  - ClassId: mo.MoRef
    Moid: 5fa04c486176752d35cc393d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04c486176752d35cc393d
  - ClassId: mo.MoRef
    Moid: 5fa04c486176752d35cc3940
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04c486176752d35cc3940
  - ClassId: mo.MoRef
    Moid: 5fa04c486176752d35cc3942
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04c486176752d35cc3942
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa04c9e6176752d35cc5446
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa04c9e6176752d35cc5446
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.42
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 61968b2f76752d31390c6458
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61968b2f76752d31390c6458
  LocatorLedOn: false
  ManagementIp: 10.58.28.42
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2400'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.42
  ModTime: '2022-10-05T21:56:10.329Z'
  Model: UCSC-C220-M5SX
  Moid: 5fa04c3a6176752d35cc3569
  Name: aio-2-p1-eu-spdc-WZP22520Y69
  NumAdaptors: 0
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa04be16f72612d30886344
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa04c736176752d35cc4535
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04c736176752d35cc4535
  - ClassId: mo.MoRef
    Moid: 5fa04c736176752d35cc4537
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04c736176752d35cc4537
  - ClassId: mo.MoRef
    Moid: 5fa04c736176752d35cc4539
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04c736176752d35cc4539
  - ClassId: mo.MoRef
    Moid: 5fa04c736176752d35cc453b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04c736176752d35cc453b
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa04c466176752d35cc38b2
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04c466176752d35cc38b2
  - ClassId: mo.MoRef
    Moid: 5fa04c466176752d35cc38b4
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04c466176752d35cc38b4
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa04be16f72612d30886344
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa04be16f72612d30886344
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520Y69
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa04c716176752d35cc44ae
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa04c716176752d35cc44ae
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio-2-p1-eu-spdc
  Uuid: B77E1C5B-A922-4F03-8DC2-F7BFEAE3245B
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa04d7e6176752d35cca241
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04d7e6176752d35cca241
  - ClassId: mo.MoRef
    Moid: 5fa04d7e6176752d35cca247
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04d7e6176752d35cca247
  - ClassId: mo.MoRef
    Moid: 5fa04d7e6176752d35cca252
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04d7e6176752d35cca252
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290576
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04cbc6176752d35cc5f12
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa04cbc6176752d35cc5f12
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d591f66176752d356a9a26
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d591f66176752d356a9a26
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa04cbf6176752d35cc6013
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa04cbf6176752d35cc6013
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa04d376176752d35cc8ccf
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa04d376176752d35cc8ccf
  Board:
    ClassId: mo.MoRef
    Moid: 5fa04d156176752d35cc80c2
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa04d156176752d35cc80c2
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdd04556176752d35e199f0
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdd04556176752d35e199f0
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04d3a6176752d35cc8e38
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa04d3a6176752d35cc8e38
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7ebbb6176752d357bc12c
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb7ebbb6176752d357bc12c
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7ebc66176752d357bc5a8
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb7ebc66176752d357bc5a8
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7ebb96176752d357bc05a
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb7ebb96176752d357bc05a
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 44C 88T
  CreateTime: '2020-11-02T18:15:29.841Z'
  DeviceMoId: 5fa04cb86f72612d30889bc8
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa04d206176752d35cc846b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04d206176752d35cc846b
  - ClassId: mo.MoRef
    Moid: 5fa04d206176752d35cc846e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04d206176752d35cc846e
  - ClassId: mo.MoRef
    Moid: 5fa04d206176752d35cc8470
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04d206176752d35cc8470
  - ClassId: mo.MoRef
    Moid: 5fa04d206176752d35cc8474
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04d206176752d35cc8474
  - ClassId: mo.MoRef
    Moid: 5fa04d206176752d35cc8476
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04d206176752d35cc8476
  - ClassId: mo.MoRef
    Moid: 5fa04d206176752d35cc8478
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04d206176752d35cc8478
  - ClassId: mo.MoRef
    Moid: 5fa04d206176752d35cc847a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04d206176752d35cc847a
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa04d756176752d35cc9fcd
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa04d756176752d35cc9fcd
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.43
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fa04d246176752d35cc8624
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa04d246176752d35cc8624
  LocatorLedOn: false
  ManagementIp: 10.58.28.43
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.43
  ModTime: '2022-08-03T14:47:23.602Z'
  Model: UCSC-C220-M5SX
  Moid: 5fa04cc16176752d35cc60ce
  Name: aio-3-p1-eu-spdc-WZP22520Y54
  NumAdaptors: 0
  NumCpuCores: 44
  NumCpuCoresEnabled: 44
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 88
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa04cb86f72612d30889bc8
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa04d4b6176752d35cc938e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04d4b6176752d35cc938e
  - ClassId: mo.MoRef
    Moid: 5fa04d4b6176752d35cc9390
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04d4b6176752d35cc9390
  - ClassId: mo.MoRef
    Moid: 5fa04d4b6176752d35cc9392
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04d4b6176752d35cc9392
  - ClassId: mo.MoRef
    Moid: 5fa04d4b6176752d35cc9394
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04d4b6176752d35cc9394
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa04d1e6176752d35cc835f
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04d1e6176752d35cc835f
  - ClassId: mo.MoRef
    Moid: 5fa04d1e6176752d35cc8364
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04d1e6176752d35cc8364
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa04cb86f72612d30889bc8
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa04cb86f72612d30889bc8
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520Y54
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa04d496176752d35cc92d1
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa04d496176752d35cc92d1
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio-3-p1-eu-spdc
  Uuid: C0977AF8-616A-4445-A85B-7E5A72A797E2
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa04e926176752d35cd0f34
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04e926176752d35cd0f34
  - ClassId: mo.MoRef
    Moid: 5fa04e926176752d35cd0f3e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04e926176752d35cd0f3e
  - ClassId: mo.MoRef
    Moid: 5fa04e926176752d35cd0f44
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04e926176752d35cd0f44
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290577
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04e246176752d35cce117
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa04e246176752d35cce117
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5b6ae6176752d357def31
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5b6ae6176752d357def31
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa04dd76176752d35ccc001
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa04dd76176752d35ccc001
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa04e4a6176752d35ccf4ef
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa04e4a6176752d35ccf4ef
  Board:
    ClassId: mo.MoRef
    Moid: 5fa04e2b6176752d35cce412
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa04e2b6176752d35cce412
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb2c6176752d35de0eb6
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb2c6176752d35de0eb6
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04e4a6176752d35ccf4b8
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa04e4a6176752d35ccf4b8
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734cb6176752d35337841
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb734cb6176752d35337841
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb734d96176752d35337de8
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb734d96176752d35337de8
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2020-11-02T18:21:26.472Z'
  DeviceMoId: 5fa04dd16f72612d3088e6b1
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa04e346176752d35cceb2c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e346176752d35cceb2c
  - ClassId: mo.MoRef
    Moid: 5fa04e346176752d35cceb2e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e346176752d35cceb2e
  - ClassId: mo.MoRef
    Moid: 5fa04e346176752d35cceb30
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e346176752d35cceb30
  - ClassId: mo.MoRef
    Moid: 5fa04e346176752d35cceb32
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e346176752d35cceb32
  - ClassId: mo.MoRef
    Moid: 5fa04e346176752d35cceb34
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e346176752d35cceb34
  - ClassId: mo.MoRef
    Moid: 5fa04e346176752d35cceb36
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e346176752d35cceb36
  - ClassId: mo.MoRef
    Moid: 5fa04e346176752d35cceb38
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e346176752d35cceb38
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa04e896176752d35cd0af1
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa04e896176752d35cd0af1
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.44
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 61ae94b876752d3139ced1f2
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61ae94b876752d3139ced1f2
  LocatorLedOn: false
  ManagementIp: 10.58.28.44
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.44
  ModTime: '2022-10-05T21:56:19.181Z'
  Model: UCSC-C220-M5SX
  Moid: 5fa04e266176752d35cce224
  Name: comp1-p1-eu-spdc-WZP22520Y9J
  NumAdaptors: 0
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa04dd16f72612d3088e6b1
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa04e5f6176752d35ccfbc6
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04e5f6176752d35ccfbc6
  - ClassId: mo.MoRef
    Moid: 5fa04e5f6176752d35ccfbc8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04e5f6176752d35ccfbc8
  - ClassId: mo.MoRef
    Moid: 5fa04e5f6176752d35ccfbca
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04e5f6176752d35ccfbca
  - ClassId: mo.MoRef
    Moid: 5fa04e5f6176752d35ccfbcc
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04e5f6176752d35ccfbcc
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa04e326176752d35ccea09
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04e326176752d35ccea09
  - ClassId: mo.MoRef
    Moid: 5fa04e326176752d35ccea0b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04e326176752d35ccea0b
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa04dd16f72612d3088e6b1
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa04dd16f72612d3088e6b1
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520Y9J
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa04e5d6176752d35ccfb19
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa04e5d6176752d35ccfb19
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp1-p1-eu-spdc
  Uuid: 5EC2C483-EF7D-4DEB-82F9-52DA099DF38A
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa04ef96176752d35cd3429
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04ef96176752d35cd3429
  - ClassId: mo.MoRef
    Moid: 5fa04ef96176752d35cd342f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04ef96176752d35cd342f
  - ClassId: mo.MoRef
    Moid: 5fa04ef96176752d35cd3439
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa04ef96176752d35cd3439
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 029056D
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04e876176752d35cd0a33
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa04e876176752d35cd0a33
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d575d66176752d355b59c2
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d575d66176752d355b59c2
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa04e756176752d35cd02fd
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa04e756176752d35cd02fd
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa04eaf6176752d35cd1b47
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa04eaf6176752d35cd1b47
  Board:
    ClassId: mo.MoRef
    Moid: 5fa04e936176752d35cd0fa6
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa04e936176752d35cd0fa6
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb466176752d35de18b9
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb466176752d35de18b9
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa04eac6176752d35cd1a35
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa04eac6176752d35cd1a35
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf7d6176752d3570bcfe
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb7cf7d6176752d3570bcfe
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf876176752d3570c289
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb7cf876176752d3570c289
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf7d6176752d3570bcb3
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb7cf7d6176752d3570bcb3
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2020-11-02T18:23:10.313Z'
  DeviceMoId: 5fa04e6c6f72612d30890d70
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa04e9d6176752d35cd1415
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e9d6176752d35cd1415
  - ClassId: mo.MoRef
    Moid: 5fa04e9d6176752d35cd1417
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e9d6176752d35cd1417
  - ClassId: mo.MoRef
    Moid: 5fa04e9d6176752d35cd1419
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e9d6176752d35cd1419
  - ClassId: mo.MoRef
    Moid: 5fa04e9d6176752d35cd141b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e9d6176752d35cd141b
  - ClassId: mo.MoRef
    Moid: 5fa04e9d6176752d35cd141e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e9d6176752d35cd141e
  - ClassId: mo.MoRef
    Moid: 5fa04e9d6176752d35cd1420
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e9d6176752d35cd1420
  - ClassId: mo.MoRef
    Moid: 5fa04e9d6176752d35cd1422
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa04e9d6176752d35cd1422
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa04ef06176752d35cd325b
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa04ef06176752d35cd325b
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.45
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fa04ea66176752d35cd1794
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa04ea66176752d35cd1794
  LocatorLedOn: false
  ManagementIp: 10.58.28.45
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.45
  ModTime: '2022-08-03T14:56:57.549Z'
  Model: UCSC-C220-M5SX
  Moid: 5fa04e8e6176752d35cd0c4e
  Name: comp2-p1-spdc-WZP22520Y95
  NumAdaptors: 0
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa04e6c6f72612d30890d70
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa04ec46176752d35cd2316
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04ec46176752d35cd2316
  - ClassId: mo.MoRef
    Moid: 5fa04ec56176752d35cd231d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04ec56176752d35cd231d
  - ClassId: mo.MoRef
    Moid: 5fa04ec56176752d35cd2323
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04ec56176752d35cd2323
  - ClassId: mo.MoRef
    Moid: 5fa04ec56176752d35cd232f
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa04ec56176752d35cd232f
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa04e996176752d35cd120b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04e996176752d35cd120b
  - ClassId: mo.MoRef
    Moid: 5fa04e996176752d35cd120e
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa04e996176752d35cd120e
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa04e6c6f72612d30890d70
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa04e6c6f72612d30890d70
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520Y95
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa04eca6176752d35cd25e8
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa04eca6176752d35cd25e8
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp2-p1-eu-spdc
  Uuid: C90F8850-824A-4E87-A970-D03B9F8A601C
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa051916176752d35ce10d6
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa051916176752d35ce10d6
  - ClassId: mo.MoRef
    Moid: 5fa0524f6176752d35ce4d6a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa0524f6176752d35ce4d6a
  - ClassId: mo.MoRef
    Moid: 5fa0524f6176752d35ce4d70
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa0524f6176752d35ce4d70
  - ClassId: mo.MoRef
    Moid: 5fa0524f6176752d35ce4d76
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa0524f6176752d35ce4d76
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 025F533
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa0517a6176752d35ce0741
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa0517a6176752d35ce0741
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d591fb6176752d356a9bba
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d591fb6176752d356a9bba
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa0519d6176752d35ce1402
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa0519d6176752d35ce1402
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa051ea6176752d35ce2c6d
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa051ea6176752d35ce2c6d
  Board:
    ClassId: mo.MoRef
    Moid: 5fa051826176752d35ce0a84
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa051826176752d35ce0a84
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdd09406176752d35e3ba02
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdd09406176752d35e3ba02
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa051da6176752d35ce270f
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa051da6176752d35ce270f
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb83fff6176752d359bdf9c
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb83fff6176752d359bdf9c
  - ClassId: mo.MoRef
    Moid: 5fb83fff6176752d359bdf9e
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb83fff6176752d359bdf9e
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb8400a6176752d359be295
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb8400a6176752d359be295
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb83ffc6176752d359bdee9
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb83ffc6176752d359bdee9
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2020-11-02T18:35:45.061Z'
  DeviceMoId: 5fa051776f72612d3089d7e9
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa051c16176752d35ce1ecb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa051c16176752d35ce1ecb
  - ClassId: mo.MoRef
    Moid: 5fa051c16176752d35ce1ecd
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa051c16176752d35ce1ecd
  - ClassId: mo.MoRef
    Moid: 5fa051c16176752d35ce1ecf
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa051c16176752d35ce1ecf
  - ClassId: mo.MoRef
    Moid: 5fa051c16176752d35ce1ed1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa051c16176752d35ce1ed1
  - ClassId: mo.MoRef
    Moid: 5fa051c16176752d35ce1ed3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa051c16176752d35ce1ed3
  - ClassId: mo.MoRef
    Moid: 5fa051c16176752d35ce1ed5
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa051c16176752d35ce1ed5
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa053c56176752d35ceca57
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa053c56176752d35ceca57
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.47
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 5fa051c26176752d35ce1f4b
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa051c26176752d35ce1f4b
  LocatorLedOn: false
  ManagementIp: 10.58.28.47
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.47
  ModTime: '2021-10-13T11:54:48.539Z'
  Model: UCSC-C220-M4S
  Moid: 5fa051816176752d35ce095c
  Name: comp4-p1-eu-spdc-FCH2016V23J
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa051776f72612d3089d7e9
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa052126176752d35ce395e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa052126176752d35ce395e
  - ClassId: mo.MoRef
    Moid: 5fa052126176752d35ce3960
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa052126176752d35ce3960
  - ClassId: mo.MoRef
    Moid: 5fa052126176752d35ce3962
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa052126176752d35ce3962
  - ClassId: mo.MoRef
    Moid: 5fa052126176752d35ce3964
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa052126176752d35ce3964
  - ClassId: mo.MoRef
    Moid: 5fa052126176752d35ce3966
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa052126176752d35ce3966
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 5dee1d736972652d321d26b5
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa051c26176752d35ce1f0e
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa051c26176752d35ce1f0e
  - ClassId: mo.MoRef
    Moid: 5fa051c26176752d35ce1f10
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa051c26176752d35ce1f10
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa051776f72612d3089d7e9
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa051776f72612d3089d7e9
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2016V23J
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa052076176752d35ce3663
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa052076176752d35ce3663
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp4-p1-eu-spdc
  Uuid: 255683B2-E6D9-499E-8384-37C90BE802FA
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa052b06176752d35ce696c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa052b06176752d35ce696c
  - ClassId: mo.MoRef
    Moid: 5fa053576176752d35cea64b
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa053576176752d35cea64b
  - ClassId: mo.MoRef
    Moid: 5fa053576176752d35cea653
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa053576176752d35cea653
  - ClassId: mo.MoRef
    Moid: 5fa053576176752d35cea65b
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa053576176752d35cea65b
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 025F4EA
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa052a26176752d35ce6566
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa052a26176752d35ce6566
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d583ea6176752d35633d48
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d583ea6176752d35633d48
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa0529c6176752d35ce63d3
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa0529c6176752d35ce63d3
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa052ff6176752d35ce8565
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa052ff6176752d35ce8565
  Board:
    ClassId: mo.MoRef
    Moid: 5fa052c46176752d35ce6e63
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa052c46176752d35ce6e63
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdcfb4a6176752d35de1a05
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdcfb4a6176752d35de1a05
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa052f86176752d35ce8293
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa052f86176752d35ce8293
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf7e6176752d3570bd86
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb7cf7e6176752d3570bd86
  - ClassId: mo.MoRef
    Moid: 5fb7cf7e6176752d3570bd88
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fb7cf7e6176752d3570bd88
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf8a6176752d3570c383
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fb7cf8a6176752d3570c383
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fb7cf7c6176752d3570bc51
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fb7cf7c6176752d3570bc51
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2020-11-02T18:40:34.595Z'
  DeviceMoId: 5fa052926f72612d308a2325
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa052de6176752d35ce77a9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa052de6176752d35ce77a9
  - ClassId: mo.MoRef
    Moid: 5fa052de6176752d35ce77ab
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa052de6176752d35ce77ab
  - ClassId: mo.MoRef
    Moid: 5fa052de6176752d35ce77ad
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa052de6176752d35ce77ad
  - ClassId: mo.MoRef
    Moid: 5fa052de6176752d35ce77b0
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa052de6176752d35ce77b0
  - ClassId: mo.MoRef
    Moid: 5fa052de6176752d35ce77b5
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa052de6176752d35ce77b5
  - ClassId: mo.MoRef
    Moid: 5fa052de6176752d35ce77ba
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa052de6176752d35ce77ba
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa054c56176752d35cf1ea9
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa054c56176752d35cf1ea9
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.48
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 5fa052de6176752d35ce77cd
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa052de6176752d35ce77cd
  LocatorLedOn: false
  ManagementIp: 10.58.28.48
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.48
  ModTime: '2021-10-13T11:54:31.849Z'
  Model: UCSC-C220-M4S
  Moid: 5fa052a26176752d35ce6572
  Name: comp5-p1-eu-spdc-FCH2017V0TN
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa052926f72612d308a2325
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa053206176752d35ce93df
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa053206176752d35ce93df
  - ClassId: mo.MoRef
    Moid: 5fa053206176752d35ce93e1
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa053206176752d35ce93e1
  - ClassId: mo.MoRef
    Moid: 5fa053206176752d35ce93e3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa053206176752d35ce93e3
  - ClassId: mo.MoRef
    Moid: 5fa053206176752d35ce93e5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa053206176752d35ce93e5
  - ClassId: mo.MoRef
    Moid: 5fa053206176752d35ce93e7
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa053206176752d35ce93e7
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 5dee1d736972652d321d26b5
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa052d16176752d35ce722a
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa052d16176752d35ce722a
  - ClassId: mo.MoRef
    Moid: 5fa052d16176752d35ce722c
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa052d16176752d35ce722c
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa052926f72612d308a2325
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa052926f72612d308a2325
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2017V0TN
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa053226176752d35ce94b9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa053226176752d35ce94b9
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp5-p1-eu-spdc
  Uuid: DDF98507-2D6C-47D0-91B1-8D1055824D36
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fa1a8086176752d354890a8
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa1a8086176752d354890a8
  - ClassId: mo.MoRef
    Moid: 5fa1a8086176752d354890b0
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fa1a8086176752d354890b0
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fa1a79a6176752d35486b1c
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fa1a79a6176752d35486b1c
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60df21356176752d35fcc0fa
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60df21356176752d35fcc0fa
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fa1a79a6176752d35486add
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fa1a79a6176752d35486add
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fa1a7c96176752d35487b5d
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fa1a7c96176752d35487b5d
  Board:
    ClassId: mo.MoRef
    Moid: 5fa1a79f6176752d35486cb5
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fa1a79f6176752d35486cb5
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 60c703386176752d35d8fa4c
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/60c703386176752d35d8fa4c
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fa1a7c46176752d3548796a
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fa1a7c46176752d3548796a
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2020-11-03T18:55:23.726Z'
  DeviceMoId: 5fa1a78b6f72612d30e49bd3
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fa1a7aa6176752d35487019
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa1a7aa6176752d35487019
  - ClassId: mo.MoRef
    Moid: 5fa1a7aa6176752d3548701b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa1a7aa6176752d3548701b
  - ClassId: mo.MoRef
    Moid: 5fa1a7aa6176752d3548701e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa1a7aa6176752d3548701e
  - ClassId: mo.MoRef
    Moid: 5fa1a7aa6176752d35487020
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa1a7aa6176752d35487020
  - ClassId: mo.MoRef
    Moid: 5fa1a7aa6176752d35487022
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa1a7aa6176752d35487022
  - ClassId: mo.MoRef
    Moid: 5fa1a7aa6176752d35487024
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa1a7aa6176752d35487024
  - ClassId: mo.MoRef
    Moid: 5fa1a7aa6176752d35487026
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fa1a7aa6176752d35487026
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fa1a7ff6176752d35488ce1
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fa1a7ff6176752d35488ce1
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.25.52
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.25.62
    Dn: sys/rack-unit-1/mgmt/if-1
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 5
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.224
    Type: MgmtInterface
  KvmServerStateEnabled: false
  KvmVendor: Avocent
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 5fa1a7ae6176752d354871dd
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fa1a7ae6176752d354871dd
  LocatorLedOn: false
  ManagementIp: 10.58.25.52
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2400'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.25.52
  ModTime: '2022-07-25T11:59:18.409Z'
  Model: UCSC-C240-M5SX
  Moid: 5fa1a79b6176752d35486b5c
  Name: tnas-eu-spdc-WZP22511E68
  NumAdaptors: 0
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fa1a78b6f72612d30e49bd3
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fa1a7d46176752d35487ed5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa1a7d46176752d35487ed5
  - ClassId: mo.MoRef
    Moid: 5fa1a7d46176752d35487ed7
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa1a7d46176752d35487ed7
  - ClassId: mo.MoRef
    Moid: 5fa1a7d46176752d35487ed9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fa1a7d46176752d35487ed9
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fa1a7a86176752d35486f72
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa1a7a86176752d35486f72
  - ClassId: mo.MoRef
    Moid: 5fa1a7a86176752d35486f74
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fa1a7a86176752d35486f74
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fa1a78b6f72612d30e49bd3
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fa1a78b6f72612d30e49bd3
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 6102f84676752d3131905070
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/6102f84676752d3131905070
  Serial: WZP22511E68
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fa1a7d26176752d35487e63
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fa1a7d26176752d35487e63
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: tnas-eu-spdc-WZP22511E68
  Uuid: E387E164-5C97-4D36-9354-5A324E9AF813
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fdf9bf46176752d35e4426e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdf9bf46176752d35e4426e
  - ClassId: mo.MoRef
    Moid: 5fdf9c886176752d35e477e4
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477e4
  - ClassId: mo.MoRef
    Moid: 5fdf9c886176752d35e477ea
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477ea
  - ClassId: mo.MoRef
    Moid: 5fdf9c886176752d35e477f0
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdf9c886176752d35e477f0
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 022C2F4
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fdf9bff6176752d35e4471c
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fdf9bff6176752d35e4471c
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5fbe96176752d35a30aa7
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5fbe96176752d35a30aa7
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fdf9bfe6176752d35e446cf
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fdf9bfe6176752d35e446cf
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fdf9c416176752d35e45e43
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fdf9c416176752d35e45e43
  Board:
    ClassId: mo.MoRef
    Moid: 5fdf9c056176752d35e44930
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fdf9c056176752d35e44930
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdf9c2d6176752d35e45801
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9c2d6176752d35e45801
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fdf9c2d6176752d35e457e2
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9c2d6176752d35e457e2
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 60000c0b6176752d35b76e3e
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/60000c0b6176752d35b76e3e
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 60000c046176752d35b76bb3
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/60000c046176752d35b76bb3
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 6013f1496176752d35458e49
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1496176752d35458e49
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2020-12-20T18:46:25.383Z'
  DeviceMoId: 5fdf9be76f72612d300a8d81
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fdf9c106176752d35e44d71
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d71
  - ClassId: mo.MoRef
    Moid: 5fdf9c106176752d35e44d73
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d73
  - ClassId: mo.MoRef
    Moid: 5fdf9c106176752d35e44d75
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d75
  - ClassId: mo.MoRef
    Moid: 5fdf9c106176752d35e44d77
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d77
  - ClassId: mo.MoRef
    Moid: 5fdf9c106176752d35e44d79
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d79
  - ClassId: mo.MoRef
    Moid: 5fdf9c106176752d35e44d7b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d7b
  - ClassId: mo.MoRef
    Moid: 5fdf9c106176752d35e44d7d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9c106176752d35e44d7d
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fdf9c7f6176752d35e473d9
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9c7f6176752d35e473d9
  GraphicsCards: []
  Groups: p2b
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.41
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
    Moid: 5fdf9c146176752d35e44eca
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdf9c146176752d35e44eca
  LocatorLedOn: false
  ManagementIp: 10.58.50.41
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.41
  ModTime: '2022-09-22T18:21:01.939Z'
  Model: UCSC-C240-M5SN
  Moid: 5fdf9c016176752d35e44795
  Name: aio-1-p2b-eu-spdc-WZP23400AJW
  NumAdaptors: 1
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fdf9be76f72612d300a8d81
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fdf9c546176752d35e465cd
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465cd
  - ClassId: mo.MoRef
    Moid: 5fdf9c546176752d35e465cf
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465cf
  - ClassId: mo.MoRef
    Moid: 5fdf9c546176752d35e465d1
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d1
  - ClassId: mo.MoRef
    Moid: 5fdf9c546176752d35e465d3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d3
  - ClassId: mo.MoRef
    Moid: 5fdf9c546176752d35e465d9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9c546176752d35e465d9
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fdf9c0d6176752d35e44cf7
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fdf9c0d6176752d35e44cf7
  - ClassId: mo.MoRef
    Moid: 5fdf9c0d6176752d35e44cf9
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fdf9c0d6176752d35e44cf9
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fdf9be76f72612d300a8d81
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9be76f72612d300a8d81
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23400AJW
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fdf9c526176752d35e46529
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fdf9c526176752d35e46529
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio-1-p2b-eu-spdc-WZP23400AJW
  Uuid: 488930EF-5754-434B-B570-C2BD8359E739
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
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
  CreateTime: '2020-12-20T18:48:24.465Z'
  DeviceMoId: 5fdf9c676f72612d300a9c8d
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
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
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fdf9cf66176752d35e4a75b
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9cf66176752d35e4a75b
  GraphicsCards: []
  Groups: p2b
  HardwareUuid: ''
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
  LocatorLedOn: false
  ManagementIp: 10.58.50.42
  ManagementMode: IntersightStandalone
  MemoryArrays: []
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
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
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
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
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fdf9cf56176752d35e4a70f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdf9cf56176752d35e4a70f
  - ClassId: mo.MoRef
    Moid: 5fdf9d896176752d35e4e0b6
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdf9d896176752d35e4e0b6
  - ClassId: mo.MoRef
    Moid: 5fdf9d896176752d35e4e0bc
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdf9d896176752d35e4e0bc
  - ClassId: mo.MoRef
    Moid: 5fdf9d896176752d35e4e0c2
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdf9d896176752d35e4e0c2
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 022C2CE
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fdf9d006176752d35e4aae0
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fdf9d006176752d35e4aae0
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5ee266176752d359b9a6f
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5ee266176752d359b9a6f
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fdf9cfd6176752d35e4aa25
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fdf9cfd6176752d35e4aa25
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fdf9d426176752d35e4c645
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fdf9d426176752d35e4c645
  Board:
    ClassId: mo.MoRef
    Moid: 5fdf9d066176752d35e4aebe
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fdf9d066176752d35e4aebe
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdf9d2f6176752d35e4bf2f
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdf9d2f6176752d35e4bf2f
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fdf9d2e6176752d35e4bef4
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdf9d2e6176752d35e4bef4
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 60000c046176752d35b76bd5
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/60000c046176752d35b76bd5
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 60000bfd6176752d35b7692a
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/60000bfd6176752d35b7692a
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 6013f1486176752d35458daf
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/6013f1486176752d35458daf
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2020-12-20T18:50:42.597Z'
  DeviceMoId: 5fdf9cf26f72612d300aaca0
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fdf9d116176752d35e4b355
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b355
  - ClassId: mo.MoRef
    Moid: 5fdf9d116176752d35e4b357
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b357
  - ClassId: mo.MoRef
    Moid: 5fdf9d116176752d35e4b359
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b359
  - ClassId: mo.MoRef
    Moid: 5fdf9d116176752d35e4b35b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b35b
  - ClassId: mo.MoRef
    Moid: 5fdf9d116176752d35e4b35d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b35d
  - ClassId: mo.MoRef
    Moid: 5fdf9d116176752d35e4b35f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b35f
  - ClassId: mo.MoRef
    Moid: 5fdf9d116176752d35e4b361
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdf9d116176752d35e4b361
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fdf9d806176752d35e4de4d
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdf9d806176752d35e4de4d
  GraphicsCards: []
  Groups: p2b
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.43
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
    Moid: 5fdf9d156176752d35e4b534
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdf9d156176752d35e4b534
  LocatorLedOn: false
  ManagementIp: 10.58.50.43
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.43
  ModTime: '2022-09-30T16:16:42.294Z'
  Model: UCSC-C240-M5SN
  Moid: 5fdf9d026176752d35e4ac4e
  Name: aio-3-p2b-eu-spdc-WZP23400AKL
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
  - 5fdf9cf26f72612d300aaca0
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fdf9d556176752d35e4cd3d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd3d
  - ClassId: mo.MoRef
    Moid: 5fdf9d556176752d35e4cd41
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd41
  - ClassId: mo.MoRef
    Moid: 5fdf9d556176752d35e4cd43
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd43
  - ClassId: mo.MoRef
    Moid: 5fdf9d556176752d35e4cd48
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9d556176752d35e4cd48
  - ClassId: mo.MoRef
    Moid: 5fdf9d566176752d35e4cd4a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdf9d566176752d35e4cd4a
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fdf9d0f6176752d35e4b2a3
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fdf9d0f6176752d35e4b2a3
  - ClassId: mo.MoRef
    Moid: 5fdf9d0f6176752d35e4b2a5
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fdf9d0f6176752d35e4b2a5
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fdf9cf26f72612d300aaca0
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9cf26f72612d300aaca0
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23400AKL
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fdf9d536176752d35e4cc5f
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fdf9d536176752d35e4cc5f
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio-3-p2b-eu-spdc-WZP23400AKL
  Uuid: 11942B96-9C29-4871-924F-F42877A98020
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fdfa1736176752d35e673d8
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfa1736176752d35e673d8
  - ClassId: mo.MoRef
    Moid: 5fdfa2076176752d35e6b71d
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfa2076176752d35e6b71d
  - ClassId: mo.MoRef
    Moid: 5fdfa2076176752d35e6b726
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfa2076176752d35e6b726
  - ClassId: mo.MoRef
    Moid: 5fdfa2076176752d35e6b72f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfa2076176752d35e6b72f
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 022C2B2
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fdfa17d6176752d35e677fe
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fdfa17d6176752d35e677fe
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5fbe96176752d35a30a97
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5fbe96176752d35a30a97
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fdfa17b6176752d35e67765
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fdfa17b6176752d35e67765
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fdfa1bc6176752d35e693d4
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fdfa1bc6176752d35e693d4
  Board:
    ClassId: mo.MoRef
    Moid: 5fdfa1846176752d35e67a50
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fdfa1846176752d35e67a50
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdfa1a86176752d35e68947
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdfa1a86176752d35e68947
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fdfa1a86176752d35e6896b
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdfa1a86176752d35e6896b
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 60000bfa6176752d35b76833
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/60000bfa6176752d35b76833
  - ClassId: mo.MoRef
    Moid: 61b9d31376752d31394dd98b
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61b9d31376752d31394dd98b
  - ClassId: mo.MoRef
    Moid: 61c1e5c376752d3139f1d90a
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61c1e5c376752d3139f1d90a
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 60000bf76176752d35b76641
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/60000bf76176752d35b76641
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 6013f13a6176752d35458792
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/6013f13a6176752d35458792
  - ClassId: mo.MoRef
    Moid: 61b9d31376752d31394dd99b
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/61b9d31376752d31394dd99b
  - ClassId: mo.MoRef
    Moid: 61c1e32276752d3139f1582d
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/61c1e32276752d3139f1582d
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2020-12-20T19:09:52.345Z'
  DeviceMoId: 5fdfa1686f72612d300b383f
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e6a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e6a
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e70
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e70
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e72
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e72
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e74
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e74
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e76
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e76
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e78
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e78
  - ClassId: mo.MoRef
    Moid: 5fdfa18f6176752d35e67e7a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfa18f6176752d35e67e7a
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fdfa1fe6176752d35e6b22f
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdfa1fe6176752d35e6b22f
  GraphicsCards: []
  Groups: self-test-power,p2b
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.44
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
    Moid: 5fdfa1936176752d35e68058
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdfa1936176752d35e68058
  LocatorLedOn: false
  ManagementIp: 10.58.50.44
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.44
  ModTime: '2022-10-11T10:28:42.097Z'
  Model: UCSC-C220-M5SX
  Moid: 5fdfa1806176752d35e678c2
  Name: comp-1-p2b-eu-spdc-WMP240400FM
  NumAdaptors: 1
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 10
  NumFcHostInterfaces: 2
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fdfa1686f72612d300b383f
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69f99
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69f99
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69f9b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69f9b
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69f9d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69f9d
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69fa2
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69fa2
  - ClassId: mo.MoRef
    Moid: 5fdfa1d46176752d35e69fa4
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfa1d46176752d35e69fa4
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62a7eebf76752d313928bfbc
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62a7eebf76752d313928bfbc
  - ClassId: mo.MoRef
    Moid: 62a7eebf76752d313928bfbe
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62a7eebf76752d313928bfbe
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fdfa1686f72612d300b383f
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdfa1686f72612d300b383f
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WMP240400FM
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS W16
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fdfa1d16176752d35e69dd1
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fdfa1d16176752d35e69dd1
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: true
  Type: Rack
  UnitPersonality: []
  UserLabel: comp-1-p2b-eu-spdc-WMP240400FM
  Uuid: E6FB96C5-2DA8-465D-A83E-E1764CA90D5B
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: &id001
    Completed: true
    CreateTime: '2022-10-11T10:29:47.275Z'
    CreateTimeEpoch: 1665476987275
    Duration: 00:00:11
    EndTime: '2022-10-11T10:29:58.518Z'
    EndTimeEpoch: 1665476998518
    Moid: 6345459b696f6e2d30f645ba
    Name: Reboot IMC
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:29:47.303Z'
    StartTimeEpoch: 1665476987303
    Status: COMPLETED
    Type: UserDefined
  WorkflowRunning: null
  WorkflowsLast:
  - *id001
  - Completed: true
    CreateTime: '2022-10-11T10:28:15.896Z'
    CreateTimeEpoch: 1665476895896
    Duration: 00:00:09
    EndTime: '2022-10-11T10:28:24.537Z'
    EndTimeEpoch: 1665476904537
    Moid: 6345453f696f6e2d30f64470
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:28:15.928Z'
    StartTimeEpoch: 1665476895928
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:26:42.629Z'
    CreateTimeEpoch: 1665476802629
    Duration: 00:00:11
    EndTime: '2022-10-11T10:26:53.64Z'
    EndTimeEpoch: 1665476813640
    Moid: 634544e2696f6e2d30f64341
    Name: Shut Down OS
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:26:42.828Z'
    StartTimeEpoch: 1665476802828
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:25:15.869Z'
    CreateTimeEpoch: 1665476715869
    Duration: 00:00:04
    EndTime: '2022-10-11T10:25:19.782Z'
    EndTimeEpoch: 1665476719782
    Moid: 6345448b696f6e2d30f6421a
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:25:15.897Z'
    StartTimeEpoch: 1665476715897
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:23:48.899Z'
    CreateTimeEpoch: 1665476628899
    Duration: 00:00:05
    EndTime: '2022-10-11T10:23:53.717Z'
    EndTimeEpoch: 1665476633717
    Moid: 63454434696f6e2d30f64065
    Name: Power Cycle
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:23:48.934Z'
    StartTimeEpoch: 1665476628934
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:21:58.272Z'
    CreateTimeEpoch: 1665476518272
    Duration: 00:00:27
    EndTime: '2022-10-11T10:22:25.551Z'
    EndTimeEpoch: 1665476545551
    Moid: 634543c6696f6e2d30f63e9d
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:21:58.337Z'
    StartTimeEpoch: 1665476518337
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:20:15.387Z'
    CreateTimeEpoch: 1665476415387
    Duration: 00:00:24
    EndTime: '2022-10-11T10:20:39.308Z'
    EndTimeEpoch: 1665476439308
    Moid: 6345435f696f6e2d30f63db3
    Name: Hard Reset
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:20:15.417Z'
    StartTimeEpoch: 1665476415417
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:18:32.22Z'
    CreateTimeEpoch: 1665476312220
    Duration: 00:00:18
    EndTime: '2022-10-11T10:18:50.425Z'
    EndTimeEpoch: 1665476330425
    Moid: 634542f7696f6e2d30f63ca0
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:18:32.343Z'
    StartTimeEpoch: 1665476312343
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:17:06.158Z'
    CreateTimeEpoch: 1665476226158
    Duration: 00:00:07
    EndTime: '2022-10-11T10:17:13.524Z'
    EndTimeEpoch: 1665476233524
    Moid: 634542a2696f6e2d30f63bc3
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:17:06.187Z'
    StartTimeEpoch: 1665476226187
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:15:41.09Z'
    CreateTimeEpoch: 1665476141090
    Duration: 00:00:05
    EndTime: '2022-10-11T10:15:46.369Z'
    EndTimeEpoch: 1665476146369
    Moid: 6345424d696f6e2d30f63abd
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:15:41.12Z'
    StartTimeEpoch: 1665476141120
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:13:56.951Z'
    CreateTimeEpoch: 1665476036951
    Duration: 00:00:19
    EndTime: '2022-10-11T10:14:16.525Z'
    EndTimeEpoch: 1665476056525
    Moid: 634541e4696f6e2d30f639ae
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:13:57.244Z'
    StartTimeEpoch: 1665476037244
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:12:31.376Z'
    CreateTimeEpoch: 1665475951376
    Duration: 00:00:05
    EndTime: '2022-10-11T10:12:36.846Z'
    EndTimeEpoch: 1665475956846
    Moid: 6345418f696f6e2d30f635bf
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:12:31.555Z'
    StartTimeEpoch: 1665475951555
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T09:32:47.465Z'
    CreateTimeEpoch: 1665473567465
    Duration: 00:00:04
    EndTime: '2022-10-11T09:32:51.502Z'
    EndTimeEpoch: 1665473571502
    Moid: 6345383f696f6e2d30f61d0d
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T09:32:47.494Z'
    StartTimeEpoch: 1665473567494
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T09:30:45.933Z'
    CreateTimeEpoch: 1665473445933
    Duration: 00:00:05
    EndTime: '2022-10-11T09:30:51.376Z'
    EndTimeEpoch: 1665473451376
    Moid: 634537c5696f6e2d30f61b58
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T09:30:46.072Z'
    StartTimeEpoch: 1665473446072
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T08:10:31.331Z'
    CreateTimeEpoch: 1665468631331
    Duration: 00:00:04
    EndTime: '2022-10-11T08:10:35.342Z'
    EndTimeEpoch: 1665468635342
    Moid: 634524f7696f6e2d30f5ca0e
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T08:10:31.462Z'
    StartTimeEpoch: 1665468631462
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T08:05:01.481Z'
    CreateTimeEpoch: 1665468301481
    Duration: 00:00:06
    EndTime: '2022-10-11T08:05:07.577Z'
    EndTimeEpoch: 1665468307577
    Moid: 634523ad696f6e2d30f5c61c
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T08:05:01.817Z'
    StartTimeEpoch: 1665468301817
    Status: COMPLETED
    Type: UserDefined
  WorkflowsLastFailedIds: []
  WorkflowsLastIds:
  - 634523ad696f6e2d30f5c61c
  - 634524f7696f6e2d30f5ca0e
  - 634537c5696f6e2d30f61b58
  - 6345383f696f6e2d30f61d0d
  - 6345418f696f6e2d30f635bf
  - 634541e4696f6e2d30f639ae
  - 6345424d696f6e2d30f63abd
  - 634542a2696f6e2d30f63bc3
  - 634542f7696f6e2d30f63ca0
  - 6345435f696f6e2d30f63db3
  - 634543c6696f6e2d30f63e9d
  - 63454434696f6e2d30f64065
  - 6345448b696f6e2d30f6421a
  - 634544e2696f6e2d30f64341
  - 6345453f696f6e2d30f64470
  - 6345459b696f6e2d30f645ba
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fdfdc2c6176752d35fcd8af
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfdc2c6176752d35fcd8af
  - ClassId: mo.MoRef
    Moid: 5fdfdcbf6176752d35fd172c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfdcbf6176752d35fd172c
  - ClassId: mo.MoRef
    Moid: 5fdfdcbf6176752d35fd1736
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfdcbf6176752d35fd1736
  - ClassId: mo.MoRef
    Moid: 5fdfdcbf6176752d35fd173c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfdcbf6176752d35fd173c
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 022C2C2
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fdfdc396176752d35fcdf96
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fdfdc396176752d35fcdf96
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d591f66176752d356a9a42
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d591f66176752d356a9a42
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fdfdc346176752d35fcdd04
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fdfdc346176752d35fcdd04
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fdfdc756176752d35fcf7b3
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fdfdc756176752d35fcf7b3
  Board:
    ClassId: mo.MoRef
    Moid: 5fdfdc3d6176752d35fce1ad
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fdfdc3d6176752d35fce1ad
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdfdc5f6176752d35fcef2a
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdfdc5f6176752d35fcef2a
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fdfdc5b6176752d35fcee4a
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdfdc5b6176752d35fcee4a
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 60000bfa6176752d35b7683c
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/60000bfa6176752d35b7683c
  - ClassId: mo.MoRef
    Moid: 632b0c2f76752d3139a0a2bd
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/632b0c2f76752d3139a0a2bd
  - ClassId: mo.MoRef
    Moid: 63306bef76752d3139c7f4af
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/63306bef76752d3139c7f4af
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 61e4552e76752d3139d0fb33
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/61e4552e76752d3139d0fb33
  - ClassId: mo.MoRef
    Moid: 632b0c2f76752d3139a0a2bf
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/632b0c2f76752d3139a0a2bf
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2020-12-20T23:20:27.032Z'
  DeviceMoId: 5fdfdc206f72612d30120ab4
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fdfdc476176752d35fce724
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce724
  - ClassId: mo.MoRef
    Moid: 5fdfdc476176752d35fce726
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce726
  - ClassId: mo.MoRef
    Moid: 5fdfdc476176752d35fce728
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce728
  - ClassId: mo.MoRef
    Moid: 5fdfdc476176752d35fce72a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce72a
  - ClassId: mo.MoRef
    Moid: 5fdfdc476176752d35fce72c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce72c
  - ClassId: mo.MoRef
    Moid: 5fdfdc476176752d35fce72e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce72e
  - ClassId: mo.MoRef
    Moid: 5fdfdc476176752d35fce730
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfdc476176752d35fce730
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fdfdcb76176752d35fd1249
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdfdcb76176752d35fd1249
  GraphicsCards: []
  Groups: p2b
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.45
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
    Moid: 5fdfdc4c6176752d35fce94e
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdfdc4c6176752d35fce94e
  LocatorLedOn: false
  ManagementIp: 10.58.50.45
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.45
  ModTime: '2022-09-25T15:22:13.526Z'
  Model: UCSC-C220-M5SX
  Moid: 5fdfdc3b6176752d35fce0a9
  Name: comp-2-p2b-eu-spdc-WMP2404000R
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
  - 5fdfdc206f72612d30120ab4
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fdfdc8c6176752d35fd0298
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd0298
  - ClassId: mo.MoRef
    Moid: 5fdfdc8c6176752d35fd029a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd029a
  - ClassId: mo.MoRef
    Moid: 5fdfdc8c6176752d35fd029c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd029c
  - ClassId: mo.MoRef
    Moid: 5fdfdc8c6176752d35fd029f
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd029f
  - ClassId: mo.MoRef
    Moid: 5fdfdc8c6176752d35fd02a3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfdc8c6176752d35fd02a3
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fdfdc456176752d35fce61b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fdfdc456176752d35fce61b
  - ClassId: mo.MoRef
    Moid: 5fdfdc456176752d35fce620
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fdfdc456176752d35fce620
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fdfdc206f72612d30120ab4
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdfdc206f72612d30120ab4
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WMP2404000R
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fdfdc8b6176752d35fd0207
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fdfdc8b6176752d35fd0207
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp-2-p2b-eu-spdc-WMP2404000R
  Uuid: 1419A230-1C67-48C6-AA3C-C7A27F567FD9
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61dc830b76752d3139cb9dec
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61dc830b76752d3139cb9dec
  - ClassId: mo.MoRef
    Moid: 61dc839f76752d3139cbb982
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61dc839f76752d3139cbb982
  - ClassId: mo.MoRef
    Moid: 61dc839f76752d3139cbb988
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61dc839f76752d3139cbb988
  - ClassId: mo.MoRef
    Moid: 61dc839f76752d3139cbb98e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61dc839f76752d3139cbb98e
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 022C2B4
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61dc833676752d3139cba702
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61dc833676752d3139cba702
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61dc832e76752d3139cba576
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61dc832e76752d3139cba576
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61dc832476752d3139cba32d
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61dc832476752d3139cba32d
  Bmc:
    ClassId: mo.MoRef
    Moid: 61dc838f76752d3139cbb6f8
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61dc838f76752d3139cbb6f8
  Board:
    ClassId: mo.MoRef
    Moid: 61dc833176752d3139cba603
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61dc833176752d3139cba603
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61dc839176752d3139cbb771
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61dc839176752d3139cbb771
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61dc835076752d3139cbabc5
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61dc835076752d3139cbabc5
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 61dc839076752d3139cbb71a
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61dc839076752d3139cbb71a
  - ClassId: mo.MoRef
    Moid: 633e7c0876752d31394170ac
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/633e7c0876752d31394170ac
  - ClassId: mo.MoRef
    Moid: 6345c9eb76752d3139826a0c
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6345c9eb76752d3139826a0c
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 61e1412476752d31392f7477
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/61e1412476752d31392f7477
  - ClassId: mo.MoRef
    Moid: 633e7c0876752d31394170ae
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/633e7c0876752d31394170ae
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2020-12-20T23:55:43.055Z'
  DeviceMoId: 5fdfe4666f72612d30130510
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61dc837776752d3139cbb2de
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61dc837776752d3139cbb2de
  - ClassId: mo.MoRef
    Moid: 61dc837776752d3139cbb2e0
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61dc837776752d3139cbb2e0
  - ClassId: mo.MoRef
    Moid: 61dc837776752d3139cbb2e2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61dc837776752d3139cbb2e2
  - ClassId: mo.MoRef
    Moid: 61dc837876752d3139cbb2e4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61dc837876752d3139cbb2e4
  - ClassId: mo.MoRef
    Moid: 61dc837876752d3139cbb2ea
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61dc837876752d3139cbb2ea
  - ClassId: mo.MoRef
    Moid: 61dc837876752d3139cbb2ec
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61dc837876752d3139cbb2ec
  - ClassId: mo.MoRef
    Moid: 61dc837876752d3139cbb2ee
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61dc837876752d3139cbb2ee
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61dc839d76752d3139cbb954
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61dc839d76752d3139cbb954
  GraphicsCards: []
  Groups: self-test-power,p2b
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.46
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
    Moid: 61dc835176752d3139cbabff
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61dc835176752d3139cbabff
  LocatorLedOn: false
  ManagementIp: 10.58.50.46
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.46
  ModTime: '2022-10-11T19:54:19.498Z'
  Model: UCSC-C220-M5SX
  Moid: 5fdfe47f6176752d35001995
  Name: comp-3-p2b-eu-spdc-WMP24040059
  NumAdaptors: 1
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fdfe4666f72612d30130510
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61dc838276752d3139cbb4f3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61dc838276752d3139cbb4f3
  - ClassId: mo.MoRef
    Moid: 61dc838376752d3139cbb4f9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61dc838376752d3139cbb4f9
  - ClassId: mo.MoRef
    Moid: 61dc838376752d3139cbb4fb
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61dc838376752d3139cbb4fb
  - ClassId: mo.MoRef
    Moid: 61dc838376752d3139cbb4fd
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61dc838376752d3139cbb4fd
  - ClassId: mo.MoRef
    Moid: 61dc838376752d3139cbb4ff
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61dc838376752d3139cbb4ff
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61dc832c76752d3139cba4f4
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61dc832c76752d3139cba4f4
  - ClassId: mo.MoRef
    Moid: 61dc832c76752d3139cba4fa
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61dc832c76752d3139cba4fa
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fdfe4666f72612d30130510
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdfe4666f72612d30130510
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WMP24040059
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS W39
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fdfe4d06176752d35003724
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fdfe4d06176752d35003724
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp-3-p2b-eu-spdc-WMP24040059
  Uuid: 0C455BAB-4534-41B2-B84F-C27E202D2D45
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: &id002
    Completed: true
    CreateTime: '2022-10-11T19:40:52.746Z'
    CreateTimeEpoch: 1665510052746
    Duration: 00:01:33
    EndTime: '2022-10-11T19:42:25.563Z'
    EndTimeEpoch: 1665510145563
    Moid: 6345c6c4696f6e2d30f7d61f
    Name: InstallOS
    Progress: 100
    Running: false
    StartTime: '2022-10-11T19:40:52.746Z'
    StartTimeEpoch: 1665510052746
    Status: COMPLETED
    Type: UserDefined
  WorkflowRunning: null
  WorkflowsLast:
  - *id002
  - Completed: true
    CreateTime: '2022-10-11T19:40:51.331Z'
    CreateTimeEpoch: 1665510051331
    Duration: 00:01:36
    EndTime: '2022-10-11T19:42:27.154Z'
    EndTimeEpoch: 1665510147154
    Moid: 6345c6c3696f6e2d30f7d5c4
    Name: Operating System Install
    Progress: 100
    Running: false
    StartTime: '2022-10-11T19:40:51.598Z'
    StartTimeEpoch: 1665510051598
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T19:40:38.066Z'
    CreateTimeEpoch: 1665510038066
    Duration: 00:00:06
    EndTime: '2022-10-11T19:40:44.885Z'
    EndTimeEpoch: 1665510044885
    Moid: 6345c6b5696f6e2d30f7d55d
    Name: Power Cycle
    Progress: 100
    Running: false
    StartTime: '2022-10-11T19:40:38.414Z'
    StartTimeEpoch: 1665510038414
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T18:38:46.612Z'
    CreateTimeEpoch: 1665506326612
    Duration: 00:58:24
    EndTime: '2022-10-11T19:37:10.059Z'
    EndTimeEpoch: 1665509830059
    Moid: 6345b836696f6e2d30f7aaa0
    Name: InstallOS
    Progress: 100
    Running: false
    StartTime: '2022-10-11T18:38:46.612Z'
    StartTimeEpoch: 1665506326612
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T18:38:45.257Z'
    CreateTimeEpoch: 1665506325257
    Duration: 00:58:26
    EndTime: '2022-10-11T19:37:11.228Z'
    EndTimeEpoch: 1665509831228
    Moid: 6345b834696f6e2d30f7aa3b
    Name: Operating System Install
    Progress: 100
    Running: false
    StartTime: '2022-10-11T18:38:45.562Z'
    StartTimeEpoch: 1665506325562
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T18:38:31.886Z'
    CreateTimeEpoch: 1665506311886
    Duration: 00:00:07
    EndTime: '2022-10-11T18:38:38.635Z'
    EndTimeEpoch: 1665506318635
    Moid: 6345b827696f6e2d30f7a93c
    Name: Power Cycle
    Progress: 100
    Running: false
    StartTime: '2022-10-11T18:38:31.915Z'
    StartTimeEpoch: 1665506311915
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T17:56:46.658Z'
    CreateTimeEpoch: 1665503806658
    Duration: 00:38:17
    EndTime: '2022-10-11T18:35:03.636Z'
    EndTimeEpoch: 1665506103636
    Moid: 6345ae5e696f6e2d30f76915
    Name: InstallOS
    Progress: 100
    Running: false
    StartTime: '2022-10-11T17:56:46.658Z'
    StartTimeEpoch: 1665503806658
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T17:56:44.616Z'
    CreateTimeEpoch: 1665503804616
    Duration: 00:38:20
    EndTime: '2022-10-11T18:35:04.989Z'
    EndTimeEpoch: 1665506104989
    Moid: 6345ae5c696f6e2d30f768b5
    Name: Operating System Install
    Progress: 100
    Running: false
    StartTime: '2022-10-11T17:56:44.896Z'
    StartTimeEpoch: 1665503804896
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T17:56:30.022Z'
    CreateTimeEpoch: 1665503790022
    Duration: 00:00:05
    EndTime: '2022-10-11T17:56:35.952Z'
    EndTimeEpoch: 1665503795952
    Moid: 6345ae4d696f6e2d30f76847
    Name: Power Cycle
    Progress: 100
    Running: false
    StartTime: '2022-10-11T17:56:30.051Z'
    StartTimeEpoch: 1665503790051
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T17:26:23.872Z'
    CreateTimeEpoch: 1665501983872
    Duration: 00:00:04
    EndTime: '2022-10-11T17:26:28.924Z'
    EndTimeEpoch: 1665501988924
    Moid: 6345a73f696f6e2d30f7502b
    Name: Turn Off Locator
    Progress: 100
    Running: false
    StartTime: '2022-10-11T17:26:24.011Z'
    StartTimeEpoch: 1665501984011
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T17:25:09.652Z'
    CreateTimeEpoch: 1665501909652
    Duration: 00:00:04
    EndTime: '2022-10-11T17:25:13.708Z'
    EndTimeEpoch: 1665501913708
    Moid: 6345a6f5696f6e2d30f74bfa
    Name: Turn On Locator
    Progress: 100
    Running: false
    StartTime: '2022-10-11T17:25:09.681Z'
    StartTimeEpoch: 1665501909681
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T17:19:29.272Z'
    CreateTimeEpoch: 1665501569272
    Duration: 00:00:14
    EndTime: '2022-10-11T17:19:43.323Z'
    EndTimeEpoch: 1665501583323
    Moid: 6345a5a1696f6e2d30f7456c
    Name: Turn Off Locator
    Progress: 100
    Running: false
    StartTime: '2022-10-11T17:19:29.511Z'
    StartTimeEpoch: 1665501569511
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T17:18:27.183Z'
    CreateTimeEpoch: 1665501507183
    Duration: 00:00:05
    EndTime: '2022-10-11T17:18:32.352Z'
    EndTimeEpoch: 1665501512352
    Moid: 6345a563696f6e2d30f743d4
    Name: Turn On Locator
    Progress: 100
    Running: false
    StartTime: '2022-10-11T17:18:27.241Z'
    StartTimeEpoch: 1665501507241
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T15:38:16.158Z'
    CreateTimeEpoch: 1665495496158
    Duration: 00:08:01
    EndTime: '2022-10-11T15:46:17.988Z'
    EndTimeEpoch: 1665495977988
    Moid: 63458de8696f6e2d30f6fbe9
    Name: InstallOS
    Progress: 8.235294
    Running: false
    StartTime: '2022-10-11T15:38:16.158Z'
    StartTimeEpoch: 1665495496158
    Status: FAILED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T15:38:14.299Z'
    CreateTimeEpoch: 1665495494299
    Duration: 00:08:12
    EndTime: '2022-10-11T15:46:26.866Z'
    EndTimeEpoch: 1665495986866
    Moid: 63458de5696f6e2d30f6fb89
    Name: Operating System Install
    Progress: 33.333336
    Running: false
    StartTime: '2022-10-11T15:38:14.821Z'
    StartTimeEpoch: 1665495494821
    Status: FAILED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T15:37:44.574Z'
    CreateTimeEpoch: 1665495464574
    Duration: 00:00:11
    EndTime: '2022-10-11T15:37:55.429Z'
    EndTimeEpoch: 1665495475429
    Moid: 63458dc8696f6e2d30f6f7fb
    Name: Power Cycle
    Progress: 100
    Running: false
    StartTime: '2022-10-11T15:37:44.619Z'
    StartTimeEpoch: 1665495464619
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T15:33:14.165Z'
    CreateTimeEpoch: 1665495194165
    Duration: 00:00:06
    EndTime: '2022-10-11T15:33:20.016Z'
    EndTimeEpoch: 1665495200016
    Moid: 63458cba696f6e2d30f6f576
    Name: Power Cycle
    Progress: 100
    Running: false
    StartTime: '2022-10-11T15:33:14.204Z'
    StartTimeEpoch: 1665495194204
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T12:18:23.635Z'
    CreateTimeEpoch: 1665483503635
    Duration: 01:00:27
    EndTime: '2022-10-11T13:18:50.736Z'
    EndTimeEpoch: 1665487130736
    Moid: 63455f0f696f6e2d30f6792f
    Name: InstallOS
    Progress: 100
    Running: false
    StartTime: '2022-10-11T12:18:23.635Z'
    StartTimeEpoch: 1665483503635
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T12:18:21.184Z'
    CreateTimeEpoch: 1665483501184
    Duration: 01:00:32
    EndTime: '2022-10-11T13:18:53.339Z'
    EndTimeEpoch: 1665487133339
    Moid: 63455f0c696f6e2d30f678ca
    Name: Operating System Install
    Progress: 100
    Running: false
    StartTime: '2022-10-11T12:18:21.54Z'
    StartTimeEpoch: 1665483501540
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T12:13:55.583Z'
    CreateTimeEpoch: 1665483235583
    Duration: 00:00:58
    EndTime: '2022-10-11T12:14:53.985Z'
    EndTimeEpoch: 1665483293985
    Moid: 63455e03696f6e2d30f6763f
    Name: InstallOS
    Progress: 7.058824
    Running: false
    StartTime: '2022-10-11T12:13:55.583Z'
    StartTimeEpoch: 1665483235583
    Status: FAILED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T12:13:54.486Z'
    CreateTimeEpoch: 1665483234486
    Duration: 00:01:00
    EndTime: '2022-10-11T12:14:54.361Z'
    EndTimeEpoch: 1665483294361
    Moid: 63455e02696f6e2d30f675a8
    Name: Operating System Install
    Progress: 33.333336
    Running: false
    StartTime: '2022-10-11T12:13:54.565Z'
    StartTimeEpoch: 1665483234565
    Status: FAILED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T12:08:43.729Z'
    CreateTimeEpoch: 1665482923729
    Duration: 00:01:43
    EndTime: '2022-10-11T12:10:26.331Z'
    EndTimeEpoch: 1665483026331
    Moid: 63455ccb696f6e2d30f6738f
    Name: InstallOS
    Progress: 100
    Running: false
    StartTime: '2022-10-11T12:08:43.729Z'
    StartTimeEpoch: 1665482923729
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T12:08:39.056Z'
    CreateTimeEpoch: 1665482919056
    Duration: 00:01:49
    EndTime: '2022-10-11T12:10:29.338Z'
    EndTimeEpoch: 1665483029338
    Moid: 63455cc6696f6e2d30f6732f
    Name: Operating System Install
    Progress: 100
    Running: false
    StartTime: '2022-10-11T12:08:40.033Z'
    StartTimeEpoch: 1665482920033
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:29:47.733Z'
    CreateTimeEpoch: 1665476987733
    Duration: 00:00:11
    EndTime: '2022-10-11T10:29:58.867Z'
    EndTimeEpoch: 1665476998867
    Moid: 6345459b696f6e2d30f645d9
    Name: Reboot IMC
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:29:47.762Z'
    StartTimeEpoch: 1665476987762
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:28:16.569Z'
    CreateTimeEpoch: 1665476896569
    Duration: 00:00:03
    EndTime: '2022-10-11T10:28:19.831Z'
    EndTimeEpoch: 1665476899831
    Moid: 63454540696f6e2d30f644a1
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:28:16.601Z'
    StartTimeEpoch: 1665476896601
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:26:45.728Z'
    CreateTimeEpoch: 1665476805728
    Duration: 00:00:09
    EndTime: '2022-10-11T10:26:54.629Z'
    EndTimeEpoch: 1665476814629
    Moid: 634544e5696f6e2d30f6435f
    Name: Shut Down OS
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:26:45.914Z'
    StartTimeEpoch: 1665476805914
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:25:16.392Z'
    CreateTimeEpoch: 1665476716392
    Duration: 00:00:03
    EndTime: '2022-10-11T10:25:19.749Z'
    EndTimeEpoch: 1665476719749
    Moid: 6345448c696f6e2d30f6423e
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:25:16.423Z'
    StartTimeEpoch: 1665476716423
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:23:49.376Z'
    CreateTimeEpoch: 1665476629376
    Duration: 00:00:04
    EndTime: '2022-10-11T10:23:53.323Z'
    EndTimeEpoch: 1665476633323
    Moid: 63454435696f6e2d30f64090
    Name: Power Cycle
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:23:49.405Z'
    StartTimeEpoch: 1665476629405
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:21:59.769Z'
    CreateTimeEpoch: 1665476519769
    Duration: 00:00:27
    EndTime: '2022-10-11T10:22:26.232Z'
    EndTimeEpoch: 1665476546232
    Moid: 634543c7696f6e2d30f63ec3
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:21:59.919Z'
    StartTimeEpoch: 1665476519919
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:20:16.105Z'
    CreateTimeEpoch: 1665476416105
    Duration: 00:00:23
    EndTime: '2022-10-11T10:20:39.816Z'
    EndTimeEpoch: 1665476439816
    Moid: 63454360696f6e2d30f63dd2
    Name: Hard Reset
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:20:16.132Z'
    StartTimeEpoch: 1665476416132
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:18:34.661Z'
    CreateTimeEpoch: 1665476314661
    Duration: 00:00:17
    EndTime: '2022-10-11T10:18:51.054Z'
    EndTimeEpoch: 1665476331054
    Moid: 634542fa696f6e2d30f63cb9
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:18:34.919Z'
    StartTimeEpoch: 1665476314919
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:17:06.859Z'
    CreateTimeEpoch: 1665476226859
    Duration: 00:00:05
    EndTime: '2022-10-11T10:17:11.311Z'
    EndTimeEpoch: 1665476231311
    Moid: 634542a2696f6e2d30f63be2
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:17:06.887Z'
    StartTimeEpoch: 1665476226887
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:15:41.774Z'
    CreateTimeEpoch: 1665476141774
    Duration: 00:00:05
    EndTime: '2022-10-11T10:15:46.249Z'
    EndTimeEpoch: 1665476146249
    Moid: 6345424d696f6e2d30f63aee
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:15:41.803Z'
    StartTimeEpoch: 1665476141803
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:13:58.657Z'
    CreateTimeEpoch: 1665476038657
    Duration: 00:00:22
    EndTime: '2022-10-11T10:14:20.417Z'
    EndTimeEpoch: 1665476060417
    Moid: 634541e6696f6e2d30f639cf
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:13:58.923Z'
    StartTimeEpoch: 1665476038923
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T10:12:32.251Z'
    CreateTimeEpoch: 1665475952251
    Duration: 00:00:04
    EndTime: '2022-10-11T10:12:36.728Z'
    EndTimeEpoch: 1665475956728
    Moid: 63454190696f6e2d30f635f6
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T10:12:32.41Z'
    StartTimeEpoch: 1665475952410
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T09:32:48.867Z'
    CreateTimeEpoch: 1665473568867
    Duration: 00:00:04
    EndTime: '2022-10-11T09:32:52.14Z'
    EndTimeEpoch: 1665473572140
    Moid: 63453840696f6e2d30f61d3e
    Name: Power On
    Progress: 100
    Running: false
    StartTime: '2022-10-11T09:32:48.895Z'
    StartTimeEpoch: 1665473568895
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T09:30:47.743Z'
    CreateTimeEpoch: 1665473447743
    Duration: 00:00:04
    EndTime: '2022-10-11T09:30:51.6Z'
    EndTimeEpoch: 1665473451600
    Moid: 634537c7696f6e2d30f61b77
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T09:30:47.904Z'
    StartTimeEpoch: 1665473447904
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T08:10:33.183Z'
    CreateTimeEpoch: 1665468633183
    Duration: 00:00:03
    EndTime: '2022-10-11T08:10:36.816Z'
    EndTimeEpoch: 1665468636816
    Moid: 634524f9696f6e2d30f5ca5f
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T08:10:33.418Z'
    StartTimeEpoch: 1665468633418
    Status: COMPLETED
    Type: UserDefined
  - Completed: true
    CreateTime: '2022-10-11T08:05:03.602Z'
    CreateTimeEpoch: 1665468303602
    Duration: 00:00:05
    EndTime: '2022-10-11T08:05:08.029Z'
    EndTimeEpoch: 1665468308029
    Moid: 634523af696f6e2d30f5c63b
    Name: Power Off
    Progress: 100
    Running: false
    StartTime: '2022-10-11T08:05:03.777Z'
    StartTimeEpoch: 1665468303777
    Status: COMPLETED
    Type: UserDefined
  WorkflowsLastFailedIds: []
  WorkflowsLastIds:
  - 634523af696f6e2d30f5c63b
  - 634524f9696f6e2d30f5ca5f
  - 634537c7696f6e2d30f61b77
  - 63453840696f6e2d30f61d3e
  - 63454190696f6e2d30f635f6
  - 634541e6696f6e2d30f639cf
  - 6345424d696f6e2d30f63aee
  - 634542a2696f6e2d30f63be2
  - 634542fa696f6e2d30f63cb9
  - 63454360696f6e2d30f63dd2
  - 634543c7696f6e2d30f63ec3
  - 63454435696f6e2d30f64090
  - 6345448c696f6e2d30f6423e
  - 634544e5696f6e2d30f6435f
  - 63454540696f6e2d30f644a1
  - 6345459b696f6e2d30f645d9
  - 63455cc6696f6e2d30f6732f
  - 63455ccb696f6e2d30f6738f
  - 63455e02696f6e2d30f675a8
  - 63455e03696f6e2d30f6763f
  - 63455f0c696f6e2d30f678ca
  - 63455f0f696f6e2d30f6792f
  - 63458cba696f6e2d30f6f576
  - 63458dc8696f6e2d30f6f7fb
  - 63458de5696f6e2d30f6fb89
  - 63458de8696f6e2d30f6fbe9
  - 6345a563696f6e2d30f743d4
  - 6345a5a1696f6e2d30f7456c
  - 6345a6f5696f6e2d30f74bfa
  - 6345a73f696f6e2d30f7502b
  - 6345ae4d696f6e2d30f76847
  - 6345ae5c696f6e2d30f768b5
  - 6345ae5e696f6e2d30f76915
  - 6345b827696f6e2d30f7a93c
  - 6345b834696f6e2d30f7aa3b
  - 6345b836696f6e2d30f7aaa0
  - 6345c6b5696f6e2d30f7d55d
  - 6345c6c3696f6e2d30f7d5c4
  - 6345c6c4696f6e2d30f7d61f
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fdfe80c6176752d3502af12
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfe80c6176752d3502af12
  - ClassId: mo.MoRef
    Moid: 5fdfe8786176752d3502df2e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfe8786176752d3502df2e
  - ClassId: mo.MoRef
    Moid: 5fdfe8786176752d3502df34
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfe8786176752d3502df34
  - ClassId: mo.MoRef
    Moid: 5fdfe8786176752d3502df3a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fdfe8786176752d3502df3a
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 022C32A
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fdfe80d6176752d3502aff4
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fdfe80d6176752d3502aff4
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d591f66176752d356a9a0d
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d591f66176752d356a9a0d
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fdfe80d6176752d3502afd6
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fdfe80d6176752d3502afd6
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fdfe82e6176752d3502bfe7
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fdfe82e6176752d3502bfe7
  Board:
    ClassId: mo.MoRef
    Moid: 5fdfe80d6176752d3502b05b
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fdfe80d6176752d3502b05b
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdfe8176176752d3502b687
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdfe8176176752d3502b687
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fdfe8176176752d3502b656
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fdfe8176176752d3502b656
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 60000bfa6176752d35b7684c
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/60000bfa6176752d35b7684c
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 60000bf76176752d35b76661
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/60000bf76176752d35b76661
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 6013f13a6176752d354587d4
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/6013f13a6176752d354587d4
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2020-12-21T00:10:53.684Z'
  DeviceMoId: 5fdfe7d86f72612d30136fed
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fdfe80e6176752d3502b139
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b139
  - ClassId: mo.MoRef
    Moid: 5fdfe80e6176752d3502b13b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b13b
  - ClassId: mo.MoRef
    Moid: 5fdfe80e6176752d3502b13d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b13d
  - ClassId: mo.MoRef
    Moid: 5fdfe80e6176752d3502b13f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b13f
  - ClassId: mo.MoRef
    Moid: 5fdfe80e6176752d3502b141
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b141
  - ClassId: mo.MoRef
    Moid: 5fdfe80e6176752d3502b143
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b143
  - ClassId: mo.MoRef
    Moid: 5fdfe80e6176752d3502b145
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fdfe80e6176752d3502b145
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fdfe8706176752d3502dc1c
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fdfe8706176752d3502dc1c
  GraphicsCards: []
  Groups: p2b
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.47
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
    Moid: 5fdfe80f6176752d3502b1ab
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fdfe80f6176752d3502b1ab
  LocatorLedOn: false
  ManagementIp: 10.58.50.47
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.47
  ModTime: '2022-07-25T10:27:49.459Z'
  Model: UCSC-C220-M5SX
  Moid: 5fdfe80d6176752d3502b008
  Name: comp-4-p2b-eu-spdc-WMP24040061
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
  - 5fdfe7d86f72612d30136fed
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fdfe8456176752d3502c9f4
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502c9f4
  - ClassId: mo.MoRef
    Moid: 5fdfe8456176752d3502c9f9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502c9f9
  - ClassId: mo.MoRef
    Moid: 5fdfe8456176752d3502c9fb
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502c9fb
  - ClassId: mo.MoRef
    Moid: 5fdfe8456176752d3502c9fe
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502c9fe
  - ClassId: mo.MoRef
    Moid: 5fdfe8456176752d3502ca01
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fdfe8456176752d3502ca01
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fdfe80e6176752d3502b0f2
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fdfe80e6176752d3502b0f2
  - ClassId: mo.MoRef
    Moid: 5fdfe80e6176752d3502b0f5
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fdfe80e6176752d3502b0f5
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fdfe7d86f72612d30136fed
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdfe7d86f72612d30136fed
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WMP24040061
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fdfe8436176752d3502c897
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fdfe8436176752d3502c897
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp-4-p2b-eu-spdc-WMP24040061
  Uuid: B947D1F9-F0A0-4D6F-AF63-16A48DD0A96E
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fe295996176752d351194cb
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe295996176752d351194cb
  - ClassId: mo.MoRef
    Moid: 5fe2964b6176752d3511d49e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe2964b6176752d3511d49e
  - ClassId: mo.MoRef
    Moid: 5fe2964b6176752d3511d4a6
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe2964b6176752d3511d4a6
  - ClassId: mo.MoRef
    Moid: 5fe2964b6176752d3511d4ae
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe2964b6176752d3511d4ae
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02209B0
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fe295a86176752d351199d4
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fe295a86176752d351199d4
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d59a906176752d356f19de
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d59a906176752d356f19de
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fe295a06176752d3511970b
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fe295a06176752d3511970b
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fe296236176752d3511c7e1
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fe296236176752d3511c7e1
  Board:
    ClassId: mo.MoRef
    Moid: 5fe295ac6176752d35119ad6
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fe295ac6176752d35119ad6
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fe295d26176752d3511a875
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fe295d26176752d3511a875
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fe295d46176752d3511a8da
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fe295d46176752d3511a8da
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fe295d56176752d3511a94c
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fe295d56176752d3511a94c
  - ClassId: mo.MoRef
    Moid: 5fe295d56176752d3511a94e
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fe295d56176752d3511a94e
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fe2961f6176752d3511c6a9
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fe2961f6176752d3511c6a9
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fe295df6176752d3511acde
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fe295df6176752d3511acde
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 16C 32T
  CreateTime: '2020-12-23T00:56:10.784Z'
  DeviceMoId: 5fe295916f72612d306438ac
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fe295cb6176752d3511a613
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe295cb6176752d3511a613
  - ClassId: mo.MoRef
    Moid: 5fe295cb6176752d3511a615
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe295cb6176752d3511a615
  - ClassId: mo.MoRef
    Moid: 5fe295cb6176752d3511a617
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe295cb6176752d3511a617
  - ClassId: mo.MoRef
    Moid: 5fe295cb6176752d3511a619
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe295cb6176752d3511a619
  - ClassId: mo.MoRef
    Moid: 5fe295cb6176752d3511a61b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe295cb6176752d3511a61b
  - ClassId: mo.MoRef
    Moid: 5fe295cb6176752d3511a61d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe295cb6176752d3511a61d
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fe296476176752d3511d322
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fe296476176752d3511d322
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.57
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fe295c66176752d3511a4ef
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fe295c66176752d3511a4ef
  LocatorLedOn: false
  ManagementIp: 10.58.28.57
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.57
  ModTime: '2022-10-05T22:01:40.722Z'
  Model: UCSC-C220-M4S
  Moid: 5fe295aa6176752d35119a62
  Name: esx6-eu-spdc-FCH2006V04E
  NumAdaptors: 4
  NumCpuCores: 16
  NumCpuCoresEnabled: 16
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 32
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fe295916f72612d306438ac
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fe296126176752d3511c185
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe296126176752d3511c185
  - ClassId: mo.MoRef
    Moid: 5fe296126176752d3511c188
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe296126176752d3511c188
  - ClassId: mo.MoRef
    Moid: 5fe296126176752d3511c18a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe296126176752d3511c18a
  - ClassId: mo.MoRef
    Moid: 5fe296126176752d3511c18c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe296126176752d3511c18c
  - ClassId: mo.MoRef
    Moid: 5fe296126176752d3511c18e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe296126176752d3511c18e
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fe295b76176752d35119ded
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fe295b76176752d35119ded
  - ClassId: mo.MoRef
    Moid: 5fe295b76176752d35119def
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fe295b76176752d35119def
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fe295916f72612d306438ac
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fe295916f72612d306438ac
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2006V04E
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fe296096176752d3511bd79
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fe296096176752d3511bd79
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx6-eu-spdc-FCH2006V04E
  Uuid: FEC83158-DFCF-4DFF-B91C-2A0370B70C5E
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fe32f066176752d354c0bad
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe32f066176752d354c0bad
  - ClassId: mo.MoRef
    Moid: 5fe32fe36176752d354c63a3
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe32fe36176752d354c63a3
  - ClassId: mo.MoRef
    Moid: 5fe32fe36176752d354c63af
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe32fe36176752d354c63af
  - ClassId: mo.MoRef
    Moid: 5fe32fe36176752d354c63b5
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe32fe36176752d354c63b5
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 1
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02209B5
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fe32f156176752d354c11a1
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fe32f156176752d354c11a1
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d57e6f6176752d355fff41
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d57e6f6176752d355fff41
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fe32f106176752d354c0fde
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fe32f106176752d354c0fde
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fe32fb46176752d354c51cb
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fe32fb46176752d354c51cb
  Board:
    ClassId: mo.MoRef
    Moid: 5fe32eba6176752d354be952
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fe32eba6176752d354be952
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fe32fa16176752d354c48fc
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fe32fa16176752d354c48fc
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fe32f996176752d354c46a2
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fe32f996176752d354c46a2
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fe32f946176752d354c4477
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fe32f946176752d354c4477
  - ClassId: mo.MoRef
    Moid: 5fe32f946176752d354c4479
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fe32f946176752d354c4479
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fe32f926176752d354c439e
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fe32f926176752d354c439e
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fe32f9b6176752d354c4765
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fe32f9b6176752d354c4765
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 16C 32T
  CreateTime: '2020-12-23T11:50:47.381Z'
  DeviceMoId: 5fe32eb66f72612d3075c96a
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fe32ed96176752d354bf85b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32ed96176752d354bf85b
  - ClassId: mo.MoRef
    Moid: 5fe32ed96176752d354bf85d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32ed96176752d354bf85d
  - ClassId: mo.MoRef
    Moid: 5fe32ed96176752d354bf85f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32ed96176752d354bf85f
  - ClassId: mo.MoRef
    Moid: 5fe32ed96176752d354bf861
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32ed96176752d354bf861
  - ClassId: mo.MoRef
    Moid: 5fe32ed96176752d354bf863
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32ed96176752d354bf863
  - ClassId: mo.MoRef
    Moid: 5fe32ed96176752d354bf869
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32ed96176752d354bf869
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fe32fd86176752d354c5fd3
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fe32fd86176752d354c5fd3
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.58
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fe32f726176752d354c36fc
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fe32f726176752d354c36fc
  LocatorLedOn: false
  ManagementIp: 10.58.28.58
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.58
  ModTime: '2022-10-04T10:52:53.602Z'
  Model: UCSC-C220-M4S
  Moid: 5fe32f176176752d354c125a
  Name: esx7-eu-spdc-FCH2004V0M6
  NumAdaptors: 4
  NumCpuCores: 16
  NumCpuCoresEnabled: 16
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 32
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fe32eb66f72612d3075c96a
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fe32fba6176752d354c53f6
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe32fba6176752d354c53f6
  - ClassId: mo.MoRef
    Moid: 5fe32fba6176752d354c53f8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe32fba6176752d354c53f8
  - ClassId: mo.MoRef
    Moid: 5fe32fba6176752d354c53fa
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe32fba6176752d354c53fa
  - ClassId: mo.MoRef
    Moid: 5fe32fba6176752d354c53fc
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe32fba6176752d354c53fc
  - ClassId: mo.MoRef
    Moid: 5fe32fba6176752d354c5402
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe32fba6176752d354c5402
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fe32eca6176752d354bf09d
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fe32eca6176752d354bf09d
  - ClassId: mo.MoRef
    Moid: 5fe32eca6176752d354bf0a3
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fe32eca6176752d354bf0a3
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fe32eb66f72612d3075c96a
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fe32eb66f72612d3075c96a
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2004V0M6
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+CRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fe32fb86176752d354c533f
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fe32fb86176752d354c533f
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx7-eu-spdc-FCH2004V0M6
  Uuid: 3FF508C3-1B1D-4992-B21D-E075BF4CC580
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 5fe32f736176752d354c3768
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe32f736176752d354c3768
  - ClassId: mo.MoRef
    Moid: 5fe3307b6176752d354c9610
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe3307b6176752d354c9610
  - ClassId: mo.MoRef
    Moid: 5fe3307b6176752d354c9616
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe3307b6176752d354c9616
  - ClassId: mo.MoRef
    Moid: 5fe3307b6176752d354c961d
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/5fe3307b6176752d354c961d
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 025F50E
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5fe32f556176752d354c2c4b
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5fe32f556176752d354c2c4b
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5a00c6176752d35723f4d
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5a00c6176752d35723f4d
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 5fe32f5f6176752d354c3034
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5fe32f5f6176752d354c3034
  Bmc:
    ClassId: mo.MoRef
    Moid: 5fe3301e6176752d354c7762
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5fe3301e6176752d354c7762
  Board:
    ClassId: mo.MoRef
    Moid: 5fe32f616176752d354c3121
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5fe32f616176752d354c3121
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fe3300d6176752d354c70a6
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fe3300d6176752d354c70a6
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5fe3300b6176752d354c6fdd
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5fe3300b6176752d354c6fdd
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 5fe3300e6176752d354c70f8
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fe3300e6176752d354c70f8
  - ClassId: mo.MoRef
    Moid: 5fe3300e6176752d354c70fa
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/5fe3300e6176752d354c70fa
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 5fe330146176752d354c7343
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/5fe330146176752d354c7343
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 5fe330056176752d354c6dcf
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/5fe330056176752d354c6dcf
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2020-12-23T11:51:47.386Z'
  DeviceMoId: 5fe32f4d6f72612d3075db4b
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 5fe32f636176752d354c3242
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32f636176752d354c3242
  - ClassId: mo.MoRef
    Moid: 5fe32f636176752d354c3244
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32f636176752d354c3244
  - ClassId: mo.MoRef
    Moid: 5fe32f636176752d354c3246
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32f636176752d354c3246
  - ClassId: mo.MoRef
    Moid: 5fe32f636176752d354c3249
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32f636176752d354c3249
  - ClassId: mo.MoRef
    Moid: 5fe32f636176752d354c324b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32f636176752d354c324b
  - ClassId: mo.MoRef
    Moid: 5fe32f636176752d354c324d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/5fe32f636176752d354c324d
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 5fe330666176752d354c8f03
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/5fe330666176752d354c8f03
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.59
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 5fe32f996176752d354c465f
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5fe32f996176752d354c465f
  LocatorLedOn: false
  ManagementIp: 10.58.28.59
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.59
  ModTime: '2022-10-05T22:01:39.625Z'
  Model: UCSC-C220-M4S
  Moid: 5fe32f536176752d354c2ade
  Name: esx8-eu-spdc-FCH2017V0T1
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5fe32f4d6f72612d3075db4b
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5fe330336176752d354c7dcc
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe330336176752d354c7dcc
  - ClassId: mo.MoRef
    Moid: 5fe330336176752d354c7dce
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe330336176752d354c7dce
  - ClassId: mo.MoRef
    Moid: 5fe330336176752d354c7dd0
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe330336176752d354c7dd0
  - ClassId: mo.MoRef
    Moid: 5fe330336176752d354c7dd2
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe330336176752d354c7dd2
  - ClassId: mo.MoRef
    Moid: 5fe330336176752d354c7dd4
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5fe330336176752d354c7dd4
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 5fe32f6b6176752d354c3502
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fe32f6b6176752d354c3502
  - ClassId: mo.MoRef
    Moid: 5fe32f6b6176752d354c3504
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/5fe32f6b6176752d354c3504
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5fe32f4d6f72612d3075db4b
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fe32f4d6f72612d3075db4b
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2017V0T1
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5fe330306176752d354c7d16
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5fe330306176752d354c7d16
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx8-eu-spdc-FCH2017V0T1
  Uuid: C6D4CE10-5067-439D-8959-A63F60A785BF
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026a9b26176752d350b092c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026a9b26176752d350b092c
  - ClassId: mo.MoRef
    Moid: 6026a9b26176752d350b0936
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026a9b26176752d350b0936
  - ClassId: mo.MoRef
    Moid: 6026a9b26176752d350b093c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026a9b26176752d350b093c
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026a9256176752d350ac4cb
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026a9256176752d350ac4cb
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d583e76176752d35633b20
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d583e76176752d35633b20
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026a9266176752d350ac595
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026a9266176752d350ac595
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026a96e6176752d350ae891
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026a96e6176752d350ae891
  Board:
    ClassId: mo.MoRef
    Moid: 6026a9106176752d350ab8fb
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026a9106176752d350ab8fb
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026a9546176752d350add60
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026a9546176752d350add60
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026a9556176752d350addcd
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026a9556176752d350addcd
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026a9556176752d350adda7
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026a9556176752d350adda7
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026a9596176752d350adf39
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026a9596176752d350adf39
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2021-02-12T16:13:34.147Z'
  DeviceMoId: 6026a9096f72612d305e7b8b
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026a93b6176752d350ad0a6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a93b6176752d350ad0a6
  - ClassId: mo.MoRef
    Moid: 6026a93b6176752d350ad0ab
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a93b6176752d350ad0ab
  - ClassId: mo.MoRef
    Moid: 6026a93b6176752d350ad0ad
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a93b6176752d350ad0ad
  - ClassId: mo.MoRef
    Moid: 6026a93b6176752d350ad0af
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a93b6176752d350ad0af
  - ClassId: mo.MoRef
    Moid: 6026a93b6176752d350ad0b9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a93b6176752d350ad0b9
  - ClassId: mo.MoRef
    Moid: 6026a93b6176752d350ad0bb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a93b6176752d350ad0bb
  - ClassId: mo.MoRef
    Moid: 6026a93b6176752d350ad0bd
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a93b6176752d350ad0bd
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026a9a76176752d350b04d4
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026a9a76176752d350b04d4
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.55
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026a9406176752d350ad427
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026a9406176752d350ad427
  LocatorLedOn: false
  ManagementIp: 10.58.29.55
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.55
  ModTime: '2022-07-25T12:28:34.452Z'
  Model: UCSC-C240-M5SN
  Moid: 6026a92e6176752d350ac89a
  Name: POD-4A-AIO-1-WZP23400AK9
  NumAdaptors: 0
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026a9096f72612d305e7b8b
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026a9806176752d350af121
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026a9806176752d350af121
  - ClassId: mo.MoRef
    Moid: 6026a9806176752d350af123
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026a9806176752d350af123
  - ClassId: mo.MoRef
    Moid: 6026a9806176752d350af125
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026a9806176752d350af125
  - ClassId: mo.MoRef
    Moid: 6026a9806176752d350af127
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026a9806176752d350af127
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026a90f6176752d350ab8b6
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026a90f6176752d350ab8b6
  - ClassId: mo.MoRef
    Moid: 6026a90f6176752d350ab8b8
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026a90f6176752d350ab8b8
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026a9096f72612d305e7b8b
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026a9096f72612d305e7b8b
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23400AK9
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6151f3b976752d3137cd09a4
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6151f3b976752d3137cd09a4
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: POD-4A-AIO-1-WZP23400AK9
  Uuid: 59E49A8A-0E43-475E-8E5D-479A7DB11077
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026aae86176752d350bac36
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026aae86176752d350bac36
  - ClassId: mo.MoRef
    Moid: 6026aae86176752d350bac3c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026aae86176752d350bac3c
  - ClassId: mo.MoRef
    Moid: 6026aae86176752d350bac44
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026aae86176752d350bac44
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026a99d6176752d350affe5
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026a99d6176752d350affe5
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d583e66176752d35633afb
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d583e66176752d35633afb
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026a9a06176752d350b01ed
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026a9a06176752d350b01ed
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026a9fb6176752d350b2d0f
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026a9fb6176752d350b2d0f
  Board:
    ClassId: mo.MoRef
    Moid: 6026a9c06176752d350b0e87
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026a9c06176752d350b0e87
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026a9e46176752d350b20dd
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026a9e46176752d350b20dd
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026a9e46176752d350b2058
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026a9e46176752d350b2058
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026a9e56176752d350b20fa
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026a9e56176752d350b20fa
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026a9e56176752d350b2150
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026a9e56176752d350b2150
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2021-02-12T16:15:54.638Z'
  DeviceMoId: 6026a9976f72612d305e8e4c
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026a9c96176752d350b13f1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a9c96176752d350b13f1
  - ClassId: mo.MoRef
    Moid: 6026a9c96176752d350b13f3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a9c96176752d350b13f3
  - ClassId: mo.MoRef
    Moid: 6026a9c96176752d350b13f5
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a9c96176752d350b13f5
  - ClassId: mo.MoRef
    Moid: 6026a9c96176752d350b13f8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a9c96176752d350b13f8
  - ClassId: mo.MoRef
    Moid: 6026a9c96176752d350b13fa
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a9c96176752d350b13fa
  - ClassId: mo.MoRef
    Moid: 6026a9c96176752d350b13fc
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a9c96176752d350b13fc
  - ClassId: mo.MoRef
    Moid: 6026a9c96176752d350b13fe
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026a9c96176752d350b13fe
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026aae06176752d350ba92d
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026aae06176752d350ba92d
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.56
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026a9cc6176752d350b1528
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026a9cc6176752d350b1528
  LocatorLedOn: false
  ManagementIp: 10.58.29.56
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.56
  ModTime: '2022-07-25T14:59:50.055Z'
  Model: UCSC-C240-M5SN
  Moid: 6026a9ba6176752d350b0bc2
  Name: POD-4A-AIO-2-WZP23400AK7
  NumAdaptors: 0
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026a9976f72612d305e8e4c
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026aa0c6176752d350b3764
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026aa0c6176752d350b3764
  - ClassId: mo.MoRef
    Moid: 6026aa0c6176752d350b3766
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026aa0c6176752d350b3766
  - ClassId: mo.MoRef
    Moid: 6026aa0c6176752d350b3768
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026aa0c6176752d350b3768
  - ClassId: mo.MoRef
    Moid: 6026aa0c6176752d350b376a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026aa0c6176752d350b376a
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026a9c76176752d350b1368
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026a9c76176752d350b1368
  - ClassId: mo.MoRef
    Moid: 6026a9c76176752d350b136a
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026a9c76176752d350b136a
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026a9976f72612d305e8e4c
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026a9976f72612d305e8e4c
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23400AK7
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026aa0d6176752d350b37cb
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026aa0d6176752d350b37cb
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: POD-4A-AIO-2-WZP23400AK7
  Uuid: 426F89A8-7017-4D6A-A1CC-35C9619F072E
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026aadc6176752d350ba760
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026aadc6176752d350ba760
  - ClassId: mo.MoRef
    Moid: 6026aadc6176752d350ba766
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026aadc6176752d350ba766
  - ClassId: mo.MoRef
    Moid: 6026aadc6176752d350ba76c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026aadc6176752d350ba76c
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026aa446176752d350b4f9b
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026aa446176752d350b4f9b
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d58c7b6176752d3567e5d7
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d58c7b6176752d3567e5d7
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026aa3e6176752d350b4d0b
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026aa3e6176752d350b4d0b
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026aa9a6176752d350b8256
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026aa9a6176752d350b8256
  Board:
    ClassId: mo.MoRef
    Moid: 6026aa596176752d350b5b6b
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026aa596176752d350b5b6b
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026aa826176752d350b7293
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026aa826176752d350b7293
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026aa846176752d350b7342
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026aa846176752d350b7342
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026aa846176752d350b7307
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026aa846176752d350b7307
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026aa886176752d350b754a
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026aa886176752d350b754a
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2021-02-12T16:18:33.85Z'
  DeviceMoId: 6026aa376f72612d305ea314
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026aa646176752d350b6171
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aa646176752d350b6171
  - ClassId: mo.MoRef
    Moid: 6026aa646176752d350b6173
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aa646176752d350b6173
  - ClassId: mo.MoRef
    Moid: 6026aa646176752d350b6175
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aa646176752d350b6175
  - ClassId: mo.MoRef
    Moid: 6026aa646176752d350b6177
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aa646176752d350b6177
  - ClassId: mo.MoRef
    Moid: 6026aa646176752d350b6179
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aa646176752d350b6179
  - ClassId: mo.MoRef
    Moid: 6026aa646176752d350b617b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aa646176752d350b617b
  - ClassId: mo.MoRef
    Moid: 6026aa646176752d350b617d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aa646176752d350b617d
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026aad56176752d350ba21e
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026aad56176752d350ba21e
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.57
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026aa686176752d350b64a5
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026aa686176752d350b64a5
  LocatorLedOn: false
  ManagementIp: 10.58.29.57
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.57
  ModTime: '2022-07-25T10:42:22.459Z'
  Model: UCSC-C240-M5SN
  Moid: 6026aa596176752d350b5bd5
  Name: POD-4A-AIO-3-WZP23400AM2
  NumAdaptors: 0
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026aa376f72612d305ea314
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026aaaa6176752d350b8b32
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026aaaa6176752d350b8b32
  - ClassId: mo.MoRef
    Moid: 6026aaaa6176752d350b8b36
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026aaaa6176752d350b8b36
  - ClassId: mo.MoRef
    Moid: 6026aaaa6176752d350b8b38
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026aaaa6176752d350b8b38
  - ClassId: mo.MoRef
    Moid: 6026aaaa6176752d350b8b3a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026aaaa6176752d350b8b3a
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026aa696176752d350b64ee
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026aa696176752d350b64ee
  - ClassId: mo.MoRef
    Moid: 6026aa696176752d350b64f0
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026aa696176752d350b64f0
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026aa376f72612d305ea314
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026aa376f72612d305ea314
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23400AM2
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026aaa96176752d350b8afc
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026aaa96176752d350b8afc
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: POD-4A-AIO-3-WZP23400AM2
  Uuid: 08E6E0BA-83BE-4C8B-BC41-42DEE33593B6
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026ab866176752d350bf5a1
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026ab866176752d350bf5a1
  - ClassId: mo.MoRef
    Moid: 6026ab866176752d350bf5a7
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026ab866176752d350bf5a7
  - ClassId: mo.MoRef
    Moid: 6026ab866176752d350bf5ad
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026ab866176752d350bf5ad
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026aaec6176752d350badf3
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026aaec6176752d350badf3
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5ae216176752d35797f92
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5ae216176752d35797f92
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026aaea6176752d350bad1e
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026aaea6176752d350bad1e
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026ab3b6176752d350bd275
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026ab3b6176752d350bd275
  Board:
    ClassId: mo.MoRef
    Moid: 6026ab006176752d350bb56e
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026ab006176752d350bb56e
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026ab246176752d350bc83d
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026ab246176752d350bc83d
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026ab226176752d350bc73d
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026ab226176752d350bc73d
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026ab286176752d350bca16
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026ab286176752d350bca16
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026ab2f6176752d350bcda6
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026ab2f6176752d350bcda6
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2021-02-12T16:21:20.909Z'
  DeviceMoId: 6026aade6f72612d305eb7fd
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026ab136176752d350bbdf4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ab136176752d350bbdf4
  - ClassId: mo.MoRef
    Moid: 6026ab136176752d350bbdf6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ab136176752d350bbdf6
  - ClassId: mo.MoRef
    Moid: 6026ab136176752d350bbdf8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ab136176752d350bbdf8
  - ClassId: mo.MoRef
    Moid: 6026ab136176752d350bbdfa
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ab136176752d350bbdfa
  - ClassId: mo.MoRef
    Moid: 6026ab136176752d350bbdfc
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ab136176752d350bbdfc
  - ClassId: mo.MoRef
    Moid: 6026ab136176752d350bbdfe
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ab136176752d350bbdfe
  - ClassId: mo.MoRef
    Moid: 6026ab136176752d350bbe00
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ab136176752d350bbe00
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026ab7f6176752d350bf32e
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026ab7f6176752d350bf32e
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.54
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026ab166176752d350bbf0c
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026ab166176752d350bbf0c
  LocatorLedOn: false
  ManagementIp: 10.58.29.54
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.54
  ModTime: '2022-07-25T18:57:17.98Z'
  Model: UCSC-C220-M5SX
  Moid: 6026ab006176752d350bb5b4
  Name: comp1-p4A-eu-spdc
  NumAdaptors: 0
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026aade6f72612d305eb7fd
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026ab546176752d350be0d6
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026ab546176752d350be0d6
  - ClassId: mo.MoRef
    Moid: 6026ab546176752d350be0d8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026ab546176752d350be0d8
  - ClassId: mo.MoRef
    Moid: 6026ab546176752d350be0da
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026ab546176752d350be0da
  - ClassId: mo.MoRef
    Moid: 6026ab546176752d350be0dc
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026ab546176752d350be0dc
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026ab0d6176752d350bbb9f
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026ab0d6176752d350bbb9f
  - ClassId: mo.MoRef
    Moid: 6026ab0d6176752d350bbba1
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026ab0d6176752d350bbba1
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026aade6f72612d305eb7fd
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026aade6f72612d305eb7fd
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WMP24040045
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026ab566176752d350be18e
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026ab566176752d350be18e
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp1-p4a-eu-spdc-WMP24040045
  Uuid: 74B3F3EF-AD4C-4588-9C85-D771EA1401E7
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026ac1c6176752d350c334b
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026ac1c6176752d350c334b
  - ClassId: mo.MoRef
    Moid: 6026ac1c6176752d350c3351
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026ac1c6176752d350c3351
  - ClassId: mo.MoRef
    Moid: 6026ac1c6176752d350c3357
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026ac1c6176752d350c3357
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290056A
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026ab8f6176752d350bf8c3
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026ab8f6176752d350bf8c3
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d57e6c6176752d355ffd9c
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d57e6c6176752d355ffd9c
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026ab7b6176752d350bf1aa
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026ab7b6176752d350bf1aa
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026abce6176752d350c1341
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026abce6176752d350c1341
  Board:
    ClassId: mo.MoRef
    Moid: 6026ab936176752d350bfa93
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026ab936176752d350bfa93
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026abb26176752d350c0581
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026abb26176752d350c0581
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026abad6176752d350c03ce
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026abad6176752d350c03ce
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026abb36176752d350c05d2
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026abb36176752d350c05d2
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026abc36176752d350c0ed5
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026abc36176752d350c0ed5
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2021-02-12T16:23:46.487Z'
  DeviceMoId: 6026ab6f6f72612d305ec984
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026aba36176752d350c00d0
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aba36176752d350c00d0
  - ClassId: mo.MoRef
    Moid: 6026aba36176752d350c00d2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aba36176752d350c00d2
  - ClassId: mo.MoRef
    Moid: 6026aba36176752d350c00d4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aba36176752d350c00d4
  - ClassId: mo.MoRef
    Moid: 6026aba36176752d350c00d6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aba36176752d350c00d6
  - ClassId: mo.MoRef
    Moid: 6026aba36176752d350c00d8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aba36176752d350c00d8
  - ClassId: mo.MoRef
    Moid: 6026aba36176752d350c00da
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aba36176752d350c00da
  - ClassId: mo.MoRef
    Moid: 6026aba36176752d350c00dc
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026aba36176752d350c00dc
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026ac0c6176752d350c2bc3
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026ac0c6176752d350c2bc3
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.58
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026aba06176752d350bffad
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026aba06176752d350bffad
  LocatorLedOn: false
  ManagementIp: 10.58.29.58
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.58
  ModTime: '2022-07-25T09:32:56.736Z'
  Model: UCSC-C220-M5SX
  Moid: 6026ab926176752d350bfa1f
  Name: comp2-p4a-eu-spdc-WZP22520B04
  NumAdaptors: 0
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026ab6f6f72612d305ec984
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026abe86176752d350c1d60
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026abe86176752d350c1d60
  - ClassId: mo.MoRef
    Moid: 6026abe86176752d350c1d62
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026abe86176752d350c1d62
  - ClassId: mo.MoRef
    Moid: 6026abe86176752d350c1d64
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026abe86176752d350c1d64
  - ClassId: mo.MoRef
    Moid: 6026abe86176752d350c1d66
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026abe86176752d350c1d66
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026ab9b6176752d350bfded
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026ab9b6176752d350bfded
  - ClassId: mo.MoRef
    Moid: 6026ab9b6176752d350bfdf0
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026ab9b6176752d350bfdf0
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026ab6f6f72612d305ec984
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026ab6f6f72612d305ec984
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520B04
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026abe26176752d350c1b2e
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026abe26176752d350c1b2e
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp2-p4a-eu-spdc-WZP22520B04
  Uuid: E0345CE5-7E43-4D8B-A3CD-A644912E8A18
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026ae136176752d350d11cd
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026ae136176752d350d11cd
  - ClassId: mo.MoRef
    Moid: 6026aebd6176752d350d5e36
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026aebd6176752d350d5e36
  - ClassId: mo.MoRef
    Moid: 6026aebd6176752d350d5e3e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026aebd6176752d350d5e3e
  - ClassId: mo.MoRef
    Moid: 6026aebd6176752d350d5e44
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026aebd6176752d350d5e44
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 1
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290579
  AvailableMemory: 196608
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026ae336176752d350d1ded
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026ae336176752d350d1ded
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d583e66176752d35633aef
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d583e66176752d35633aef
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026ae166176752d350d1327
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026ae166176752d350d1327
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026ae6e6176752d350d3800
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026ae6e6176752d350d3800
  Board:
    ClassId: mo.MoRef
    Moid: 6026ae3c6176752d350d213f
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026ae3c6176752d350d213f
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026ae586176752d350d2e5b
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026ae586176752d350d2e5b
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026ae576176752d350d2df7
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026ae576176752d350d2df7
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026ae5c6176752d350d2ff8
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026ae5c6176752d350d2ff8
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026ae626176752d350d3248
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026ae626176752d350d3248
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 16C 32T
  CreateTime: '2021-02-12T16:34:57.893Z'
  DeviceMoId: 6026ae116f72612d305f1e80
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026ae466176752d350d26bf
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ae466176752d350d26bf
  - ClassId: mo.MoRef
    Moid: 6026ae466176752d350d26c1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ae466176752d350d26c1
  - ClassId: mo.MoRef
    Moid: 6026ae466176752d350d26c3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ae466176752d350d26c3
  - ClassId: mo.MoRef
    Moid: 6026ae466176752d350d26c5
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ae466176752d350d26c5
  - ClassId: mo.MoRef
    Moid: 6026ae466176752d350d26c7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ae466176752d350d26c7
  - ClassId: mo.MoRef
    Moid: 6026ae466176752d350d26c9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ae466176752d350d26c9
  - ClassId: mo.MoRef
    Moid: 6026ae466176752d350d26cb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026ae466176752d350d26cb
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026aeac6176752d350d559f
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026aeac6176752d350d559f
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.53
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 6026ae426176752d350d2425
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026ae426176752d350d2425
  LocatorLedOn: false
  ManagementIp: 10.58.28.53
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2400'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.53
  ModTime: '2022-09-22T15:31:44.949Z'
  Model: UCSC-C220-M5SX
  Moid: 6026ae316176752d350d1cf6
  Name: comp3-p2a-eu-spdc-WZP2335149W
  NumAdaptors: 1
  NumCpuCores: 16
  NumCpuCoresEnabled: 16
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 32
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026ae116f72612d305f1e80
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026ae896176752d350d4710
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026ae896176752d350d4710
  - ClassId: mo.MoRef
    Moid: 6026ae896176752d350d4712
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026ae896176752d350d4712
  - ClassId: mo.MoRef
    Moid: 6026ae896176752d350d4714
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026ae896176752d350d4714
  - ClassId: mo.MoRef
    Moid: 6026ae896176752d350d4716
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026ae896176752d350d4716
  - ClassId: mo.MoRef
    Moid: 6026ae896176752d350d4718
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026ae896176752d350d4718
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026ae446176752d350d259f
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026ae446176752d350d259f
  - ClassId: mo.MoRef
    Moid: 6026ae446176752d350d25a1
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026ae446176752d350d25a1
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026ae116f72612d305f1e80
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026ae116f72612d305f1e80
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP2335149W
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-CRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026ae836176752d350d448c
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026ae836176752d350d448c
  TopologyScanStatus: ''
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp3-p2a-eu-spdc-WZP2335149W
  Uuid: 377D8CB8-8CA3-4E8D-A9F0-32C37EFCFB6E
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026af0e6176752d350d83a1
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026af0e6176752d350d83a1
  - ClassId: mo.MoRef
    Moid: 6026afa76176752d350dc7d0
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026afa76176752d350dc7d0
  - ClassId: mo.MoRef
    Moid: 6026afa76176752d350dc7d9
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026afa76176752d350dc7d9
  - ClassId: mo.MoRef
    Moid: 6026afa76176752d350dc7df
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026afa76176752d350dc7df
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 029057B
  AvailableMemory: 196608
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026af096176752d350d8118
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026af096176752d350d8118
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d583e66176752d35633b0d
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d583e66176752d35633b0d
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026af036176752d350d7fee
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026af036176752d350d7fee
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026af5d6176752d350da545
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026af5d6176752d350da545
  Board:
    ClassId: mo.MoRef
    Moid: 6026af1f6176752d350d89db
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026af1f6176752d350d89db
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026af3d6176752d350d9787
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026af3d6176752d350d9787
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026af3b6176752d350d9676
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026af3b6176752d350d9676
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026af486176752d350d9c44
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026af486176752d350d9c44
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026af526176752d350da135
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026af526176752d350da135
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 24C 48T
  CreateTime: '2021-02-12T16:38:58.845Z'
  DeviceMoId: 6026aefd6f72612d305f3c94
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026af2d6176752d350d8f86
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026af2d6176752d350d8f86
  - ClassId: mo.MoRef
    Moid: 6026af2d6176752d350d8f88
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026af2d6176752d350d8f88
  - ClassId: mo.MoRef
    Moid: 6026af2d6176752d350d8f8a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026af2d6176752d350d8f8a
  - ClassId: mo.MoRef
    Moid: 6026af2d6176752d350d8f8d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026af2d6176752d350d8f8d
  - ClassId: mo.MoRef
    Moid: 6026af2d6176752d350d8f8f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026af2d6176752d350d8f8f
  - ClassId: mo.MoRef
    Moid: 6026af2d6176752d350d8f91
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026af2d6176752d350d8f91
  - ClassId: mo.MoRef
    Moid: 6026af2d6176752d350d8f93
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026af2d6176752d350d8f93
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026af9c6176752d350dc218
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026af9c6176752d350dc218
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.54
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 6026af346176752d350d92fb
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026af346176752d350d92fb
  LocatorLedOn: false
  ManagementIp: 10.58.28.54
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.54
  ModTime: '2022-09-22T15:33:06.354Z'
  Model: UCSC-C220-M5SX
  Moid: 6026af226176752d350d8b38
  Name: comp4-p2a-eu-spdc-WZP22520Y8W
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026aefd6f72612d305f3c94
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026af716176752d350dad61
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026af716176752d350dad61
  - ClassId: mo.MoRef
    Moid: 6026af716176752d350dad67
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026af716176752d350dad67
  - ClassId: mo.MoRef
    Moid: 6026af716176752d350dad69
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026af716176752d350dad69
  - ClassId: mo.MoRef
    Moid: 6026af716176752d350dad6b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026af716176752d350dad6b
  - ClassId: mo.MoRef
    Moid: 6026af716176752d350dad6d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026af716176752d350dad6d
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026af316176752d350d91f2
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026af316176752d350d91f2
  - ClassId: mo.MoRef
    Moid: 6026af316176752d350d91f4
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026af316176752d350d91f4
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026aefd6f72612d305f3c94
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026aefd6f72612d305f3c94
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520Y8W
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026af6d6176752d350dabd2
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026af6d6176752d350dabd2
  TopologyScanStatus: ''
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp4-p2a-eu-spdc-WZP22520Y8W
  Uuid: 4E59411A-C668-4E4F-963B-7B629D6AD56B
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026afea6176752d350de45f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026afea6176752d350de45f
  - ClassId: mo.MoRef
    Moid: 6026b0916176752d350e207d
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b0916176752d350e207d
  - ClassId: mo.MoRef
    Moid: 6026b0916176752d350e2083
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b0916176752d350e2083
  - ClassId: mo.MoRef
    Moid: 6026b0916176752d350e2089
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b0916176752d350e2089
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 029056F
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026b0046176752d350deb6e
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026b0046176752d350deb6e
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d583e66176752d35633ae1
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d583e66176752d35633ae1
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026aff36176752d350de754
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026aff36176752d350de754
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026b04b6176752d350e0621
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026b04b6176752d350e0621
  Board:
    ClassId: mo.MoRef
    Moid: 6026b00f6176752d350deec7
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026b00f6176752d350deec7
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026b02d6176752d350df997
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026b02d6176752d350df997
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026b02b6176752d350df8cd
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026b02b6176752d350df8cd
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026b0316176752d350dfae1
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026b0316176752d350dfae1
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026b0386176752d350dfd84
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026b0386176752d350dfd84
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 24C 48T
  CreateTime: '2021-02-12T16:42:49.026Z'
  DeviceMoId: 6026afe76f72612d305f5af6
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026b0196176752d350df329
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0196176752d350df329
  - ClassId: mo.MoRef
    Moid: 6026b0196176752d350df32d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0196176752d350df32d
  - ClassId: mo.MoRef
    Moid: 6026b0196176752d350df330
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0196176752d350df330
  - ClassId: mo.MoRef
    Moid: 6026b0196176752d350df332
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0196176752d350df332
  - ClassId: mo.MoRef
    Moid: 6026b0196176752d350df337
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0196176752d350df337
  - ClassId: mo.MoRef
    Moid: 6026b0196176752d350df339
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0196176752d350df339
  - ClassId: mo.MoRef
    Moid: 6026b0196176752d350df33b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0196176752d350df33b
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026b0866176752d350e1c83
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026b0866176752d350e1c83
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.37
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026b0176176752d350df2ad
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026b0176176752d350df2ad
  LocatorLedOn: false
  ManagementIp: 10.58.29.37
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.37
  ModTime: '2022-07-26T06:37:58.829Z'
  Model: UCSC-C220-M5SX
  Moid: 6026b0086176752d350dec89
  Name: esx01-eu-spdc-WZP22520Y99
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 4
  NumFcHostInterfaces: 4
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026afe76f72612d305f5af6
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026b05b6176752d350e0b84
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b05b6176752d350e0b84
  - ClassId: mo.MoRef
    Moid: 6026b05b6176752d350e0b86
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b05b6176752d350e0b86
  - ClassId: mo.MoRef
    Moid: 6026b05b6176752d350e0b88
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b05b6176752d350e0b88
  - ClassId: mo.MoRef
    Moid: 6026b05b6176752d350e0b8a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b05b6176752d350e0b8a
  - ClassId: mo.MoRef
    Moid: 6026b05b6176752d350e0b8c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b05b6176752d350e0b8c
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026b0146176752d350df0c9
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b0146176752d350df0c9
  - ClassId: mo.MoRef
    Moid: 6026b0146176752d350df0cb
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b0146176752d350df0cb
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026afe76f72612d305f5af6
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026afe76f72612d305f5af6
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520Y99
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026b0586176752d350e0a6a
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026b0586176752d350e0a6a
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx01-eu-spdc-WZP22520Y99
  Uuid: A8CE07B5-3859-4F88-B678-BF2AFF0F04F0
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026b0a36176752d350e2730
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b0a36176752d350e2730
  - ClassId: mo.MoRef
    Moid: 6026b14b6176752d350e6e33
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b14b6176752d350e6e33
  - ClassId: mo.MoRef
    Moid: 6026b14b6176752d350e6e39
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b14b6176752d350e6e39
  - ClassId: mo.MoRef
    Moid: 6026b14b6176752d350e6e3f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b14b6176752d350e6e3f
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290576
  AvailableMemory: 524288
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026b0a96176752d350e2ade
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026b0a96176752d350e2ade
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d58c7b6176752d3567e5b7
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d58c7b6176752d3567e5b7
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026b0ad6176752d350e2ccb
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026b0ad6176752d350e2ccb
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026b0fe6176752d350e4e9a
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026b0fe6176752d350e4e9a
  Board:
    ClassId: mo.MoRef
    Moid: 6026b0c96176752d350e3875
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026b0c96176752d350e3875
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026b0e06176752d350e4330
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026b0e06176752d350e4330
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026b0df6176752d350e42c0
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026b0df6176752d350e42c0
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026b0e76176752d350e461d
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026b0e76176752d350e461d
  - ClassId: mo.MoRef
    Moid: 61b9f21e76752d3139542d8f
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61b9f21e76752d3139542d8f
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026b0f56176752d350e4ab0
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026b0f56176752d350e4ab0
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 61b9f04676752d313953da88
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/61b9f04676752d313953da88
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2021-02-12T16:45:57.737Z'
  DeviceMoId: 6026b0a16f72612d305f7116
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026b0d66176752d350e3ef3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0d66176752d350e3ef3
  - ClassId: mo.MoRef
    Moid: 6026b0d66176752d350e3ef5
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0d66176752d350e3ef5
  - ClassId: mo.MoRef
    Moid: 6026b0d66176752d350e3ef7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0d66176752d350e3ef7
  - ClassId: mo.MoRef
    Moid: 6026b0d66176752d350e3ef9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0d66176752d350e3ef9
  - ClassId: mo.MoRef
    Moid: 6026b0d66176752d350e3efc
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0d66176752d350e3efc
  - ClassId: mo.MoRef
    Moid: 6026b0d66176752d350e3efe
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0d66176752d350e3efe
  - ClassId: mo.MoRef
    Moid: 6026b0d66176752d350e3f00
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b0d66176752d350e3f00
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026b1426176752d350e6aee
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026b1426176752d350e6aee
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.36
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026b0d26176752d350e3d8d
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026b0d26176752d350e3d8d
  LocatorLedOn: false
  ManagementIp: 10.58.29.36
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.36
  ModTime: '2022-07-25T15:12:35.959Z'
  Model: UCSC-C220-M5SX
  Moid: 6026b0c56176752d350e3741
  Name: esx00-eu-spdc-WZP22520AXQ
  NumAdaptors: 1
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 4
  NumFcHostInterfaces: 4
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026b0a16f72612d305f7116
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026b1196176752d350e5a38
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b1196176752d350e5a38
  - ClassId: mo.MoRef
    Moid: 6026b1196176752d350e5a3a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b1196176752d350e5a3a
  - ClassId: mo.MoRef
    Moid: 6026b1196176752d350e5a3c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b1196176752d350e5a3c
  - ClassId: mo.MoRef
    Moid: 6026b1196176752d350e5a3e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b1196176752d350e5a3e
  - ClassId: mo.MoRef
    Moid: 6026b1196176752d350e5a40
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b1196176752d350e5a40
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026b0d26176752d350e3d62
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b0d26176752d350e3d62
  - ClassId: mo.MoRef
    Moid: 6026b0d26176752d350e3d67
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b0d26176752d350e3d67
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026b0a16f72612d305f7116
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026b0a16f72612d305f7116
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520AXQ
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: User_Label
    Value: Hsiad
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026b1116176752d350e56c9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026b1116176752d350e56c9
  TopologyScanStatus: ''
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx00-eu-spdc-WZP22520AXQ
  Uuid: 5917D0BA-E5B0-4FF5-8176-0349350453DB
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026b31a6176752d350f39fd
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b31a6176752d350f39fd
  - ClassId: mo.MoRef
    Moid: 6026b31a6176752d350f3a03
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b31a6176752d350f3a03
  - ClassId: mo.MoRef
    Moid: 6026b31a6176752d350f3a09
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b31a6176752d350f3a09
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290573
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026b2446176752d350ece36
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026b2446176752d350ece36
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d583e66176752d35633ad3
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d583e66176752d35633ad3
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026b2406176752d350eccc0
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026b2406176752d350eccc0
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026b2d06176752d350f1803
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026b2d06176752d350f1803
  Board:
    ClassId: mo.MoRef
    Moid: 6026b2986176752d350ef90e
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026b2986176752d350ef90e
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026b2bf6176752d350f0d90
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026b2bf6176752d350f0d90
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026b2be6176752d350f0d71
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026b2be6176752d350f0d71
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6026b2bf6176752d350f0ded
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6026b2bf6176752d350f0ded
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6026b2c56176752d350f1178
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6026b2c56176752d350f1178
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 24C 48T
  CreateTime: '2021-02-12T16:53:40.604Z'
  DeviceMoId: 6026b2376f72612d305fa447
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026b2a36176752d350eff81
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b2a36176752d350eff81
  - ClassId: mo.MoRef
    Moid: 6026b2a36176752d350eff83
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b2a36176752d350eff83
  - ClassId: mo.MoRef
    Moid: 6026b2a36176752d350eff85
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b2a36176752d350eff85
  - ClassId: mo.MoRef
    Moid: 6026b2a36176752d350eff87
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b2a36176752d350eff87
  - ClassId: mo.MoRef
    Moid: 6026b2a36176752d350eff8d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b2a36176752d350eff8d
  - ClassId: mo.MoRef
    Moid: 6026b2a36176752d350eff92
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b2a36176752d350eff92
  - ClassId: mo.MoRef
    Moid: 6026b2a36176752d350eff98
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b2a36176752d350eff98
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026b3126176752d350f36fa
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026b3126176752d350f36fa
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.59
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026b2a76176752d350f0164
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026b2a76176752d350f0164
  LocatorLedOn: false
  ManagementIp: 10.58.29.59
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.59
  ModTime: '2022-10-05T21:56:15.721Z'
  Model: UCSC-C220-M5SX
  Moid: 6026b2946176752d350ef654
  Name: comp3-p4a-eu-spdc-WZP22520Y8X
  NumAdaptors: 0
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026b2376f72612d305fa447
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026b2e76176752d350f22fa
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b2e76176752d350f22fa
  - ClassId: mo.MoRef
    Moid: 6026b2e76176752d350f22fc
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b2e76176752d350f22fc
  - ClassId: mo.MoRef
    Moid: 6026b2e76176752d350f22fe
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b2e76176752d350f22fe
  - ClassId: mo.MoRef
    Moid: 6026b2e76176752d350f2300
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b2e76176752d350f2300
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026b2a16176752d350efed9
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b2a16176752d350efed9
  - ClassId: mo.MoRef
    Moid: 6026b2a16176752d350efedb
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b2a16176752d350efedb
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026b2376f72612d305fa447
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026b2376f72612d305fa447
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP22520Y8X
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026b2e56176752d350f2177
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026b2e56176752d350f2177
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp-3-p4a-eu-spdc-WZP22520Y8X
  Uuid: 047AD2B8-0E6F-45C4-895C-A9A14C5032E3
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026b5886176752d3510429b
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b5886176752d3510429b
  - ClassId: mo.MoRef
    Moid: 6026b6566176752d3510939d
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b6566176752d3510939d
  - ClassId: mo.MoRef
    Moid: 6026b6566176752d351093a6
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b6566176752d351093a6
  - ClassId: mo.MoRef
    Moid: 6026b6566176752d351093b0
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b6566176752d351093b0
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02ACA37
  AvailableMemory: 524288
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026b5a86176752d35104c46
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026b5a86176752d35104c46
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d583e76176752d35633b6c
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d583e76176752d35633b6c
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026b58d6176752d35104543
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026b58d6176752d35104543
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026b5e96176752d35106683
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026b5e96176752d35106683
  Board:
    ClassId: mo.MoRef
    Moid: 6026b5b06176752d35104fb1
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026b5b06176752d35104fb1
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026b5cf6176752d35105dbc
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026b5cf6176752d35105dbc
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026b5ce6176752d35105d6f
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026b5ce6176752d35105d6f
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2021-02-12T17:06:51.177Z'
  DeviceMoId: 6026b5846f72612d30b98bb0
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026b5b56176752d351051b4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b5b56176752d351051b4
  - ClassId: mo.MoRef
    Moid: 6026b5b66176752d351051bd
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b5b66176752d351051bd
  - ClassId: mo.MoRef
    Moid: 6026b5b66176752d351051bf
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b5b66176752d351051bf
  - ClassId: mo.MoRef
    Moid: 6026b5b66176752d351051c1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b5b66176752d351051c1
  - ClassId: mo.MoRef
    Moid: 6026b5b66176752d351051c3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b5b66176752d351051c3
  - ClassId: mo.MoRef
    Moid: 6026b5b66176752d351051c5
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b5b66176752d351051c5
  - ClassId: mo.MoRef
    Moid: 6026b5b66176752d351051c7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b5b66176752d351051c7
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026b6546176752d35109238
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026b6546176752d35109238
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.25.41
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.25.62
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
    Moid: 6026b5bf6176752d351056f7
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026b5bf6176752d351056f7
  LocatorLedOn: false
  ManagementIp: 10.58.25.41
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.25.41
  ModTime: '2022-07-26T06:42:20.017Z'
  Model: UCSC-C240-M5SX
  Moid: 6026b5ab6176752d35104d78
  Name: aio1-p5g-eu-spdc-WZP23450C7D
  NumAdaptors: 1
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026b5846f72612d30b98bb0
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026b6076176752d35106eac
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6076176752d35106eac
  - ClassId: mo.MoRef
    Moid: 6026b6076176752d35106eb2
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6076176752d35106eb2
  - ClassId: mo.MoRef
    Moid: 6026b6076176752d35106eb4
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6076176752d35106eb4
  - ClassId: mo.MoRef
    Moid: 6026b6076176752d35106eb6
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6076176752d35106eb6
  - ClassId: mo.MoRef
    Moid: 6026b6076176752d35106eb8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6076176752d35106eb8
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026b5b56176752d351050fe
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b5b56176752d351050fe
  - ClassId: mo.MoRef
    Moid: 6026b5b56176752d35105106
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b5b56176752d35105106
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026b5846f72612d30b98bb0
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026b5846f72612d30b98bb0
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23450C7D
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026b6036176752d35106d43
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026b6036176752d35106d43
  TopologyScanStatus: ''
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio1-p5g-eu-spdc-WZP23450C7D
  Uuid: 92532B9A-32D6-4860-9F0D-0175CF1E05EC
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026b65d6176752d35109a9e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b65d6176752d35109a9e
  - ClassId: mo.MoRef
    Moid: 6026b6d86176752d3510eef3
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b6d86176752d3510eef3
  - ClassId: mo.MoRef
    Moid: 6026b6d86176752d3510eef9
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b6d86176752d3510eef9
  - ClassId: mo.MoRef
    Moid: 6026b6d86176752d3510eeff
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b6d86176752d3510eeff
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02ACA38
  AvailableMemory: 524288
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026b65f6176752d35109d0d
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026b65f6176752d35109d0d
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5a0066176752d35723ca2
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5a0066176752d35723ca2
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026b65e6176752d35109c67
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026b65e6176752d35109c67
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026b6a36176752d3510c524
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026b6a36176752d3510c524
  Board:
    ClassId: mo.MoRef
    Moid: 6026b65f6176752d35109dcd
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026b65f6176752d35109dcd
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026b6876176752d3510b45e
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026b6876176752d3510b45e
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026b6896176752d3510b5a5
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026b6896176752d3510b5a5
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2021-02-12T17:09:51.492Z'
  DeviceMoId: 6026b6346f72612d30b997b6
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026b6616176752d3510a05e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b6616176752d3510a05e
  - ClassId: mo.MoRef
    Moid: 6026b6616176752d3510a060
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b6616176752d3510a060
  - ClassId: mo.MoRef
    Moid: 6026b6616176752d3510a062
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b6616176752d3510a062
  - ClassId: mo.MoRef
    Moid: 6026b6616176752d3510a064
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b6616176752d3510a064
  - ClassId: mo.MoRef
    Moid: 6026b6616176752d3510a066
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b6616176752d3510a066
  - ClassId: mo.MoRef
    Moid: 6026b6616176752d3510a068
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b6616176752d3510a068
  - ClassId: mo.MoRef
    Moid: 6026b6616176752d3510a06a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026b6616176752d3510a06a
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026b6d06176752d3510eb8c
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026b6d06176752d3510eb8c
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.25.42
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.25.62
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
    Moid: 6026b66c6176752d3510aaa1
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026b66c6176752d3510aaa1
  LocatorLedOn: false
  ManagementIp: 10.58.25.42
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.25.42
  ModTime: '2022-07-26T07:42:52.527Z'
  Model: UCSC-C240-M5SX
  Moid: 6026b65f6176752d35109d55
  Name: aio2-p5g-eu-spdc-WZP23450C8M
  NumAdaptors: 1
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026b6346f72612d30b997b6
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026b6af6176752d3510d000
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6af6176752d3510d000
  - ClassId: mo.MoRef
    Moid: 6026b6af6176752d3510d004
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6af6176752d3510d004
  - ClassId: mo.MoRef
    Moid: 6026b6af6176752d3510d006
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6af6176752d3510d006
  - ClassId: mo.MoRef
    Moid: 6026b6af6176752d3510d008
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6af6176752d3510d008
  - ClassId: mo.MoRef
    Moid: 6026b6af6176752d3510d00c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026b6af6176752d3510d00c
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026b65d6176752d35109a39
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b65d6176752d35109a39
  - ClassId: mo.MoRef
    Moid: 6026b65d6176752d35109a3e
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026b65d6176752d35109a3e
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026b6346f72612d30b997b6
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026b6346f72612d30b997b6
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23450C8M
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026b6a76176752d3510c920
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026b6a76176752d3510c920
  TopologyScanStatus: ''
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio2-p5g-eu-spdc-WZP23450C8M
  Uuid: D7070881-4FEC-4BB3-9DA1-F46BE65D4B59
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026b9b86176752d3537fdb2
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026b9b86176752d3537fdb2
  - ClassId: mo.MoRef
    Moid: 6026bc016176752d3539621c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026bc016176752d3539621c
  - ClassId: mo.MoRef
    Moid: 6232073876752d313965b827
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6232073876752d313965b827
  - ClassId: mo.MoRef
    Moid: 6232073876752d313965b82d
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6232073876752d313965b82d
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02ACA39
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026b9a26176752d3537f14c
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026b9a26176752d3537f14c
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d58c7b6176752d3567e5c9
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d58c7b6176752d3567e5c9
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026b9a26176752d3537f129
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026b9a26176752d3537f129
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026bbec6176752d35394ee8
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026bbec6176752d35394ee8
  Board:
    ClassId: mo.MoRef
    Moid: 6026bbdf6176752d3539428e
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026bbdf6176752d3539428e
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026bbe66176752d35394a3f
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026bbe66176752d35394a3f
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026bbe66176752d35394aa6
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026bbe66176752d35394aa6
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2021-02-12T17:23:46.943Z'
  DeviceMoId: 6026b8a26f72612d30b9b627
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026bbe26176752d353944f7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbe26176752d353944f7
  - ClassId: mo.MoRef
    Moid: 6026bbe26176752d353944f9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbe26176752d353944f9
  - ClassId: mo.MoRef
    Moid: 6026bbe26176752d353944fe
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbe26176752d353944fe
  - ClassId: mo.MoRef
    Moid: 6026bbe26176752d35394500
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbe26176752d35394500
  - ClassId: mo.MoRef
    Moid: 6026bbe26176752d35394502
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbe26176752d35394502
  - ClassId: mo.MoRef
    Moid: 6026bbe26176752d35394504
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbe26176752d35394504
  - ClassId: mo.MoRef
    Moid: 6026bbe26176752d35394514
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbe26176752d35394514
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026bc006176752d353960aa
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026bc006176752d353960aa
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.51
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
    Moid: 6026bbe36176752d353945ff
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026bbe36176752d353945ff
  LocatorLedOn: false
  ManagementIp: 10.58.50.51
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.51
  ModTime: '2022-07-25T12:34:26.527Z'
  Model: UCSC-C240-M5SX
  Moid: 6026b9a26176752d3537f191
  Name: aio3-p5g-eu-spdc-WZP23450C8K
  NumAdaptors: 1
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026b8a26f72612d30b9b627
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026bbf76176752d3539570f
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bbf76176752d3539570f
  - ClassId: mo.MoRef
    Moid: 6026bbf76176752d35395711
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bbf76176752d35395711
  - ClassId: mo.MoRef
    Moid: 6026bbf76176752d35395713
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bbf76176752d35395713
  - ClassId: mo.MoRef
    Moid: 6232070b76752d313965aee0
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6232070b76752d313965aee0
  - ClassId: mo.MoRef
    Moid: 6232070b76752d313965aef1
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6232070b76752d313965aef1
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026bbe16176752d35394488
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026bbe16176752d35394488
  - ClassId: mo.MoRef
    Moid: 6026bbe16176752d3539448a
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026bbe16176752d3539448a
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026b8a26f72612d30b9b627
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026b8a26f72612d30b9b627
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 62a7a61076752d313919e9ce
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/62a7a61076752d313919e9ce
  Serial: WZP23450C8K
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026bbf76176752d353956ab
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026bbf76176752d353956ab
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio3-p5g-eu-spdc-WZP23450C8K
  Uuid: 9A6D909E-F7C5-4481-BF21-424340DA652C
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026bb906176752d353910c5
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026bb906176752d353910c5
  - ClassId: mo.MoRef
    Moid: 6026bc026176752d35396502
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026bc026176752d35396502
  - ClassId: mo.MoRef
    Moid: 6026bc026176752d35396514
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026bc026176752d35396514
  - ClassId: mo.MoRef
    Moid: 6026bc026176752d35396528
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026bc026176752d35396528
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02ACA2F
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026bb9c6176752d35391629
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026bb9c6176752d35391629
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d591f66176752d356a9a01
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d591f66176752d356a9a01
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026bb956176752d353912f4
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026bb956176752d353912f4
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026bbf76176752d35395607
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026bbf76176752d35395607
  Board:
    ClassId: mo.MoRef
    Moid: 6026bbae6176752d35391fb5
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026bbae6176752d35391fb5
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026bbc76176752d35392e5b
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026bbc76176752d35392e5b
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026bbc76176752d35392e9a
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026bbc76176752d35392e9a
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2021-02-12T17:32:12.556Z'
  DeviceMoId: 6026b9416f72612d30b9be8a
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026bbc36176752d35392b4d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbc36176752d35392b4d
  - ClassId: mo.MoRef
    Moid: 6026bbc36176752d35392b67
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbc36176752d35392b67
  - ClassId: mo.MoRef
    Moid: 6026bbc36176752d35392b7f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbc36176752d35392b7f
  - ClassId: mo.MoRef
    Moid: 6026bbc36176752d35392b9d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbc36176752d35392b9d
  - ClassId: mo.MoRef
    Moid: 6026bbc36176752d35392ba1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbc36176752d35392ba1
  - ClassId: mo.MoRef
    Moid: 6026bbc36176752d35392bb2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbc36176752d35392bb2
  - ClassId: mo.MoRef
    Moid: 6026bbc46176752d35392bb7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bbc46176752d35392bb7
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026bc016176752d35396393
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026bc016176752d35396393
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.49
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026bbc26176752d35392a7d
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026bbc26176752d35392a7d
  LocatorLedOn: false
  ManagementIp: 10.58.29.49
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.49
  ModTime: '2022-09-14T07:29:53.042Z'
  Model: UCSC-C220-M5SX
  Moid: 6026bb9c6176752d353915f2
  Name: cu-p5g-eu-spdc-WZP23440N11
  NumAdaptors: 1
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026b9416f72612d30b9be8a
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026bbfb6176752d35395a79
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bbfb6176752d35395a79
  - ClassId: mo.MoRef
    Moid: 6026bbfb6176752d35395a7c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bbfb6176752d35395a7c
  - ClassId: mo.MoRef
    Moid: 6026bbfb6176752d35395a80
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bbfb6176752d35395a80
  - ClassId: mo.MoRef
    Moid: 6026bbfb6176752d35395a86
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bbfb6176752d35395a86
  - ClassId: mo.MoRef
    Moid: 6026bbfb6176752d35395a88
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bbfb6176752d35395a88
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026bbc16176752d3539296f
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026bbc16176752d3539296f
  - ClassId: mo.MoRef
    Moid: 6026bbc16176752d35392971
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026bbc16176752d35392971
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026b9416f72612d30b9be8a
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026b9416f72612d30b9be8a
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23440N11
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026bbfb6176752d353959bb
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026bbfb6176752d353959bb
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: cu-p5g-eu-spdc-WZP23440N11
  Uuid: 2AA15DD4-19F7-44BD-85F7-682E3B3EBE10
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026bc4b6176752d3539a9c9
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026bc4b6176752d3539a9c9
  - ClassId: mo.MoRef
    Moid: 6026bc6d6176752d3539cdbf
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026bc6d6176752d3539cdbf
  - ClassId: mo.MoRef
    Moid: 6026bc6d6176752d3539cdcd
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026bc6d6176752d3539cdcd
  - ClassId: mo.MoRef
    Moid: 6026bc6d6176752d3539cdd8
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026bc6d6176752d3539cdd8
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 524288
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6026bc4e6176752d3539acf0
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6026bc4e6176752d3539acf0
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5705b6176752d35587eef
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5705b6176752d35587eef
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026bc4b6176752d3539a9ee
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026bc4b6176752d3539a9ee
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026bc636176752d3539c3aa
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026bc636176752d3539c3aa
  Board:
    ClassId: mo.MoRef
    Moid: 6026bc4f6176752d3539aed6
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026bc4f6176752d3539aed6
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026bc546176752d3539b555
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026bc546176752d3539b555
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026bc536176752d3539b442
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026bc536176752d3539b442
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 630611c876752d3139904c1e
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/630611c876752d3139904c1e
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 630611c876752d3139904c1c
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/630611c876752d3139904c1c
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2021-02-12T17:35:10.559Z'
  DeviceMoId: 6026bbb86f72612d30b9e10d
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026bc516176752d3539b202
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bc516176752d3539b202
  - ClassId: mo.MoRef
    Moid: 6026bc516176752d3539b204
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bc516176752d3539b204
  - ClassId: mo.MoRef
    Moid: 6026bc516176752d3539b209
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bc516176752d3539b209
  - ClassId: mo.MoRef
    Moid: 6026bc516176752d3539b220
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bc516176752d3539b220
  - ClassId: mo.MoRef
    Moid: 6026bc516176752d3539b231
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bc516176752d3539b231
  - ClassId: mo.MoRef
    Moid: 6026bc516176752d3539b236
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bc516176752d3539b236
  - ClassId: mo.MoRef
    Moid: 6026bc516176752d3539b240
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026bc516176752d3539b240
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026bc6c6176752d3539ccd3
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026bc6c6176752d3539ccd3
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.50
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6026bc516176752d3539b1b7
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026bc516176752d3539b1b7
  LocatorLedOn: true
  ManagementIp: 10.58.29.50
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.50
  ModTime: '2022-09-14T07:43:11.793Z'
  Model: UCSC-C220-M5SX
  Moid: 6026bc4e6176752d3539ad8b
  Name: core-p5g-eu-spdc-WZP23440N02
  NumAdaptors: 1
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026bbb86f72612d30b9e10d
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026bc686176752d3539c879
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bc686176752d3539c879
  - ClassId: mo.MoRef
    Moid: 6026bc686176752d3539c87d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bc686176752d3539c87d
  - ClassId: mo.MoRef
    Moid: 6026bc686176752d3539c882
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bc686176752d3539c882
  - ClassId: mo.MoRef
    Moid: 6026bc686176752d3539c884
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bc686176752d3539c884
  - ClassId: mo.MoRef
    Moid: 6026bc686176752d3539c887
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026bc686176752d3539c887
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026bc516176752d3539b162
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026bc516176752d3539b162
  - ClassId: mo.MoRef
    Moid: 6026bc516176752d3539b167
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026bc516176752d3539b167
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026bbb86f72612d30b9e10d
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026bbb86f72612d30b9e10d
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23440N02
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRSL
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026bc656176752d3539c672
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026bc656176752d3539c672
  TopologyScanStatus: ''
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: core-p5g-eu-spdc-WZP23440N02
  Uuid: 7644B88F-BACA-4F07-A058-2EB1C6D21446
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6026c0356176752d353b7f27
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026c0356176752d353b7f27
  - ClassId: mo.MoRef
    Moid: 6026c1896176752d353c109c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026c1896176752d353c109c
  - ClassId: mo.MoRef
    Moid: 6026c1896176752d353c10a2
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026c1896176752d353c10a2
  - ClassId: mo.MoRef
    Moid: 6026c1896176752d353c10a8
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6026c1896176752d353c10a8
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02ACA2E
  AvailableMemory: 524288
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 60a2aa376176752d35dd2519
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/60a2aa376176752d35dd2519
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d5a89b6176752d3576ae09
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d5a89b6176752d3576ae09
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6026c03f6176752d353b82c2
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6026c03f6176752d353b82c2
  Bmc:
    ClassId: mo.MoRef
    Moid: 6026c0946176752d353ba76a
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6026c0946176752d353ba76a
  Board:
    ClassId: mo.MoRef
    Moid: 6026c0596176752d353b9027
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6026c0596176752d353b9027
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6026c0766176752d353b9bb7
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6026c0766176752d353b9bb7
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6026c0796176752d353b9ceb
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6026c0796176752d353b9ceb
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 60a3c96b6176752d3559815f
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/60a3c96b6176752d3559815f
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 60a3c9826176752d35598d8f
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/60a3c9826176752d35598d8f
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2021-02-12T17:52:18.53Z'
  DeviceMoId: 6026c0336f72612d30ba2932
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6026c0666176752d353b94f2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026c0666176752d353b94f2
  - ClassId: mo.MoRef
    Moid: 6026c0666176752d353b94f6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026c0666176752d353b94f6
  - ClassId: mo.MoRef
    Moid: 6026c0666176752d353b94f9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026c0666176752d353b94f9
  - ClassId: mo.MoRef
    Moid: 6026c0666176752d353b94fb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026c0666176752d353b94fb
  - ClassId: mo.MoRef
    Moid: 6026c0666176752d353b94fe
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026c0666176752d353b94fe
  - ClassId: mo.MoRef
    Moid: 6026c0666176752d353b9500
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026c0666176752d353b9500
  - ClassId: mo.MoRef
    Moid: 6026c0666176752d353b9506
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6026c0666176752d353b9506
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6026c1806176752d353c0e17
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6026c1806176752d353c0e17
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.39
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
    Moid: 6026c0696176752d353b967a
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6026c0696176752d353b967a
  LocatorLedOn: false
  ManagementIp: 10.58.50.39
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.39
  ModTime: '2022-09-22T14:40:05.271Z'
  Model: UCSC-C220-M5SX
  Moid: 6026c0526176752d353b8b29
  Name: esx22-eu-spdc-WZP2343171Y
  NumAdaptors: 1
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6026c0336f72612d30ba2932
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6026c1566176752d353bfba4
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026c1566176752d353bfba4
  - ClassId: mo.MoRef
    Moid: 6026c1566176752d353bfbab
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026c1566176752d353bfbab
  - ClassId: mo.MoRef
    Moid: 6026c1566176752d353bfbad
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026c1566176752d353bfbad
  - ClassId: mo.MoRef
    Moid: 6026c1566176752d353bfbaf
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026c1566176752d353bfbaf
  - ClassId: mo.MoRef
    Moid: 6026c1566176752d353bfbb2
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6026c1566176752d353bfbb2
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6026c05f6176752d353b927b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026c05f6176752d353b927b
  - ClassId: mo.MoRef
    Moid: 6026c05f6176752d353b927d
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6026c05f6176752d353b927d
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6026c0336f72612d30ba2932
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6026c0336f72612d30ba2932
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP2343171Y
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6026c0a36176752d353baccf
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6026c0a36176752d353baccf
  TopologyScanStatus: ''
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx22-eu-spdc-WZP2343171Y
  Uuid: 63C75335-736F-4B9D-B43F-9AFB25267276
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6061d7fe6176752d3573dfe4
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6061d7fe6176752d3573dfe4
  - ClassId: mo.MoRef
    Moid: 6061d7fe6176752d3573dfea
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6061d7fe6176752d3573dfea
  - ClassId: mo.MoRef
    Moid: 60e66fbb76752d31311689b7
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/60e66fbb76752d31311689b7
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6061d6bd6176752d35735fd9
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6061d6bd6176752d35735fd9
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d57e6c6176752d355ffdbf
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d57e6c6176752d355ffdbf
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6061d6ba6176752d35735e98
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6061d6ba6176752d35735e98
  Bmc:
    ClassId: mo.MoRef
    Moid: 6061d6f66176752d357377b7
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6061d6f66176752d357377b7
  Board:
    ClassId: mo.MoRef
    Moid: 6061d6c36176752d357361f6
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6061d6c36176752d357361f6
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6061d6df6176752d35736d61
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6061d6df6176752d35736d61
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6061d6d96176752d35736a3f
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6061d6d96176752d35736a3f
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2021-03-29T13:31:44.081Z'
  DeviceMoId: 6061d69a6f72612d30c09961
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6061d6cc6176752d35736605
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6061d6cc6176752d35736605
  - ClassId: mo.MoRef
    Moid: 6061d6cc6176752d35736609
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6061d6cc6176752d35736609
  - ClassId: mo.MoRef
    Moid: 6061d6cd6176752d3573660f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6061d6cd6176752d3573660f
  - ClassId: mo.MoRef
    Moid: 6061d6cd6176752d35736616
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6061d6cd6176752d35736616
  - ClassId: mo.MoRef
    Moid: 6061d6cd6176752d3573661c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6061d6cd6176752d3573661c
  - ClassId: mo.MoRef
    Moid: 6061d6cd6176752d3573661e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6061d6cd6176752d3573661e
  - ClassId: mo.MoRef
    Moid: 6061d6cd6176752d35736620
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6061d6cd6176752d35736620
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6061d7f56176752d3573dd6b
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6061d7f56176752d3573dd6b
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.244.70
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.244.1
    Dn: sys/rack-unit-1/mgmt/if-1
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 1
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: MgmtInterface
  KvmServerStateEnabled: false
  KvmVendor: Avocent
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6061d6d46176752d35736897
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6061d6d46176752d35736897
  LocatorLedOn: false
  ManagementIp: 10.58.244.70
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.244.70
  ModTime: '2022-08-09T07:28:44.157Z'
  Model: UCSC-C220-M5SX
  Moid: 6061d6c06176752d357360aa
  Name: ' C220-WZP23360FH9'
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
  - 6061d69a6f72612d30c09961
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6061d70e6176752d35738359
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6061d70e6176752d35738359
  - ClassId: mo.MoRef
    Moid: 6061d70e6176752d3573835b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6061d70e6176752d3573835b
  - ClassId: mo.MoRef
    Moid: 6061d70e6176752d3573835e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6061d70e6176752d3573835e
  - ClassId: mo.MoRef
    Moid: 60e66fad76752d3131168747
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/60e66fad76752d3131168747
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6061d6c76176752d3573641f
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6061d6c76176752d3573641f
  - ClassId: mo.MoRef
    Moid: 6061d6c76176752d35736421
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6061d6c76176752d35736421
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6061d69a6f72612d30c09961
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6061d69a6f72612d30c09961
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23360FH9
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6061d7106176752d35738410
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6061d7106176752d35738410
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: B9F16E2C-2593-4915-BA83-6F0A8F1D9110
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 606324346176752d3508482f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/606324346176752d3508482f
  - ClassId: mo.MoRef
    Moid: 606324346176752d3508483a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/606324346176752d3508483a
  - ClassId: mo.MoRef
    Moid: 60e6a20976752d31312351cb
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/60e6a20976752d31312351cb
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 606323a16176752d3508036e
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/606323a16176752d3508036e
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d56aab6176752d35556a37
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d56aab6176752d35556a37
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6063239f6176752d35080272
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6063239f6176752d35080272
  Bmc:
    ClassId: mo.MoRef
    Moid: 606323e46176752d350822d4
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/606323e46176752d350822d4
  Board:
    ClassId: mo.MoRef
    Moid: 606323a86176752d3508073d
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/606323a86176752d3508073d
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 606323cf6176752d350818af
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/606323cf6176752d350818af
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 606323cf6176752d35081878
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/606323cf6176752d35081878
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2021-03-30T13:12:04.406Z'
  DeviceMoId: 606323916f72612d30e34f36
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 606323b46176752d35080b7b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/606323b46176752d35080b7b
  - ClassId: mo.MoRef
    Moid: 606323b46176752d35080b7d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/606323b46176752d35080b7d
  - ClassId: mo.MoRef
    Moid: 606323b46176752d35080b7f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/606323b46176752d35080b7f
  - ClassId: mo.MoRef
    Moid: 606323b46176752d35080b81
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/606323b46176752d35080b81
  - ClassId: mo.MoRef
    Moid: 606323b46176752d35080b84
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/606323b46176752d35080b84
  - ClassId: mo.MoRef
    Moid: 606323b46176752d35080b88
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/606323b46176752d35080b88
  - ClassId: mo.MoRef
    Moid: 606323b46176752d35080b8a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/606323b46176752d35080b8a
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6063242b6176752d3508444c
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6063242b6176752d3508444c
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.244.186
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.244.1
    Dn: sys/rack-unit-1/mgmt/if-1
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 1
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: MgmtInterface
  KvmServerStateEnabled: false
  KvmVendor: Avocent
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 606323b86176752d35080d72
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/606323b86176752d35080d72
  LocatorLedOn: false
  ManagementIp: 10.58.244.186
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.244.186
  ModTime: '2022-07-26T01:46:26.691Z'
  Model: UCSC-C220-M5SX
  Moid: 606323a46176752d350804cb
  Name: ' C220-WZP23350ZAQ'
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
  - 606323916f72612d30e34f36
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 606323fd6176752d35082e60
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/606323fd6176752d35082e60
  - ClassId: mo.MoRef
    Moid: 606323fd6176752d35082e62
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/606323fd6176752d35082e62
  - ClassId: mo.MoRef
    Moid: 606323fd6176752d35082e64
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/606323fd6176752d35082e64
  - ClassId: mo.MoRef
    Moid: 60e6a1fe76752d3131234e9c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/60e6a1fe76752d3131234e9c
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 606323b26176752d35080a8c
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/606323b26176752d35080a8c
  - ClassId: mo.MoRef
    Moid: 606323b26176752d35080a8e
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/606323b26176752d35080a8e
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 606323916f72612d30e34f36
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/606323916f72612d30e34f36
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23350ZAQ
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 606323fb6176752d35082d77
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/606323fb6176752d35082d77
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 0A5ECF8C-F6A6-4D83-BF34-9DBC23EDF170
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 60632c5a6176752d350bd685
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/60632c5a6176752d350bd685
  - ClassId: mo.MoRef
    Moid: 60e635da76752d3131052f4f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/60e635da76752d3131052f4f
  - ClassId: mo.MoRef
    Moid: 60e635e476752d31310532a5
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/60e635e476752d31310532a5
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 524288
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 60632bd06176752d350b9c60
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/60632bd06176752d350b9c60
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d567c66176752d3553d903
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d567c66176752d3553d903
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 60632bd16176752d350b9c9e
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/60632bd16176752d350b9c9e
  Bmc:
    ClassId: mo.MoRef
    Moid: 60632c146176752d350bbc42
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/60632c146176752d350bbc42
  Board:
    ClassId: mo.MoRef
    Moid: 60632be16176752d350ba27c
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/60632be16176752d350ba27c
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 60632bf66176752d350bad4b
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/60632bf66176752d350bad4b
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 60632bf86176752d350bae37
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/60632bf86176752d350bae37
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 56C 112T
  CreateTime: '2021-03-30T13:47:06.719Z'
  DeviceMoId: 60632bb46f72612d30e4222e
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 60632be36176752d350ba37b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632be36176752d350ba37b
  - ClassId: mo.MoRef
    Moid: 60632be36176752d350ba37d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632be36176752d350ba37d
  - ClassId: mo.MoRef
    Moid: 60632be36176752d350ba380
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632be36176752d350ba380
  - ClassId: mo.MoRef
    Moid: 60632be36176752d350ba382
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632be36176752d350ba382
  - ClassId: mo.MoRef
    Moid: 60632be36176752d350ba384
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632be36176752d350ba384
  - ClassId: mo.MoRef
    Moid: 60632be36176752d350ba386
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632be36176752d350ba386
  - ClassId: mo.MoRef
    Moid: 60632be36176752d350ba388
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632be36176752d350ba388
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 60632c526176752d350bd31d
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/60632c526176752d350bd31d
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.244.236
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.244.1
    Dn: sys/rack-unit-1/mgmt/if-1
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 1
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: MgmtInterface
  KvmServerStateEnabled: false
  KvmVendor: Avocent
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 60632beb6176752d350ba74c
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/60632beb6176752d350ba74c
  LocatorLedOn: false
  ManagementIp: 10.58.244.236
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.244.236
  ModTime: '2022-07-25T18:36:07.383Z'
  Model: UCSC-C240-M5SX
  Moid: 60632bda6176752d350b9fc0
  Name: C240-WZP232102PH
  NumAdaptors: 1
  NumCpuCores: 56
  NumCpuCoresEnabled: 56
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 112
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 60632bb46f72612d30e4222e
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 60632c2e6176752d350bc698
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/60632c2e6176752d350bc698
  - ClassId: mo.MoRef
    Moid: 60632c2e6176752d350bc69b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/60632c2e6176752d350bc69b
  - ClassId: mo.MoRef
    Moid: 60e5496876752d323209f9be
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/60e5496876752d323209f9be
  - ClassId: mo.MoRef
    Moid: 60e5496876752d323209f9d4
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/60e5496876752d323209f9d4
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 60632be16176752d350ba285
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/60632be16176752d350ba285
  - ClassId: mo.MoRef
    Moid: 60632be16176752d350ba287
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/60632be16176752d350ba287
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 60632bb46f72612d30e4222e
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/60632bb46f72612d30e4222e
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 62a7838b76752d3139131bb8
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/62a7838b76752d3139131bb8
  Serial: WZP232102PH
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 60632c236176752d350bc264
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/60632c236176752d350bc264
  TopologyScanStatus: ''
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 9B8B6F4D-B13B-449A-9B64-6567B91D0259
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 60632e556176752d350ca911
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/60632e556176752d350ca911
  - ClassId: mo.MoRef
    Moid: 614881c976752d31379979d0
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/614881c976752d31379979d0
  - ClassId: mo.MoRef
    Moid: 6148825d76752d313799a3a8
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6148825d76752d313799a3a8
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 1
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 327680
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 60632dce6176752d350c7200
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/60632dce6176752d350c7200
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d58c7b6176752d3567e5ee
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d58c7b6176752d3567e5ee
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 60632dca6176752d350c6f0f
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/60632dca6176752d350c6f0f
  Bmc:
    ClassId: mo.MoRef
    Moid: 60632e0b6176752d350c8aa5
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/60632e0b6176752d350c8aa5
  Board:
    ClassId: mo.MoRef
    Moid: 60632dd36176752d350c7423
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/60632dd36176752d350c7423
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 60632dfe6176752d350c85fc
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/60632dfe6176752d350c85fc
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 60632df86176752d350c83e9
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/60632df86176752d350c83e9
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2021-03-30T13:55:27.375Z'
  DeviceMoId: 60632d896f72612d30e45356
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 60632dde6176752d350c7a0f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632dde6176752d350c7a0f
  - ClassId: mo.MoRef
    Moid: 60632dde6176752d350c7a11
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632dde6176752d350c7a11
  - ClassId: mo.MoRef
    Moid: 60632dde6176752d350c7a13
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632dde6176752d350c7a13
  - ClassId: mo.MoRef
    Moid: 60632dde6176752d350c7a1c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632dde6176752d350c7a1c
  - ClassId: mo.MoRef
    Moid: 60632dde6176752d350c7a1e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632dde6176752d350c7a1e
  - ClassId: mo.MoRef
    Moid: 60632dde6176752d350c7a20
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632dde6176752d350c7a20
  - ClassId: mo.MoRef
    Moid: 60632dde6176752d350c7a22
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/60632dde6176752d350c7a22
  FaultSummary: 65536
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 60632e4d6176752d350ca55a
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/60632e4d6176752d350ca55a
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.250.241
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.250.1
    Dn: sys/rack-unit-1/mgmt/if-1
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 1
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: MgmtInterface
  KvmServerStateEnabled: false
  KvmVendor: Avocent
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 60632de26176752d350c7b66
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/60632de26176752d350c7b66
  LocatorLedOn: false
  ManagementIp: 10.58.250.241
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.250.241
  ModTime: '2022-10-10T17:31:36.327Z'
  Model: UCSC-C220-M5SX
  Moid: 60632dcf6176752d350c72bc
  Name: C220-231
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
  - 60632d896f72612d30e45356
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 60632e226176752d350c937e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/60632e226176752d350c937e
  - ClassId: mo.MoRef
    Moid: 60632e226176752d350c9380
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/60632e226176752d350c9380
  - ClassId: mo.MoRef
    Moid: 6148822c76752d313799958b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6148822c76752d313799958b
  - ClassId: mo.MoRef
    Moid: 6148822c76752d3137999592
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6148822c76752d3137999592
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 60632dde6176752d350c79f6
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/60632dde6176752d350c79f6
  - ClassId: mo.MoRef
    Moid: 60632dde6176752d350c79f8
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/60632dde6176752d350c79f8
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 60632d896f72612d30e45356
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/60632d896f72612d30e45356
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23240NNZ
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+CRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 60632e206176752d350c92ce
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/60632e206176752d350c92ce
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 69E3C014-747B-4FC6-874F-F4380C0F440D
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6098fe5c6176752d35a6d757
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6098fe5c6176752d35a6d757
  - ClassId: mo.MoRef
    Moid: 6098feee6176752d35a7188b
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6098feee6176752d35a7188b
  - ClassId: mo.MoRef
    Moid: 6098feee6176752d35a71898
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6098feee6176752d35a71898
  - ClassId: mo.MoRef
    Moid: 6098feee6176752d35a7189e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6098feee6176752d35a7189e
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02ACA3A
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6098fe666176752d35a6db07
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6098fe666176752d35a6db07
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 60d583e66176752d35633b12
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/60d583e66176752d35633b12
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6098fe646176752d35a6da3d
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6098fe646176752d35a6da3d
  Bmc:
    ClassId: mo.MoRef
    Moid: 6098fea86176752d35a6f55f
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6098fea86176752d35a6f55f
  Board:
    ClassId: mo.MoRef
    Moid: 6098fe6c6176752d35a6dd09
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6098fe6c6176752d35a6dd09
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6098fe8f6176752d35a6ea60
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6098fe8f6176752d35a6ea60
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6098fe976176752d35a6ef45
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6098fe976176752d35a6ef45
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 613aa37a76752d313753b743
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/613aa37a76752d313753b743
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2021-05-10T09:35:36.868Z'
  DeviceMoId: 6098fe506f72612d30e78ffb
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6098fe776176752d35a6e132
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6098fe776176752d35a6e132
  - ClassId: mo.MoRef
    Moid: 6098fe776176752d35a6e134
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6098fe776176752d35a6e134
  - ClassId: mo.MoRef
    Moid: 6098fe776176752d35a6e136
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6098fe776176752d35a6e136
  - ClassId: mo.MoRef
    Moid: 6098fe776176752d35a6e139
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6098fe776176752d35a6e139
  - ClassId: mo.MoRef
    Moid: 6098fe776176752d35a6e13b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6098fe776176752d35a6e13b
  - ClassId: mo.MoRef
    Moid: 6098fe776176752d35a6e13d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6098fe776176752d35a6e13d
  - ClassId: mo.MoRef
    Moid: 6098fe776176752d35a6e13f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6098fe776176752d35a6e13f
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6098fee96176752d35a7145b
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6098fee96176752d35a7145b
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.25.33
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.25.62
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
    Moid: 6098fe7b6176752d35a6e31e
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6098fe7b6176752d35a6e31e
  LocatorLedOn: false
  ManagementIp: 10.58.25.33
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2400'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.25.33
  ModTime: '2022-07-25T08:06:46.826Z'
  Model: UCSC-C240-M5SX
  Moid: 6098fe686176752d35a6dbc8
  Name: esx91-eu-spdc-WZP234411LW
  NumAdaptors: 1
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 4
  NumFcHostInterfaces: 4
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6098fe506f72612d30e78ffb
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6098febb6176752d35a6fd4b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6098febb6176752d35a6fd4b
  - ClassId: mo.MoRef
    Moid: 6098febb6176752d35a6fd4d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6098febb6176752d35a6fd4d
  - ClassId: mo.MoRef
    Moid: 6098febb6176752d35a6fd4f
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6098febb6176752d35a6fd4f
  - ClassId: mo.MoRef
    Moid: 6098febb6176752d35a6fd51
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6098febb6176752d35a6fd51
  - ClassId: mo.MoRef
    Moid: 6098febb6176752d35a6fd53
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6098febb6176752d35a6fd53
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 60990a8d6176752d35ac64eb
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/60990a8d6176752d35ac64eb
  - ClassId: mo.MoRef
    Moid: 60990a8d6176752d35ac64ed
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/60990a8d6176752d35ac64ed
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6098fe506f72612d30e78ffb
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6098fe506f72612d30e78ffb
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 613a17b076752d31372d3059
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/613a17b076752d31372d3059
  Serial: WZP234411LW
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: LAB-ID
    Value: DMZ
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6098feb96176752d35a6fc1a
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6098feb96176752d35a6fc1a
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx91-eu-spdc-WZP234411LW
  Uuid: 5834CCAA-BD55-4A13-8BBA-095B3B2BA172
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 612518d976752d3131db183e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/612518d976752d3131db183e
  - ClassId: mo.MoRef
    Moid: 612518d976752d3131db1845
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/612518d976752d3131db1845
  - ClassId: mo.MoRef
    Moid: 612518d976752d3131db1850
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/612518d976752d3131db1850
  - ClassId: mo.MoRef
    Moid: 61a9519a76752d31396fee88
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61a9519a76752d31396fee88
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0290553
  AvailableMemory: 196608
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61260a7476752d3131235a8b
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61260a7476752d3131235a8b
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6126090276752d313122dc32
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6126090276752d313122dc32
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61260a6f76752d3131235a0a
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61260a6f76752d3131235a0a
  Bmc:
    ClassId: mo.MoRef
    Moid: 6126311876752d31312ef3d1
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6126311876752d31312ef3d1
  Board:
    ClassId: mo.MoRef
    Moid: 61260a9076752d31312362de
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61260a9076752d31312362de
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61260c6876752d313123f4f6
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61260c6876752d313123f4f6
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61260aaa76752d3131236e01
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61260aaa76752d3131236e01
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 61260c6876752d313123f506
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61260c6876752d313123f506
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 6126311776752d31312ef3af
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/6126311776752d31312ef3af
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 24C 48T
  CreateTime: '2021-08-25T09:16:49.025Z'
  DeviceMoId: 5ecf87256f72612d3068b971
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6126083776752d3131229cfc
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6126083776752d3131229cfc
  - ClassId: mo.MoRef
    Moid: 6126083776752d3131229cfe
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6126083776752d3131229cfe
  - ClassId: mo.MoRef
    Moid: 6126083776752d3131229d06
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6126083776752d3131229d06
  - ClassId: mo.MoRef
    Moid: 6126083776752d3131229d0e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6126083776752d3131229d0e
  - ClassId: mo.MoRef
    Moid: 6126083776752d3131229d10
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6126083776752d3131229d10
  - ClassId: mo.MoRef
    Moid: 6126083776752d3131229d12
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6126083776752d3131229d12
  - ClassId: mo.MoRef
    Moid: 6126083776752d3131229d18
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6126083776752d3131229d18
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 612518d876752d3131db17da
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/612518d876752d3131db17da
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.52
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 6126310b76752d31312eef90
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6126310b76752d31312eef90
  LocatorLedOn: false
  ManagementIp: 10.58.28.52
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.52
  ModTime: '2022-09-22T15:31:34.439Z'
  Model: UCSC-C240-M5SX
  Moid: 61260a8076752d3131235d3a
  Name: comp2-p2a-eu-spdc-WZP22511E6G
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5ecf87256f72612d3068b971
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 612517ea76752d3131daca97
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/612517ea76752d3131daca97
  - ClassId: mo.MoRef
    Moid: 612517ea76752d3131daca99
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/612517ea76752d3131daca99
  - ClassId: mo.MoRef
    Moid: 612517ea76752d3131daca9b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/612517ea76752d3131daca9b
  - ClassId: mo.MoRef
    Moid: 612517ea76752d3131daca9d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/612517ea76752d3131daca9d
  - ClassId: mo.MoRef
    Moid: 61bb2c5976752d313999516d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61bb2c5976752d313999516d
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61260a9576752d31312363ee
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61260a9576752d31312363ee
  - ClassId: mo.MoRef
    Moid: 61260a9576752d31312363f0
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61260a9576752d31312363f0
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5ecf87256f72612d3068b971
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5ecf87256f72612d3068b971
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 62e8fc3376752d3139c8a327
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/62e8fc3376752d3139c8a327
  Serial: WZP22511E6G
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6123643976752d31315847b6
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6123643976752d31315847b6
  TopologyScanStatus: ''
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp2-p2a-eu-spdc-WZP22511E6G
  Uuid: 52568773-B235-4BDC-A1CB-A2C44B91E46A
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61324fe876752d3131fd76fc
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61324fe876752d3131fd76fc
  - ClassId: mo.MoRef
    Moid: 61324fe976752d3131fd7713
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61324fe976752d3131fd7713
  - ClassId: mo.MoRef
    Moid: 61324fe976752d3131fd7723
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61324fe976752d3131fd7723
  - ClassId: mo.MoRef
    Moid: 613276a676752d31310766ab
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/613276a676752d31310766ab
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61324f9e76752d3131fd5b40
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61324f9e76752d3131fd5b40
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61324fa676752d3131fd5ca1
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61324fa676752d3131fd5ca1
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61324f9676752d3131fd5979
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61324f9676752d3131fd5979
  Bmc:
    ClassId: mo.MoRef
    Moid: 61324fc276752d3131fd6aa0
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61324fc276752d3131fd6aa0
  Board:
    ClassId: mo.MoRef
    Moid: 61324fa876752d3131fd5d94
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61324fa876752d3131fd5d94
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61324fba76752d3131fd6616
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61324fba76752d3131fd6616
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61324fba76752d3131fd664e
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61324fba76752d3131fd664e
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6132c44476752d31311c8820
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6132c44476752d31311c8820
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2021-09-03T16:39:03.142Z'
  DeviceMoId: 61320ad96f72612d300340e7
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61324fb176752d3131fd6258
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61324fb176752d3131fd6258
  - ClassId: mo.MoRef
    Moid: 61324fb176752d3131fd626e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61324fb176752d3131fd626e
  - ClassId: mo.MoRef
    Moid: 61324fb176752d3131fd6279
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61324fb176752d3131fd6279
  - ClassId: mo.MoRef
    Moid: 61324fb176752d3131fd6283
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61324fb176752d3131fd6283
  - ClassId: mo.MoRef
    Moid: 61324fb276752d3131fd628b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61324fb276752d3131fd628b
  - ClassId: mo.MoRef
    Moid: 61324fb276752d3131fd628f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61324fb276752d3131fd628f
  - ClassId: mo.MoRef
    Moid: 61324fb276752d3131fd6293
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61324fb276752d3131fd6293
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61324fe676752d3131fd7670
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61324fe676752d3131fd7670
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.40
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
    Moid: 61324fb476752d3131fd637e
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61324fb476752d3131fd637e
  LocatorLedOn: false
  ManagementIp: 10.58.50.40
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.40
  ModTime: '2022-09-28T14:42:51.444Z'
  Model: UCSC-C220-M5SX
  Moid: 61324fa676752d3131fd5d08
  Name: esx20-eu-spdc-WMP24040053
  NumAdaptors: 1
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 2
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61320ad96f72612d300340e7
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6132264b76752d3131f2948e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6132264b76752d3131f2948e
  - ClassId: mo.MoRef
    Moid: 61324fd076752d3131fd6fd3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61324fd076752d3131fd6fd3
  - ClassId: mo.MoRef
    Moid: 61324fd076752d3131fd6fdc
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61324fd076752d3131fd6fdc
  - ClassId: mo.MoRef
    Moid: 61324fd076752d3131fd6fde
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61324fd076752d3131fd6fde
  - ClassId: mo.MoRef
    Moid: 61324fd076752d3131fd6fe0
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61324fd076752d3131fd6fe0
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61324faf76752d3131fd6156
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61324faf76752d3131fd6156
  - ClassId: mo.MoRef
    Moid: 61324faf76752d3131fd6163
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61324faf76752d3131fd6163
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61320ad96f72612d300340e7
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61320ad96f72612d300340e7
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WMP24040053
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61324fce76752d3131fd6ec9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61324fce76752d3131fd6ec9
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx20-eu-spdc-WMP24040053
  Uuid: F06EF79A-56C0-435F-93F5-8E3305F63538
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6139bd4276752d31371364c3
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6139bd4276752d31371364c3
  - ClassId: mo.MoRef
    Moid: 6139bdd576752d3137138db8
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6139bdd576752d3137138db8
  - ClassId: mo.MoRef
    Moid: 6139bdd576752d3137138dbe
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6139bdd576752d3137138dbe
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6139bd4a76752d3137136771
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6139bd4a76752d3137136771
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6139bd4c76752d31371367ad
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6139bd4c76752d31371367ad
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6139bd4876752d31371366dc
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6139bd4876752d31371366dc
  Bmc:
    ClassId: mo.MoRef
    Moid: 6139bd8b76752d31371378ee
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6139bd8b76752d31371378ee
  Board:
    ClassId: mo.MoRef
    Moid: 6139bd5276752d31371368a1
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6139bd5276752d31371368a1
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6139bd7676752d3137137227
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6139bd7676752d3137137227
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6139bd7576752d3137137168
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6139bd7576752d3137137168
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 48T
  CreateTime: '2021-09-09T07:52:46.907Z'
  DeviceMoId: 6139bd1a6f72612d30db6982
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6139bd5d76752d3137136bd4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6139bd5d76752d3137136bd4
  - ClassId: mo.MoRef
    Moid: 6139bd5d76752d3137136bd6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6139bd5d76752d3137136bd6
  - ClassId: mo.MoRef
    Moid: 6139bd5d76752d3137136bd8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6139bd5d76752d3137136bd8
  - ClassId: mo.MoRef
    Moid: 6139bd5d76752d3137136bda
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6139bd5d76752d3137136bda
  - ClassId: mo.MoRef
    Moid: 6139bd5d76752d3137136bde
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6139bd5d76752d3137136bde
  - ClassId: mo.MoRef
    Moid: 6139bd5d76752d3137136be0
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6139bd5d76752d3137136be0
  - ClassId: mo.MoRef
    Moid: 6139bd5d76752d3137136be2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6139bd5d76752d3137136be2
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6139bdcc76752d3137138ad2
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6139bdcc76752d3137138ad2
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.48
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 6139bd6176752d3137136d2a
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6139bd6176752d3137136d2a
  LocatorLedOn: false
  ManagementIp: 10.58.29.48
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.48
  ModTime: '2022-09-14T07:29:37.945Z'
  Model: UCSC-C240-M5SX
  Moid: 6139bd4e76752d3137136802
  Name: du-p5g-eu-spdc-WZP2526088F
  NumAdaptors: 1
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6139bd1a6f72612d30db6982
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6139bda276752d3137137f53
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6139bda276752d3137137f53
  - ClassId: mo.MoRef
    Moid: 6139bda276752d3137137f55
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6139bda276752d3137137f55
  - ClassId: mo.MoRef
    Moid: 6139bda276752d3137137f59
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6139bda276752d3137137f59
  - ClassId: mo.MoRef
    Moid: 6139bda276752d3137137f5d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6139bda276752d3137137f5d
  - ClassId: mo.MoRef
    Moid: 629f08ca76752d31397e0810
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/629f08ca76752d31397e0810
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 628e604c76752d31396f945c
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/628e604c76752d31396f945c
  - ClassId: mo.MoRef
    Moid: 628e604c76752d31396f9468
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/628e604c76752d31396f9468
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6139bd1a6f72612d30db6982
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6139bd1a6f72612d30db6982
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 62a70bb176752d3139fadfb8
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/62a70bb176752d3139fadfb8
  Serial: WZP2526088F
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6139bda076752d3137137e4f
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6139bda076752d3137137e4f
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: du-p5g-eu-spdc-WZP2526088F
  Uuid: 9AE59DAA-8EC4-4486-9807-E28FCF6ECE22
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6141c20676752d3137758edc
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c20676752d3137758edc
  - ClassId: mo.MoRef
    Moid: 6141c20676752d3137758ee2
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c20676752d3137758ee2
  - ClassId: mo.MoRef
    Moid: 6141c29876752d313775c212
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c29876752d313775c212
  - ClassId: mo.MoRef
    Moid: 6141c29876752d313775c218
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c29876752d313775c218
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6141c1ef76752d31377584c4
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6141c1ef76752d31377584c4
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6141c1f476752d3137758685
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6141c1f476752d3137758685
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6141c1ed76752d3137758429
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6141c1ed76752d3137758429
  Bmc:
    ClassId: mo.MoRef
    Moid: 6141c27776752d313775b68b
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6141c27776752d313775b68b
  Board:
    ClassId: mo.MoRef
    Moid: 6141c1f776752d31377587df
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6141c1f776752d31377587df
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6141c26776752d313775b0bd
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6141c26776752d313775b0bd
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6141c27076752d313775b3e4
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6141c27076752d313775b3e4
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 16C 32T
  CreateTime: '2021-09-15T09:50:46.284Z'
  DeviceMoId: 6141c1e76f72612d30d2b35f
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6141c20376752d3137758da8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c20376752d3137758da8
  - ClassId: mo.MoRef
    Moid: 6141c20376752d3137758daa
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c20376752d3137758daa
  - ClassId: mo.MoRef
    Moid: 6141c20376752d3137758dac
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c20376752d3137758dac
  - ClassId: mo.MoRef
    Moid: 6141c20376752d3137758dae
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c20376752d3137758dae
  - ClassId: mo.MoRef
    Moid: 6141c20376752d3137758db4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c20376752d3137758db4
  - ClassId: mo.MoRef
    Moid: 6141c20376752d3137758db6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c20376752d3137758db6
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6141c2a276752d313775c498
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6141c2a276752d313775c498
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.25.37
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.25.62
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
    Moid: 6141c22376752d3137759a3c
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6141c22376752d3137759a3c
  LocatorLedOn: false
  ManagementIp: 10.58.25.37
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.25.37
  ModTime: '2022-10-08T17:00:20.544Z'
  Model: UCSC-C220-M4S
  Moid: 6141c1f676752d313775876f
  Name: esx95-eu-spdc-FCH2017V241
  NumAdaptors: 4
  NumCpuCores: 16
  NumCpuCoresEnabled: 16
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 32
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6141c1e76f72612d30d2b35f
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6141c28f76752d313775be80
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c28f76752d313775be80
  - ClassId: mo.MoRef
    Moid: 6141c28f76752d313775be82
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c28f76752d313775be82
  - ClassId: mo.MoRef
    Moid: 6141c28f76752d313775be84
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c28f76752d313775be84
  - ClassId: mo.MoRef
    Moid: 6141c28f76752d313775be86
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c28f76752d313775be86
  - ClassId: mo.MoRef
    Moid: 6141c28f76752d313775be88
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c28f76752d313775be88
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6141c20176752d3137758cc4
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6141c20176752d3137758cc4
  - ClassId: mo.MoRef
    Moid: 6141c20176752d3137758cc6
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6141c20176752d3137758cc6
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6141c1e76f72612d30d2b35f
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6141c1e76f72612d30d2b35f
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2017V241
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6141c29276752d313775bf93
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6141c29276752d313775bf93
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx95-eu-spdc-FCH2017V241
  Uuid: D091BEC9-EB83-4683-A6C2-9BAAFD114D90
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6141c34276752d3137760184
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c34276752d3137760184
  - ClassId: mo.MoRef
    Moid: 6141c34276752d313776018a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c34276752d313776018a
  - ClassId: mo.MoRef
    Moid: 6141c36e76752d3137761120
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c36e76752d3137761120
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6141c36f76752d313776116c
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6141c36f76752d313776116c
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6141c36076752d3137760bc5
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6141c36076752d3137760bc5
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6141c37676752d31377613b3
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6141c37676752d31377613b3
  Bmc:
    ClassId: mo.MoRef
    Moid: 6141c35676752d3137760846
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6141c35676752d3137760846
  Board:
    ClassId: mo.MoRef
    Moid: 6141c39f76752d313776250d
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6141c39f76752d313776250d
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6141c37776752d3137761424
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6141c37776752d3137761424
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6141c37d76752d31377616cf
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6141c37d76752d31377616cf
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2021-09-15T09:55:47.475Z'
  DeviceMoId: 6141c3186f72612d30d2d8f8
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6141c36276752d3137760c67
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c36276752d3137760c67
  - ClassId: mo.MoRef
    Moid: 6141c36276752d3137760c69
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c36276752d3137760c69
  - ClassId: mo.MoRef
    Moid: 6141c36276752d3137760c6b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c36276752d3137760c6b
  - ClassId: mo.MoRef
    Moid: 6141c36276752d3137760c6d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c36276752d3137760c6d
  - ClassId: mo.MoRef
    Moid: 6141c36276752d3137760c70
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c36276752d3137760c70
  - ClassId: mo.MoRef
    Moid: 6141c36276752d3137760c74
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c36276752d3137760c74
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6141c33476752d313775fb7d
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6141c33476752d313775fb7d
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.25.35
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.25.62
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
    Moid: 6141c3a076752d31377625d2
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6141c3a076752d31377625d2
  LocatorLedOn: false
  ManagementIp: 10.58.25.35
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.25.35
  ModTime: '2022-10-05T21:51:45.747Z'
  Model: UCSC-C220-M4S
  Moid: 6141c32376752d313775f536
  Name: esx93-eu-spdc-FCH2108V1HE
  NumAdaptors: 3
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6141c3186f72612d30d2d8f8
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6141c34176752d31377600d3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c34176752d31377600d3
  - ClassId: mo.MoRef
    Moid: 6141c34176752d31377600d5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c34176752d31377600d5
  - ClassId: mo.MoRef
    Moid: 6141c34176752d31377600d9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c34176752d31377600d9
  - ClassId: mo.MoRef
    Moid: 6141c34176752d31377600df
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c34176752d31377600df
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6141c36676752d3137760e13
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6141c36676752d3137760e13
  - ClassId: mo.MoRef
    Moid: 6141c36676752d3137760e15
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6141c36676752d3137760e15
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6141c3186f72612d30d2d8f8
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6141c3186f72612d30d2d8f8
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2108V1HE
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6141c33076752d313775fa28
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6141c33076752d313775fa28
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx93-eu-spdc-FCH2108V1HE
  Uuid: 107BC182-F3F7-4E75-A006-FC1CFB0A9877
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6141c39b76752d31377623a4
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c39b76752d31377623a4
  - ClassId: mo.MoRef
    Moid: 6141c44376752d3137765f1a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c44376752d3137765f1a
  - ClassId: mo.MoRef
    Moid: 6141c44376752d3137765f20
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c44376752d3137765f20
  - ClassId: mo.MoRef
    Moid: 6141c44376752d3137765f26
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c44376752d3137765f26
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 1
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6141c3a176752d3137762649
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6141c3a176752d3137762649
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6141c3b176752d3137762abc
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6141c3b176752d3137762abc
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6141c3a376752d31377626cc
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6141c3a376752d31377626cc
  Bmc:
    ClassId: mo.MoRef
    Moid: 6141c3e076752d3137763bb4
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6141c3e076752d3137763bb4
  Board:
    ClassId: mo.MoRef
    Moid: 6141c3a876752d3137762832
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6141c3a876752d3137762832
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6141c37f76752d31377617cf
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6141c37f76752d31377617cf
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6141c38e76752d3137761eaf
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6141c38e76752d3137761eaf
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2021-09-15T09:58:05.642Z'
  DeviceMoId: 6141c37c6f72612d30d2e54d
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6141c3af76752d3137762a1a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3af76752d3137762a1a
  - ClassId: mo.MoRef
    Moid: 6141c3af76752d3137762a1c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3af76752d3137762a1c
  - ClassId: mo.MoRef
    Moid: 6141c3af76752d3137762a1e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3af76752d3137762a1e
  - ClassId: mo.MoRef
    Moid: 6141c3af76752d3137762a22
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3af76752d3137762a22
  - ClassId: mo.MoRef
    Moid: 6141c3af76752d3137762a24
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3af76752d3137762a24
  - ClassId: mo.MoRef
    Moid: 6141c3af76752d3137762a26
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3af76752d3137762a26
  FaultSummary: 1
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6141c44876752d313776614f
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6141c44876752d313776614f
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Warnings (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.25.34
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.25.62
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
    Moid: 6141c3be76752d31377630ab
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6141c3be76752d31377630ab
  LocatorLedOn: false
  ManagementIp: 10.58.25.34
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.25.34
  ModTime: '2022-10-05T22:01:49.104Z'
  Model: UCSC-C220-M4S
  Moid: 6141c3ad76752d31377629ad
  Name: esx92-eu-spdc-FCH2017V2AF
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6141c37c6f72612d30d2e54d
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6141c40d76752d3137764c6d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40d76752d3137764c6d
  - ClassId: mo.MoRef
    Moid: 6141c40d76752d3137764c71
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40d76752d3137764c71
  - ClassId: mo.MoRef
    Moid: 6141c40d76752d3137764c73
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40d76752d3137764c73
  - ClassId: mo.MoRef
    Moid: 6141c40d76752d3137764c75
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40d76752d3137764c75
  - ClassId: mo.MoRef
    Moid: 6141c40d76752d3137764c77
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40d76752d3137764c77
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6141c3ab76752d3137762939
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6141c3ab76752d3137762939
  - ClassId: mo.MoRef
    Moid: 6141c3ab76752d313776293b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6141c3ab76752d313776293b
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6141c37c6f72612d30d2e54d
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6141c37c6f72612d30d2e54d
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2017V2AF
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+WRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6141c40676752d3137764a15
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6141c40676752d3137764a15
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx92-eu-spdc-WZP234411LW
  Uuid: B3BA0AA2-15DA-42A2-BCD9-A157DCDA6DDA
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6141c3aa76752d31377628bd
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c3aa76752d31377628bd
  - ClassId: mo.MoRef
    Moid: 6141c44876752d3137766123
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c44876752d3137766123
  - ClassId: mo.MoRef
    Moid: 6141c44876752d313776612f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c44876752d313776612f
  - ClassId: mo.MoRef
    Moid: 6141c44876752d3137766137
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6141c44876752d3137766137
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 2
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6141c3b476752d3137762bcc
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6141c3b476752d3137762bcc
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6141c3b976752d3137762e3e
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6141c3b976752d3137762e3e
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6141c3b076752d3137762a51
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6141c3b076752d3137762a51
  Bmc:
    ClassId: mo.MoRef
    Moid: 6141c40676752d31377649ef
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6141c40676752d31377649ef
  Board:
    ClassId: mo.MoRef
    Moid: 6141c3ba76752d3137762ebe
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6141c3ba76752d3137762ebe
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6141c40376752d3137764699
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6141c40376752d3137764699
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6141c40376752d3137764712
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6141c40376752d3137764712
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2021-09-15T09:58:14.502Z'
  DeviceMoId: 6141c3976f72612d30d2e7d0
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6141c3cb76752d3137763497
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3cb76752d3137763497
  - ClassId: mo.MoRef
    Moid: 6141c3cb76752d313776349a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3cb76752d313776349a
  - ClassId: mo.MoRef
    Moid: 6141c3cb76752d313776349c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3cb76752d313776349c
  - ClassId: mo.MoRef
    Moid: 6141c3cb76752d31377634a2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3cb76752d31377634a2
  - ClassId: mo.MoRef
    Moid: 6141c3cb76752d31377634a7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3cb76752d31377634a7
  - ClassId: mo.MoRef
    Moid: 6141c3cb76752d31377634a9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6141c3cb76752d31377634a9
  FaultSummary: 2
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6141c43e76752d3137765e0c
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6141c43e76752d3137765e0c
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Warnings (2)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.25.36
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.25.62
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
    Moid: 6141c3c976752d313776344b
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6141c3c976752d313776344b
  LocatorLedOn: false
  ManagementIp: 10.58.25.36
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.25.36
  ModTime: '2022-10-08T14:39:54.029Z'
  Model: UCSC-C220-M4S
  Moid: 6141c3b676752d3137762cf2
  Name: esx94-eu-spdc-FCH2017V2AH
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6141c3976f72612d30d2e7d0
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6141c40e76752d3137764cd8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40e76752d3137764cd8
  - ClassId: mo.MoRef
    Moid: 6141c40e76752d3137764ce3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40e76752d3137764ce3
  - ClassId: mo.MoRef
    Moid: 6141c40e76752d3137764ce5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40e76752d3137764ce5
  - ClassId: mo.MoRef
    Moid: 6141c40e76752d3137764ce7
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40e76752d3137764ce7
  - ClassId: mo.MoRef
    Moid: 6141c40e76752d3137764ce9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6141c40e76752d3137764ce9
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6141c3c476752d3137763236
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6141c3c476752d3137763236
  - ClassId: mo.MoRef
    Moid: 6141c3c476752d3137763239
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6141c3c476752d3137763239
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6141c3976f72612d30d2e7d0
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6141c3976f72612d30d2e7d0
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2017V2AH
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-WRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  - Key: LAB-ID
    Value: DMZ
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6141c39b76752d3137762372
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6141c39b76752d3137762372
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx94-eu-spdc-FCH2017V2AH
  Uuid: 2ED4A546-87C9-4B15-8FFF-6C6D83573F36
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6169b3d476752d313973000c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6169b3d476752d313973000c
  - ClassId: mo.MoRef
    Moid: 6169b46576752d31397328de
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6169b46576752d31397328de
  - ClassId: mo.MoRef
    Moid: 6169b46576752d31397328e8
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6169b46576752d31397328e8
  - ClassId: mo.MoRef
    Moid: 6169b46576752d31397328ee
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6169b46576752d31397328ee
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6169b39676752d313972f2e2
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6169b39676752d313972f2e2
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6169b3bb76752d313972fb38
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6169b3bb76752d313972fb38
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6169b3e376752d31397303fa
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6169b3e376752d31397303fa
  Bmc:
    ClassId: mo.MoRef
    Moid: 6169b45476752d3139732402
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6169b45476752d3139732402
  Board:
    ClassId: mo.MoRef
    Moid: 6169b39b76752d313972f3be
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6169b39b76752d313972f3be
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6169b3ff76752d3139730c05
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6169b3ff76752d3139730c05
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6169b42376752d3139731674
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6169b42376752d3139731674
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2021-10-15T17:00:45.709Z'
  DeviceMoId: 6169b3926f72612d30589b53
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6169b3c076752d313972fc04
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b3c076752d313972fc04
  - ClassId: mo.MoRef
    Moid: 6169b3c076752d313972fc06
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b3c076752d313972fc06
  - ClassId: mo.MoRef
    Moid: 6169b3c076752d313972fc0c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b3c076752d313972fc0c
  - ClassId: mo.MoRef
    Moid: 6169b3c076752d313972fc0e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b3c076752d313972fc0e
  - ClassId: mo.MoRef
    Moid: 6169b3c076752d313972fc10
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b3c076752d313972fc10
  - ClassId: mo.MoRef
    Moid: 6169b3c076752d313972fc12
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b3c076752d313972fc12
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6169b46976752d31397329b9
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6169b46976752d31397329b9
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.60
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 6169b39e76752d313972f4c4
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6169b39e76752d313972f4c4
  LocatorLedOn: false
  ManagementIp: 10.58.28.60
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.60
  ModTime: '2022-10-05T22:01:40.266Z'
  Model: UCSC-C220-M4S
  Moid: 6169b3bd76752d313972fba0
  Name: esx9-eu-spdc-FCH2016V23J
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6169b3926f72612d30589b53
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6169b45e76752d313973274f
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b45e76752d313973274f
  - ClassId: mo.MoRef
    Moid: 6169b45e76752d3139732751
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b45e76752d3139732751
  - ClassId: mo.MoRef
    Moid: 6169b45e76752d3139732753
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b45e76752d3139732753
  - ClassId: mo.MoRef
    Moid: 6169b45e76752d3139732755
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b45e76752d3139732755
  - ClassId: mo.MoRef
    Moid: 6169b45e76752d313973275c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b45e76752d313973275c
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6169b3be76752d313972fbda
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6169b3be76752d313972fbda
  - ClassId: mo.MoRef
    Moid: 6169b3be76752d313972fbdc
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6169b3be76752d313972fbdc
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6169b3926f72612d30589b53
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6169b3926f72612d30589b53
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2016V23J
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6169b43f76752d3139731cf3
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6169b43f76752d3139731cf3
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx9-eu-spdc-FCH2016V23J
  Uuid: 255683B2-E6D9-499E-8384-37C90BE802FA
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6169b74a76752d313973df34
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6169b74a76752d313973df34
  - ClassId: mo.MoRef
    Moid: 6169b7be76752d313973fc01
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6169b7be76752d313973fc01
  - ClassId: mo.MoRef
    Moid: 6169b7be76752d313973fc07
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6169b7be76752d313973fc07
  - ClassId: mo.MoRef
    Moid: 6169b7be76752d313973fc0d
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6169b7be76752d313973fc0d
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6169b74676752d313973ddf7
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6169b74676752d313973ddf7
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6169b76376752d313973e78a
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6169b76376752d313973e78a
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6169b74b76752d313973df8d
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6169b74b76752d313973df8d
  Bmc:
    ClassId: mo.MoRef
    Moid: 6169b79776752d313973f53b
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6169b79776752d313973f53b
  Board:
    ClassId: mo.MoRef
    Moid: 6169b74776752d313973de4c
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6169b74776752d313973de4c
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6169b73976752d313973d9c8
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6169b73976752d313973d9c8
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6169b70b76752d313973cd97
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6169b70b76752d313973cd97
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2021-10-15T17:16:22.027Z'
  DeviceMoId: 6169b7086f72612d3058fe9b
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6169b73d76752d313973dab2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b73d76752d313973dab2
  - ClassId: mo.MoRef
    Moid: 6169b73d76752d313973dab4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b73d76752d313973dab4
  - ClassId: mo.MoRef
    Moid: 6169b73d76752d313973dab9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b73d76752d313973dab9
  - ClassId: mo.MoRef
    Moid: 6169b73d76752d313973dabd
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b73d76752d313973dabd
  - ClassId: mo.MoRef
    Moid: 6169b73d76752d313973dac3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b73d76752d313973dac3
  - ClassId: mo.MoRef
    Moid: 6169b73e76752d313973dac5
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6169b73e76752d313973dac5
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6169b7c976752d313973fe70
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6169b7c976752d313973fe70
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.28.61
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.28.62
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
    Moid: 6169b76176752d313973e5f6
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6169b76176752d313973e5f6
  LocatorLedOn: false
  ManagementIp: 10.58.28.61
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.28.61
  ModTime: '2022-10-05T22:01:40.284Z'
  Model: UCSC-C220-M4S
  Moid: 6169b76576752d313973e815
  Name: esx10-eu-spdc-FCH2017V0TN
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6169b7086f72612d3058fe9b
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6169b7e876752d31397404a6
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b7e876752d31397404a6
  - ClassId: mo.MoRef
    Moid: 6169b7e876752d31397404a8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b7e876752d31397404a8
  - ClassId: mo.MoRef
    Moid: 6169b7e876752d31397404aa
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b7e876752d31397404aa
  - ClassId: mo.MoRef
    Moid: 6169b7e876752d31397404ac
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b7e876752d31397404ac
  - ClassId: mo.MoRef
    Moid: 6169b7e876752d31397404ae
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6169b7e876752d31397404ae
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6169b74876752d313973de90
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6169b74876752d313973de90
  - ClassId: mo.MoRef
    Moid: 6169b74876752d313973de92
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6169b74876752d313973de92
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6169b7086f72612d3058fe9b
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6169b7086f72612d3058fe9b
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2017V0TN
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6169b7d776752d31397400fb
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6169b7d776752d31397400fb
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx10-eu-spdc-FCH2017V0TN
  Uuid: DDF98507-2D6C-47D0-91B1-8D1055824D36
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 616ea33676752d3139b2235f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/616ea33676752d3139b2235f
  - ClassId: mo.MoRef
    Moid: 616ea3df76752d3139b256df
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/616ea3df76752d3139b256df
  - ClassId: mo.MoRef
    Moid: 616ea3df76752d3139b256e5
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/616ea3df76752d3139b256e5
  - ClassId: mo.MoRef
    Moid: 616ea3df76752d3139b256eb
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/616ea3df76752d3139b256eb
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 616ea34676752d3139b225b9
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/616ea34676752d3139b225b9
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 616ea34476752d3139b2254e
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/616ea34476752d3139b2254e
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 616ea34276752d3139b224e5
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/616ea34276752d3139b224e5
  Bmc:
    ClassId: mo.MoRef
    Moid: 616ea3b976752d3139b24c6b
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/616ea3b976752d3139b24c6b
  Board:
    ClassId: mo.MoRef
    Moid: 616ea34b76752d3139b22745
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/616ea34b76752d3139b22745
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 616ea38b76752d3139b23c3c
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/616ea38b76752d3139b23c3c
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 616ea38176752d3139b2395a
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/616ea38176752d3139b2395a
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 24C 48T
  CreateTime: '2021-10-19T10:51:52.032Z'
  DeviceMoId: 616ea3296f72612d30e81fe9
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 616ea35c76752d3139b2310a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/616ea35c76752d3139b2310a
  - ClassId: mo.MoRef
    Moid: 616ea35c76752d3139b2310c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/616ea35c76752d3139b2310c
  - ClassId: mo.MoRef
    Moid: 616ea35c76752d3139b2310e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/616ea35c76752d3139b2310e
  - ClassId: mo.MoRef
    Moid: 616ea35c76752d3139b23110
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/616ea35c76752d3139b23110
  - ClassId: mo.MoRef
    Moid: 616ea35c76752d3139b23112
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/616ea35c76752d3139b23112
  - ClassId: mo.MoRef
    Moid: 616ea35c76752d3139b23114
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/616ea35c76752d3139b23114
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 616ea3ec76752d3139b259c8
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/616ea3ec76752d3139b259c8
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.51
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 616ea35d76752d3139b23138
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/616ea35d76752d3139b23138
  LocatorLedOn: false
  ManagementIp: 10.58.29.51
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.51
  ModTime: '2022-10-05T22:01:40.055Z'
  Model: UCSC-C220-M4S
  Moid: 616ea34876752d3139b2261f
  Name: esx11-eu-spdc-FCH2050V125
  NumAdaptors: 4
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 2
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 616ea3296f72612d30e81fe9
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 616ea3c876752d3139b25168
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/616ea3c876752d3139b25168
  - ClassId: mo.MoRef
    Moid: 616ea3c876752d3139b2516a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/616ea3c876752d3139b2516a
  - ClassId: mo.MoRef
    Moid: 616ea3c876752d3139b2516c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/616ea3c876752d3139b2516c
  - ClassId: mo.MoRef
    Moid: 616ea3c876752d3139b2516e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/616ea3c876752d3139b2516e
  - ClassId: mo.MoRef
    Moid: 616ea3c876752d3139b25170
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/616ea3c876752d3139b25170
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 616ea35676752d3139b22efd
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/616ea35676752d3139b22efd
  - ClassId: mo.MoRef
    Moid: 616ea35676752d3139b22eff
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/616ea35676752d3139b22eff
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 616ea3296f72612d30e81fe9
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/616ea3296f72612d30e81fe9
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2050V125
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 616ea3c076752d3139b24e1b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/616ea3c076752d3139b24e1b
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx11-eu-spdc-FCH2050V125
  Uuid: 631340A1-15FA-4CD9-9C1C-1A9EE4B63A3C
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e54
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fad76752d3139f50e54
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e90
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fad76752d3139f50e90
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 1
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 393216
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e46
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61c35fad76752d3139f50e46
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e2f
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61c35fad76752d3139f50e2f
  Bmc:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e64
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61c35fad76752d3139f50e64
  Board:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e3c
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61c35fad76752d3139f50e3c
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A
  Cpu: 2S 24C 48T
  CreateTime: '2021-12-22T17:26:05.425Z'
  DeviceMoId: 61c35fa36f72612d3005590c
  Dn: sys/rack-unit-2
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e36
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50e36
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e48
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50e48
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e80
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50e80
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e96
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50e96
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f57
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f50f57
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51045
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51045
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f41
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61c35fad76752d3139f50f41
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Warnings (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.49.234.198
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.49.234.254
    Dn: sys/rack-unit-2/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e4a
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61c35fad76752d3139f50e4a
  LocatorLedOn: false
  ManagementIp: 10.49.234.198
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.49.234.198
  ModTime: '2022-09-16T09:32:59.731Z'
  Model: UCSC-C240-M4S
  Moid: 61c35fad76752d3139f50e2d
  Name: berlin-ucsm-2
  NumAdaptors: 2
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 4
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ok
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61c35fa36f72612d3005590c
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e70
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fad76752d3139f50e70
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e8e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fad76752d3139f50e8e
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f37
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fad76752d3139f50f37
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e58
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fad76752d3139f50e58
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51055
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fae76752d3139f51055
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61c35fa36f72612d3005590c
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: FCH1930V0PH
  ServerId: 2
  ServiceProfile: org-root/ls-esxi-250
  SharedScope: ''
  State: P+WRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61c35fac76752d3139f50de9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61c35fac76752d3139f50de9
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: e427071e-4906-4cbe-9968-b42f10252e8f
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e5a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fad76752d3139f50e5a
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5110e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fae76752d3139f5110e
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 1
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 393216
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e74
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61c35fad76752d3139f50e74
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e94
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61c35fad76752d3139f50e94
  Bmc:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e9e
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61c35fad76752d3139f50e9e
  Board:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ef8
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61c35fad76752d3139f50ef8
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A
  Cpu: 2S 24C 48T
  CreateTime: '2021-12-22T17:26:05.471Z'
  DeviceMoId: 61c35fa36f72612d3005590c
  Dn: sys/rack-unit-6
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e4e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50e4e
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ec2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50ec2
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ed8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50ed8
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ee4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50ee4
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f49
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50f49
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51091
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51091
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51077
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61c35fae76752d3139f51077
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Warnings (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.49.234.195
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.49.234.254
    Dn: sys/rack-unit-6/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5106b
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61c35fae76752d3139f5106b
  LocatorLedOn: false
  ManagementIp: 10.49.234.195
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '1600'
  MgmtIdentity: null
  MgmtIpAddress: 10.49.234.195
  ModTime: '2022-09-06T13:30:51.467Z'
  Model: UCSC-C240-M4S
  Moid: 61c35fad76752d3139f50e3e
  Name: berlin-ucsm-6
  NumAdaptors: 2
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 4
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: power-off
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61c35fa36f72612d3005590c
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e56
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fad76752d3139f50e56
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ec8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fad76752d3139f50ec8
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ef6
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fad76752d3139f50ef6
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e42
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fad76752d3139f50e42
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5105f
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fae76752d3139f5105f
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61c35fa36f72612d3005590c
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: FCH1930V0KM
  ServerId: 6
  ServiceProfile: org-root/ls-openstack-243
  SharedScope: ''
  State: P-WRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61c35fac76752d3139f50de9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61c35fac76752d3139f50de9
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: d432e3fe-c503-42de-ac38-3fe8826630ad
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ed2
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fad76752d3139f50ed2
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 720896
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51120
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/61c35fae76752d3139f51120
  BiosVfSelectMemoryRasConfiguration: null
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51126
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61c35fae76752d3139f51126
  Bmc:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510ad
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61c35fae76752d3139f510ad
  Board:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ee6
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61c35fad76752d3139f50ee6
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A
  Cpu: 2S 28C 56T
  CreateTime: '2021-12-22T17:26:05.499Z'
  DeviceMoId: 61c35fa36f72612d3005590c
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e62
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50e62
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e9c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50e9c
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50eb2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50eb2
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ec4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50ec4
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f21
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50f21
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51112
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51112
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ea2
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61c35fad76752d3139f50ea2
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.49.234.199
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.49.234.254
    Dn: sys/rack-unit-1/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e6e
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61c35fad76752d3139f50e6e
  LocatorLedOn: false
  ManagementIp: 10.49.234.199
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.49.234.199
  ModTime: '2022-09-02T06:38:24.184Z'
  Model: UCSC-C240-M5SX
  Moid: 61c35fad76752d3139f50e50
  Name: berlin-ucsm-1
  NumAdaptors: 1
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 1
  NumFcHostInterfaces: 0
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: power-off
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61c35fa36f72612d3005590c
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f2b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fad76752d3139f50f2b
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5104d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f5104d
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51051
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fae76752d3139f51051
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510a3
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fae76752d3139f510a3
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61c35fa36f72612d3005590c
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: WZP21490417
  ServerId: 1
  ServiceProfile: org-root/ls-esxi-242
  SharedScope: ''
  State: P-HRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61c35fac76752d3139f50de9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61c35fac76752d3139f50de9
  TopologyScanStatus: ''
  TotalMemory: 720896
  TotalMemoryGB: 704
  TotalMemoryUnit: 704 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 9752341f-61fd-42d1-88a7-8f438fa44f86
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510d5
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fae76752d3139f510d5
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f511a0
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fae76752d3139f511a0
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 1
    ObjectType: compute.AlarmSummary
    Warning: 1
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 262144
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5105b
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61c35fae76752d3139f5105b
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51097
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61c35fae76752d3139f51097
  Bmc:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510a9
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61c35fae76752d3139f510a9
  Board:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510a5
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61c35fae76752d3139f510a5
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A
  Cpu: 2S 24C 48T
  CreateTime: '2021-12-22T17:26:05.541Z'
  DeviceMoId: 61c35fa36f72612d3005590c
  Dn: sys/rack-unit-4
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e7a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50e7a
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f31
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50f31
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f4d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f50f4d
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f59
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f50f59
  - ClassId: mo.MoRef
    Moid: 61c35faf76752d3139f511d3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35faf76752d3139f511d3
  - ClassId: mo.MoRef
    Moid: 61c35faf76752d3139f511d7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35faf76752d3139f511d7
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510d3
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61c35fae76752d3139f510d3
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.49.234.197
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.49.234.254
    Dn: sys/rack-unit-4/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f5b
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61c35fae76752d3139f50f5b
  LocatorLedOn: false
  ManagementIp: 10.49.234.197
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.49.234.197
  ModTime: '2022-09-02T06:39:58.947Z'
  Model: UCSC-C240-M4SX
  Moid: 61c35fad76752d3139f50e78
  Name: berlin-ucsm-4
  NumAdaptors: 2
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 5
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: power-off
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61c35fa36f72612d3005590c
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50e7c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fad76752d3139f50e7c
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f6b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f50f6b
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51031
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f51031
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f23
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fad76752d3139f50f23
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f33
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fad76752d3139f50f33
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61c35fa36f72612d3005590c
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: FCH1916V1CT
  ServerId: 4
  ServiceProfile: org-root/ls-esxi-247
  SharedScope: ''
  State: P-CRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61c35fac76752d3139f50de9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61c35fac76752d3139f50de9
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 2a867a6d-01fb-4c8f-babc-f6d14738e8e6
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51114
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fae76752d3139f51114
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51142
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fae76752d3139f51142
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 3
    ObjectType: compute.AlarmSummary
    Warning: 2
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 262144
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f71
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61c35fae76752d3139f50f71
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510fe
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61c35fae76752d3139f510fe
  Bmc:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510df
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61c35fae76752d3139f510df
  Board:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51075
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61c35fae76752d3139f51075
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A
  Cpu: 2S 24C 48T
  CreateTime: '2021-12-22T17:26:05.57Z'
  DeviceMoId: 61c35fa36f72612d3005590c
  Dn: sys/rack-unit-5
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f27
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50f27
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f45
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50f45
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f7b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f50f7b
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f83
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f50f83
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51083
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51083
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51118
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51118
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f2f
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61c35fad76752d3139f50f2f
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (3)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.49.234.206
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.49.234.254
    Dn: sys/rack-unit-5/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50f39
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61c35fad76752d3139f50f39
  LocatorLedOn: false
  ManagementIp: 10.49.234.206
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.49.234.206
  ModTime: '2022-09-02T06:39:58.961Z'
  Model: UCSC-C240-M4SX
  Moid: 61c35fad76752d3139f50e88
  Name: berlin-ucsm-5
  NumAdaptors: 2
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 5
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: power-off
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61c35fa36f72612d3005590c
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f79
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f50f79
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51152
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f51152
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51154
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f51154
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50eac
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fad76752d3139f50eac
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f5f
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fae76752d3139f50f5f
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61c35fa36f72612d3005590c
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: FCH1916V0UY
  ServerId: 5
  ServiceProfile: org-root/ls-esxi-245
  SharedScope: ''
  State: P-CRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61c35fac76752d3139f50de9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61c35fac76752d3139f50de9
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 2c9d0ff7-3885-4e0e-a46d-0824263dc836
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f85
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fae76752d3139f50f85
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 1
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 262144
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f53
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61c35fae76752d3139f50f53
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51095
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61c35fae76752d3139f51095
  Bmc:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5119c
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61c35fae76752d3139f5119c
  Board:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5115e
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61c35fae76752d3139f5115e
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A
  Cpu: 2S 24C 48T
  CreateTime: '2021-12-22T17:26:05.605Z'
  DeviceMoId: 61c35fa36f72612d3005590c
  Dn: sys/rack-unit-8
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61c35fad76752d3139f50ee2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fad76752d3139f50ee2
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f65
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f50f65
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f81
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f50f81
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5103f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f5103f
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51059
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51059
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510bb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f510bb
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5115a
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61c35fae76752d3139f5115a
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Warnings (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.49.234.194
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.49.234.254
    Dn: sys/rack-unit-8/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51065
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61c35fae76752d3139f51065
  LocatorLedOn: false
  ManagementIp: 10.49.234.194
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.49.234.194
  ModTime: '2022-07-25T19:04:21.96Z'
  Model: UCSC-C220-M4S
  Moid: 61c35fad76752d3139f50eae
  Name: berlin-ucsm-8
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: power-off
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61c35fa36f72612d3005590c
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f77
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f50f77
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f510e5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f510e5
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f8f
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fae76752d3139f50f8f
  - ClassId: mo.MoRef
    Moid: 61c35faf76752d3139f511e1
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35faf76752d3139f511e1
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61c35fa36f72612d3005590c
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: FCH1849V26H
  ServerId: 8
  ServiceProfile: org-root/ls-openstack-249
  SharedScope: ''
  State: P-WRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61c35fac76752d3139f50de9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61c35fac76752d3139f50de9
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: b65728fc-6d7e-44ed-883d-2843e9f074e9
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f69
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61c35fae76752d3139f50f69
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 1
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 786432
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f511b6
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61c35fae76752d3139f511b6
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51067
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61c35fae76752d3139f51067
  Bmc:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f511b0
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61c35fae76752d3139f511b0
  Board:
    ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5110c
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61c35fae76752d3139f5110c
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A
  Cpu: 2S 28C 56T
  CreateTime: '2021-12-22T17:26:05.674Z'
  DeviceMoId: 61c35fa36f72612d3005590c
  Dn: sys/rack-unit-7
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51033
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51033
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51043
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51043
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51102
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51102
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51104
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51104
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f51134
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f51134
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5114a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61c35fae76752d3139f5114a
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f8d
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61c35fae76752d3139f50f8d
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Warnings (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.49.234.205
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.49.234.254
    Dn: sys/rack-unit-7/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 61c35faf76752d3139f511dd
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61c35faf76752d3139f511dd
  LocatorLedOn: false
  ManagementIp: 10.49.234.205
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.49.234.205
  ModTime: '2022-09-08T11:44:00.846Z'
  Model: UCSC-C240-M4S
  Moid: 61c35fad76752d3139f50efa
  Name: berlin-ucsm-7
  NumAdaptors: 1
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 2
  NumFcHostInterfaces: 0
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ok
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61c35fa36f72612d3005590c
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5108f
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f5108f
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f5119e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61c35fae76752d3139f5119e
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50f99
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fae76752d3139f50f99
  - ClassId: mo.MoRef
    Moid: 61c35fae76752d3139f50fcd
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61c35fae76752d3139f50fcd
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61c35fa36f72612d3005590c
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: FCH1930V1LA
  ServerId: 7
  ServiceProfile: org-root/ls-cml-244
  SharedScope: ''
  State: P+WRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61c35fac76752d3139f50de9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61c35fac76752d3139f50de9
  TopologyScanStatus: ''
  TotalMemory: 786432
  TotalMemoryGB: 768
  TotalMemoryUnit: 768 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: a2724bbd-ceba-404f-8dd9-d4ae4dca2aa9
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61df0d4876752d3139507bfd
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61df0d4876752d3139507bfd
  - ClassId: mo.MoRef
    Moid: 61df0ddf76752d3139509944
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61df0ddf76752d3139509944
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 028743F
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61df0d5276752d3139507d3e
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61df0d5276752d3139507d3e
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61df0d5476752d3139507da6
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61df0d5476752d3139507da6
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61df0d5076752d3139507cf1
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61df0d5076752d3139507cf1
  Bmc:
    ClassId: mo.MoRef
    Moid: 61df0d9376752d313950897c
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61df0d9376752d313950897c
  Board:
    ClassId: mo.MoRef
    Moid: 61df0d5a76752d3139507fb3
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61df0d5a76752d3139507fb3
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61df0d8076752d3139508693
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61df0d8076752d3139508693
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61df0d7f76752d3139508680
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61df0d7f76752d3139508680
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 20C 40T
  CreateTime: '2022-01-12T17:18:14.782Z'
  DeviceMoId: 61df0d3c6f72612d307e5a50
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61df0d6576752d31395082cb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0d6576752d31395082cb
  - ClassId: mo.MoRef
    Moid: 61df0d6576752d31395082cd
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0d6576752d31395082cd
  - ClassId: mo.MoRef
    Moid: 61df0d6576752d31395082cf
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0d6576752d31395082cf
  - ClassId: mo.MoRef
    Moid: 61df0d6576752d31395082d1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0d6576752d31395082d1
  - ClassId: mo.MoRef
    Moid: 61df0d6576752d31395082d3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0d6576752d31395082d3
  - ClassId: mo.MoRef
    Moid: 61df0d6576752d31395082d5
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0d6576752d31395082d5
  - ClassId: mo.MoRef
    Moid: 61df0d6576752d31395082d7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0d6576752d31395082d7
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61df0dd676752d3139509730
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61df0dd676752d3139509730
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.34
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 61df0d6976752d3139508387
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61df0d6976752d3139508387
  LocatorLedOn: false
  ManagementIp: 10.58.29.34
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2400'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.34
  ModTime: '2022-07-25T21:44:40.652Z'
  Model: SE-NODE-G2
  Moid: 61df0d5676752d3139507e9e
  Name: sn12-eu-spdc-WZP23430C4D
  NumAdaptors: 1
  NumCpuCores: 20
  NumCpuCoresEnabled: 20
  NumCpus: 2
  NumEthHostInterfaces: 4
  NumFcHostInterfaces: 4
  NumThreads: 40
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61df0d3c6f72612d307e5a50
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61df0da976752d3139508dbd
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df0da976752d3139508dbd
  - ClassId: mo.MoRef
    Moid: 61df0da976752d3139508dbf
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df0da976752d3139508dbf
  - ClassId: mo.MoRef
    Moid: 61df0da976752d3139508dc5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df0da976752d3139508dc5
  - ClassId: mo.MoRef
    Moid: 61df0da976752d3139508dc7
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df0da976752d3139508dc7
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61df0d6376752d3139508267
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61df0d6376752d3139508267
  - ClassId: mo.MoRef
    Moid: 61df0d6376752d3139508272
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61df0d6376752d3139508272
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61df0d3c6f72612d307e5a50
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61df0d3c6f72612d307e5a50
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23430C4D
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61df0da776752d3139508d70
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61df0da776752d3139508d70
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: sn12-eu-spdc-WZP23430C4D
  Uuid: 843C55E5-7F48-4991-930C-B4C0BE537B4E
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61df0e0376752d313950af8e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61df0e0376752d313950af8e
  - ClassId: mo.MoRef
    Moid: 61df0e9b76752d313950d32e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61df0e9b76752d313950d32e
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 1
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 028757B
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61df0e0e76752d313950b200
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61df0e0e76752d313950b200
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61df0e1076752d313950b25b
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61df0e1076752d313950b25b
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61df0e0c76752d313950b16a
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61df0e0c76752d313950b16a
  Bmc:
    ClassId: mo.MoRef
    Moid: 61df0e4e76752d313950c0ca
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61df0e4e76752d313950c0ca
  Board:
    ClassId: mo.MoRef
    Moid: 61df0e1776752d313950b4dd
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61df0e1776752d313950b4dd
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61df0e3c76752d313950bd9f
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61df0e3c76752d313950bd9f
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61df0e3c76752d313950bd89
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61df0e3c76752d313950bd89
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 20C 40T
  CreateTime: '2022-01-12T17:21:24.275Z'
  DeviceMoId: 61df0df76f72612d307e6ad3
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61df0e2176752d313950b760
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0e2176752d313950b760
  - ClassId: mo.MoRef
    Moid: 61df0e2176752d313950b762
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0e2176752d313950b762
  - ClassId: mo.MoRef
    Moid: 61df0e2176752d313950b764
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0e2176752d313950b764
  - ClassId: mo.MoRef
    Moid: 61df0e2176752d313950b766
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0e2176752d313950b766
  - ClassId: mo.MoRef
    Moid: 61df0e2176752d313950b768
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0e2176752d313950b768
  - ClassId: mo.MoRef
    Moid: 61df0e2176752d313950b76a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0e2176752d313950b76a
  - ClassId: mo.MoRef
    Moid: 61df0e2176752d313950b770
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df0e2176752d313950b770
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61df0e9276752d313950d1b1
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61df0e9276752d313950d1b1
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.35
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 61df0e2576752d313950b881
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61df0e2576752d313950b881
  LocatorLedOn: false
  ManagementIp: 10.58.29.35
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2400'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.35
  ModTime: '2022-09-21T14:45:29.193Z'
  Model: SE-NODE-G2
  Moid: 61df0e1476752d313950b310
  Name: sn13-eu-spdc-WZP234301R9
  NumAdaptors: 1
  NumCpuCores: 20
  NumCpuCoresEnabled: 20
  NumCpus: 2
  NumEthHostInterfaces: 4
  NumFcHostInterfaces: 4
  NumThreads: 40
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61df0df76f72612d307e6ad3
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61df0e6676752d313950c637
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df0e6676752d313950c637
  - ClassId: mo.MoRef
    Moid: 61df0e6676752d313950c639
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df0e6676752d313950c639
  - ClassId: mo.MoRef
    Moid: 61df0e6676752d313950c63b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df0e6676752d313950c63b
  - ClassId: mo.MoRef
    Moid: 61df0e6676752d313950c63d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df0e6676752d313950c63d
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61df0e1f76752d313950b707
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61df0e1f76752d313950b707
  - ClassId: mo.MoRef
    Moid: 61df0e1f76752d313950b709
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61df0e1f76752d313950b709
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61df0df76f72612d307e6ad3
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61df0df76f72612d307e6ad3
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP234301R9
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+CRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61df0e6376752d313950c5ad
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61df0e6376752d313950c5ad
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: sn13-eu-spdc-WZP234301R9
  Uuid: BF7EBAB6-78EB-472B-AAA2-30220861E8C4
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61df11e876752d3139517bcf
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61df11e876752d3139517bcf
  - ClassId: mo.MoRef
    Moid: 61df127f76752d3139519b84
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61df127f76752d3139519b84
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 0287440
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61df11f276752d3139517e6a
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61df11f276752d3139517e6a
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61df11f576752d3139517f24
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61df11f576752d3139517f24
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61df11f076752d3139517deb
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61df11f076752d3139517deb
  Bmc:
    ClassId: mo.MoRef
    Moid: 61df123476752d3139518def
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61df123476752d3139518def
  Board:
    ClassId: mo.MoRef
    Moid: 61df120d76752d313951853b
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61df120d76752d313951853b
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61df122676752d3139518b8b
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61df122676752d3139518b8b
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61df122876752d3139518bff
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61df122876752d3139518bff
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 20C 40T
  CreateTime: '2022-01-12T17:38:19.272Z'
  DeviceMoId: 61df11db6f72612d307ebf0f
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61df120b76752d31395184c0
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df120b76752d31395184c0
  - ClassId: mo.MoRef
    Moid: 61df120b76752d31395184c2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df120b76752d31395184c2
  - ClassId: mo.MoRef
    Moid: 61df120b76752d31395184c4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df120b76752d31395184c4
  - ClassId: mo.MoRef
    Moid: 61df120b76752d31395184c6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df120b76752d31395184c6
  - ClassId: mo.MoRef
    Moid: 61df120b76752d31395184c8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df120b76752d31395184c8
  - ClassId: mo.MoRef
    Moid: 61df120b76752d31395184ca
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df120b76752d31395184ca
  - ClassId: mo.MoRef
    Moid: 61df120b76752d31395184cd
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61df120b76752d31395184cd
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61df127676752d31395198e8
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61df127676752d31395198e8
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.29.33
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.29.62
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
    Moid: 61df120c76752d31395184ee
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61df120c76752d31395184ee
  LocatorLedOn: false
  ManagementIp: 10.58.29.33
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2400'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.29.33
  ModTime: '2022-07-26T07:33:45.675Z'
  Model: SE-NODE-G2
  Moid: 61df120b76752d3139518492
  Name: sn11-eu-spdc-WZP23430C4N
  NumAdaptors: 1
  NumCpuCores: 20
  NumCpuCoresEnabled: 20
  NumCpus: 2
  NumEthHostInterfaces: 4
  NumFcHostInterfaces: 4
  NumThreads: 40
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61df11db6f72612d307ebf0f
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61df124b76752d3139519087
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df124b76752d3139519087
  - ClassId: mo.MoRef
    Moid: 61df124b76752d3139519089
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df124b76752d3139519089
  - ClassId: mo.MoRef
    Moid: 61df124b76752d313951908b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df124b76752d313951908b
  - ClassId: mo.MoRef
    Moid: 61df124b76752d313951908e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61df124b76752d313951908e
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61df120e76752d31395185b9
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61df120e76752d31395185b9
  - ClassId: mo.MoRef
    Moid: 61df120e76752d31395185bb
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61df120e76752d31395185bb
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61df11db6f72612d307ebf0f
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61df11db6f72612d307ebf0f
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23430C4N
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61df124976752d313951901f
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61df124976752d313951901f
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: sn11-eu-spdc-WZP23430C4N
  Uuid: 4DFF0346-6926-4025-8B69-A7C015A4F215
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61e9984676752d3139e59c63
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9984676752d3139e59c63
  - ClassId: mo.MoRef
    Moid: 61e998fd76752d3139e5c121
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e998fd76752d3139e5c121
  - ClassId: mo.MoRef
    Moid: 62e8de8976752d3139c3d46d
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62e8de8976752d3139c3d46d
  - ClassId: mo.MoRef
    Moid: 62e8de8976752d3139c3d4d5
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62e8de8976752d3139c3d4d5
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 131072
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61e9985276752d3139e59ed2
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61e9985276752d3139e59ed2
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61e9985476752d3139e59f16
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61e9985476752d3139e59f16
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61e9984e76752d3139e59e3f
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61e9984e76752d3139e59e3f
  Bmc:
    ClassId: mo.MoRef
    Moid: 61e998b176752d3139e5b34b
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61e998b176752d3139e5b34b
  Board:
    ClassId: mo.MoRef
    Moid: 61e9985c76752d3139e5a06f
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61e9985c76752d3139e5a06f
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61e9989a76752d3139e5adcf
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61e9989a76752d3139e5adcf
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61e9989476752d3139e5ac2d
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61e9989476752d3139e5ac2d
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 61e998a076752d3139e5aec5
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61e998a076752d3139e5aec5
  - ClassId: mo.MoRef
    Moid: 61e998a076752d3139e5aec7
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61e998a076752d3139e5aec7
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 61e998a276752d3139e5af62
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e998a276752d3139e5af62
  - ClassId: mo.MoRef
    Moid: 61e998a276752d3139e5af64
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e998a276752d3139e5af64
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 16C 32T
  CreateTime: '2022-01-20T17:13:58.282Z'
  DeviceMoId: 61e998396f72612d305682d9
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61e9984276752d3139e59bd4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9984276752d3139e59bd4
  - ClassId: mo.MoRef
    Moid: 61e9984276752d3139e59bd6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9984276752d3139e59bd6
  - ClassId: mo.MoRef
    Moid: 61e9984276752d3139e59bd8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9984276752d3139e59bd8
  - ClassId: mo.MoRef
    Moid: 61e9984276752d3139e59bda
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9984276752d3139e59bda
  - ClassId: mo.MoRef
    Moid: 61e9984276752d3139e59bdc
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9984276752d3139e59bdc
  - ClassId: mo.MoRef
    Moid: 61e9984276752d3139e59bde
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9984276752d3139e59bde
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61e998e176752d3139e5bb5d
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61e998e176752d3139e5bb5d
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.49
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
    Moid: 61e9986b76752d3139e5a342
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61e9986b76752d3139e5a342
  LocatorLedOn: false
  ManagementIp: 10.58.50.49
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.49
  ModTime: '2022-10-05T21:51:45.558Z'
  Model: UCSC-C240-M4SX
  Moid: 61e9985676752d3139e59f59
  Name: aio2-p3b-eu-spdc-FCH2017V1J8
  NumAdaptors: 4
  NumCpuCores: 16
  NumCpuCoresEnabled: 16
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 32
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61e998396f72612d305682d9
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61e998db76752d3139e5ba7a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e998db76752d3139e5ba7a
  - ClassId: mo.MoRef
    Moid: 61e998db76752d3139e5ba7c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e998db76752d3139e5ba7c
  - ClassId: mo.MoRef
    Moid: 61e998db76752d3139e5ba7e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e998db76752d3139e5ba7e
  - ClassId: mo.MoRef
    Moid: 62e8de8976752d3139c3d45b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e8de8976752d3139c3d45b
  - ClassId: mo.MoRef
    Moid: 62e8de8976752d3139c3d45d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e8de8976752d3139c3d45d
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61e9986776752d3139e5a20c
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61e9986776752d3139e5a20c
  - ClassId: mo.MoRef
    Moid: 61e9986776752d3139e5a20e
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61e9986776752d3139e5a20e
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61e998396f72612d305682d9
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61e998396f72612d305682d9
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 62166fa776752d3139ca2ba6
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/62166fa776752d3139ca2ba6
  Serial: FCH2017V1J8
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61e998b576752d3139e5b3ca
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61e998b576752d3139e5b3ca
  TopologyScanStatus: ''
  TotalMemory: 131072
  TotalMemoryGB: 128
  TotalMemoryUnit: 128 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio2-eu-spdc-FCH2017V1J8
  Uuid: E1827F82-84CF-41BE-99BD-AE4B53E3C676
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61e99b4f76752d3139e62994
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e99b4f76752d3139e62994
  - ClassId: mo.MoRef
    Moid: 61e99c3776752d3139e65508
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e99c3776752d3139e65508
  - ClassId: mo.MoRef
    Moid: 62e8db8d76752d3139c3528b
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62e8db8d76752d3139c3528b
  - ClassId: mo.MoRef
    Moid: 62e8db8d76752d3139c3528d
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62e8db8d76752d3139c3528d
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 131072
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61e99b6376752d3139e62d2d
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61e99b6376752d3139e62d2d
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61e99b4876752d3139e6285a
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61e99b4876752d3139e6285a
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61e99b6676752d3139e62da9
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61e99b6676752d3139e62da9
  Bmc:
    ClassId: mo.MoRef
    Moid: 61e99bb776752d3139e63dbb
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61e99bb776752d3139e63dbb
  Board:
    ClassId: mo.MoRef
    Moid: 61e99b6776752d3139e62de1
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61e99b6776752d3139e62de1
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61e99bbd76752d3139e63f25
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61e99bbd76752d3139e63f25
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61e99bbb76752d3139e63edb
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61e99bbb76752d3139e63edb
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 61e99bee76752d3139e6475d
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61e99bee76752d3139e6475d
  - ClassId: mo.MoRef
    Moid: 61e99bee76752d3139e64762
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61e99bee76752d3139e64762
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 61e99bc476752d3139e64072
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e99bc476752d3139e64072
  - ClassId: mo.MoRef
    Moid: 61e99bc476752d3139e64074
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e99bc476752d3139e64074
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 16C 32T
  CreateTime: '2022-01-20T17:26:57.903Z'
  DeviceMoId: 61e99b2d6f72612d3056bb7d
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61e99b8776752d3139e635c4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99b8776752d3139e635c4
  - ClassId: mo.MoRef
    Moid: 61e99b8776752d3139e635c6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99b8776752d3139e635c6
  - ClassId: mo.MoRef
    Moid: 61e99b8776752d3139e635c8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99b8776752d3139e635c8
  - ClassId: mo.MoRef
    Moid: 61e99b8776752d3139e635ca
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99b8776752d3139e635ca
  - ClassId: mo.MoRef
    Moid: 61e99b8776752d3139e635cc
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99b8776752d3139e635cc
  - ClassId: mo.MoRef
    Moid: 61e99b8776752d3139e635ce
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99b8776752d3139e635ce
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61e99c3976752d3139e6556e
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61e99c3976752d3139e6556e
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.50
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
    Moid: 61e99b8476752d3139e63541
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61e99b8476752d3139e63541
  LocatorLedOn: false
  ManagementIp: 10.58.50.50
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.50
  ModTime: '2022-10-05T21:51:45.642Z'
  Model: UCSC-C240-M4SX
  Moid: 61e99b6176752d3139e62d14
  Name: aio3-p3b-eu-spdc-FCH2017V1J5
  NumAdaptors: 4
  NumCpuCores: 16
  NumCpuCoresEnabled: 16
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 32
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61e99b2d6f72612d3056bb7d
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61e99bdb76752d3139e64423
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e99bdb76752d3139e64423
  - ClassId: mo.MoRef
    Moid: 61e99bdb76752d3139e64429
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e99bdb76752d3139e64429
  - ClassId: mo.MoRef
    Moid: 61e99bdb76752d3139e6442b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e99bdb76752d3139e6442b
  - ClassId: mo.MoRef
    Moid: 62e8db9676752d3139c35350
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e8db9676752d3139c35350
  - ClassId: mo.MoRef
    Moid: 62e8dba176752d3139c354b5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e8dba176752d3139c354b5
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62aebbf676752d3139112c40
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62aebbf676752d3139112c40
  - ClassId: mo.MoRef
    Moid: 62aebbf676752d3139112c43
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62aebbf676752d3139112c43
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61e99b2d6f72612d3056bb7d
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61e99b2d6f72612d3056bb7d
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 62e8db4076752d3139c34740
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/62e8db4076752d3139c34740
  Serial: FCH2017V1J5
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61e99bb876752d3139e63e32
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61e99bb876752d3139e63e32
  TopologyScanStatus: ''
  TotalMemory: 131072
  TotalMemoryGB: 128
  TotalMemoryUnit: 128 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio3-p3b-eu-spdc-FCH2017V1J5
  Uuid: 5231EC80-A36E-4217-97C7-D707EC0E2955
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61e99faa76752d3139e71016
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e99faa76752d3139e71016
  - ClassId: mo.MoRef
    Moid: 61e9a06976752d3139e73cdb
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a06976752d3139e73cdb
  - ClassId: mo.MoRef
    Moid: 61e9a06976752d3139e73ce1
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a06976752d3139e73ce1
  - ClassId: mo.MoRef
    Moid: 61e9a06976752d3139e73ce7
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a06976752d3139e73ce7
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61e99fb476752d3139e71245
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61e99fb476752d3139e71245
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61e99fb876752d3139e712e0
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61e99fb876752d3139e712e0
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61e99fb676752d3139e71275
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61e99fb676752d3139e71275
  Bmc:
    ClassId: mo.MoRef
    Moid: 61e9a00b76752d3139e72645
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61e9a00b76752d3139e72645
  Board:
    ClassId: mo.MoRef
    Moid: 61e99fbe76752d3139e71414
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61e99fbe76752d3139e71414
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61e9a01c76752d3139e72997
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61e9a01c76752d3139e72997
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61e9a00776752d3139e72595
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61e9a00776752d3139e72595
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 61e99ffe76752d3139e72410
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61e99ffe76752d3139e72410
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 61e99ffc76752d3139e72336
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e99ffc76752d3139e72336
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2022-01-20T17:45:29.68Z'
  DeviceMoId: 61e99f9c6f72612d3057152d
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61e99fcb76752d3139e716bb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99fcb76752d3139e716bb
  - ClassId: mo.MoRef
    Moid: 61e99fcb76752d3139e716c1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99fcb76752d3139e716c1
  - ClassId: mo.MoRef
    Moid: 61e99fcb76752d3139e716c3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99fcb76752d3139e716c3
  - ClassId: mo.MoRef
    Moid: 61e99fcb76752d3139e716c5
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99fcb76752d3139e716c5
  - ClassId: mo.MoRef
    Moid: 61e99fcb76752d3139e716c7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99fcb76752d3139e716c7
  - ClassId: mo.MoRef
    Moid: 61e99fcb76752d3139e716c9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e99fcb76752d3139e716c9
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61e9a06376752d3139e73ba0
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61e9a06376752d3139e73ba0
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.57
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
    Moid: 61e99fcc76752d3139e71716
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61e99fcc76752d3139e71716
  LocatorLedOn: false
  ManagementIp: 10.58.50.57
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.57
  ModTime: '2022-09-30T16:16:02.702Z'
  Model: UCSC-C220-M4S
  Moid: 61e99fb976752d3139e71340
  Name: comp1-p3b-eu-spdc-FCH2108V1FC
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61e99f9c6f72612d3057152d
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61e9a04c76752d3139e733a3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a04c76752d3139e733a3
  - ClassId: mo.MoRef
    Moid: 61e9a04c76752d3139e733a5
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a04c76752d3139e733a5
  - ClassId: mo.MoRef
    Moid: 61e9a04c76752d3139e733a7
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a04c76752d3139e733a7
  - ClassId: mo.MoRef
    Moid: 61e9a04c76752d3139e733a9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a04c76752d3139e733a9
  - ClassId: mo.MoRef
    Moid: 61e9a04c76752d3139e733ab
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a04c76752d3139e733ab
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61e99fc976752d3139e71675
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61e99fc976752d3139e71675
  - ClassId: mo.MoRef
    Moid: 61e99fc976752d3139e7167b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61e99fc976752d3139e7167b
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61e99f9c6f72612d3057152d
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61e99f9c6f72612d3057152d
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2108V1FC
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61e9a02076752d3139e72a11
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61e9a02076752d3139e72a11
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp1-p3b-eu-spdc-FCH2108V1FC
  Uuid: C7C7560B-2706-4300-AF00-77AA9980C526
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61e9a1b176752d3139e7766c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a1b176752d3139e7766c
  - ClassId: mo.MoRef
    Moid: 61e9a25376752d3139e79762
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a25376752d3139e79762
  - ClassId: mo.MoRef
    Moid: 61e9a25376752d3139e79768
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a25376752d3139e79768
  - ClassId: mo.MoRef
    Moid: 61e9a25376752d3139e7976e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a25376752d3139e7976e
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61e9a1b376752d3139e77706
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61e9a1b376752d3139e77706
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61e9a1bc76752d3139e779a1
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61e9a1bc76752d3139e779a1
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61e9a1b276752d3139e776ae
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61e9a1b276752d3139e776ae
  Bmc:
    ClassId: mo.MoRef
    Moid: 61e9a21b76752d3139e78ce6
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61e9a21b76752d3139e78ce6
  Board:
    ClassId: mo.MoRef
    Moid: 61e9a1c576752d3139e77bab
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61e9a1c576752d3139e77bab
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61e9a20476752d3139e78983
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61e9a20476752d3139e78983
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61e9a21676752d3139e78c40
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61e9a21676752d3139e78c40
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 61e9a20c76752d3139e78ac9
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61e9a20c76752d3139e78ac9
  - ClassId: mo.MoRef
    Moid: 61e9a20c76752d3139e78acb
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61e9a20c76752d3139e78acb
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 61e9a21276752d3139e78bf6
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e9a21276752d3139e78bf6
  - ClassId: mo.MoRef
    Moid: 61e9a21276752d3139e78bf8
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e9a21276752d3139e78bf8
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2022-01-20T17:54:02.384Z'
  DeviceMoId: 61e9a19a6f72612d30573d28
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61e9a1a776752d3139e7734c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a1a776752d3139e7734c
  - ClassId: mo.MoRef
    Moid: 61e9a1a776752d3139e7734e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a1a776752d3139e7734e
  - ClassId: mo.MoRef
    Moid: 61e9a1a776752d3139e77350
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a1a776752d3139e77350
  - ClassId: mo.MoRef
    Moid: 61e9a1a776752d3139e77352
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a1a776752d3139e77352
  - ClassId: mo.MoRef
    Moid: 61e9a1a776752d3139e77354
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a1a776752d3139e77354
  - ClassId: mo.MoRef
    Moid: 61e9a1a776752d3139e7735a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a1a776752d3139e7735a
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61e9a25e76752d3139e79a35
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61e9a25e76752d3139e79a35
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.58
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
    Moid: 61e9a1d376752d3139e77f78
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61e9a1d376752d3139e77f78
  LocatorLedOn: false
  ManagementIp: 10.58.50.58
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.58
  ModTime: '2022-09-30T16:15:58.349Z'
  Model: UCSC-C220-M4S
  Moid: 61e9a1ba76752d3139e778f3
  Name: comp2-p3b-eu-spdc-FCH2017V1Y6
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61e9a19a6f72612d30573d28
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61e9a23e76752d3139e792aa
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a23e76752d3139e792aa
  - ClassId: mo.MoRef
    Moid: 61e9a23e76752d3139e792ac
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a23e76752d3139e792ac
  - ClassId: mo.MoRef
    Moid: 61e9a23e76752d3139e792ae
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a23e76752d3139e792ae
  - ClassId: mo.MoRef
    Moid: 61e9a23e76752d3139e792b0
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a23e76752d3139e792b0
  - ClassId: mo.MoRef
    Moid: 61e9a23e76752d3139e792b2
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a23e76752d3139e792b2
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61e9a1a476752d3139e772bc
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61e9a1a476752d3139e772bc
  - ClassId: mo.MoRef
    Moid: 61e9a1a476752d3139e772be
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61e9a1a476752d3139e772be
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61e9a19a6f72612d30573d28
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61e9a19a6f72612d30573d28
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2017V1Y6
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61e9a24976752d3139e79580
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61e9a24976752d3139e79580
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp2-p3b-eu-spdc-FCH2017V1Y6
  Uuid: 47CBCD23-2E33-4742-A317-44FCEBA422F2
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61e9a42276752d3139e7f581
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a42276752d3139e7f581
  - ClassId: mo.MoRef
    Moid: 61e9a4d076752d3139e81852
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a4d076752d3139e81852
  - ClassId: mo.MoRef
    Moid: 61e9a4d076752d3139e81858
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a4d076752d3139e81858
  - ClassId: mo.MoRef
    Moid: 61e9a4d076752d3139e8185e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61e9a4d076752d3139e8185e
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61e9a43276752d3139e7f7c9
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61e9a43276752d3139e7f7c9
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61e9a42f76752d3139e7f735
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61e9a42f76752d3139e7f735
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61e9a42776752d3139e7f62d
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61e9a42776752d3139e7f62d
  Bmc:
    ClassId: mo.MoRef
    Moid: 61e9a47e76752d3139e80532
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61e9a47e76752d3139e80532
  Board:
    ClassId: mo.MoRef
    Moid: 61e9a43776752d3139e7f87e
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61e9a43776752d3139e7f87e
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61e9a49176752d3139e8097a
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61e9a49176752d3139e8097a
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61e9a48976752d3139e807af
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61e9a48976752d3139e807af
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 61e9a49376752d3139e809a6
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61e9a49376752d3139e809a6
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 61e9a47876752d3139e803a0
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e9a47876752d3139e803a0
  - ClassId: mo.MoRef
    Moid: 61e9a47876752d3139e803a2
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e9a47876752d3139e803a2
  - ClassId: mo.MoRef
    Moid: 61e9a47876752d3139e803a4
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61e9a47876752d3139e803a4
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 28C 56T
  CreateTime: '2022-01-20T18:04:33.121Z'
  DeviceMoId: 61e9a40d6f72612d30576dcc
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61e9a41476752d3139e7f2f0
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a41476752d3139e7f2f0
  - ClassId: mo.MoRef
    Moid: 61e9a41476752d3139e7f2f2
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a41476752d3139e7f2f2
  - ClassId: mo.MoRef
    Moid: 61e9a41476752d3139e7f2f4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a41476752d3139e7f2f4
  - ClassId: mo.MoRef
    Moid: 61e9a41476752d3139e7f2f6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a41476752d3139e7f2f6
  - ClassId: mo.MoRef
    Moid: 61e9a41476752d3139e7f2f8
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a41476752d3139e7f2f8
  - ClassId: mo.MoRef
    Moid: 61e9a41476752d3139e7f2fa
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61e9a41476752d3139e7f2fa
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61e9a4ce76752d3139e817f3
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61e9a4ce76752d3139e817f3
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.59
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
    Moid: 61e9a41f76752d3139e7f4d5
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61e9a41f76752d3139e7f4d5
  LocatorLedOn: false
  ManagementIp: 10.58.50.59
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.59
  ModTime: '2022-09-30T16:46:03.845Z'
  Model: UCSC-C220-M4S
  Moid: 61e9a43176752d3139e7f79a
  Name: comp3-p3b-eu-spdc-FCH2017V24J
  NumAdaptors: 4
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61e9a40d6f72612d30576dcc
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61e9a4cd76752d3139e81798
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a4cd76752d3139e81798
  - ClassId: mo.MoRef
    Moid: 61e9a4cd76752d3139e8179a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a4cd76752d3139e8179a
  - ClassId: mo.MoRef
    Moid: 61e9a4cd76752d3139e8179c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a4cd76752d3139e8179c
  - ClassId: mo.MoRef
    Moid: 61e9a4cd76752d3139e8179e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a4cd76752d3139e8179e
  - ClassId: mo.MoRef
    Moid: 61e9a4cd76752d3139e817a0
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61e9a4cd76752d3139e817a0
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61e9a41376752d3139e7f296
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61e9a41376752d3139e7f296
  - ClassId: mo.MoRef
    Moid: 61e9a41376752d3139e7f298
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61e9a41376752d3139e7f298
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61e9a40d6f72612d30576dcc
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61e9a40d6f72612d30576dcc
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: FCH2017V24J
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61e9a4b276752d3139e810d4
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61e9a4b276752d3139e810d4
  TopologyScanStatus: ''
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: comp3-p3b-eu-spdc-FCH2017V24J
  Uuid: 48753718-3DB4-4502-B2A0-58BC21922BA3
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 61fa65c676752d31394920a0
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61fa65c676752d31394920a0
  - ClassId: mo.MoRef
    Moid: 61fa667c76752d313949481e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/61fa667c76752d313949481e
  - ClassId: mo.MoRef
    Moid: 62e8dfa176752d3139c406e3
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62e8dfa176752d3139c406e3
  - ClassId: mo.MoRef
    Moid: 62e8dfa176752d3139c406ec
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62e8dfa176752d3139c406ec
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 131072
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61fa65bd76752d3139491d63
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61fa65bd76752d3139491d63
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61fa65bf76752d3139491e7b
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61fa65bf76752d3139491e7b
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 61fa65b376752d31394919d5
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61fa65b376752d31394919d5
  Bmc:
    ClassId: mo.MoRef
    Moid: 61fa664276752d3139493e22
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61fa664276752d3139493e22
  Board:
    ClassId: mo.MoRef
    Moid: 61fa65e676752d313949290a
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61fa65e676752d313949290a
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61fa663476752d3139493c47
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61fa663476752d3139493c47
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61fa663976752d3139493d1b
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61fa663976752d3139493d1b
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 61fa665e76752d31394941a0
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61fa665e76752d31394941a0
  - ClassId: mo.MoRef
    Moid: 61fa665e76752d31394941a2
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/61fa665e76752d31394941a2
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices:
  - ClassId: mo.MoRef
    Moid: 61fa665076752d3139493ff7
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61fa665076752d3139493ff7
  - ClassId: mo.MoRef
    Moid: 61fa665076752d3139493ff9
    ObjectType: boot.PxeDevice
    link: https://www.intersight.com/api/v1/boot/PxeDevices/61fa665076752d3139493ff9
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 16C 32T
  CreateTime: '2022-02-02T11:06:42.252Z'
  DeviceMoId: 61fa65ab6f72612d300ab92a
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 61fa65f276752d3139492ce7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61fa65f276752d3139492ce7
  - ClassId: mo.MoRef
    Moid: 61fa65f276752d3139492ceb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61fa65f276752d3139492ceb
  - ClassId: mo.MoRef
    Moid: 61fa65f276752d3139492ced
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61fa65f276752d3139492ced
  - ClassId: mo.MoRef
    Moid: 61fa65f276752d3139492cef
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61fa65f276752d3139492cef
  - ClassId: mo.MoRef
    Moid: 61fa65f276752d3139492cf1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61fa65f276752d3139492cf1
  - ClassId: mo.MoRef
    Moid: 61fa65f276752d3139492cf3
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/61fa65f276752d3139492cf3
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61fa667a76752d313949477f
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61fa667a76752d313949477f
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.48
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
    Moid: 61fa661e76752d313949380f
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61fa661e76752d313949380f
  LocatorLedOn: false
  ManagementIp: 10.58.50.48
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.48
  ModTime: '2022-09-30T15:45:59.104Z'
  Model: UCSC-C240-M4SX
  Moid: 61fa65c276752d3139491f4a
  Name: aio1-p3b-eu-spdc-FCH2017V1J7
  NumAdaptors: 4
  NumCpuCores: 16
  NumCpuCoresEnabled: 16
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 32
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61fa65ab6f72612d300ab92a
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61fa663c76752d3139493d5b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61fa663c76752d3139493d5b
  - ClassId: mo.MoRef
    Moid: 61fa663c76752d3139493d5d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61fa663c76752d3139493d5d
  - ClassId: mo.MoRef
    Moid: 61fa663c76752d3139493d5f
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61fa663c76752d3139493d5f
  - ClassId: mo.MoRef
    Moid: 62e8dfa176752d3139c406db
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e8dfa176752d3139c406db
  - ClassId: mo.MoRef
    Moid: 62e8dfa176752d3139c406ea
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e8dfa176752d3139c406ea
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
  PlatformType: IMCM4
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 61fa662576752d3139493943
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61fa662576752d3139493943
  - ClassId: mo.MoRef
    Moid: 61fa662576752d3139493945
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/61fa662576752d3139493945
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61fa65ab6f72612d300ab92a
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61fa65ab6f72612d300ab92a
  Revision: ''
  Rn: ''
  SasExpanders:
  - ClassId: mo.MoRef
    Moid: 61fe6b2e76752d313991c34f
    ObjectType: storage.SasExpander
    link: https://www.intersight.com/api/v1/storage/SasExpanders/61fe6b2e76752d313991c34f
  Serial: FCH2017V1J7
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61fa662b76752d3139493adb
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61fa662b76752d3139493adb
  TopologyScanStatus: ''
  TotalMemory: 131072
  TotalMemoryGB: 128
  TotalMemoryUnit: 128 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: aio1-p3b-eu-spdc-FCH2017V1J7
  Uuid: BB16A414-DF14-47B4-8889-BAD3872F8926
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f505
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62d157fe76752d313915f505
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f61c
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/62d157fe76752d313915f61c
  BiosVfSelectMemoryRasConfiguration: null
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f85f
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/62d157ff76752d313915f85f
  Bmc:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f52f
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/62d157fe76752d313915f52f
  Board:
    ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f877
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/62d157ff76752d313915f877
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A,B
  Cpu: 2S 40C 80T
  CreateTime: '2022-07-15T12:05:18.024Z'
  DeviceMoId: 62d157f56f72612d31c554a7
  Dn: sys/rack-unit-2
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f4fa
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f4fa
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f4fe
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f4fe
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f503
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f503
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f521
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f521
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f585
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f585
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f824
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157ff76752d313915f824
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f84d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157ff76752d313915f84d
  FaultSummary: 0
  GenericInventoryHolders: []
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.24.55
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.24.62
    Dn: sys/rack-unit-2/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f4fc
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/62d157fe76752d313915f4fc
  LocatorLedOn: false
  ManagementIp: 10.58.24.55
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.24.55
  ModTime: '2022-09-22T15:53:08.603Z'
  Model: HXAF220C-M5SN
  Moid: 62d157fd76752d313915f4f6
  Name: HX1-eu-spdc-2
  NumAdaptors: 1
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: unassociated
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 62d157f56f72612d31c554a7
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f4f8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f4f8
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f51b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f51b
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f527
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f527
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f54b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f54b
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f555
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f555
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f557
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f557
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f589
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f589
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f626
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f626
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f851
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157ff76752d313915f851
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f86a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157ff76752d313915f86a
  - ClassId: mo.MoRef
    Moid: 62d1580076752d313915f89e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d1580076752d313915f89e
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 6242d1016972652d32eda017
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f50e
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d157fe76752d313915f50e
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f53b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d157fe76752d313915f53b
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 62d157f56f72612d31c554a7
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/62d157f56f72612d31c554a7
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: WZP24100SN0
  ServerId: 2
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 62d157fc76752d313915f48a
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/62d157fc76752d313915f48a
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: aabe58d4-dcf0-4eb9-8d34-1b659bee43a4
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5af
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62d157fe76752d313915f5af
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 786432
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f523
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/62d157fe76752d313915f523
  BiosVfSelectMemoryRasConfiguration: null
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 62d1580076752d313915f8a4
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/62d1580076752d313915f8a4
  Bmc:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5bb
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/62d157fe76752d313915f5bb
  Board:
    ClassId: mo.MoRef
    Moid: 62d1580076752d313915f8e2
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/62d1580076752d313915f8e2
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A,B
  Cpu: 2S 52C 104T
  CreateTime: '2022-07-15T12:05:18.124Z'
  DeviceMoId: 62d157f56f72612d31c554a7
  Dn: sys/rack-unit-6
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f53d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f53d
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5b7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f5b7
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f602
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f602
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f63a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f63a
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f65c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f65c
  - ClassId: mo.MoRef
    Moid: 62d1580076752d313915f88c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d1580076752d313915f88c
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f53f
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/62d157fe76752d313915f53f
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.24.59
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.24.62
    Dn: sys/rack-unit-6/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 62d1580076752d313915f8e0
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/62d1580076752d313915f8e0
  LocatorLedOn: false
  ManagementIp: 10.58.24.59
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.24.59
  ModTime: '2022-09-22T15:53:08.603Z'
  Model: HXAF240C-M5SX
  Moid: 62d157fe76752d313915f512
  Name: HX1-eu-spdc-6
  NumAdaptors: 1
  NumCpuCores: 52
  NumCpuCoresEnabled: 52
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 104
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: unassociated
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 62d157f56f72612d31c554a7
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f670
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f670
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f68a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f68a
  - ClassId: mo.MoRef
    Moid: 62d1580076752d313915f89a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d1580076752d313915f89a
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 6242d1016972652d32eda017
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f662
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d157fe76752d313915f662
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f80a
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d157ff76752d313915f80a
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 62d157f56f72612d31c554a7
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/62d157f56f72612d31c554a7
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: WMP250901AY
  ServerId: 6
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 62d157fc76752d313915f48a
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/62d157fc76752d313915f48a
  TopologyScanStatus: ''
  TotalMemory: 786432
  TotalMemoryGB: 768
  TotalMemoryUnit: 768 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: d00fd2ac-71d3-4199-9447-84024fa3a999
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 62e10ecb76752d3139a82f9a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62e10ecb76752d3139a82f9a
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 3
    ObjectType: compute.AlarmSummary
    Warning: 4
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f70a
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/62d157ff76752d313915f70a
  BiosVfSelectMemoryRasConfiguration: null
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 62d1580076752d313915f8a8
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/62d1580076752d313915f8a8
  Bmc:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f583
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/62d157fe76752d313915f583
  Board:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f614
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/62d157fe76752d313915f614
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2022-07-15T12:05:18.176Z'
  DeviceMoId: 62d157f56f72612d31c554a7
  Dn: sys/rack-unit-4
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f531
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f531
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f533
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f533
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f543
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f543
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f56b
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f56b
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f591
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f591
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f593
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f593
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f820
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157ff76752d313915f820
  FaultSummary: 0
  GenericInventoryHolders: []
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (3)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.24.57
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.24.62
    Dn: sys/rack-unit-4/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f60e
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/62d157fe76752d313915f60e
  LocatorLedOn: false
  ManagementIp: 10.58.24.57
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.24.57
  ModTime: '2022-10-10T19:18:35.664Z'
  Model: HXAF220C-M5SN
  Moid: 62d157fe76752d313915f529
  Name: HX1-eu-spdc-4
  NumAdaptors: 1
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: inaccessible
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 62d157f56f72612d31c554a7
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f547
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f547
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f595
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f595
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5bf
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f5bf
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f658
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f658
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f680
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f680
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f6b0
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f6b0
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f6c8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157ff76752d313915f6c8
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f6dc
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157ff76752d313915f6dc
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f70c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157ff76752d313915f70c
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f828
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157ff76752d313915f828
  - ClassId: mo.MoRef
    Moid: 62e413eb76752d3139f3e4e8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e413eb76752d3139f3e4e8
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 6242d1016972652d32eda017
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f6fc
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d157ff76752d313915f6fc
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f810
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d157ff76752d313915f810
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 62d157f56f72612d31c554a7
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/62d157f56f72612d31c554a7
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: WZP24100SMP
  ServerId: 4
  ServiceProfile: ''
  SharedScope: ''
  State: P+CRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 62d157fc76752d313915f48a
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/62d157fc76752d313915f48a
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: eae8582c-b839-4bc8-9722-f2975b75d02d
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f6a6
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62d157fe76752d313915f6a6
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 786432
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f67e
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/62d157fe76752d313915f67e
  BiosVfSelectMemoryRasConfiguration: null
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5b5
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/62d157fe76752d313915f5b5
  Bmc:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f66c
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/62d157fe76752d313915f66c
  Board:
    ClassId: mo.MoRef
    Moid: 62d1580076752d313915f8ac
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/62d1580076752d313915f8ac
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A,B
  Cpu: 2S 52C 104T
  CreateTime: '2022-07-15T12:05:18.241Z'
  DeviceMoId: 62d157f56f72612d31c554a7
  Dn: sys/rack-unit-5
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f551
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f551
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5b9
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f5b9
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f618
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f618
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f648
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f648
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f700
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157ff76752d313915f700
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f736
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157ff76752d313915f736
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f575
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/62d157fe76752d313915f575
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.24.58
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.24.62
    Dn: sys/rack-unit-5/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f58f
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/62d157fe76752d313915f58f
  LocatorLedOn: false
  ManagementIp: 10.58.24.58
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.24.58
  ModTime: '2022-09-22T15:53:08.603Z'
  Model: HXAF240C-M5SX
  Moid: 62d157fe76752d313915f549
  Name: HX1-eu-spdc-5
  NumAdaptors: 1
  NumCpuCores: 52
  NumCpuCoresEnabled: 52
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 104
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: unassociated
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 62d157f56f72612d31c554a7
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f59d
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f59d
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f81c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157ff76752d313915f81c
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f86f
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157ff76752d313915f86f
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 6242d1016972652d32eda017
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f686
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d157fe76752d313915f686
  - ClassId: mo.MoRef
    Moid: 62d1580076752d313915f8a2
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d1580076752d313915f8a2
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 62d157f56f72612d31c554a7
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/62d157f56f72612d31c554a7
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: WMP250901B0
  ServerId: 5
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 62d157fc76752d313915f48a
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/62d157fc76752d313915f48a
  TopologyScanStatus: ''
  TotalMemory: 786432
  TotalMemoryGB: 768
  TotalMemoryUnit: 768 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 91c7a946-aa0f-4832-bbe8-8ea83eedecd2
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f565
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62d157fe76752d313915f565
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 786432
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f72c
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/62d157ff76752d313915f72c
  BiosVfSelectMemoryRasConfiguration: null
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5a7
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/62d157fe76752d313915f5a7
  Bmc:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5f0
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/62d157fe76752d313915f5f0
  Board:
    ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f62c
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/62d157fe76752d313915f62c
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A,B
  Cpu: 2S 52C 104T
  CreateTime: '2022-07-15T12:05:18.303Z'
  DeviceMoId: 62d157f56f72612d31c554a7
  Dn: sys/rack-unit-7
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5ad
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f5ad
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f604
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f604
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f63e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f63e
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f698
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157fe76752d313915f698
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f808
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d157ff76752d313915f808
  - ClassId: mo.MoRef
    Moid: 62d1580076752d313915f8d6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62d1580076752d313915f8d6
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f608
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/62d157fe76752d313915f608
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.24.54
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.24.62
    Dn: sys/rack-unit-7/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f84b
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/62d157ff76752d313915f84b
  LocatorLedOn: false
  ManagementIp: 10.58.24.54
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.24.54
  ModTime: '2022-09-22T15:53:08.603Z'
  Model: HXAF240C-M5SX
  Moid: 62d157fe76752d313915f563
  Name: HX1-eu-spdc-7
  NumAdaptors: 1
  NumCpuCores: 52
  NumCpuCoresEnabled: 52
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 104
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: unassociated
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 62d157f56f72612d31c554a7
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f5a3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f5a3
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f620
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f620
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f63c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62d157fe76752d313915f63c
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 6242d1016972652d32eda017
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62d157fe76752d313915f674
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d157fe76752d313915f674
  - ClassId: mo.MoRef
    Moid: 62d157ff76752d313915f74c
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62d157ff76752d313915f74c
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 62d157f56f72612d31c554a7
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/62d157f56f72612d31c554a7
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: WMP2509019D
  ServerId: 7
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 62d157fc76752d313915f48a
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/62d157fc76752d313915f48a
  TopologyScanStatus: ''
  TotalMemory: 786432
  TotalMemoryGB: 768
  TotalMemoryUnit: 768 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 3e44f22e-5d7d-41a1-be9e-ff686c681a34
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 62e2b60c76752d3139eacfcd
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62e2b60c76752d3139eacfcd
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 62e2b81176752d3139eb21e3
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/62e2b81176752d3139eb21e3
  BiosVfSelectMemoryRasConfiguration: null
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 62e2b60c76752d3139eacfc5
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/62e2b60c76752d3139eacfc5
  Bmc:
    ClassId: mo.MoRef
    Moid: 62e2b54b76752d3139eab328
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/62e2b54b76752d3139eab328
  Board:
    ClassId: mo.MoRef
    Moid: 62e2b60c76752d3139eacfc0
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/62e2b60c76752d3139eacfc0
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A,B
  Cpu: 2S 40C 80T
  CreateTime: '2022-07-28T16:11:55.683Z'
  DeviceMoId: 62d157f56f72612d31c554a7
  Dn: sys/rack-unit-3
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae838
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62e2b69076752d3139eae838
  - ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae83e
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62e2b69076752d3139eae83e
  - ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae844
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62e2b69076752d3139eae844
  - ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae84a
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62e2b69076752d3139eae84a
  - ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae850
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62e2b69076752d3139eae850
  - ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae856
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62e2b69076752d3139eae856
  - ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae85c
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62e2b69076752d3139eae85c
  FaultSummary: 0
  GenericInventoryHolders: []
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.24.53
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.24.62
    Dn: sys/rack-unit-3/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae836
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/62e2b69076752d3139eae836
  LocatorLedOn: false
  ManagementIp: 10.58.24.53
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.24.53
  ModTime: '2022-09-22T15:53:08.603Z'
  Model: HXAF220C-M5SN
  Moid: 62e2b54b76752d3139eab326
  Name: HX1-eu-spdc-3
  NumAdaptors: 1
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: unassociated
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 62d157f56f72612d31c554a7
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3eea
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3eea
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3eee
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3eee
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3ef0
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3ef0
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3ef2
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3ef2
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3ef4
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3ef4
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3ef6
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3ef6
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3ef8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3ef8
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3efa
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3efa
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3efc
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3efc
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3efe
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3efe
  - ClassId: mo.MoRef
    Moid: 62e2b8cf76752d3139eb3f60
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62e2b8cf76752d3139eb3f60
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 6242d1016972652d32eda017
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae7ea
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62e2b69076752d3139eae7ea
  - ClassId: mo.MoRef
    Moid: 62e2b69076752d3139eae7ec
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62e2b69076752d3139eae7ec
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 62d157f56f72612d31c554a7
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/62d157f56f72612d31c554a7
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: WZP24100SML
  ServerId: 3
  ServiceProfile: ''
  SharedScope: ''
  State: P-HRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 62d157fc76752d313915f48a
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/62d157fc76752d313915f48a
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 3b62a70d-a2fa-40f3-906c-62f280272040
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 62ebec4776752d313946783f
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62ebec4776752d313946783f
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 2
    ObjectType: compute.AlarmSummary
    Warning: 6
  Alerts: []
  Ancestors: []
  AssetTag: Unknown
  AvailableMemory: 393216
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 62ebed8776752d313946bf9a
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/62ebed8776752d313946bf9a
  BiosVfSelectMemoryRasConfiguration: null
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 62ebec4776752d3139467835
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/62ebec4776752d3139467835
  Bmc:
    ClassId: mo.MoRef
    Moid: 62ebeb3876752d3139464b21
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/62ebeb3876752d3139464b21
  Board:
    ClassId: mo.MoRef
    Moid: 62ebec4776752d3139467830
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/62ebec4776752d3139467830
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 40C 80T
  CreateTime: '2022-08-04T15:52:24.767Z'
  DeviceMoId: 62d157f56f72612d31c554a7
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 62ebec8776752d31394682a6
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62ebec8776752d31394682a6
  - ClassId: mo.MoRef
    Moid: 62ebec8776752d31394682ac
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62ebec8776752d31394682ac
  - ClassId: mo.MoRef
    Moid: 62ebec8776752d31394682b4
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62ebec8776752d31394682b4
  - ClassId: mo.MoRef
    Moid: 62ebec8776752d31394682bb
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62ebec8776752d31394682bb
  - ClassId: mo.MoRef
    Moid: 62ebec8776752d31394682c1
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62ebec8776752d31394682c1
  - ClassId: mo.MoRef
    Moid: 62ebec8776752d31394682c7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62ebec8776752d31394682c7
  - ClassId: mo.MoRef
    Moid: 62ebec8776752d31394682cd
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/62ebec8776752d31394682cd
  FaultSummary: 0
  GenericInventoryHolders: []
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (2)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.24.56
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.24.62
    Dn: sys/rack-unit-1/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 62ebec8776752d31394682a4
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/62ebec8776752d31394682a4
  LocatorLedOn: false
  ManagementIp: 10.58.24.56
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2933'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.24.56
  ModTime: '2022-09-24T03:31:08.727Z'
  Model: HXAF220C-M5SN
  Moid: 62ebeb3876752d3139464b1f
  Name: HX1-eu-spdc-1
  NumAdaptors: 1
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.RackUnit
  OperPowerState: 'off'
  OperReason: []
  OperState: inaccessible
  Operability: inoperable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 62d157f56f72612d31c554a7
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e262
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e262
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e278
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e278
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e27a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e27a
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e27c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e27c
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e27e
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e27e
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e280
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e280
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e282
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e282
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e284
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e284
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e286
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e286
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e288
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e288
  - ClassId: mo.MoRef
    Moid: 62ebee6376752d313946e2d8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/62ebee6376752d313946e2d8
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 6242d1016972652d32eda017
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 62ebec8676752d313946825b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62ebec8676752d313946825b
  - ClassId: mo.MoRef
    Moid: 62ebec8676752d313946825d
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/62ebec8676752d313946825d
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 62d157f56f72612d31c554a7
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/62d157f56f72612d31c554a7
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: WZP24100SMV
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P-CRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 62d157fc76752d313915f48a
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/62d157fc76752d313915f48a
  TopologyScanStatus: ''
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: c5fb6a88-931b-4564-afe8-c3de7bd09c76
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6311ac4676752d31398e533a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6311ac4676752d31398e533a
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 1
  Alerts: []
  Ancestors: []
  AssetTag: ''
  AvailableMemory: 688128
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6311ae0876752d31398e9a37
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6311ae0876752d31398e9a37
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6311ac4676752d31398e5336
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6311ac4676752d31398e5336
  Bmc:
    ClassId: mo.MoRef
    Moid: 6311aae876752d31398e1a52
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6311aae876752d31398e1a52
  Board:
    ClassId: mo.MoRef
    Moid: 6311ac4676752d31398e5331
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6311ac4676752d31398e5331
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ClassId: compute.RackUnit
  ConnectionStatus: A
  Cpu: 2S 28C 56T
  CreateTime: '2022-09-02T07:04:08.416Z'
  DeviceMoId: 61c35fa36f72612d3005590c
  Dn: sys/rack-unit-3
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6311ac8376752d31398e5c81
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6311ac8376752d31398e5c81
  - ClassId: mo.MoRef
    Moid: 6311ac8376752d31398e5c85
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6311ac8376752d31398e5c85
  - ClassId: mo.MoRef
    Moid: 6311ac8376752d31398e5c89
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6311ac8376752d31398e5c89
  - ClassId: mo.MoRef
    Moid: 6311ac8376752d31398e5c8d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6311ac8376752d31398e5c8d
  - ClassId: mo.MoRef
    Moid: 6311ac8376752d31398e5c91
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6311ac8376752d31398e5c91
  - ClassId: mo.MoRef
    Moid: 6311ac8376752d31398e5c95
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6311ac8376752d31398e5c95
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6311b39576752d31398f844f
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6311b39576752d31398f844f
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Warnings (1)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.49.234.196
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.49.234.254
    Dn: sys/rack-unit-3/mgmt/ipv4-pooled-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: VnicIpV4PooledAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6311ac8376752d31398e5c7f
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6311ac8376752d31398e5c7f
  LocatorLedOn: false
  ManagementIp: 10.49.234.196
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '1866'
  MgmtIdentity: null
  MgmtIpAddress: 10.49.234.196
  ModTime: '2022-09-16T09:32:59.721Z'
  Model: UCSC-C220-M4S
  Moid: 6311aae876752d31398e1a50
  Name: berlin-ucsm-3
  NumAdaptors: 1
  NumCpuCores: 28
  NumCpuCoresEnabled: 28
  NumCpus: 2
  NumEthHostInterfaces: 3
  NumFcHostInterfaces: 0
  NumThreads: 56
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ok
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61c35fa36f72612d3005590c
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6311b01a76752d31398ef2c6
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6311b01a76752d31398ef2c6
  - ClassId: mo.MoRef
    Moid: 6311b01a76752d31398ef2f8
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6311b01a76752d31398ef2f8
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6311ac8376752d31398e5c3b
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6311ac8376752d31398e5c3b
  - ClassId: mo.MoRef
    Moid: 6311ac8376752d31398e5c3d
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6311ac8376752d31398e5c3d
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61c35fa36f72612d3005590c
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c
  Revision: '0'
  Rn: ''
  SasExpanders: []
  Serial: FCH2031V0YM
  ServerId: 3
  ServiceProfile: org-root/ls-esxi-246
  SharedScope: ''
  State: P+WRU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61c35fac76752d3139f50de9
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61c35fac76752d3139f50de9
  TopologyScanStatus: ''
  TotalMemory: 688128
  TotalMemoryGB: 672
  TotalMemoryUnit: 672 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: ''
  Uuid: 1435af2a-2b44-4dc8-906d-bba6b92f14d5
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a51
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6336f19576752d3139f05a51
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a73
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6336f19576752d3139f05a73
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a91
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6336f19576752d3139f05a91
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05ab1
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6336f19576752d3139f05ab1
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors: []
  AssetTag: 02ACA2D
  AvailableMemory: 524288
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05aa1
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/6336f19576752d3139f05aa1
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a5d
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6336f19576752d3139f05a5d
  Biosunits:
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a95
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6336f19576752d3139f05a95
  Bmc:
    ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a7b
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6336f19576752d3139f05a7b
  Board:
    ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a7f
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6336f19576752d3139f05a7f
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05aa9
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/6336f19576752d3139f05aa9
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a57
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/6336f19576752d3139f05a57
  BootHddDevices:
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a9b
    ObjectType: boot.HddDevice
    link: https://www.intersight.com/api/v1/boot/HddDevices/6336f19576752d3139f05a9b
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices:
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a9d
    ObjectType: boot.VmediaDevice
    link: https://www.intersight.com/api/v1/boot/VmediaDevices/6336f19576752d3139f05a9d
  ClassId: compute.RackUnit
  ConnectionStatus: ''
  Cpu: 2S 48C 96T
  CreateTime: '2022-09-30T13:39:33.631Z'
  DeviceMoId: 6336f14d6f72612d31d41b72
  Dn: sys/rack-unit-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  Fanmodules:
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a55
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6336f19576752d3139f05a55
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a5f
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6336f19576752d3139f05a5f
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a63
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6336f19576752d3139f05a63
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a6d
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6336f19576752d3139f05a6d
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a93
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6336f19576752d3139f05a93
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05aad
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6336f19576752d3139f05aad
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05ab7
    ObjectType: equipment.FanModule
    link: https://www.intersight.com/api/v1/equipment/FanModules/6336f19576752d3139f05ab7
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a4f
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6336f19576752d3139f05a4f
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.50.38
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
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05aa5
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6336f19576752d3139f05aa5
  LocatorLedOn: false
  ManagementIp: 10.58.50.38
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.38
  ModTime: '2022-09-30T13:39:33.734Z'
  Model: UCSC-C220-M5SX
  Moid: 6336f19576752d3139f05a4b
  Name: esx21-eu-spdc-WZP23440N1P
  NumAdaptors: 1
  NumCpuCores: 48
  NumCpuCoresEnabled: 48
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 2
  NumThreads: 96
  ObjectType: compute.RackUnit
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 6336f14d6f72612d31d41b72
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a53
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6336f19576752d3139f05a53
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a69
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6336f19576752d3139f05a69
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a6b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6336f19576752d3139f05a6b
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a85
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6336f19576752d3139f05a85
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05aa3
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6336f19576752d3139f05aa3
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
  PlatformType: IMCM5
  Presence: equipped
  PreviousFru: null
  Processors: []
  Psus:
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05a7d
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6336f19576752d3139f05a7d
  - ClassId: mo.MoRef
    Moid: 6336f19576752d3139f05ab9
    ObjectType: equipment.Psu
    link: https://www.intersight.com/api/v1/equipment/Psus/6336f19576752d3139f05ab9
  RackEnclosureSlot: null
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 6336f14d6f72612d31d41b72
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/6336f14d6f72612d31d41b72
  Revision: ''
  Rn: ''
  SasExpanders: []
  Serial: WZP23440N1P
  ServerId: 1
  ServiceProfile: ''
  SharedScope: ''
  State: P+HRS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 6336f15976752d3139f0515b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/6336f15976752d3139f0515b
  TopologyScanStatus: ''
  TotalMemory: 524288
  TotalMemoryGB: 512
  TotalMemoryUnit: 512 [GiB]
  TunneledKvm: false
  Type: Rack
  UnitPersonality: []
  UserLabel: esx21-eu-spdc-WZP23440N1P
  Uuid: A70A9B63-0590-4094-AE4C-9E766970C115
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters: []
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 5efdfb9d6176752d3559bb60
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/5efdfb9d6176752d3559bb60
  AssetTag: ''
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 5f65fa2c6176752d35bbfa4e
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/5f65fa2c6176752d35bbfa4e
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 5efdfb926176752d3559b7ed
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/5efdfb926176752d3559b7ed
  BiosVfSelectMemoryRasConfiguration: null
  Bmc:
    ClassId: mo.MoRef
    Moid: 5efdfbd26176752d3559d739
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/5efdfbd26176752d3559d739
  Board:
    ClassId: mo.MoRef
    Moid: 5efdfb9b6176752d3559bacb
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/5efdfb9b6176752d3559bacb
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 5fdd3acc6176752d35f738cb
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/5fdd3acc6176752d35f738cb
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 5f65fa2d6176752d35bbfaa2
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/5f65fa2d6176752d35bbfaa2
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '1'
  ClassId: compute.Blade
  Cpu: 2S 24C 48T
  CreateTime: '2020-07-02T15:22:01.086Z'
  DeviceMoId: 5efdfb7e6f72612d30e4501e
  Dn: sys/chassis-1/server-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 5efdfb9d6176752d3559bb60
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/5efdfb9d6176752d3559bb60
  EquipmentIoExpanders:
  - ClassId: mo.MoRef
    Moid: 5efdfbac6176752d3559c1b1
    ObjectType: equipment.IoExpander
    link: https://www.intersight.com/api/v1/equipment/IoExpanders/5efdfbac6176752d3559c1b1
  FaultSummary: 0
  GenericInventoryHolders: []
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: ''
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: ''
    Dn: ''
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: ''
    Type: MgmtInterface
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 5efdfbaa6176752d3559c10a
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/5efdfbaa6176752d3559c10a
  LocatorLedOn: false
  ManagementIp: ''
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2400'
  MgmtIdentity: null
  MgmtIpAddress: ''
  ModTime: '2021-06-11T06:52:08.413Z'
  Model: UCSC-C3K-M4SRB
  Moid: 5efdfb996176752d3559b9d5
  Name: C3X60M4-FCH21067808
  NumAdaptors: 0
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.Blade
  OperPowerState: 'off'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 5efdfb7e6f72612d30e4501e
  Parent:
    ClassId: mo.MoRef
    Moid: 5efdfb9d6176752d3559bb60
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/5efdfb9d6176752d3559bb60
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 5efdfbd26176752d3559d7a9
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5efdfbd26176752d3559d7a9
  - ClassId: mo.MoRef
    Moid: 5efdfbd26176752d3559d7cc
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/5efdfbd26176752d3559d7cc
  PciNodes: null
  PermissionResources:
  - ClassId: mo.MoRef
    Moid: 5dee1d2f6972652d321d25c8
    ObjectType: organization.Organization
    link: https://www.intersight.com/api/v1/organization/Organizations/5dee1d2f6972652d321d25c8
  PlatformType: IMC
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 5efdfb7e6f72612d30e4501e
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/5efdfb7e6f72612d30e4501e
  Revision: ''
  Rn: ''
  ScaledMode: ''
  Serial: FCH21067808
  ServiceProfile: ''
  SharedScope: ''
  SlotId: 1
  State: P-HBS
  StorageControllers: []
  StorageEnclosures:
  - ClassId: mo.MoRef
    Moid: 5efdfbe26176752d3559df03
    ObjectType: storage.Enclosure
    link: https://www.intersight.com/api/v1/storage/Enclosures/5efdfbe26176752d3559df03
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 5efdfbd26176752d3559d809
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/5efdfbd26176752d3559d809
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 937E6EE7-0EA5-42CE-9EAE-A960BF1F0BAD
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 62a72bd476752d313901412e
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/62a72bd476752d313901412e
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 61bb973576752d3139b05c2e
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/61bb973576752d3139b05c2e
  AssetTag: ''
  AvailableMemory: 262144
  BiosBootmode:
    ClassId: mo.MoRef
    Moid: 61bb972a76752d3139b05a96
    ObjectType: bios.BootMode
    link: https://www.intersight.com/api/v1/bios/BootModes/61bb972a76752d3139b05a96
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 61bb972876752d3139b059fe
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/61bb972876752d3139b059fe
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 61bb972d76752d3139b05ae8
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/61bb972d76752d3139b05ae8
  Bmc:
    ClassId: mo.MoRef
    Moid: 61bb977376752d3139b070d4
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/61bb977376752d3139b070d4
  Board:
    ClassId: mo.MoRef
    Moid: 61bb973476752d3139b05bf3
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/61bb973476752d3139b05bf3
  BootCddDevices: []
  BootDeviceBootSecurity:
    ClassId: mo.MoRef
    Moid: 61bb976a76752d3139b06c33
    ObjectType: boot.DeviceBootSecurity
    link: https://www.intersight.com/api/v1/boot/DeviceBootSecurities/61bb976a76752d3139b06c33
  BootDeviceBootmode:
    ClassId: mo.MoRef
    Moid: 61bb976876752d3139b06bc3
    ObjectType: boot.DeviceBootMode
    link: https://www.intersight.com/api/v1/boot/DeviceBootModes/61bb976876752d3139b06bc3
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '1'
  ClassId: compute.Blade
  Cpu: 2S 24C 48T
  CreateTime: '2021-12-16T19:44:49.285Z'
  DeviceMoId: 61bb97146f72612d301e5946
  Dn: sys/chassis-1/server-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 61bb973576752d3139b05c2e
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/61bb973576752d3139b05c2e
  EquipmentIoExpanders:
  - ClassId: mo.MoRef
    Moid: 61bb974576752d3139b060c2
    ObjectType: equipment.IoExpander
    link: https://www.intersight.com/api/v1/equipment/IoExpanders/61bb974576752d3139b060c2
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 61be9cac76752d31394b1a8a
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/61be9cac76752d31394b1a8a
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: ''
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: ''
    Dn: ''
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: ''
    Type: MgmtInterface
  KvmServerStateEnabled: false
  KvmVendor: Avocent
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 61bb974276752d3139b05fe5
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/61bb974276752d3139b05fe5
  LocatorLedOn: false
  ManagementIp: ''
  ManagementMode: IntersightStandalone
  MemoryArrays: []
  MemorySpeed: '2400'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.50.34
  ModTime: '2022-07-18T07:31:28.961Z'
  Model: UCSC-C3K-M4SRB
  Moid: 61bb973176752d3139b05b78
  Name: ynasc1-eu-spdc-FCH20487P5X-1
  NumAdaptors: 0
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.Blade
  OperPowerState: 'on'
  OperReason: []
  OperState: ''
  Operability: ''
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 61bb97146f72612d301e5946
  Parent:
    ClassId: mo.MoRef
    Moid: 61bb973576752d3139b05c2e
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/61bb973576752d3139b05c2e
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 61bb978576752d3139b07616
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61bb978576752d3139b07616
  - ClassId: mo.MoRef
    Moid: 61bb978576752d3139b07618
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/61bb978576752d3139b07618
  PciNodes: []
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
  PlatformType: IMC
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 61bb97146f72612d301e5946
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/61bb97146f72612d301e5946
  Revision: ''
  Rn: ''
  ScaledMode: ''
  Serial: FCH21067808
  ServiceProfile: ''
  SharedScope: ''
  SlotId: 1
  State: P+HBS
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 61bb978176752d3139b07532
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/61bb978176752d3139b07532
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 937E6EE7-0EA5-42CE-9EAE-A960BF1F0BAD
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e3141c
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6336a4b276752d3139e3141c
  - ClassId: mo.MoRef
    Moid: 6336a50b76752d3139e32a16
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6336a50b76752d3139e32a16
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  AssetTag: ''
  AvailableMemory: 393216
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e314c3
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/6336a4b276752d3139e314c3
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e3143f
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6336a4b276752d3139e3143f
  BiosVfSelectMemoryRasConfiguration: null
  Bmc:
    ClassId: mo.MoRef
    Moid: 6335c26e76752d3139b9694e
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6335c26e76752d3139b9694e
  Board:
    ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31423
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6336a4b276752d3139e31423
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '2'
  ClassId: compute.Blade
  Cpu: 2S 40C 80T
  CreateTime: '2022-09-29T16:06:06.567Z'
  DeviceMoId: 618942976f72612d309dfbe1
  Dn: sys/chassis-2/blade-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  EquipmentIoExpanders: []
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6335c40f76752d3139b9b32a
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6335c40f76752d3139b9b32a
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.52.41
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.52.62
    Dn: sys/chassis-2/blade-1/mgmt/ipv4-static-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.224
    Type: VnicIpV4StaticAddr
  - Address: 10.58.26.5
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.26.62
    Dn: sys/chassis-2/blade-1/mgmt/ipv4-prof-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4ProfDerivedAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31447
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6336a4b276752d3139e31447
  LocatorLedOn: false
  ManagementIp: 10.58.26.5
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.52.41, 10.58.26.5
  ModTime: '2022-10-12T04:45:04.097Z'
  Model: UCSB-B200-M5
  Moid: 6335c26e76752d3139b9694c
  Name: FI-ucsb1-eu-spdc-2-1
  NumAdaptors: 2
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.Blade
  OperPowerState: 'off'
  OperReason: []
  OperState: power-off
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 618942976f72612d309dfbe1
  Parent:
    ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e3143b
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6336a4b276752d3139e3143b
  PciNodes: []
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 618942976f72612d309dfbe1
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1
  Revision: '0'
  Rn: ''
  ScaledMode: none
  Serial: FLM241501FB
  ServiceProfile: org-root/org-EU-SPN/ls-esx51-eu-spdc
  SharedScope: ''
  SlotId: 1
  State: P-HBU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 618942be76752d3139ace73b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 315220a5-2121-4e5b-0101-e1dc0000010f
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31487
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6336a4b276752d3139e31487
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31492
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6336a4b276752d3139e31492
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  AssetTag: ''
  AvailableMemory: 393216
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e3143d
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/6336a4b276752d3139e3143d
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31437
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6336a4b276752d3139e31437
  BiosVfSelectMemoryRasConfiguration: null
  Bmc:
    ClassId: mo.MoRef
    Moid: 6335c53776752d3139b9e46b
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6335c53776752d3139b9e46b
  Board:
    ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e3142a
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6336a4b276752d3139e3142a
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '2'
  ClassId: compute.Blade
  Cpu: 2S 40C 80T
  CreateTime: '2022-09-29T16:14:17.973Z'
  DeviceMoId: 618942976f72612d309dfbe1
  Dn: sys/chassis-2/blade-2
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  EquipmentIoExpanders: []
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6335c4c976752d3139b9d1f2
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6335c4c976752d3139b9d1f2
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.52.42
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.52.62
    Dn: sys/chassis-2/blade-2/mgmt/ipv4-static-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.224
    Type: VnicIpV4StaticAddr
  - Address: 10.58.26.6
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.26.62
    Dn: sys/chassis-2/blade-2/mgmt/ipv4-prof-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4ProfDerivedAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6335c53776752d3139b9e46d
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6335c53776752d3139b9e46d
  LocatorLedOn: false
  ManagementIp: 10.58.26.6
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.52.42, 10.58.26.6
  ModTime: '2022-10-12T02:34:29.347Z'
  Model: UCSB-B200-M5
  Moid: 6335c45976752d3139b9bf94
  Name: FI-ucsb1-eu-spdc-2-2
  NumAdaptors: 2
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.Blade
  OperPowerState: 'on'
  OperReason: []
  OperState: ok
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 618942976f72612d309dfbe1
  Parent:
    ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31426
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6336a4b276752d3139e31426
  PciNodes: []
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 618942976f72612d309dfbe1
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1
  Revision: '0'
  Rn: ''
  ScaledMode: none
  Serial: FLM24140BJB
  ServiceProfile: org-root/org-EU-SPN/ls-esx52-eu-spdc
  SharedScope: ''
  SlotId: 2
  State: P+HBU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 618942be76752d3139ace73b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b
  TotalMemory: 393216
  TotalMemoryGB: 384
  TotalMemoryUnit: 384 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 315220a5-2121-4e5b-0101-e1dc0000011f
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31428
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6336a4b276752d3139e31428
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 11
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  AssetTag: ''
  AvailableMemory: 262144
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e314c5
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6336a4b276752d3139e314c5
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31443
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6336a4b276752d3139e31443
  Bmc:
    ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e3144d
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6336a4b276752d3139e3144d
  Board:
    ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31445
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6336a4b276752d3139e31445
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '1'
  ClassId: compute.Blade
  Cpu: 2S 24C 48T
  CreateTime: '2022-09-29T18:20:35.079Z'
  DeviceMoId: 618942976f72612d309dfbe1
  Dn: sys/chassis-1/blade-1
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  EquipmentIoExpanders: []
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6335e1f376752d3139bf12c7
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6335e1f376752d3139bf12c7
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (11)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.52.33
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.52.62
    Dn: sys/chassis-1/blade-1/mgmt/ipv4-static-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.224
    Type: VnicIpV4StaticAddr
  - Address: 10.58.26.1
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.26.62
    Dn: sys/chassis-1/blade-1/mgmt/ipv4-prof-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4ProfDerivedAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e3147f
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6336a4b276752d3139e3147f
  LocatorLedOn: false
  ManagementIp: 10.58.26.1
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.52.33, 10.58.26.1
  ModTime: '2022-10-12T03:15:04.431Z'
  Model: UCSB-B200-M4
  Moid: 6335e1f376752d3139bf12b8
  Name: FI-ucsb1-eu-spdc-1-1
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.Blade
  OperPowerState: 'off'
  OperReason: []
  OperState: power-off
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 618942976f72612d309dfbe1
  Parent:
    ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6336a4b276752d3139e31483
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6336a4b276752d3139e31483
  PciNodes: []
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 618942976f72612d309dfbe1
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1
  Revision: '0'
  Rn: ''
  ScaledMode: none
  Serial: FCH205371PZ
  ServiceProfile: org-root/org-EU-SPN/ls-esx41-eu-spdc
  SharedScope: ''
  SlotId: 1
  State: P-CBU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 618942be76752d3139ace73b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 315220a5-2121-4e5b-0101-e1dc0000014f
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6337063276752d3139f3cc25
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6337063276752d3139f3cc25
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 10
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  AssetTag: ''
  AvailableMemory: 262144
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 6337f64f76752d31391e7818
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6337f64f76752d31391e7818
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85e8
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6337f68b76752d31391e85e8
  Bmc:
    ClassId: mo.MoRef
    Moid: 6337021776752d3139f31631
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6337021776752d3139f31631
  Board:
    ClassId: mo.MoRef
    Moid: 6337063276752d3139f3cc64
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6337063276752d3139f3cc64
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '1'
  ClassId: compute.Blade
  Cpu: 2S 24C 48T
  CreateTime: '2022-09-30T14:46:36.147Z'
  DeviceMoId: 618942976f72612d309dfbe1
  Dn: sys/chassis-1/blade-2
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  EquipmentIoExpanders: []
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 6337021776752d3139f31633
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6337021776752d3139f31633
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (10)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.52.34
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.52.62
    Dn: sys/chassis-1/blade-2/mgmt/ipv4-static-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.224
    Type: VnicIpV4StaticAddr
  - Address: 10.58.26.2
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.26.62
    Dn: sys/chassis-1/blade-2/mgmt/ipv4-prof-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4ProfDerivedAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85fb
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f68b76752d31391e85fb
  LocatorLedOn: false
  ManagementIp: 10.58.26.2
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.52.34, 10.58.26.2
  ModTime: '2022-10-12T05:25:04.485Z'
  Model: UCSB-B200-M4
  Moid: 6337014c76752d3139f2f459
  Name: FI-ucsb1-eu-spdc-1-2
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.Blade
  OperPowerState: 'off'
  OperReason: []
  OperState: power-off
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 618942976f72612d309dfbe1
  Parent:
    ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85d2
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6337f68b76752d31391e85d2
  PciNodes: []
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 618942976f72612d309dfbe1
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1
  Revision: '0'
  Rn: ''
  ScaledMode: none
  Serial: FCH20527XXD
  ServiceProfile: org-root/org-EU-SPN/ls-esx42-eu-spdc
  SharedScope: ''
  SlotId: 2
  State: P-CBU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 618942be76752d3139ace73b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 315220a5-2121-4e5b-0101-e1dc0000015f
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6337063276752d3139f3cc89
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6337063276752d3139f3cc89
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 8
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  AssetTag: ''
  AvailableMemory: 262144
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e8566
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6337f68b76752d31391e8566
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e8561
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6337f68b76752d31391e8561
  Bmc:
    ClassId: mo.MoRef
    Moid: 6337063276752d3139f3ccae
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6337063276752d3139f3ccae
  Board:
    ClassId: mo.MoRef
    Moid: 6337063276752d3139f3ccb0
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6337063276752d3139f3ccb0
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '1'
  ClassId: compute.Blade
  Cpu: 2S 24C 48T
  CreateTime: '2022-09-30T15:07:30.234Z'
  DeviceMoId: 618942976f72612d309dfbe1
  Dn: sys/chassis-1/blade-3
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  EquipmentIoExpanders: []
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 63371c9176752d3139f7dab5
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/63371c9176752d3139f7dab5
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Critical (8)
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.52.35
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.52.62
    Dn: sys/chassis-1/blade-3/mgmt/ipv4-static-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.224
    Type: VnicIpV4StaticAddr
  - Address: 10.58.26.3
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.26.62
    Dn: sys/chassis-1/blade-3/mgmt/ipv4-prof-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4ProfDerivedAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85be
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f68b76752d31391e85be
  LocatorLedOn: false
  ManagementIp: 10.58.26.3
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.52.35, 10.58.26.3
  ModTime: '2022-10-12T04:05:04.473Z'
  Model: UCSB-B200-M4
  Moid: 6337063276752d3139f3cc83
  Name: FI-ucsb1-eu-spdc-1-3
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.Blade
  OperPowerState: 'off'
  OperReason: []
  OperState: power-off
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 618942976f72612d309dfbe1
  Parent:
    ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6337f64f76752d31391e780c
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6337f64f76752d31391e780c
  PciNodes: []
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 618942976f72612d309dfbe1
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1
  Revision: '0'
  Rn: ''
  ScaledMode: none
  Serial: FCH20437VXH
  ServiceProfile: org-root/org-EU-SPN/ls-esx43-eu-spdc
  SharedScope: ''
  SlotId: 3
  State: P-CBU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 618942be76752d3139ace73b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 315220a5-2121-4e5b-0101-e1dc0000012f
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6337f64f76752d31391e780a
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6337f64f76752d31391e780a
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  AssetTag: ''
  AvailableMemory: 262144
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings: null
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85ae
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6337f68b76752d31391e85ae
  BiosVfSelectMemoryRasConfiguration:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85bc
    ObjectType: bios.VfSelectMemoryRasConfiguration
    link: https://www.intersight.com/api/v1/bios/VfSelectMemoryRasConfigurations/6337f68b76752d31391e85bc
  Bmc:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85cc
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6337f68b76752d31391e85cc
  Board:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85da
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6337f68b76752d31391e85da
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '1'
  ClassId: compute.Blade
  Cpu: 2S 24C 48T
  CreateTime: '2022-09-30T16:42:57.259Z'
  DeviceMoId: 618942976f72612d309dfbe1
  Dn: sys/chassis-1/blade-4
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  EquipmentIoExpanders: []
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 63371c9176752d3139f7da8e
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/63371c9176752d3139f7da8e
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.52.36
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.52.62
    Dn: sys/chassis-1/blade-4/mgmt/ipv4-static-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.224
    Type: VnicIpV4StaticAddr
  - Address: 10.58.26.4
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.26.62
    Dn: sys/chassis-1/blade-4/mgmt/ipv4-prof-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4ProfDerivedAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6337f6cc76752d31391e9345
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f6cc76752d31391e9345
  LocatorLedOn: false
  ManagementIp: 10.58.26.4
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2133'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.52.36, 10.58.26.4
  ModTime: '2022-10-11T10:14:59.054Z'
  Model: UCSB-B200-M4
  Moid: 63371c9176752d3139f7da74
  Name: FI-ucsb1-eu-spdc-1-4
  NumAdaptors: 1
  NumCpuCores: 24
  NumCpuCoresEnabled: 24
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 0
  NumThreads: 48
  ObjectType: compute.Blade
  OperPowerState: 'on'
  OperReason: []
  OperState: ok
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 618942976f72612d309dfbe1
  Parent:
    ClassId: mo.MoRef
    Moid: 619d058176752d313994941f
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d058176752d313994941f
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e859a
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6337f68b76752d31391e859a
  PciNodes: []
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 618942976f72612d309dfbe1
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1
  Revision: '0'
  Rn: ''
  ScaledMode: none
  Serial: FCH205371UU
  ServiceProfile: org-root/org-EU-SPN/ls-esx44-eu-spdc
  SharedScope: ''
  SlotId: 4
  State: P+HBU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 618942be76752d3139ace73b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b
  TotalMemory: 262144
  TotalMemoryGB: 256
  TotalMemoryUnit: 256 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 315220a5-2121-4e5b-0101-e1dc0000013f
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e8581
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6337f68b76752d31391e8581
  - ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85b2
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6337f68b76752d31391e85b2
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  AssetTag: ''
  AvailableMemory: 196608
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 63371d0c76752d3139f7ee4d
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/63371d0c76752d3139f7ee4d
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e856e
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6337f68b76752d31391e856e
  BiosVfSelectMemoryRasConfiguration: null
  Bmc:
    ClassId: mo.MoRef
    Moid: 6337f64f76752d31391e7812
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6337f64f76752d31391e7812
  Board:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e8577
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6337f68b76752d31391e8577
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '2'
  ClassId: compute.Blade
  Cpu: 2S 40C 80T
  CreateTime: '2022-09-30T16:42:57.291Z'
  DeviceMoId: 618942976f72612d309dfbe1
  Dn: sys/chassis-2/blade-4
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  EquipmentIoExpanders: []
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 63371c9176752d3139f7da90
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/63371c9176752d3139f7da90
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.52.44
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.52.62
    Dn: sys/chassis-2/blade-4/mgmt/ipv4-static-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.224
    Type: VnicIpV4StaticAddr
  - Address: 10.58.26.8
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.26.62
    Dn: sys/chassis-2/blade-4/mgmt/ipv4-prof-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4ProfDerivedAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6337f6cc76752d31391e931c
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f6cc76752d31391e931c
  LocatorLedOn: false
  ManagementIp: 10.58.26.8
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.52.44, 10.58.26.8
  ModTime: '2022-10-11T10:14:59.053Z'
  Model: UCSB-B200-M5
  Moid: 63371c9176752d3139f7da78
  Name: FI-ucsb1-eu-spdc-2-4
  NumAdaptors: 2
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.Blade
  OperPowerState: 'on'
  OperReason: []
  OperState: ok
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 618942976f72612d309dfbe1
  Parent:
    ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85a2
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6337f68b76752d31391e85a2
  PciNodes: []
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 618942976f72612d309dfbe1
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1
  Revision: '0'
  Rn: ''
  ScaledMode: none
  Serial: FLM24140B0B
  ServiceProfile: org-root/org-EU-SPN/ls-esx54-eu-spdc
  SharedScope: ''
  SlotId: 4
  State: P+HBU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 618942be76752d3139ace73b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 315220a5-2121-4e5b-0101-e1dc0000015e
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
- AccountMoid: 5be4b2ce67626c6d661ca38d
  Adapters:
  - ClassId: mo.MoRef
    Moid: 6337f64f76752d31391e7808
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6337f64f76752d31391e7808
  - ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e8558
    ObjectType: adapter.Unit
    link: https://www.intersight.com/api/v1/adapter/Units/6337f68b76752d31391e8558
  AdminPowerState: policy
  AlarmSummary:
    ClassId: compute.AlarmSummary
    Critical: 0
    ObjectType: compute.AlarmSummary
    Warning: 0
  Alerts: []
  Ancestors:
  - ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  AssetTag: ''
  AvailableMemory: 196608
  BiosBootmode: null
  BiosPostComplete: false
  BiosTokenSettings:
    ClassId: mo.MoRef
    Moid: 63371d0c76752d3139f7ee4b
    ObjectType: bios.TokenSettings
    link: https://www.intersight.com/api/v1/bios/TokenSettings/63371d0c76752d3139f7ee4b
  BiosUnits:
  - ClassId: mo.MoRef
    Moid: 6337f6cc76752d31391e934d
    ObjectType: bios.Unit
    link: https://www.intersight.com/api/v1/bios/Units/6337f6cc76752d31391e934d
  BiosVfSelectMemoryRasConfiguration: null
  Bmc:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e8588
    ObjectType: management.Controller
    link: https://www.intersight.com/api/v1/management/Controllers/6337f68b76752d31391e8588
  Board:
    ClassId: mo.MoRef
    Moid: 6337f64f76752d31391e781c
    ObjectType: compute.Board
    link: https://www.intersight.com/api/v1/compute/Boards/6337f64f76752d31391e781c
  BootCddDevices: []
  BootDeviceBootSecurity: null
  BootDeviceBootmode: null
  BootHddDevices: []
  BootIscsiDevices: []
  BootNvmeDevices: []
  BootPchStorageDevices: []
  BootPxeDevices: []
  BootSanDevices: []
  BootSdDevices: []
  BootUefiShellDevices: []
  BootUsbDevices: []
  BootVmediaDevices: []
  ChassisId: '2'
  ClassId: compute.Blade
  Cpu: 2S 40C 80T
  CreateTime: '2022-09-30T16:42:57.325Z'
  DeviceMoId: 618942976f72612d309dfbe1
  Dn: sys/chassis-2/blade-3
  DomainGroupMoid: 5be4b2ce67626c6d661ca39c
  EquipmentChassis:
    ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  EquipmentIoExpanders: []
  FaultSummary: 0
  GenericInventoryHolders:
  - ClassId: mo.MoRef
    Moid: 63371c9176752d3139f7da92
    ObjectType: inventory.GenericInventoryHolder
    link: https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/63371c9176752d3139f7da92
  GraphicsCards: []
  Groups: ''
  HardwareUuid: ''
  Health: Healthy
  InventoryDeviceInfo: null
  KvmIpAddresses:
  - Address: 10.58.52.43
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.52.62
    Dn: sys/chassis-2/blade-3/mgmt/ipv4-static-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.0
    Type: VnicIpV4StaticAddr
  - Address: 10.58.26.7
    Category: Equipment
    ClassId: compute.IpAddress
    DefaultGateway: 10.58.26.62
    Dn: sys/chassis-2/blade-3/mgmt/ipv4-prof-addr
    HttpPort: 80
    HttpsPort: 443
    KvmPort: 2068
    KvmVlan: 0
    Name: Outband
    ObjectType: compute.IpAddress
    Subnet: 255.255.255.192
    Type: VnicIpV4ProfDerivedAddr
  KvmServerStateEnabled: false
  KvmVendor: ''
  LocatorLed:
    ClassId: mo.MoRef
    Moid: 6337f68b76752d31391e85dc
    ObjectType: equipment.LocatorLed
    link: https://www.intersight.com/api/v1/equipment/LocatorLeds/6337f68b76752d31391e85dc
  LocatorLedOn: false
  ManagementIp: 10.58.26.7
  ManagementMode: UCSM
  MemoryArrays: []
  MemorySpeed: '2666'
  MgmtIdentity: null
  MgmtIpAddress: 10.58.52.43, 10.58.26.7
  ModTime: '2022-10-11T10:13:44.417Z'
  Model: UCSB-B200-M5
  Moid: 63371c9176752d3139f7da82
  Name: FI-ucsb1-eu-spdc-2-3
  NumAdaptors: 2
  NumCpuCores: 40
  NumCpuCoresEnabled: 40
  NumCpus: 2
  NumEthHostInterfaces: 8
  NumFcHostInterfaces: 0
  NumThreads: 80
  ObjectType: compute.Blade
  OperPowerState: 'on'
  OperReason: []
  OperState: ok
  Operability: operable
  Owners:
  - 5be4b2ce67626c6d661ca38d
  - 618942976f72612d309dfbe1
  Parent:
    ClassId: mo.MoRef
    Moid: 619d05ae76752d313994a00a
    ObjectType: equipment.Chassis
    link: https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a
  PciDevices:
  - ClassId: mo.MoRef
    Moid: 6337f6cc76752d31391e9340
    ObjectType: pci.Device
    link: https://www.intersight.com/api/v1/pci/Devices/6337f6cc76752d31391e9340
  PciNodes: []
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
  PlatformType: UCSFI
  Presence: equipped
  PreviousFru: null
  Processors: []
  RegisteredDevice:
    ClassId: mo.MoRef
    Moid: 618942976f72612d309dfbe1
    ObjectType: asset.DeviceRegistration
    link: https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1
  Revision: '0'
  Rn: ''
  ScaledMode: none
  Serial: FLM241501CT
  ServiceProfile: org-root/org-EU-SPN/ls-esx53-eu-spdc
  SharedScope: ''
  SlotId: 3
  State: P+HBU
  StorageControllers: []
  StorageEnclosures: []
  Tags:
  - Key: Intersight.LicenseTier
    Value: Premier
  TopSystem:
    ClassId: mo.MoRef
    Moid: 618942be76752d3139ace73b
    ObjectType: top.System
    link: https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b
  TotalMemory: 196608
  TotalMemoryGB: 192
  TotalMemoryUnit: 192 [GiB]
  TunneledKvm: false
  Type: Blade
  UserLabel: ''
  Uuid: 315220a5-2121-4e5b-0101-e1dc0000014e
  Vendor: Cisco Systems Inc
  Vmedia: null
  WorkflowLast: null
  WorkflowRunning: null
  WorkflowsLast: []
  WorkflowsLastFailedIds: []
  WorkflowsLastIds: []
```