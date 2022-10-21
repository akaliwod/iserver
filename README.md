# iserver

iserver is command line tool providing monitoring and state control of Intersight managed servers.

## Key Features

iserver builds on top Intersight capabilities for server management tasks i.e.:
- [Servers inventory](./doc/features/ServersInventory.md)
- [Server details](./doc/features/ServerDetails.md)
- [Power control](./doc/features/PowerControl.md)
- [Locator LED control](./doc/features/LedControl.md)
- [Operating System installation](./doc/features/OsInstall.md)
- [Workflows](./doc/features/Workflows.md)
- [Workflow details](./doc/features/Workflow.md)

Note: most of the tests performed on rack servers

## Installation

- iserver binary is compiled for Windows, Linux and MAC
- download the latest release from the [Releases](https://github.com/akaliwod/iserver/releases/latest) page.
- move binary somewhere that is on your path (e.g. /usr/local/bin)

If binary is not available or you prefer using source code, clone the repository and run iserver using Python3 with [required](requirements) pip3 packages.

## Requirements

- iserver **requires** [isctl](https://github.com/cgascoig/isctl)
- make sure you have isctl in your path (e.g. /usr/local/bin)
- make sure that isctl is configured with Intersight API keys

Important: OS installation requires isctl version >= 0.1.18
