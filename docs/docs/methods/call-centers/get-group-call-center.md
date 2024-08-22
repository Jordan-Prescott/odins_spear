---
description: my_api.get.group_call_center()
---

#  🎧 GET - Group Call Center

Retrieves deatiled information on a single Call Center.

### Parameters&#x20;

* service_user_id (str): Target Call Center's ID

### Returns

* Dict: Target Call Centers details.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_call_center(
    service_user_id="myCallCenterUserID"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "serviceInstanceProfile": {
    "name": "TestCallCenter",
    "callingLineIdLastName": "TestCallCenter",
    "callingLineIdFirstName": "TestCallCenter",
    "hiraganaLastName": "TestCallCenter",
    "hiraganaFirstName": "Call Center",
    "language": "English",
    "timeZone": "America/Denver",
    "timeZoneDisplayName": "(GMT-06:00) (US) Mountain Time"
  },
  "type": "Premium",
  "routingType": "Priority Based",
  "policy": "Circular",
  "enableVideo": false,
  "queueLength": 3,
  "enableReporting": false,
  "allowCallerToDialEscapeDigit": false,
  "escapeDigit": 3,
  "resetCallStatisticsUponEntryInQueue": true,
  "allowAgentLogoff": true,
  "allowCallWaitingForAgents": true,
  "allowCallsToAgentsInWrapUp": true,
  "overrideAgentWrapUpTime": false,
  "forceDeliveryOfCalls": false,
  "enableAutomaticStateChangeForAgents": false,
  "externalPreferredAudioCodec": "None",
  "internalPreferredAudioCodec": "None",
  "playRingingWhenOfferingCall": true,
  "callCenterQueueThresholdsIsActive": false,
  "serviceUserId": "TestCallCenter"
}
```
