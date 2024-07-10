---
description: api.put.service_provider_trunk_group_call_capacity()
---

# 🚿 PUT - Service Provider Trunk Group Call Capacity

Updates the max active calls and the bursting max active calls for the given service provider.

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID for which the max active calls needs to be updated 
*  updates (dict): The updates to be applied to the service provider's trunking call capacity

### Returns

* Dict: Returns the updated call capacity for the service provider

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.service_provider_trunk_group_call_capacity(
  my_service_provider_id = "ServiceProviderID",
  updates = {
    "maxActiveCalls": 30,
    "burstingMaxActiveCalls": -1
    }
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "serviceProviderId": "odin.mock.clone.ent1",
  "maxActiveCalls": 10,
  "burstingMaxActiveCalls": 10,
  "numberOfBurstingBTLUs": 0
}
```
