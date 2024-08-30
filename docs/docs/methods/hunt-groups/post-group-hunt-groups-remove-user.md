---
description: my_api.post.group_hunt_groups_remove_user()
---

#  👋 POST - Group Hunt Groups Remove User

Removes the specified user from all hunt groups in which it currently exists. 

### Parameters&#x20;

* service_provider_id (str): The service provider ID in which the target user exists.
* group_id (str): The group ID where the user exists.
* user_id (str): The User ID of the user that is to be removed from the hunt group(s).

### Returns

* List: Service user ID's (str) of the hunt groups from which the specified user has been removed. 

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.post.group_hunt_groups_remove_user(
    service_provider_id = "Test Service Provider ID",
    group_id = "Test Group ID",
    user_id = "test_user@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
["test_hunt_group_1@domain.com", "test_hunt_group2@domain.com"]
```
