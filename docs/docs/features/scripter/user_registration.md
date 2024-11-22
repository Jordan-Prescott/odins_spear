---
description: api.scripter.user_registration()
---

# 🔗 User Association

This script is to pull User Id's, Registered Device Names, and Registration status from every user within a group. This is helpful to diagnose issues, and identify devices that have gone offline.

This script uses the below methods to achieve this:

```python
api.get.bulk_user_registration()
```

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise where group is hosted.&#x20;
* group\_id (str): Target Group you would like to pull the registration of users for.&#x20;

### Return

* dict: Returns a dictionary output containing User ID, Device Name, and Registration Status&#x20;

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.scripter.user_registration(
    "ServiceProviderID", 
    "GroupID", 
)
```
{% endcode %}

### Formatted Output

```json
{
   "User1@odin.com":{
      "registration":{
         "Device123":{
            "registered":true
         }
      }
   },
   "User2@odin.com":{
      "registration":{
         
      }
   },
   "User3@odin.com":{
      "registration":{
         "DeskPhone":{
            "registered":true
         },
         "HomePhone":{
            "registered":true
         }
      }
   }
}
```
