---
description: my_api.get.group_dns()
---

# 1️⃣ GET - Group DNs

Gets all numbers assigned to group.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where group is hosted.
* group\_id (str): Group ID of target group.

### Returns

* Dict: Dictionary containing all DNs assigned to group.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_dns(
    "serviceProviderId",
    "groupID",
)
```
{% endcode %}

### Example Returned Data (Formatted)

```
{
  "serviceProviderId": "odin.mock.ent1",
  "groupId": "odin.mock.grp1",
  "dns": [
    {
      "assigned": true,
      "activated": true,
      "min": "+1-9709580001",
      "max": "+1-9709580009"
    },
    {
      "assigned": false,
      "activated": false,
      "min": "+1-9709580010",
      "max": null
    }
  ]
}
```
