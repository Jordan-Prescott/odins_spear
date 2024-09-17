---
description: my_api.put.group_hunt_group()
---

# 🍏 PUT - Group Hunt Group

Update a Hunt Groups (HG) settings.

{% hint style="warning" %}
**Modifying Agents in Hunt Group -** Remember to follow the correct formatting, the list contains dictionaries of userId and the  users id.\
Example - \[{"userId":"9709580001"}, {"userId":"9709580002"}]
{% endhint %}

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID of where the group that hosts the HG is located.
* group\_id (_type_): Group ID of where the HG is located.&#x20;
* hunt\_group\_user\_id (str): Target service user ID of the HG.&#x20;
* updates (dict): Updates to be applied to HG.

### Returns

* None: This method does not return any specific value.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_service_provider_id = "serviceProviderId"
my_group_id = "groupId"
my_hunt_group_id = "huntGroupID@domain.com"
updates = {
	"serviceInstanceProfile":{
		"name":"odin.mock.hg.2",
		"callingLineIdLastName":"odin.mock.hg.2",
		"callingLineIdFirstName":"odin.mock.hg.2",
		"hiraganaLastName":"odin.mock.hg.2",
		"hiraganaFirstName":"Hunt Group",
		"language":"English",
		"timeZone":"America/Denver",
		"aliases":[]
	},
	"policy":"Regular",
	"huntAfterNoAnswer":true,
	"noAnswerNumberOfRings":5,
	"forwardAfterTimeout":false,
	"forwardTimeoutSeconds":10,
	"allowCallWaitingForAgents":true,
	"useSystemHuntGroupCLIDSetting":true,
	"includeHuntGroupNameInCLID":true,
	"enableNotReachableForwarding":false,
	"makeBusyWhenNotReachable":false,
	"agents":[
		{"userId":"9709580001"},
		{"userId":"9709580002"}
	]
}

my_api.put.group_hunt_group(
    service_provider_id = my_service_provider_id ,
    group_id = my_group_id,
    hunt_group_user_id = my_hunt_group_user_id,
    updates = my_updates
)
```
