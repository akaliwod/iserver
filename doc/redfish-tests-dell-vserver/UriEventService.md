# Resource: /redfish/v1/EventService

Vendor | Model
--- | ---
Dell | vServer

## /redfish/v1/EventService

```{
    "@odata.context": "/redfish/v1/$metadata#EventService.EventService",
    "@odata.id": "/redfish/v1/EventService",
    "@odata.type": "#EventService.v1_7_0.EventService",
    "Actions": {
        "#EventService.SubmitTestEvent": {
            "EventType@Redfish.AllowableValues": [
                "Alert"
            ],
            "target": "/redfish/v1/EventService/Actions/EventService.SubmitTestEvent"
        }
    },
    "DeliveryRetryAttempts": 5,
    "DeliveryRetryIntervalSeconds": 60,
    "Description": "Event Service represents the properties for the service",
    "EventFormatTypes": [
        "Event",
        "MetricReport"
    ],
    "EventFormatTypes@odata.count": 2,
    "EventTypesForSubscription": [
        "Alert",
        "MetricReport",
        "Other"
    ],
    "EventTypesForSubscription@odata.count": 3,
    "Id": "EventService",
    "Name": "Event Service",
    "SMTP": {
        "Authentication": "None",
        "ConnectionProtocol": "StartTLS",
        "FromAddress": "",
        "Password": null,
        "Port": 25,
        "ServerAddress": "0.0.0.0",
        "Username": ""
    },
    "SSEFilterPropertiesSupported": {
        "EventFormatType": true,
        "EventType": true,
        "MessageId": true,
        "MetricReportDefinition": true,
        "OriginResource": true,
        "RegistryPrefix": true,
        "ResourceType": true,
        "SubordinateResources": false
    },
    "ServerSentEventUri": "/redfish/v1/SSE",
    "ServiceEnabled": false,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Disabled"
    },
    "Subscriptions": {
        "@odata.id": "/redfish/v1/EventService/Subscriptions"
    }
}
```

## /redfish/v1/EventService/Subscriptions

```{
    "@odata.context": "/redfish/v1/$metadata#EventDestinationCollection.EventDestinationCollection",
    "@odata.id": "/redfish/v1/EventService/Subscriptions",
    "@odata.type": "#EventDestinationCollection.EventDestinationCollection",
    "Description": "List of Event subscriptions",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Event Subscriptions Collection"
}
```

