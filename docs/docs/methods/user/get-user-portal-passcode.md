---
description: api.get.user_portal_passcode()
---

# 🔐 GET - User Portal Passcode

Pulls the Portal Passcode form a given user.

### Parameters&#x20;

* user\_id (str): Target user ID of the user you would like retrieve the password from.

### Returns

* Dict: Portal Passcode

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_portal_passcode(
    "user_ID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "isLoginDisabled": false,
  "expirationDays": 30,
  "passcode": "*****",
  "userId": "123456789@www.domain.com"
}
```