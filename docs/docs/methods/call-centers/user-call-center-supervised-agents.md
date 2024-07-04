---
description: my_api.user_call_center_supervised_agents()
---

# 👓 PUT - User Call Center Supervised Agents

Update the list of agents a supervisor has in a single Call Center (CC).

### Parameters&#x20;

* call\_center\_user\_id (str): Service user ID of the target CC.&#x20;
* supervisor\_user\_id (str): User ID of the supervisor.&#x20;
* supervisor\_ids (list): List of user IDs of agents to apply to supervisor.

### Returns

* Dict: Superivor ID and list of agents they supervise.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_call_center = "call_center_user_id@domain.com"
my_supervsor_id = "supervisor_id@domain.com"
my_agents = ["userid_1@domain.com", "userid_2@domain.com", "userid_3@domain.com"]

my_api.put.user_call_center_supervised_agents(
    call_center_user_id = my_call_center,
    supervsor_user_id = my_supervsor_id,
    agent_ids = my_agents
)
```
