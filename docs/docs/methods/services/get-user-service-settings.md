---
description: my_api.get.user_service_settings()
---

# ⚙️ GET - User Service Settings

This method grabs all of a Broadwork entity's service settings.

### Parameters&#x20;

* user\_id (str): User ID of the target Broadworks entity.

### Returns

* Dict: Broadworks entity and all service settings.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# updating a users service pack
my_api.get.user_service_settings(
    "userId@domain.com"
)
```
{% endcode %}

### Example Data Returned (Formatted)
```json
{
  "userId": "user@odinapi.net",
  "Advice Of Charge": {
    "isActive": false,
    "aocType": "During Call"
    }
}
```
```