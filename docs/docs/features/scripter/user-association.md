---
description: api.scripter.user_association()
---

# 🔗 User Association

This script is to identify a user's associations with Call Centers (CC), Hunt Groups (HG), and Pick Up Groups. Additionally, this returns other key information of the user such as extension, phone number, and services and feature packs assigned as this data can be useful when reviewing which CC and HG they are associated to for example if an agent in a CC has a higher feature pack than needed for work in x CC.

This script uses the below methods to achieve this:

```python
api.get.call_pickup_group_user()
api.get.group_hunt_group_user()
api.get.user_call_center()
api.get.user_report()
```

### Parameters&#x20;

* service\_provider\_id: Service Provider where the group is hosted.
* group\_id: Group where the User is located.
* user\_id: Target user ID.

### Return

* dict: Returns a dictionary output containing all CC, HG, and Pick Up a user is assigned to.&#x20;

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.scripter.user_association(
    "ServiceProviderID", 
    "GroupID", 
    "UserID"
)
```
{% endcode %}

### Formatted Output

```json
{
   "userId":"TestUser2076@Domain.com",
   "firstName":"John",
   "lastName":"Smith",
   "extension":"2076",
   "phoneNumber":"012345678910",
   "aliases":[
      "12@Domain"
   ],
   "services":[
      
   ],
   "featurePacks":[
      "WBX-B",
      "Agent-AGPCCSA",
      "Call-R"
   ],
   "huntGroups":[
      "KallumTEST@Domain.com",
      "FrontDoorOverflow3",
      "CallumTest",
      "Maintenance"
   ],
   "callCenters":[
      "DemoCC",
      "CallCenterName",
      "TechSupport_CC"
   ],
   "pickUpGroup":"tech and service"
}
```
