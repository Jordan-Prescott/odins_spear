---
description: my_api.post.auto_attendant_remove_user()
---

#  👋 POST - Auto Attendant Remove User

Returns a list of the available Auto Attendants (AAs) built in the same group as the specified user. NOTE: This does not remove the user from the group.

### Parameters&#x20;

* service_provider_id (str): Service Provider ID where the user is built. 
* group_id (str): Group ID where the user is built. 
* user_id (str): User ID of the user.

### Returns

* List: List of the Service User IDs of the AAs in the group.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.post.auto_attendant_remove_user(
    service_provider_id="my_service_provider_id",
    group_id="my_group_id", 
    user_id="test_user@domain.net"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
["basic_aa@domain.net", "odin_test@domain.net"]


```
