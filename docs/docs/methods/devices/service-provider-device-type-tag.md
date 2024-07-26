---
description: my_api.service_provider_device_type_tag()
---

# 🎐 PUT - Service Provider Device Type Tag

Update tags applied to device types at the Service Provider or Enterprise level.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where Group is located.&#x20;
* device\_type (str): The target device type to apply the updates.&#x20;
* tag\_name (str): Name of the tag to add or update.&#x20;
* tag\_value (str): Value of tag to add or update.

### Returns

* Dict: Python dictionary of the new state after updates have been applied.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.service_provider_device_type_tag(
    "servivce_provider_id",
    "group_id",
    "device_type",
    tag_name= "tagName",
    tag_value= "tagValue"
)
```
