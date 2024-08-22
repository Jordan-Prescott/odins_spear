---
description: my_api.get.auto_attendants()
---

#  📞 GET - Auto Attendants

Returns a complete list of all Auto Attendants in a single group.

### Parameters&#x20;

* service_provider_id (str): Service Provider where Group is hosted.
* group_id (str): Target Group where Auto Attendants are hosted.
### Returns

* List: List of Auto Attendants with basic info on them.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.auto_attendants(
    service_provider_id="serviceProviderId",
    group_id="groupId"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
  {
    "serviceUserId": "testAA",
    "name": "My Test AA",
    "video": false,
    "phoneNumber": 123456789,
    "extension": "6060",
    "department": "Department Name",
    "isActive": true,
    "type": "Basic"
  },
  {
    "serviceUserId": "OtherAA",
    "name": "Another AA",
    "video": false,
    "phoneNumber": null,
    "extension": null,
    "department": null,
    "isActive": true,
    "type": "Basic"
  }
]
```
