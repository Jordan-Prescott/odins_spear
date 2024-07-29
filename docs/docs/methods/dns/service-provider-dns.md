---
description: my_api.get.service_provider_dns()
---

# 4️⃣ GET - Service Provider DNs

Returns all numbers assigned to Service Provider/ Enterprise with the group its assigned to and if the numbers can be deleted.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where target numbers are located.

### Returns

* Dict: All numbers assigned to Service Provider/ Enterprise with group and delete status.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.service_provider_dns(
    "serviceProviderId"
)
```
{% endcode %}

### Example Returned Data (Formatted)

```
{
  "serviceProviderId": "odin.mock.ent1",
  "dns": [
    {
      "canDelete": true,
      "groupId": null,
      "min": "+1-9709580015",
      "max": "+1-9709580100"
    },
    {
      "canDelete": false,
      "groupId": "odin.mock.grp1",
      "min": "+1-9709580001",
      "max": "+1-9709580010"
    }
  ]
}
```
