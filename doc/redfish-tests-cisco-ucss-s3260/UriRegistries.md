# Resource: /redfish/v1/Registries

Vendor | Model
--- | ---
Cisco | UCSS-S3260

## /redfish/v1/Registries

```{
    "@odata.context": "/redfish/v1/$metadata#Registries",
    "@odata.id": "/redfish/v1/Registries",
    "@odata.type": "#MessageRegistryFileCollection.MessageRegistryFileCollection",
    "Description": "Registry Repository",
    "Members": [
        {
            "@odata.id": "/redfish/v1/Registries/Base"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUcsFaults"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoUcsMessageRegistry"
        },
        {
            "@odata.id": "/redfish/v1/Registries/CiscoBiosAttributeRegistry.v1_0_0"
        }
    ],
    "Members@odata.count": 4,
    "Name": "Registry File Collection"
}
```

## /redfish/v1/Registries/Base

```{
    "@odata.context": "/redfish/v1/$metadata#Registries/Members/$entity",
    "@odata.id": "/redfish/v1/Registries/Base",
    "@odata.type": "#MessageRegistryFile.v1_0_2.MessageRegistryFile",
    "Description": "Base Message Registry File locations",
    "Id": "Base",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/Base/Base.1.4.0.json"
        }
    ],
    "Name": "Base Message Registry file",
    "Registry": "Base.1.4"
}
```

## /redfish/v1/Registries/CiscoBiosAttributeRegistry.v1_0_0

```{
    "@odata.context": "/redfish/v1/$metadata#Registries/Members/$entity",
    "@odata.id": "/redfish/v1/Registries/CiscoBiosAttributeRegistry.v1_0_0",
    "@odata.type": "#MessageRegistryFile.v1_0_2.MessageRegistryFile",
    "Description": "BIOS Attribute Registry File locations",
    "Id": "CiscoBiosAttributeRegistry.v1_0_0",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/CiscoBiosAttributeRegistry.v1_0_0/BiosAttributeRegistry"
        }
    ],
    "Name": "BIOS Attribute Registry",
    "Registry": "BiosAttributeRegistry.1.0"
}
```

## /redfish/v1/Registries/CiscoUcsFaults

```{
    "@odata.context": "/redfish/v1/$metadata#Registries/Members/$entity",
    "@odata.id": "/redfish/v1/Registries/CiscoUcsFaults",
    "@odata.type": "#MessageRegistryFile.v1_0_2.MessageRegistryFile",
    "Description": "Faults RegistryFile for this system",
    "Id": "CiscoUcsFaults",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/CiscoUcsFaults/CiscoUcsFaultCodes.v1_0_0.json"
        }
    ],
    "Name": "Faults Registry",
    "Registry": "CiscoUcsFaultCodes.1.0"
}
```

## /redfish/v1/Registries/CiscoUcsMessageRegistry

```{
    "@odata.context": "/redfish/v1/$metadata#Registries/Members/$entity",
    "@odata.id": "/redfish/v1/Registries/CiscoUcsMessageRegistry",
    "@odata.type": "#MessageRegistryFile.v1_0_2.MessageRegistryFile",
    "Description": "Cisco UCS  Message Registry File locations",
    "Id": "CiscoUcsMessageRegistry",
    "Languages": [
        "en"
    ],
    "Location": [
        {
            "Language": "en",
            "Uri": "/redfish/v1/Registries/CiscoUcsMessageRegistry/CiscoUCS.v1_0_0.json"
        }
    ],
    "Name": "Cisco UCS Message Registry file",
    "Registry": "CiscoUCS.1.0"
}
```

