---
description: my_api.put.user_call_processing_policy()
---

# 🗃️ PUT - User Call Processing Policy

Update the Call Processing Policies for a specified user. 

### Parameters&#x20;

* user\_id (str): The user ID of the user whose call processing policies need updating.
* updates (dict): Updates to apply to the specified user. 

### Returns

* Dict: Returns the updated call processing policies.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.user_call_processing_policy(
    "userID@domain.com",
    updates = {
        "clidPolicy": "Use DN",
        "emergencyClidPolicy": "Use DN",
        "allowAlternateNumbersForRedirectingIdentity": "true",
        "useGroupName": "false"
    }
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "useUserCLIDSetting": False, 
  "useUserMediaSetting": False, 
  "useUserCallLimitsSetting": False, 
  "useUserDCLIDSetting": False, 
  "useUserTranslationRoutingSetting": False, 
  "useMaxSimultaneousCalls": True, 
  "maxSimultaneousCalls": 5, 
  "useMaxSimultaneousVideoCalls": True, 
  "maxSimultaneousVideoCalls": 5, 
  "useMaxCallTimeForAnsweredCalls": True, 
  "maxCallTimeForAnsweredCallsMinutes": 1440, 
  "useMaxCallTimeForUnansweredCalls": False, 
  "maxCallTimeForUnansweredCallsMinutes": 2, 
  "mediaPolicySelection": "No Restrictions", 
  "useMaxConcurrentRedirectedCalls": True, 
  "maxConcurrentRedirectedCalls": 5, 
  "useMaxFindMeFollowMeDepth": True, 
  "maxFindMeFollowMeDepth": 2, 
  "maxRedirectionDepth": 5, 
  "useMaxConcurrentFindMeFollowMeInvocations": True, 
  "maxConcurrentFindMeFollowMeInvocations": 2, 
  "clidPolicy": "Use DN", 
  "emergencyClidPolicy": "Use DN", 
  "allowAlternateNumbersForRedirectingIdentity": True, 
  "useGroupName": False, 
  "blockCallingNameForExternalCalls": False, 
  "enableDialableCallerID": False, 
  "allowConfigurableCLIDForRedirectingIdentity": True, 
  "allowDepartmentCLIDNameOverride": False, 
  "useUserPhoneListLookupSetting": False, 
  "enablePhoneListLookup": False, 
  "useMaxConcurrentTerminatingAlertingRequests": False, 
  "maxConcurrentTerminatingAlertingRequests": 10, 
  "includeRedirectionsInMaximumNumberOfConcurrentCalls": False, 
  "allowMobileDNForRedirectingIdentity": False, 
  "userId": "userID@domain.com"
}

```

