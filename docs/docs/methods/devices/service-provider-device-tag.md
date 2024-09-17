---
description: my_api.put.service_provider_device_tag()
---

# 🛰️ PUT - Service Provider Device Tag

Update a single tag assigned to a device at the Service Provider or Enterprise level.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where Group is located.&#x20;
* device\_name (str): Device name of the target device.&#x20;
* tag\_name (str): Name of the tag to add or update.
* tag\_value (str): Value of tag to add or update.

### Returns

* Dict: Python dictionary of the new state after updates have been applied.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.service_provider_device_tag(
    "servivce_provider_id",
    "group_id",
    "device_name",
    tag_name= "tagName",
    tag_value= "tagValue"
)
```
