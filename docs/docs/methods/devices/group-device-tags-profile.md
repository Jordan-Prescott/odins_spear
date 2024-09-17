---
description: my_api.put.group_device_tags_profile()
---

# 🏷️ PUT - Group Device Tags Profile

Update a config file for a single device at the Group level.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where target device is located.&#x20;
* device\_name (str): Device name of the target device.
* tags (dict): List of dictionaries tag name and value entries.

### Returns

* Dict: Python dictionary of the new state after updates have been applied.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

tags = [
        {
            "tagName": "%LK-SDial-Lbl4%",
            "tagValue": "label4",
        },
        {
            "tagName": "%LK-SDial-Str4%",
            "tagValue": "string4",
        },
        {
            "tagName": "%test%",
            "tagValue": "testing",
            "actualTagValue": "testing"
        },
        {
            "tagName": "%testing%",
            "tagValue": "testing2",
        }
]


my_api.put.group_device_tags_profile(
    "servivce_provider_id",
    "group_id",
    "device_name",
    tags=tags
)
```
