---
description: my_api.get.group_call_centers()
---

#  🎧 GET - Group Call Centers

Retrieves a list of active call centers within a specified group, along with their settings.

### Parameters&#x20;

* service_provider_id (str): Service Provider where Group is hosted.
* group_id (str): Target Group where Call Centers are hosted.

### Returns

* List: List of Call Centers and their settings.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_call_centers(
    service_provider_id="serviceProviderId",
    group_id="groupId"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
  {
    "serviceUserId": "TestCallCenter1",
    "name": "TestCallCenter1",
    "video": false,
    "phoneNumber": null,
    "extension": null,
    "department": null,
    "isActive": true,
    "policy": "Circular",
    "type": "Premium"
  },
  {
    "serviceUserId": "TestCallCenter2",
    "name": "TestCallCenter2",
    "video": false,
    "phoneNumber": null,
    "extension": null,
    "department": null,
    "isActive": true,
    "policy": "Similtaneous",
    "type": "Standard"
  }
]
```
