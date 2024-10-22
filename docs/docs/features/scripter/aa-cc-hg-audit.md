---
description: my_api.scripter.aa_cc_hg_audit()
---

# ✔️ AA, CC, HG Audit

This script returns the services assigned to Auto Attendants, Call Centres, and Hunt Groups. Only services are applied to these entities and there are scenarios one would need to focus services assigned to these entities.

The script makes use of the following methods:

```python
api.get.auto_attendants()
api.get.group_call_centers()
api.get.group_hunt_groups()
api.get.user_services_assigned()
```

### Parameters&#x20;

* service\_provider\_id: Service Provider ID or Enterprise ID containing the Group ID.
* group\_id: Group ID to generate the report for.

### Return

* dict: A dictionary containting service packs assigned in the group.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

print(my_api.scripter.aa_cc_hg_audit(
      "serviceProviderId",
      "groupId"
   )
)
```

### Example returned data (formatted):

```json
{
   "autoAttendants":[
      {
         "serviceUserId":"basic_aa@domain.com",
         "type":"Basic",
         "services":[
            
         ]
      }
   ],
   "callCenters":[
      {
         "serviceUserId":"basic_cc@domain.com",
         "type":"Basic",
         "services":[
            
         ]
      }
   ],
   "huntGroups":[
      {
         "serviceUserId":"EVA_External_HG@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"EVA_Internal_HG@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"EVA_External_HG_SB@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"EVA_Internal_HG_SB@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"testing@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"odin.mock.hg.2@domain.com",
         "services":[
            
         ]
      }
   ]
}

```
