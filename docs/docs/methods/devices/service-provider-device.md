---
description: my_api.put.service_provider_device()
---

# 📞 PUT - Service Provider Device

Update a single device in a Service Provider or Enterprise.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where device is located. &#x20;
* device\_name (str): Device name of the target device.&#x20;
* updates (dict): Updates to apply to the target device.

### Returns

* Dict: Python dictionary of the new state after updates have been applied.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

updates = {
    "deviceType": "Polycom Soundpoint IP 500",
    "protocol": "SIP 2.0",
    "numberOfPorts": {
        "quantity": "3"
    },
    "numberOfAssignedPorts": 0,
    "status": "Online",
    "transportProtocol": "UDP",
    "useCustomUserNamePassword": True,
    "deviceLevel": "Service Provider",
    "accessDeviceCredentials": {
        "userName": None
    },
    "tags": [],
    "relatedServices": []
}


my_api.put.service_provider_device(
    "service_provider_id",
    "group_id",
    updates=updates
)
```
