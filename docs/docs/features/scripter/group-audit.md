---
description: api.scripter.group_audit()
---

# ☑️ Group Audit

This script will  generate a JSON output containing detail, and summaries, of elements of the group which are typically chargeable to a customer.

Currently, the script produces information around:

* User Count and Limits
* Group DNs
* Group Services
* User Services
* User Service Packs
* Trunking Call Capacity

The script makes use of the following methods:

```python
api.get.group_services()
api.get.group_services_assigned()
api.get.group_dns()
api.get.group()
api.get.group_trunk_groups_call_capacity()
```

### Parameters&#x20;

* service\_provider\_id: Service Provider where the group is hosted.
* group\_id: Group where the User is located.

### Return

* dict: Returns dictionary containing all group information. Including Users, Group DNs, Group Services, User Services, User Service Packs, Trunking Capacity.

### How To Use:

```python
from odins_spear import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()


print(my_api.scripter.group_audit("ServiceProviderID", "GroupID"))
```

### Example returned data (formatted):

```json
{
    "group_detail": {
        "defaultDomain": "bworks.provider.com",
        "userLimit": 50,
        "userCount": 4,
        "groupName": "Example Group 1",
        "callingLineIdName": "Example Group 1",
        "callingLineIdPhoneNumber": "+441632123456",
        "callingLineIdDisplayPhoneNumber": "01632123456",
        "timeZone": "Europe/London",
        "timeZoneDisplayName": "(GMT) Greenwich Mean Time",
        "serviceProviderId": "Ent1",
        "groupId": "GrpA"
    },
    "licence_breakdown": {
        "user_services": [
            {
                "serviceName": "Authentication",
                "usage": 1,
                "users": [
                    "User1"
                ]
            },
            {
                "serviceName": "Call Forwarding Always",
                "usage": 2,
                "users": [
                    "User1",
                    "User2"
                ]
            },
            {
                "serviceName": "Call Forwarding Busy",
                "usage": 2,
                "users": [
                    "User1",
                    "User3"
                ]
            }
        ],
        "group_services": [
            {
                "serviceName": "Auto Attendant",
                "usage": 1
            },
            {
                "serviceName": "Hunt Group",
                "usage": 5
            },
            {
                "serviceName": "Music On Hold",
                "usage": 1
            },
            {
                "serviceName": "Trunk Group",
                "usage": 2
            }
        ],
        "service_pack_services": [
            {
                "servicePackName": "Standard",
                "usage": 3,
                "description": "Standard Pack",
                "users": [
                    "User1",
                    "User2",
                    "User3"
                ]
            },
            {
                "servicePackName": "Premium",
                "usage": 1,
                "description": "Premium Pack",
                "users": [
                    "User4"
                ]
            }
        ]
    },
    "group_DNs": {
        "assigned": {
            "activated": [
		"+44-1632123456"
            ],
            "deactivated": [
                "+44-1632654321"
            ],
            "total_assigned_DNs": 2
        },
        "unassigned": {
            "activated": [
                "+44-1632456123"
            ],
            "deactivated": [
                "+44-1632321654"
            ],
            "total_unassigned_DNs": 2
        },
        "total_DNs": 4
    },
    "group_trunking": {
        "maxActiveCalls": 10,
        "maxAvailableActiveCalls": 10,
        "burstingMaxActiveCalls": 1,
        "burstingMaxAvailableActiveCalls": 1,
        "maxAvailableNumberOfBurstingBTLUs": 0,
        "numberOfBurstingBTLUs": 0
    }
}
```
