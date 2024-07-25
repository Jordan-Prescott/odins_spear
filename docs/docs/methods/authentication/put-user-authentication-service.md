---
description: my_api.put.user_authentication_service()
---

# 👮‍♀️ PUT - User Authentication Service

Set new SIP Authentication passowrd for a single user. Authentication service must be assigned to the user in order to use this method. 

### Parameters&#x20;

* user\_id (str): Target user ID to reset the SIP authentication password.&#x20;
* new\_password (str): New web authentication password to apply to new user. Please note: the password must be at least 6 characters and not more than 60 characters; including 1 uppercase alpha char(s); including 1 lowercase alpha char(s); In addition, it cannot contain the authentication name.

### Returns

* Dict: Python dictionary of the user that has been updated. The password will not be printed to the terminal. 

### How To Use:

The below code will update the user's Authentication password.

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.user_authentication_service(
    "john.smith@testdomain.net",
    "NewPassword123!"
)
```
{% endcode %}

### Example Returned Data of Device (Formatted)

```json
{
    "userId": "john.smith@testdomain.net", 
    "userName": "john.smith", 
    "newPassword": ""
    }
```