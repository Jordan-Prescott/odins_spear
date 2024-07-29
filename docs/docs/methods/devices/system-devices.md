---
description: my_api.put.system_devices()
---

# 💻 PUT - System Devices

Update a single device in the Broadworks system.

### Parameters&#x20;

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
	"deviceType":"Polycom_VVX400",
	"protocol":"SIP 2.0",
	"transportProtocol":"UDP",
	"useCustomUserNamePassword":False,
	"deviceLevel":"System"
}


my_api.put.system_devices(
    "device_name",
    updates=updates
)
```
