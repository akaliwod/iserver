# iserver

iserver is command line tool providing monitoring and state control of Intersight managed servers.

## Key Features

The key iserver features leverage Intersight API

- [Servers inventory](./doc/features/ServersInventory.md)
- [Server details](./doc/features/ServerDetails.md)
- [Power control](./doc/features/PowerControl.md)
- [Locator LED control](./doc/features/LedControl.md)
- [Operating System installation](./doc/features/OsInstall.md)
- [Workflows](./doc/features/Workflows.md)
- [Workflow details](./doc/features/Workflow.md)

Additionally iserver supports [Redfish](./doc/redfish/README.md) and [UCSM](./doc/ucsm/README.md) API with the special use case of [power and thermal monitoring](./doc/green/README.md).

## Installation

- iserver binary is compiled for Windows, Linux and MAC
- download the latest release from the [Releases](https://wwwin-github.cisco.com/emear-telcocloud/iserver/releases/latest) page.
- move binary somewhere that is on your path (e.g. /usr/local/bin)

If binary is not available or you prefer using source code, clone the repository and run iserver using Python3 with [required](requirements) pip3 packages.

## Requirements

- iserver **requires** [isctl](https://github.com/cgascoig/isctl)
- make sure you have isctl in your path (e.g. /usr/local/bin)
- make sure that isctl is configured with Intersight API keys

Important: OS installation requires isctl version >= 0.1.18
