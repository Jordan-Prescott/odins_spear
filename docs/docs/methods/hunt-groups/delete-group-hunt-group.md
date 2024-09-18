---
description: my_api.delete.group_hunt_group()
---

#  💔 DELETE - Group Hunt Group

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

my_api.delete.group_hunt_group(
    service_user_id = "test_hunt_groupd@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
    "serviceInstanceProfile": {
        "name": "test_hunt_group",
        "callingLineIdLastName": "Hunt Group",
        "callingLineIdFirstName": "Test",
        "hiraganaLastName": "Hunt Group",
        "hiraganaFirstName": "Test",
        "language": "English",
        "timeZone": "Europe/London",
        "timeZoneDisplayName": "(GMT+01:00) Greenwich Mean Time",
        "aliases": []
    },
    "policy": "Regular",
    "huntAfterNoAnswer": False,
    "noAnswerNumberOfRings": 5,
    "forwardAfterTimeout": False,
    "forwardTimeoutSeconds": 10,
    "allowCallWaitingForAgents": False,
    "useSystemHuntGroupCLIDSetting": True,
    "includeHuntGroupNameInCLID": True,
    "enableNotReachableForwarding": False,
    "makeBusyWhenNotReachable": False,
    "allowMembersToControlGroupBusy": False,
    "enableGroupBusy": False,
    "applyGroupBusyWhenTerminatingToAgent": False,
    "serviceUserId": "test_hunt_group@domain.com",
    "resellerId": None,
    "serviceProviderId": "ExampleServiceProvider",
    "groupId": "ExampleGroup",
    "isEnterprise": True,
    "agents": []
}
```
