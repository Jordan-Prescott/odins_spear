---
description: api.get.user_by_id()
---

# 🆔 GET - User By ID

Returns extensive details of a single user including alias, enpoint device, and more common details like first and last name.

### Parameters&#x20;

* user\_id (str): Target user ID of the user you would like to review.

### Returns

* Dict: Python dictionary of the users details

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_by_id(
    "user_ID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "serviceProviderId": "ent.odin",
  "groupId": "grp.odin",
  "userId": "testdept@lab.tekvoice.net",
  "lastName": "dsd",
  "firstName": "dsd",
  "callingLineIdLastName": "dsd",
  "callingLineIdFirstName": "ddsdsd",
  "hiraganaLastName": "dsd",
  "hiraganaFirstName": "dsd",
  "phoneNumber": "5136549859",
  "extension": "9859",
  "callingLineIdPhoneNumber": "9871515000",
  "department": {
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "name": "mayur"
  },
  "departmentFullPath": "mayur (grp.odin)",
  "language": "English",
  "timeZone": "America/Denver",
  "timeZoneDisplayName": "(GMT-06:00) (US) Mountain Time",
  "defaultAlias": "testdept@lab.tekvoice.net",
  "accessDeviceEndpoint": {
    "accessDevice": {
      "deviceType": "BroadWorks Media Server",
      "protocol": "SIP 2.0",
      "numberOfPorts": {
        "unlimited": "true"
      },
      "numberOfAssignedPorts": 1,
      "status": "Online",
      "transportProtocol": "Unspecified",
      "useCustomUserNamePassword": false,
      "deviceName": "broadworks-media-server",
      "macAddress": "",
      "deviceLevel": "Group",
      "accessDeviceCredentials": {
        "userName": null
      },
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "tags": [],
      "relatedServices": []
    },
    "linePort": "testdept_lin1@lab.tekvoice.net",
    "staticRegistrationCapable": "true",
    "useDomain": "true",
    "supportVisualDeviceManagement": "true",
    "contacts": [
      {
        "sipContact": "sip1"
      },
      {
        "sipContact": "sip2"
      },
      {
        "sipContact": "sip3"
      },
      {
        "sipContact": "sip4"
      },
      {
        "sipContact": "sip5"
      }
    ]
  },
  "countryCode": "1",
  "networkClassOfService": "testncos1",
  "allowVideo": true,
  "domain": "lab.tekvoice.net",
  "endpointType": "accessDeviceEndpoint",
  "aliases": [],
  "trunkAddressing": {
    "trunkGroupDeviceEndpoint": {
      "contacts": []
    }
  },
  "isEnterprise": true,
  "passwordExpiresDays": 2147483647
}
```
