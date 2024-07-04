---
description: api.get.service_provider_trunk_group_call_capacity()
---

# 🚿 GET - Service Provider Trunk Group Call Capacity

Fetches trunk call capacity details of a single Service Provider.

### Parameters&#x20;

* service\_provider\_id (str): Target Service Provider/ Enterprise ID.

### Returns

* Dict: Trunk call capacity details of a single Service Provider/ Enterprise ID.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.service_provider_trunk_group_call_capacity(
    "ServiceProviderID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "serviceProviderId": "odin.mock.clone.ent1",
  "maxActiveCalls": 10,
  "burstingMaxActiveCalls": 10
}
```
