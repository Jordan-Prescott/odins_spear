---
description: my_api.get.user_services_assigned()
---


# 🍒 GET - user_services_assigned

This method updates a Broadwork entity's services and service packs if applicable. Any entity that can have a service or service pack assigned can be pulled down, such as a user's service pack or a Hunt Group services. Note that services and service packs are separated into two lists when passed to the method, if you only want to get one list only pass in the list you wish to update. For example, adding the service pack 'SP-A' to user A will only require I pass this in the service_pack parameter

Fetch all services assigned to a broadwrok entity, this can be a user, AA, CC, or HG.

### Parameters

* user\_id (str): User ID of the target user.

### Returns

* Dict: User services assigned to the user.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# Get a users service pack
my_api.get.user_services_assigned(
    "userId@domain.com"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
   "userId":"123456789@test",
   "userServices":[
      {
         "serviceName":"Authentication"
      },
      {
         "serviceName":"Basic Call Logs"
      },
      {
         "serviceName":"Call Waiting",
         "isActive":true
      },
      {
         "serviceName":"External Calling Line ID Delivery",
         "isActive":true
      },
      {
         "serviceName":"Internal Calling Line ID Delivery",
         "isActive":true
      }
   ],
   "groupServices":[
      {
         "serviceName":"Music On Hold",
         "isActive":true
      }
   ]
}
```
