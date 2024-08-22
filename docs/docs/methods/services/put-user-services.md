---
description: my_api.put.user_services()
---

# 🧍 PUT - User Services

This method updates a Broadwork entity's services and service packs if applicable. Any entity that can have a service or service pack assigned can be updated such as a user's service pack or a Hunt Group services. Note that services and service packs are separated into two lists when passed to the method, if you only want to update one list only pass in the list you wish to update. For example, adding the service pack 'SP-A' to user A will only require I pass this in the service\_pack parameter.&#x20;

### Parameters&#x20;

* user\_id (str): User ID of the target user.
* services (list): List of services to be applied to user.&#x20;
* service\_packs (list): List of service packs to be applied to user.&#x20;
* assigned (bool, optional): Assign (True) or unassign(False). Defaults to True.

### Returns

* Dict: User services assigned to the user.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# updating a users service pack
my_api.put.user_services(
    "userId@domain.com",
    service_packs=["SP-A"],
    assigned=True
)

my_api.user_services(
user_id = hunt_group_user_id,
services = hunt_group_services,
assigned = False
)
```
