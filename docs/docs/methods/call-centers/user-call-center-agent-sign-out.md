---
description: my_api.user_call_center_agent_sign_out()
---

# 🛑 PUT - User Call Center Agent Sign Out

Sign the user out of their assigned Call Centers (CC).

### Parameters&#x20;

* user\_id (str): User ID of the target user.

### Returns

* None: This method does not return any specific value.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_agent_user_id = "user_id@domain.com"

my_api.put.user_call_center_agent_sign_out(
    user_id = my_agent_user_id
)
```
