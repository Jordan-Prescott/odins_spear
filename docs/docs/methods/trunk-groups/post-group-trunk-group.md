---
description: api.post.group_trunk_group()
---

# 🚿 POST - Group Trunk Group

Builds a Trunk Group (TG) in the specified group. Please note, several fields are set to have default values. Please see below.
            
### Parameters&#x20;

* service\_provider\_id (str): Service provider ID for which the max active calls needs to be updated 
* group\_id (str): The group ID where the HG should be built.
* trunk\_name (str): The name of the new TG.
* max\_active\_calls (str): The maximum active calls to be set on the TG.
* payload (dict, optional): Configuration for the TG.
* sip\_authentication\_username (str, optional): The SIP authentication username for the TG. This field is required if "requireAuthentication" in the payload is set to "true". 
* sip\_authentication\_password (str, optional): The SIP authentication password for the TG. You can generate a password for this using get.sip_password_generator. This field is required if "requireAuthentication" in the payload is set to "true". 

### Returns

* Dict: Returns the Trunk Group profile. 

### Default Fields&#x20;

* "capacityExceededTrapInitialCalls":0,
* "capacityExceededTrapOffsetCalls":0,
* "clidSourceForScreenedCallsPolicy":"Profile Name Profile Number",
* "continuousOptionsSendingIntervalSeconds":30,
* "failureOptionsSendingIntervalSeconds":10,
* "failureThresholdCounter":1,
* "invitationTimeout":6,
* "inviteFailureThresholdCounter":1,
* "inviteFailureThresholdWindowSeconds":30,
* "pilotUserCallOptimizationPolicy":"Optimize For User Services",
* "pilotUserCallingLineAssertedIdentityPolicy":"Unscreened Originating Calls",
* "pilotUserCallingLineIdentityForEmergencyCallsPolicy":"No Calls",
* "pilotUserCallingLineIdentityForExternalCallsPolicy":"No Calls",
* "pilotUserChargeNumberPolicy":"No Calls",
* "requireAuthentication":"false",
* "successThresholdCounter":1,
* "useSystemUserLookupPolicy":"true",
* "userLookupPolicy":"Basic"


### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.group_trunk_group(
  my_service_provider_id = "ServiceProviderID",
  my_group_id =  "GroupID",
  my_trunk_group_name = "Odin Test Trunk"
  max_active_calls = 2
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "maxActiveCalls": 2,
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
  "useSystemCallingLineAssertedIdentityPolicy": False,
  "totalActiveIncomingCalls": 0,
  "totalActiveOutgoingCalls": 0,
  "pilotUserCallOptimizationPolicy": "Optimize For User Services",
  "clidSourceForScreenedCallsPolicy": "Profile Name Profile Number",
  "useSystemCLIDSourceForScreenedCallsPolicy": False,
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
