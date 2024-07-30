---
description: my_api.get.group_call_center_bounced_calls()
---

#  📞 GET - Group Call Center Bounced Calls

Retrieves the number of rings before a call is bounced from the specified call center.

### Parameters&#x20;

* service_user_id (str): Target Call Center ID


### Returns

* Dict: Amount of Rings before a call is Bounced

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_call_center_bounced_calls(
    service_user_id="TestCallCenter@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "isActive": true,
  "numberOfRingsBeforeBouncingCall": 5,
  "enableTransfer": false,
  "bounceCallWhenAgentUnavailable": true,
  "alertCallCenterCallOnHold": true,
  "alertCallCenterCallOnHoldSeconds": 30,
  "bounceCallCenterCallOnHold": false,
  "bounceCallCenterCallOnHoldSeconds": 60,
  "serviceUserId": "TestCallCenter@domain.com"
}
```
