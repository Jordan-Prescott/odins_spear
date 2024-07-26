---
description: my_api.get.group_services()
---

# 🧍 GET - Group Services

Fetch all userServices, groupServices and servicePackServices assigned to a group

### Parameters&#x20;

* group\_id (str): GroupID of the target 
* service_provider\_id (str): Service Provider or Enterprise ID of the target.
### Returns

* Dict: Authorised and assigned services within the group.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# Pulling down group service
my_api.get.group_services(
    "groupId",
    "serviceProviderId"
)
```
{% endcode %}

### Example Data Returned (Formatted)
```json
{
   "resellerId":"None",
   "serviceProviderId":"Test",
   "groupId":"TestGroup",
   "userServices":[
      {
         "serviceName":"Anonymous Call Rejection",
         "authorized":false,
         "assigned":false,
         "limited":"Unlimited",
         "quantity":-1,
         "usage":0,
         "licensed":true,
         "allowed":-1,
         "userAssignable":true,
         "groupServiceAssignable":true,
         "tags":[
            
         ],
         "alias":"Anonymous Call Rejection"
      },
      {
         "serviceName":"Authentication",
         "authorized":false,
         "assigned":false,
         "limited":"Unlimited",
         "quantity":-1,
         "usage":0,
         "licensed":true,
         "allowed":-1,
         "userAssignable":true,
         "groupServiceAssignable":true,
         "tags":[
            
         ],
         "alias":"Authentication"
      },
      {
         "serviceName":"Call Forwarding Always",
         "authorized":false,
         "assigned":false,
         "limited":"Unlimited",
         "quantity":-1,
         "usage":0,
         "licensed":true,
         "allowed":-1,
         "userAssignable":true,
         "groupServiceAssignable":true,
         "tags":[
            
         ],
         "alias":"Call Forwarding Always"
      },
      {
         "serviceName":"Call Forwarding Busy",
         "authorized":false,
         "assigned":false,
         "limited":"Unlimited",
         "quantity":-1,
         "usage":0,
         "licensed":true,
         "allowed":-1,
         "userAssignable":true,
         "groupServiceAssignable":true,
         "tags":[
            
         ],
         "alias":"Call Forwarding Busy"
      },
      {
         "serviceName":"Call Forwarding No Answer",
         "authorized":false,
         "assigned":false,
         "limited":"Unlimited",
         "quantity":-1,
         "usage":0,
         "licensed":true,
         "allowed":-1,
         "userAssignable":true,
         "groupServiceAssignable":false,
         "tags":[
            
         ],
         "alias":"Call Forwarding No Answer"
      },
      {
         "serviceName":"Call Notify",
         "authorized":false,
         "assigned":false,
         "limited":"Unlimited",
         "quantity":-1,
         "usage":0,
         "licensed":true,
         "allowed":-1,
         "userAssignable":true,
         "groupServiceAssignable":true,
         "tags":[
            
         ],
         "alias":"Call Notify"
      },
      {
         "serviceName":"Calling Line ID Delivery Blocking",
         "authorized":false,
         "assigned":false,
         "limited":"Unlimited",
         "quantity":-1,
         "usage":0,
         "licensed":true,
         "allowed":-1,
         "userAssignable":true,
         "groupServiceAssignable":true,
         "tags":[
            
         ],
         "alias":"Calling Line ID Delivery Blocking"
      },
      {
         "serviceName":"CommPilot Express",
         "authorized":false,
         "assigned":false,
         "limited":"Unlimited",
         "quantity":-1,
         "usage":0,
         "licensed":true,
         "allowed":-1,
         "userAssignable":true,
         "groupServiceAssignable":false,
         "tags":[
            
         ],
         "alias":"CommPilot Express"
      },
      {
         "serviceName":"Do Not Disturb",
         "authorized":false,
         "assigned":false,
         "limited":"Unlimited",
         "quantity":-1,
         "usage":0,
         "licensed":true,
         "allowed":-1,
         "userAssignable":true,
         "groupServiceAssignable":true,
         "tags":[
            
         ],
         "alias":"Do Not Disturb"
      }
   ]
}
```
```
