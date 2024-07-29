---
description: my_api.get.group_schedules()
---

# 📅 GET - Group Schedules

Retrieves the Business Schedules for the specified group.

### Parameters&#x20;

* service\_provider\_id (str): Target Service Provider ID where group is hosted.
* group\_id (str): Target Group ID with schedules.

### Returns

* List: List of all the groups schedules, including Name, Type and Level.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_schedules(
    "serviceProviderID",
    "groupID"
)
```
{% endcode %}

### Example Response (Formatted)

```json
[
  {
    "name": "Spring",
    "type": "Time",
    "level": "Group",
    "serviceProviderId": "serviceProviderID",
    "groupId": "groupID"
  },
  {
    "name": "Tes",
    "type": "Holiday",
    "level": "Group",
    "serviceProviderId": "serviceProviderID",
    "groupId": "groupID"
  }
]
```
