---
description: my_api.get.group_hunt_group()
---

#  🍊 GET - Group Hunt Group

Returns detailed information about the specified Hunt Group.

### Parameters&#x20;

* service_user_id (str): UserID of the target Hunt Group.

### Returns

* Dict: Returns the specified Hunt Groups settings and information, such as group policies, agents, and extension.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_hunt_group(
    service_user_id="huntGroupUserID@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
  {
  "serviceInstanceProfile": {
    "name": "huntGroupUserID@domain.com",
    "callingLineIdLastName": "Test Last Name",
    "callingLineIdFirstName": "Test First Name",
    "hiraganaLastName": "Test Last Name",
    "hiraganaFirstName": "Test First Name",
    "language": "English",
    "timeZone": "America/Denver",
    "timeZoneDisplayName": "(GMT-06:00) (US) Mountain Time",
    "aliases": []
  },
  "policy": "Regular",
  "huntAfterNoAnswer": true,
  "noAnswerNumberOfRings": 5,
  "forwardAfterTimeout": false,
  "forwardTimeoutSeconds": 10,
  "allowCallWaitingForAgents": true,
  "useSystemHuntGroupCLIDSetting": true,
  "includeHuntGroupNameInCLID": true,
  "enableNotReachableForwarding": false,
  "makeBusyWhenNotReachable": false,
  "serviceUserId": "huntGroupUserID@domain.com",
  "serviceProviderId": "serviceProivederID",
  "groupId": "groupID",
  "isEnterprise": true,
  "agents": [
    {
        "userId": "user@domain.com"
    },
    {
        "userId": "user@domain.com"
    }
  ]
}
]
```
