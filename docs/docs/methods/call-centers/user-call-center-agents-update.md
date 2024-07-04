---
description: my_api.user_call_center_agents_update()
---

# 🙋‍♂️ PUT - User Call Center Agents Update

Update the Call Centers (CC) a user is assigned to.

### Parameters&#x20;

* user\_id (str): User ID of the target user.
* call\_center\_service\_ids (list): List of CC service user IDs to update the user with.

### Returns

* None: This method does not return any specific value.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_agent_user_id = "user_id@domain.com"
my_call_centers = ["userid_1@domain.com", "userid_2@domain.com", "userid_3@domain.com"]

my_api.put.user_call_center_agents_update(
    user_id = my_agent_user_id,
    call_center_service_ids= my_call_centers 
)
```
