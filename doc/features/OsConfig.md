# Operating System Configuration

Each combination of OS vendor and version that supports template-based installation, needs associated configuration file that will be attached upon boot time by SCU.

## Get

```
# iserver get os-config --help

Usage: iserver.py get os-config [OPTIONS]

  Get operating system configuration template

Options:
  --iaccount TEXT  Intersight account  [default: isctl]
  --vendor TEXT    Vendor Name
  --version TEXT   Version Name
  --id TEXT        Version ID
  --devel          Developer output  [default: False]
  --help           Show this message and exit.
```

Example

```
# iserver get os-config --vendor Ubuntu --version "Ubuntu Server 22.04 LTS"

Validate input parameters...
Configuration file: Ubuntu2004AutoInstall [62f5b85b925a5af7c1325fc1]

#cloud-config
autoinstall:
  version: 1
  early-commands:
    - systemctl stop ssh
  network:
    network:
      version: 2
      ethernets:
        {{if .answers.NetworkDevice }}{{.answers.NetworkDevice}}{{else}}eno1{{end}}:
          {{if (eq .answers.IpVersion "V4")}}{{if (eq .answers.IpConfigType "static")}}dhcp4: no
          addresses: [{{IpToCidr .answers.IpV4Config.IpAddress .answers.IpV4Config.Netmask}}]
          gateway4: {{ .answers.IpV4Config.Gateway }}
          nameservers:
            addresses: [{{ .answers.NameServer }}]{{else}}dhcp4: yes{{end}}{{else}}
          {{if (eq .answers.IpConfigType "static")}}dhcp6: no
          addresses: ['{{.answers.IpV6Config.IpAddress}}/{{ .answers.IpV6Config.Prefix}}']
          nameservers:
            addresses: [{{ .answers.NameServer }}]{{else}}dhcp6: yes{{end}}{{end}}
  identity:
    hostname: {{ .answers.Hostname }}
    password: "{{ .answers.RootPassword }}"
    username: ubuntu
  user-data:
    disable_root: false
    chpasswd:
      list: |
        root: "{{ .answers.RootPassword }}"
      expire: false
  late-commands:
    - echo "Applied late commands" >> /tmp/log1
    - OS_INSTALL_COMPLETED_STATUS_PLACEHOLDER
    - sudo systemctl start ssh
  ssh:
    install-server: yes
  storage:
    config:
      {{if (eq (.answers.BootMode | LowerCase) "uefi")}}- {ptable: gpt, DISKID_PLACEHOLDER, wipe: superblock-recursive, preserve: false, name: '', grub_device: false, type: disk, id: disk0}
      - {device: disk0, size: 512M, wipe: superblock, flag: boot, number: 1, preserve: false, grub_device: true, type: partition, id: partition-0}
      - {fstype: fat32, volume: partition-0, preserve: false, type: format, id: format-0 }
      - {device: disk0, size: -1, wipe: superblock, flag: '', number: 2, preserve: false, type: partition, id: partition-1}
      - {fstype: ext4, volume: partition-1, preserve: false, type: format, id: format-1 }
      - {device: format-1, path: /, type: mount, id: mount-1 }
      - {device: format-0, path: /boot/efi, type: mount, id: mount-0 }{{else}}- {ptable: gpt, DISKID_PLACEHOLDER, wipe: superblock-recursive, preserve: false, name: '', grub_device: true, type: disk, id: disk0}
      - {device: disk0, size: 1148576, flag: bios_grub, number: 1, preserve: false, grub_device: false, type: partition, id: partition-0}
      - {device: disk0, size: -1, wipe: superblock, flag: '', number: 2, preserve: false, grub_device: false, type: partition, id: partition-1}
      - {fstype: ext4, volume: partition-1, preserve: false, type: format, id: format-0 }
      - {device: format-0, path: /, type: mount, id: mount-0 }{{end}}
```

Negative test: not enough parameters

```
# iserver get os-config

Validate input parameters...
[ERROR] Define os version using vendor and version names or version id
```

Negative test: wrong vendor

```
# iserver get os-config --vendor lala --version "Ubuntu Server 22.04 LTS"

Validate input parameters...
[ERROR] Vendor not found: lala
```

Negative test: wrong version

```
# iserver get os-config --vendor Ubuntu --version lala

Validate input parameters...
[ERROR] Version not found: lala
```
