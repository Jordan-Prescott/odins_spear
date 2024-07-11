---
description: api.put.group_trunk_groups_call_capacity()
---

# 📞 PUT - Group Trunk Groups Call Capacity

Updates the trunking call capacity in the specified group. 
NOTE: The max available active calls cannot be changed here. Please see service_providers_trunk_group_call_capacity to update this.

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the target group is built
* group\_id (str): Group ID whose trunk group call capacity needs updating
* max_active_calls (int, optional): The max active calls for the group. 
* bursting_max_active_calls (int, optional): The bursting max active calls for the group.
* number_of_bursting_btlus (int, optional): The number of Business Trunking License Units for bursting. 

### Returns

* Dict: Returns the updated state of the trunk group call capacity.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.group_trunk_groups_call_capacity(
  my_service_provider_id = "ServiceProviderID",
  my_group_id = "GroupID",
  max_active_calls = 5, 
  bursting_max_active_calls = -1, 
  number_of_bursting_btlus = 1
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
"maxActiveCalls": 5, 
"maxAvailableActiveCalls": 10, 
"burstingMaxActiveCalls": -1, 
"burstingMaxAvailableActiveCalls": -1, 
"serviceProviderId": "ServiceProviderID", 
"groupId": "GroupID", 
"maxAvailableNumberOfBurstingBTLUs": 1, 
"numberOfBurstingBTLUs": 1
}
```
