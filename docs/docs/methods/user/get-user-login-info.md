---
description: api.get.user_login_info()
---

# 🧅 GET - User Login Info

Pulls the Login Type and other general information about a user.

### Parameters&#x20;

* user\_id (str): Target user ID of the user you would like retrieve the information from.

### Returns

* Dict: User Information

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_login_info(
    "user_ID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
    "loginType": "User",
    "locale": "en_US",
    "encoding": "ISO-8859-1",
    "groupId": "GRPID",
    "serviceProviderId": "ServiceProv",
    "isEnterprise": true,
    "passwordExpiresDays": "-2147483648",
    "lastName": "12",
    "firstName": "12",
    "userId": "user@domain.com",
    "isAlternateUserId": false,
    "broadworksUserId": "user@domain.com",
    "departmentName": null
}
```