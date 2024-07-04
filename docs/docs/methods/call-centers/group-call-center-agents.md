---
description: my_api.group_call_center_agents()
---

# 🎧 PUT - Group Call Center Agents

This method allows you to add or remove agents in a Call Center (CC).&#x20;

Note: Leave the agent\_user\_ids blank to remove all users and to remove some only include the users you would like to include in this call center.

### Parameters&#x20;

* call\_center\_user\_id (str): Service user ID of the target call center.
* agent\_user\_ids (list): List of user IDs to be added to call center.

### Returns

* Dict: Dictionary of the new state of the CC.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_call_center = "call_center_user_id@domain.com"
my_agents = ["userid_1@domain.com", "userid_2@domain.com", "userid_3@domain.com"]

my_api.put.group_call_center_agents(
    call_center_user_id = my_call_center,
    agent_user_ids = my_agents
)
```
