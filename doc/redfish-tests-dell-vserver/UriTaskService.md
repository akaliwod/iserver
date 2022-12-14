# Resource: /redfish/v1/TaskService

Vendor | Model
--- | ---
Dell | vServer

## /redfish/v1/TaskService

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService.TaskService",
    "@odata.id": "/redfish/v1/TaskService",
    "@odata.type": "#TaskService.v1_1_5.TaskService",
    "DateTime": "2022-10-26T15:59:33-05:00",
    "Description": "Represents the properties for the service itself and has links to the actual list of Tasks",
    "Id": "TaskService",
    "Name": "Task Service",
    "ServiceEnabled": true,
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Tasks": {
        "@odata.id": "/redfish/v1/TaskService/Tasks"
    }
}
```

## /redfish/v1/TaskService/Tasks

```{
    "@odata.context": "/redfish/v1/$metadata#TaskCollection.TaskCollection",
    "@odata.id": "/redfish/v1/TaskService/Tasks",
    "@odata.type": "#TaskCollection.TaskCollection",
    "Description": "Collection of Tasks",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Task Collection"
}
```

