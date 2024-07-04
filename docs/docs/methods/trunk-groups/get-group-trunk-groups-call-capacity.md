---
description: api.get.group_trunk_groups_call_capacity()
---

# 📞 GET - Group Trunk Groups Call Capacity

Fetches Trunk Call Capacity data for a single Group.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise ID where Group is located.&#x20;
* group\_id (str): Target Group to return data on.

### Returns

* Dict: Trunk Group Call Capacity data of target group.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_trunk_groups_call_capacity(
    "ServiceProviderID",
    "GroupID"
    
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "maxActiveCalls": 3,
  "maxAvailableActiveCalls": 5,
  "burstingMaxActiveCalls": 3,
  "burstingMaxAvailableActiveCalls": 5,
  "serviceProviderId": "odin.mock.sp1",
  "groupId": "odin.mock.sp1.grp1"
}
```
