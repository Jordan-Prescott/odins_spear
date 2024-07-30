---
description: my_api.get.group_hunt_group_user()
---

#  🍐 GET - Group Hunt Group User

Returns the Hunt Group's the specified User is apart of.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* group_id (str): Target Group ID
* user_id (str): Target User ID

### Returns

* Dict: Returns the specified Hunt Groups settings and information, such as group policies, agents, and extension.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_hunt_group_user(
    service_provider_id="serviceProviderId",
    group_is="groupId",
    user_id="TargetUserId@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
    {
        "serviceUserId": "HuntGroup1",
        "name": "HuntGroup1",
        "phoneNumber": "123456789",
        "extension": "8890",
        "department": null,
        "isActive": true,
        "policy": "Simultaneous",
        "serviceProviderId": "serviceProviderId",
        "groupId": "groupId",
        "serviceInstanceProfile": {
            "name": "HuntGroup1",
            "callingLineIdLastName": "HuntGroup1",
            "callingLineIdFirstName": "HuntGroup1",
            "hiraganaLastName": "HuntGroup1",
            "hiraganaFirstName": "HuntGroup1",
            "phoneNumber": "123456789",
            "extension": "8890",
            "countryCode": "44",
            "nationalPrefix": "0",
            "language": "English",
            "timeZone": "GMT",
            "timeZoneDisplayName": "(GMT) GMT",
            "aliases": []
        },
        "huntAfterNoAnswer": false,
        "noAnswerNumberOfRings": 5,
        "forwardAfterTimeout": true,
        "forwardTimeoutSeconds": 8,
        "forwardToPhoneNumber": 3000,
        "allowCallWaitingForAgents": false,
        "useSystemHuntGroupCLIDSetting": true,
        "includeHuntGroupNameInCLID": true,
        "enableNotReachableForwarding": false,
        "makeBusyWhenNotReachable": false,
        "allowMembersToControlGroupBusy": false,
        "enableGroupBusy": false,
        "applyGroupBusyWhenTerminatingToAgent": false,
        "agents": [
            {
                "userId": "TargetUserId@domain.com",
                "lastName": "Smith",
                "firstName": "John",
                "hiraganaLastName": "Smith",
                "hiraganaFirstName": "John",
                "weight": null,
                "phoneNumber": "9827349700",
                "extension": "2444",
                "department": null,
                "emailAddress": null,
                "isPhoneNumberActivated": true,
                "countryCode": "44",
                "nationalPrefix": 0,
                "departmentName": null,
                "departmentType": null,
                "parentDepartment": null,
                "parentDepartmentType": null,
                "groupId": "groupId",
                "groupName": "Group 1"
            },
            {
                "userId": "UserID2@domain.com",
                "lastName": "Doe",
                "firstName": "Jane",
                "hiraganaLastName": "Doe",
                "hiraganaFirstName": "Jane",
                "weight": null,
                "phoneNumber": "1234986332",
                "extension": "5656",
                "department": null,
                "emailAddress": null,
                "isPhoneNumberActivated": true,
                "countryCode": "44",
                "nationalPrefix": 0,
                "departmentName": null,
                "departmentType": null,
                "parentDepartment": null,
                "parentDepartmentType": null,
                "groupId": "groupId",
                "groupName": "Group 1"
            },
            ...
        ]
    },
    {
        "serviceUserId": "HuntGroup2",
        "name": "Hunt Group 2",
        "phoneNumber": 1234509876,
        "extension": "2222",
        "department": null,
        "isActive": true,
        "policy": "Regular",
        "serviceProviderId": "serviceProviderId",
        "groupId": "groupId",
        "serviceInstanceProfile": {
            "name": "Hunt Group 2",
            "callingLineIdLastName": "HuntGroup2",
            "callingLineIdFirstName": "HuntGroup2",
            "hiraganaLastName": "HuntGroup2",
            "hiraganaFirstName": "HuntGroup2",
            "extension": "2222",
            "language": "English",
            "timeZone": "GMT",
            "timeZoneDisplayName": "(GMT) GMT",
            "aliases": []
        },
        "huntAfterNoAnswer": false,
        "noAnswerNumberOfRings": 5,
        "forwardAfterTimeout": true,
        "forwardTimeoutSeconds": 16,
        "forwardToPhoneNumber": "*553401",
        "allowCallWaitingForAgents": false,
        "useSystemHuntGroupCLIDSetting": true,
        "includeHuntGroupNameInCLID": true,
        "enableNotReachableForwarding": false,
        "makeBusyWhenNotReachable": false,
        "allowMembersToControlGroupBusy": false,
        "enableGroupBusy": false,
        "applyGroupBusyWhenTerminatingToAgent": false,
        "agents": [
            {
                "userId": "TargetUserId@domain.com"
                ...
            },
            {
                "userId": "UserId2"
                ...
            }
        ]
    },
    ...
]
```
