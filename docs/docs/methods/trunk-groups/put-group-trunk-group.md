---
description: api.put.group_trunk_group()
---

# ☎️ PUT - Group Trunk Group

Updates trunk group (TG) information.

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the target group is built
* group\_id (str): Group ID whose trunk group call capacity needs updating
* trunk\_group\_name (str): The name of the trunk group that is being updated. 
* updates (dict): Updates to be applied to the TG. 

### Returns

* Dict: Returns the updated Trunk Group profile.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.group_trunk_group(
  my_service_provider_id = "ServiceProviderID",
  my_group_id = "GroupID",
  my_trunk_group = "Odin Test Trunk
  updates = {
    "maxActiveCalls": 1,
    "maxIncomingCalls": 0,
    "maxOutgoingCalls": 0,
    "enableBursting": false
  }
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "maxActiveCalls": 1, 
  "maxIncomingCalls": 0, 
  "maxOutgoingCalls": 0, 
  "enableBursting": False, 
  "capacityExceededTrapInitialCalls": 0, 
  "capacityExceededTrapOffsetCalls": 0, 
  "invitationTimeout": 6, 
  "requireAuthentication": False, 
  "allowTerminationToTrunkGroupIdentity": False, 
  "allowTerminationToDtgIdentity": False, 
  "includeTrunkGroupIdentity": False, 
  "includeDtgIdentity": False, 
  "includeTrunkGroupIdentityForNetworkCalls": False, 
  "includeOtgIdentityForNetworkCalls": False, 
  "enableNetworkAddressIdentity": False, 
  "allowUnscreenedCalls": False, 
  "allowUnscreenedEmergencyCalls": False, 
  "pilotUserCallingLineIdentityForExternalCallsPolicy": "No Calls", 
  "pilotUserChargeNumberPolicy": "No Calls", 
  "routeToPeeringDomain": False, 
  "prefixEnabled": False, 
  "statefulReroutingEnabled": False, 
  "sendContinuousOptionsMessage": False, 
  "continuousOptionsSendingIntervalSeconds": 30, 
  "failureOptionsSendingIntervalSeconds": 10, 
  "failureThresholdCounter": 1, 
  "successThresholdCounter": 1, 
  "inviteFailureThresholdCounter": 1, 
  "inviteFailureThresholdWindowSeconds": 30, 
  "trunkGroupState": "Available", 
  "pilotUserCallingLineAssertedIdentityPolicy": "Unscreened Originating Calls", 
  "useSystemCallingLineAssertedIdentityPolicy": True, 
  "totalActiveIncomingCalls": 0, 
  "totalActiveOutgoingCalls": 0, 
  "pilotUserCallOptimizationPolicy": "Optimize For User Services", 
  "clidSourceForScreenedCallsPolicy": "Profile Name Profile Number", 
  "useSystemCLIDSourceForScreenedCallsPolicy": True, 
  "userLookupPolicy": "Basic", 
  "useSystemUserLookupPolicy": True, 
  "pilotUserCallingLineIdentityForEmergencyCallsPolicy": "No Calls", 
  "implicitRegistrationSetSupportPolicy": "Disabled", 
  "useSystemImplicitRegistrationSetSupportPolicy": True, 
  "sipIdentityForPilotAndProxyTrunkModesPolicy": "User", 
  "useSystemSIPIdentityForPilotAndProxyTrunkModesPolicy": True, 
  "useSystemSupportConnectedIdentityPolicy": True, 
  "supportConnectedIdentityPolicy": "Disabled", 
  "useSystemOptionsMessageResponseStatusCodes": True, 
  "serviceProviderId": "ServiceProviderID", 
  "groupId": "GroupID", 
  "name": "Odin Test Trunk", 
  "users": []
}

```
