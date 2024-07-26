---
description: api.put.user_portal_passcode()
---

# 👩‍👩‍👧‍👧 PUT - User Portal Passcode

Updates the specified User's portal passcode.

### Parameters&#x20;

* user_id (str): User ID of the target user you would like to change the portal passcode for. 
* new_passcode (int): New portal passcode to set for the target user.

### Raises

* AOInvalidCode: If code is less than 4 or higher than 6.

### Returns

* None: This method does not return any specific value.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.user_portal_passcode(
    "john.smith@testdomain.net",
    "12345"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[]

```
