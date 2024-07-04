---
description: my_api.user_call_center()
---

# 🟢 PUT - User Call Center

### Parameters&#x20;

* user\_id (str): User ID of the target user.&#x20;
* updates (dict): Updates to be applied to the user.

### Returns

* Dict: Agents' ACD status and status in each CC they are assigned to.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_user_id = "user_id@domain.com"
my_updates = {
	"agentACDState":"Available",
	"agentThresholdProfileName":"Default Agent Threshold Profile",
	"useDefaultGuardTimer":true,
	"enableGuardTimer":false,
	"guardTimerSeconds":5,
	"useSystemDefaultUnavailableSettings":true,
	"forceAgentUnavailableOnDNDActivation":false,
	"forceAgentUnavailableOnPersonalCalls":false,
	"forceAgentUnavailableOnBouncedCallLimit":false,
	"numberConsecutiveBouncedCallsToForceAgentUnavailable":3,
	"forceAgentUnavailableOnNotReachable":false,
	"makeOutgoingCallsAsCallCenter":false,
	"callCenters":[
		{
			"serviceUserId":"mock.cc.1",
			"available":true,
			"skillLevel":null
		},
		{
			"serviceUserId":"mock.cc.2",
			"available":true,
			"skillLevel":10
		}
	]
}

my_api.put.user_call_center(
    user_id = my_user_id,
    updates= my_updates 
)
```
