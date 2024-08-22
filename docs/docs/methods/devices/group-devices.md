---
description: my_api.group_devices()
---

# 📱 PUT - Group Devices

Update a single device in a group.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where target device is located.&#x20;
* device\_name (str): Device name of target device.&#x20;
* updates (dict): Updates to apply to target device.

### Returns

* Dict: Python dictionary of the new state after updates have been applied.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

updates = {
    "deviceType": "Polycom Soundpoint IP 4000",
    "protocol": "SIP 2.0",
    "netAddress": "111.111.111.111",
    "port": 2222,
    "outboundProxyServerNetAddress": "222.222.222.222",
    "stunServerNetAddress": "333.333.333.333",
    "macAddress": "CBFB0EBBF325",
    "serialNumber": 123456789,
    "description": "description",
    "numberOfPorts": {
        "quantity": "1"
    },
    "numberOfAssignedPorts": 0,
    "status": "Online",
    "configurationMode": "Default",
    "physicalLocation": "usa",
    "transportProtocol": "UDP",
    "useCustomUserNamePassword": True,
    "deviceName": "my-new-device-name",
    "deviceLevel": "Group",
    "accessDeviceCredentials": {
        "userName": 9871515000,
        "password": "na9@!67nak2"
    },
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "tags": [],
    "relatedServices": []
}

my_api.put.group_devices(
    "service_provider_id",
    "group_id",
    "device_name",
    updates=updates
)
```
