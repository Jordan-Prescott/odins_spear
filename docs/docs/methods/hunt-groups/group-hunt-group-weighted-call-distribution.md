---
description: my_api.put.group_hunt_group_weighted_call_distribution()
---

# 💯 PUT - Group Hunt Group Weighted Call Distribution

Update the Weighted Call Distribution (WCD) between users in a Hunt Group (HG).

Note: All weightings need to equal 100.

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the group is located.&#x20;
* group\_id (_type_): Group ID where the HG is located.&#x20;
* hunt\_group\_user\_id (str): Service user ID of the target HG.&#x20;
* agents (dict): Updates of WCD to be applied to HG.

### Raises

* AOInvalidWeighting: The WCD must equal 100 if it does not this error will be returned.

### Returns

* None: This method does not return any specific value.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_service_provider_id = "serviceProviderId"
my_group_id = "groupId"
my_hunt_group_id = "huntGroupID@domain.com"
my_agents = [
        {
            "userId": "5131110051",
            "weight": 20
        },
        {
            "userId": "5131111108",
            "weight": 20
        },
        {
            "userId": "5131111110",
            "weight": 20
        },
        {
            "userId": "5131111115",
            "weight": 40
        }
    ]

my_api.put.group_hunt_group_weighted_call_distribution(
    service_provider_id = my_service_provider_id ,
    group_id = my_group_id,
    hunt_group_user_id = my_hunt_group_user_id,
    agents= my_agents
)
```
