---
description: api.get.group_trunk_groups()
---

# 🚰 GET - Group Trunk Groups

Fetches list of all trunk groups in a single group.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where the target Trunk Group is located.

### Returns

* List: List of core details of all Trunk Groups located in a single Group.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_trunk_groups(
    "ServiceProviderID",
    "GroupID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {
    "name": "odin.mock.trunk1",
    "department": null,
    "deviceName": "odin.mock.dev1",
    "deviceLevel": "Group",
    "groupId": "odin.mock.sp.grp1",
    "serviceProviderId": "odin.mock.sp1"
  },
  {
    "name": "odin.mock.trunk1",
    "department": null,
    "deviceName": "odin.mock.dev1",
    "deviceLevel": "Group",
    "groupId": "odin.mock.sp.grp1",
    "serviceProviderId": "odin.mock.sp1"
  }
]
```
