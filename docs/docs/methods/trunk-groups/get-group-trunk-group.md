---
description: api.get.group_trunk_group()
---

# ☎️ GET - Group Trunk Group

Fetches all Trunk Group details of a single Trunk Group in a Group.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where the target Trunk Group is located.&#x20;
* trunk\_group\_name (str): Target Trunk Group Name.

### Returns

* Dict: Details of a target trunk group.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_trunk_group(
    "ServiceProviderID",
    "GroupID",
    "trunkGroupName"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "department": {
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "name": "test"
  },
  "accessDevice": {
    "deviceLevel": "Group",
    "deviceName": "Generic SIP IP-PBX Single Registration 1"
  },
  "maxActiveCalls": 5,
  "maxIncomingCalls": 5,
  "maxOutgoingCalls": 5,
  "enableBursting": false,
  "capacityExceededTrapInitialCalls": 0,
  "capacityExceededTrapOffsetCalls": 0,
  "invitationTimeout": 6,
  "requireAuthentication": false,
  "trunkGroupIdentity": "grp.odin.trunka@parkbenchsolutions.com",
  "allowTerminationToTrunkGroupIdentity": false,
  "allowTerminationToDtgIdentity": false,
  "includeTrunkGroupIdentity": false,
  "includeDtgIdentity": false,
  "includeTrunkGroupIdentityForNetworkCalls": false,
  "includeOtgIdentityForNetworkCalls": false,
  "enableNetworkAddressIdentity": false,
  "allowUnscreenedCalls": false,
  "allowUnscreenedEmergencyCalls": false,
  "pilotUserCallingLineIdentityForExternalCallsPolicy": "No Calls",
  "pilotUserChargeNumberPolicy": "No Calls",
  "callForwardingAlwaysAction": "Reroute",
  "callForwardingAlwaysForwardAddress": 123123123,
  "callForwardingAlwaysRerouteTrunkGroupKey": {
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin.audit",
    "name": "trunk.odin.audit"
  },
  "routeToPeeringDomain": false,
  "prefixEnabled": false,
  "statefulReroutingEnabled": false,
  "sendContinuousOptionsMessage": false,
  "continuousOptionsSendingIntervalSeconds": 30,
  "failureOptionsSendingIntervalSeconds": 10,
  "failureThresholdCounter": 1,
  "successThresholdCounter": 1,
  "inviteFailureThresholdCounter": 1,
  "inviteFailureThresholdWindowSeconds": 30,
  "trunkGroupState": "Available",
  "pilotUserCallingLineAssertedIdentityPolicy": "Unscreened Originating Calls",
  "useSystemCallingLineAssertedIdentityPolicy": true,
  "totalActiveIncomingCalls": 0,
  "totalActiveOutgoingCalls": 0,
  "pilotUserCallOptimizationPolicy": "Optimize For User Services",
  "clidSourceForScreenedCallsPolicy": "Profile Name Profile Number",
  "useSystemCLIDSourceForScreenedCallsPolicy": true,
  "userLookupPolicy": "Basic",
  "useSystemUserLookupPolicy": true,
  "pilotUserCallingLineIdentityForEmergencyCallsPolicy": "No Calls",
  "serviceProviderId": "ent.odin",
  "groupId": "grp.odin",
  "name": "grp.odin.trunka",
  "users": []
}
```
