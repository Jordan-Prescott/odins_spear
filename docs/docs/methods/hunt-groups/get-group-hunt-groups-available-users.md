---
description: my_api.get.group_hunt_groups_available_users()
---

#  👩‍👩‍👧‍👧 GET - Group Hunt Groups Available Users

Deletes the specified hunt group.

### Parameters&#x20;

* service_user_id (str): The service user ID of the hunt group to be deleted.

### Returns

* Dict: Profile of the deleted hunt group.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_hunt_groups_available_users(
    service_user_id="test_hgd@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
    "serviceInstanceProfile": {
        "name": "test_hg",
        "callingLineIdLastName": "hg",
        "callingLineIdFirstName": "test",
        "hiraganaLastName": "test_hg",
        "hiraganaFirstName": "Hunt Group",
        "language": "English",
        "timeZone": "Europe/London",
        "timeZoneDisplayName": "(GMT+01:00) Greenwich Mean Time",
        "aliases": []
    },
    "policy": "Regular",
    "huntAfterNoAnswer": false,
    "noAnswerNumberOfRings": 5,
    "forwardAfterTimeout": false,
    "forwardTimeoutSeconds": 10,
    "allowCallWaitingForAgents": false,
    "useSystemHuntGroupCLIDSetting": true,
    "includeHuntGroupNameInCLID": true,
    "enableNotReachableForwarding": false,
    "makeBusyWhenNotReachable": false,
    "allowMembersToControlGroupBusy": false,
    "enableGroupBusy": false,
    "applyGroupBusyWhenTerminatingToAgent": false,
    "serviceUserId": "test_hg@domain.com",
    "resellerId": null,
    "serviceProviderId": "Example Service Provider ID",
    "groupId": "Example Group ID",
    "isEnterprise": true,
    "agents": []
}
```
