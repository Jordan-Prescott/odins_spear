---
description: my_api.get.call_pickup_group_user()
---

# 🤳 GET - Call Pickup Group User

Retrieves Pickup Group information for the specified user.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* group_id (str): The Target Group ID the user is apart of.
* user_id (str): Target User ID

### Returns

* Dict: Specified users pickup group, and the users within that group.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.call_pickup_group_user(
    "my_service_provider_id", 
    "my_group_id", 
    "john.smith@testdomain.net"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json

{
  "serviceProviderId": "my_service_provider_id",
  "groupId": "my_group_id",
  "name": "Call Pickup 1",
  "users":  [
        {
        "userId": "john.smith@testdomain.net", 
        "lastName": "Smith", 
        "firstName": "John", 
        "hiraganaLastName": "Smith", 
        "hiraganaFirstName": "John", 
        "phoneNumber": "+1-23456789", 
        "extension": "1234", 
        "department": None, 
        "emailAddress": None
        }, 
        {
        "userId": "jane.smith@testdomain.net", 
        "lastName": "Smith", 
        "firstName": "Jane", 
        "hiraganaLastName": "Smith", 
        "hiraganaFirstName": "jane", 
        "phoneNumber": "+1-98765432", 
        "extension": "4321", 
        "department": None, 
        "emailAddress": None
        }
    ]
}


```

