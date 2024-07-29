---
description: my_api.get.system_dn_utilization()
---

# 8️⃣ GET - System DN Utilisation

Returns DN statistics for each Service Provider/ Enterprise such as total DNs assigned.

### Returns

* List: List of all Service Provider/ Enterprises with statistics of DNs for each.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.system_dn_utilization()
```
{% endcode %}

### Example Returned Data (Formatted)

```json
[
  {
    "serviceProviderId": "ent.odin",
    "phoneNumbers": 382,
    "assignedtoGroups": 159,
    "percentageAssigned": 41,
    "isEnterprise": true,
    "activatedOnGroups": 20
  }
]
```
