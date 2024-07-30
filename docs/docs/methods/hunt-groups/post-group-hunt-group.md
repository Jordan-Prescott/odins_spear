---
description: my_api.post.group_hunt_group()
---

# 🙋‍♂️ POST - Group Hunt Group

Builds a hunt group (HG) in the specified group. 

### Parameters&#x20;

* service\_provider\_id (str): The service provider ID in which the target group is built.
* group\_id (str): The group ID where the HG should be built.
* service\_user\_id (str): The service user ID for the new HG. This must include the domain of the user.
* clid\_first\_name (str): The Calling Line ID first name.
* clid\_last\_name (str): The Calling Line ID last name. 
* extension (str): The extension number for the HG. This must be entered as a string. 
* payload (dict, optional): HG configuration data. 
* agents (list, optional): List of user IDs (str) that should be assigned to the new HG. The user(s) must already exist in the group. 
* policy (str, optional): Regular, Circular, Simultaneous, Uniform, Weighted. Defaults to Regular.
* no\_answer\_number\_of\_rings (int, optional): Defaults to 5.
* forward\_timeout\_seconds (int, optional): Defaults to 0.

### Returns

* None: This method does not return any specific value.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

hunt_group_agents= [
    "hunt_group_user1@microv-works.com",
    "hunt_group_user2@microv-works.com"
]

my_api.post.group_hunt_group(
    my_service_provider_id = "ServiceProviderID",
    my_group_id = "GroupID", 
    service_user_id = "odin.mock.hg.2@microv-works.com", 
    clid_first_name = "odin", 
    clid_last_name = "mock.hg.2", 
    hunt_group_extension = "1234", 
    agents = hunt_group_agents, 
    policy = "Regular"    
)
```
### Example Returned Data of Hunt Group (Formatted)

```json
{
    "serviceInstanceProfile": {
        "name": "odin mock.hg.2",
        "callingLineIdLastName": "mock.hg.2",
        "callingLineIdFirstName": "odin",
        "hiraganaLastName": "odin mock.hg.2",
        "hiraganaFirstName": "Hunt Group",
        "extension": "1234",
        "language": "English",
        "timeZone": "Europe/London",
        "timeZoneDisplayName": "(GMT+01:00) Greenwich Mean Time",
        "aliases": []
    },
    "policy": "Regular",
    "huntAfterNoAnswer": False,
    "noAnswerNumberOfRings": 5,
    "forwardAfterTimeout": False,
    "forwardTimeoutSeconds": 0,
    "allowCallWaitingForAgents": False,
    "useSystemHuntGroupCLIDSetting": False,
    "includeHuntGroupNameInCLID": False,
    "enableNotReachableForwarding": False,
    "makeBusyWhenNotReachable": False,
    "allowMembersToControlGroupBusy": False,
    "enableGroupBusy": False,
    "applyGroupBusyWhenTerminatingToAgent": False,
    "serviceUserId": "odin.mock.hg.2@microv-works.com",
    "resellerId": None,
    "serviceProviderId": "ServiceProviderID",
    "groupId": "GroupID",
    "isEnterprise": True,
    "agents": [
        {
            "userId": "hunt_group_user1@microv-works.com",
            "lastName": "1",
            "firstName": "hunt_group_user",
            "hiraganaLastName": "1",
            "hiraganaFirstName": "hunt_group_user",
            "weight": None,
            "phoneNumber": None,
            "extension": "111111",
            "department": None,
            "emailAddress": None,
            "isPhoneNumberActivated": None,
            "countryCode": None,
            "nationalPrefix": None,
            "departmentName": None,
            "departmentType": None,
            "parentDepartment": None,
            "parentDepartmentType": None,
            "groupId": "GroupID",
            "groupName": "Group Name"
        }, 
        {
            "userId": "hunt_group_user2@microv-works.com",
            "lastName": "2",
            "firstName": "hunt_group_user",
            "hiraganaLastName": "2",
            "hiraganaFirstName": "hunt_group_user",
            "weight": None,
            "phoneNumber": None,
            "extension": "222222",
            "department": None,
            "emailAddress": None,
            "isPhoneNumberActivated": None,
            "countryCode": None,
            "nationalPrefix": None,
            "departmentName": None,
            "departmentType": None,
            "parentDepartment": None,
            "parentDepartmentType": None,
            "groupId": "GroupID",
            "groupName": "Group Name"
        }
    ]
}

```