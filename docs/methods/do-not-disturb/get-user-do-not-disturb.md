---
description: my_api.get.user_do_not_disturb()
---

# 🛑 GET - User Do Not Disturb

This method fetches the Do Not Disturb (DND) and Ring Splash (RS) status of a single. It takes a single User ID of the target user you would like to retrieve the status of.&#x20;

### Parameters&#x20;

* user\_id (str): Target User you would like to know the DND/ RS status of&#x20;

### Returns

* Dict: Target users DND/ RS status. True is enabled and False disabled.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_do_not_disturb(userId)
```

## Examples Data (Formatted)

```python
{
  "isActive": true,
  "ringSplash": true,
  "userId": "9709580001@microv-works.com"
}
```
