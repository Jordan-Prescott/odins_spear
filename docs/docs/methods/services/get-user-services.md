---
description: my_api.get.user_services()
---

# 🧍 GET - User Services

This method updates a Broadwork entity's services and service packs if applicable. Any entity that can have a service or service pack assigned can be updated such as a user's service pack or a Hunt Group services. Note that services and service packs are separated into two lists when passed to the method, if you only want to update one list only pass in the list you wish to GET.

### Parameters&#x20;

* user\_id (str): User ID of the target Broadworks entity.

### Returns

* Dict: Broadwork entiy and a list of services assigned.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# updating a users service pack
my_api.get.user_services(
    "userId@domain.com"
)
```
{% endcode %}

### Example Data Returned (Formatted)
```json
{
   "userId":"123456789@test.com",
   "userServices":[
      {
         "serviceName":"Call Forwarding Not Reachable",
         "assigned":false,
         "tags":[
            
         ],
         "alias":"Call Forwarding Not Reachable"
      }
   ],
   "servicePackServices":[
      {
         "assigned":false,
         "description":"Webex Contact Cnetre Premium Named Agent Cheval Group",
         "serviceName":"WBX-CCPNA-CG",
         "alias":"WBX-CCPNA-CG"
      },
      {
         "assigned":false,
         "description":"Webex for BroadWorks Basic",
         "serviceName":"WBX-B",
         "alias":"WBX-B"
      },
      {
         "assigned":true,
         "description":"SIP DID",
         "serviceName":"SIP-DID",
         "alias":"SIP-DID"
      },
      {
         "assigned":false,
         "description":"Fax to Email",
         "serviceName":"House-FE",
         "alias":"House-FE"
      },
      {
         "assigned":false,
         "description":"Fax",
         "serviceName":"House-F",
         "alias":"House-F"
      },
      {
         "assigned":false,
         "description":"Admin",
         "serviceName":"Admin-A",
         "alias":"Admin-A"
      },
      {
         "assigned":false,
         "description":"Meeting",
         "serviceName":"House-M",
         "alias":"House-M"
      },
      {
         "assigned":false,
         "description":"House",
         "serviceName":"House-H",
         "alias":"House-H"
      },
      {
         "assigned":false,
         "description":"Meeting Plus",
         "serviceName":"House-MP",
         "alias":"House-MP"
      },
      {
         "assigned":false,
         "description":"Admin Plus",
         "serviceName":"Admin-AS",
         "alias":"Admin-AS"
      }
   ],
   "serviceProviderId":"TestGroup",
   "groupId":"Test"
}
```
```
