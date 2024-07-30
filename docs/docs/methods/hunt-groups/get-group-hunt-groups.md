---
description: my_api.get.group_hunt_groups()
---

#  🍇 GET - Group Hunt Groups

Returns a list of all the Hunt Groups within the specified Group.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* group_id (str): Target Group ID

### Returns

* List: Returns a list of every Hunt Group within a Group, alongside their extension and name.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_hunt_groups(
    service_provider_id="serviceProviderID",
    group_id="groupID"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
  {
    "serviceUserId": "HuntGroup1@domain.com",
    "name": "HuntGroup1@domain.com",
    "phoneNumber": "123456789",
    "extension": "6000",
    "department": null,
    "isActive": true,
    "policy": "Regular",
    "serviceProviderId": "serviceProviderID",
    "groupId": "groupID"
  },
  {
    "serviceUserId": "HuntGroup2@domain.com",
    "name": "HuntGroup2@domain.com",
    "phoneNumber": "987654321",
    "extension": "101",
    "department": null,
    "isActive": true,
    "policy": "Circular",
    "serviceProviderId": "serviceProviderID",
    "groupId": "groupID"
  }
]
```
