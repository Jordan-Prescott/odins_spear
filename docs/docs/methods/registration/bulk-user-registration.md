---
description: my_api.get.bulk_user_registration()
---

# 💚 GET - Bulk User Registration

Gets all users in a group and their device registrations. This includes soft phones.

{% hint style="info" %}
If a users registrations is an empty list this means the user currently has no active registrations.
{% endhint %}

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise ID where Group is hosted.&#x20;
* group\_id (str): Target Group ID where users are located.

### Returns

* dict: All users devices and details on device such as registration.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.bulk_user_registration(
    "serviceProviderID",
    "groupID"
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "serviceProviderId": "LabEnterprise",
  "groupId": "regression.test",
  "users": [
    {
      "profile": {
        "userId": "test.user1@alliedtelecom.net",
        "lastName": "User 1",
        "firstName": "Test",
        "department": "Bandwidth.com (regression.test)",
        "phoneNumber": "+1-2026951172",
        "phoneNumberActivated": true,
        "emailAddress": null,
        "hiraganaLastName": "User 1",
        "hiraganaFirstName": "Test",
        "inTrunkGroup": false,
        "extension": "2639",
        "countryCode": 1,
        "nationalPrefix": null,
        "domain": "alliedtelecom.net"
      },
      "data": {
        "registrations": [
          {
            "deviceLevel": "Group",
            "deviceName": "ECG_0004f2accaf7",
            "order": 1,
            "uRI": "sip:2026951172@10.2.2.45:5060;transport=udp;jtr=22-1808",
            "expiration": "Thu May 23 08:33:00 EDT 2019",
            "line/Port": "2026951172@alliedtelecom.net",
            "endpointType": "Primary",
            "publicNetAddress": null,
            "publicPort": null,
            "privateNetAddress": null,
            "privatePort": null,
            "userAgent": "Polycom/5.4.1.14510 PolycomVVX-VVX_500-UA/5.4.1.14510",
            "lockoutStarted": null,
            "lockoutExpires": null,
            "lockoutCount": 0,
            "accessInfo": null
          }
        ],
        "userId": "test.user1@alliedtelecom.net"
      }
    },
    {
      "profile": {
        "userId": "test.user3@alliedtelecom.net",
        "lastName": "User 3",
        "firstName": "Test",
        "department": "Level3 (regression.test)",
        "phoneNumber": "+1-3092650759",
        "phoneNumberActivated": true,
        "emailAddress": null,
        "hiraganaLastName": "User 3",
        "hiraganaFirstName": "Test",
        "inTrunkGroup": false,
        "extension": "2437",
        "countryCode": 1,
        "nationalPrefix": null,
        "domain": "alliedtelecom.net"
      },
      "data": {
        "registrations": [
          {
            "deviceLevel": "Group",
            "deviceName": "ECG-0004F289F5AC",
            "order": 1,
            "uRI": "sip:2022662437@10.2.2.45:5060;transport=udp;jtr=57-2417",
            "expiration": "Thu May 23 08:34:03 EDT 2019",
            "line/Port": "2022662437@alliedtelecom.net",
            "endpointType": "Primary",
            "publicNetAddress": null,
            "publicPort": null,
            "privateNetAddress": null,
            "privatePort": null,
            "userAgent": "PolycomVVX-VVX_310-UA/5.6.2.1593",
            "lockoutStarted": null,
            "lockoutExpires": null,
            "lockoutCount": 0,
            "accessInfo": null
          }
        ],
        "userId": "test.user3@alliedtelecom.net"
      }
    },
    {
      "profile": {
        "userId": "gs.test@alliedtelecom.net",
        "lastName": "Test",
        "firstName": "GS",
        "department": null,
        "phoneNumber": "",
        "phoneNumberActivated": null,
        "emailAddress": null,
        "hiraganaLastName": "Test",
        "hiraganaFirstName": "GS",
        "inTrunkGroup": false,
        "extension": "2456",
        "countryCode": null,
        "nationalPrefix": null,
        "domain": "alliedtelecom.net"
      },
      "data": {
        "registrations": [],
        "userId": "gs.test@alliedtelecom.net"
      }
    },
    {
      "profile": {
        "userId": "test.user2@alliedtelecom.net",
        "lastName": "User 2",
        "firstName": "Test",
        "department": "Telnyx (regression.test)",
        "phoneNumber": "+1-2023478048",
        "phoneNumberActivated": true,
        "emailAddress": null,
        "hiraganaLastName": "User 2",
        "hiraganaFirstName": "Test",
        "inTrunkGroup": false,
        "extension": "6866",
        "countryCode": 1,
        "nationalPrefix": null,
        "domain": "alliedtelecom.net"
      },
      "data": {
        "registrations": [
          {
            "deviceLevel": "Group",
            "deviceName": "ECG-0004f283b2f5",
            "order": 1,
            "uRI": "sip:2023478048@10.2.2.45:5060;transport=udp;jtr=6-147",
            "expiration": "Thu May 23 08:30:12 EDT 2019",
            "line/Port": "2023478048@alliedtelecom.net",
            "endpointType": "Primary",
            "publicNetAddress": null,
            "publicPort": null,
            "privateNetAddress": null,
            "privatePort": null,
            "userAgent": "Polycom/5.4.1.14510 PolycomVVX-VVX_500-UA/5.4.1.14510",
            "lockoutStarted": null,
            "lockoutExpires": null,
            "lockoutCount": 0,
            "accessInfo": null
          }
        ],
        "userId": "test.user2@alliedtelecom.net"
      }
    },
    {
      "profile": {
        "userId": "This.Is.A.Test.User@alliedtelecom.net",
        "lastName": "User",
        "firstName": "PB.Test",
        "department": null,
        "phoneNumber": "",
        "phoneNumberActivated": null,
        "emailAddress": null,
        "hiraganaLastName": "User",
        "hiraganaFirstName": "PB.Test",
        "inTrunkGroup": false,
        "extension": "",
        "countryCode": null,
        "nationalPrefix": null,
        "domain": "alliedtelecom.net"
      },
      "data": {
        "registrations": [],
        "userId": "This.Is.A.Test.User@alliedtelecom.net"
      }
    },
    {
      "profile": {
        "userId": "Another.Test.User.From.XSP@alliedtelecom.net",
        "lastName": "XSP.Test",
        "firstName": "PB.User.XSP",
        "department": null,
        "phoneNumber": "",
        "phoneNumberActivated": null,
        "emailAddress": null,
        "hiraganaLastName": "XSP.Test",
        "hiraganaFirstName": "PB.User.XSP",
        "inTrunkGroup": false,
        "extension": "",
        "countryCode": null,
        "nationalPrefix": null,
        "domain": "alliedtelecom.net"
      },
      "data": {
        "registrations": [],
        "userId": "Another.Test.User.From.XSP@alliedtelecom.net"
      }
    },
    {
      "profile": {
        "userId": "CLi.Test.User@alliedtelecom.net",
        "lastName": "CLi.Test.User",
        "firstName": "CLi.Test.User",
        "department": null,
        "phoneNumber": "",
        "phoneNumberActivated": null,
        "emailAddress": null,
        "hiraganaLastName": "CLi.Test.User",
        "hiraganaFirstName": "CLi.Test.User",
        "inTrunkGroup": false,
        "extension": "",
        "countryCode": null,
        "nationalPrefix": null,
        "domain": "alliedtelecom.net"
      },
      "data": {
        "registrations": [],
        "userId": "CLi.Test.User@alliedtelecom.net"
      }
    },
    {
      "profile": {
        "userId": "kallani@alliedtelecom.net",
        "lastName": "Allani",
        "firstName": "Karim",
        "department": null,
        "phoneNumber": "+1-2025551234",
        "phoneNumberActivated": false,
        "emailAddress": "kallani@alliedtelecom.net",
        "hiraganaLastName": "Allani",
        "hiraganaFirstName": "Karim",
        "inTrunkGroup": false,
        "extension": "234",
        "countryCode": 1,
        "nationalPrefix": null,
        "domain": "alliedtelecom.net"
      },
      "data": {
        "registrations": [],
        "userId": "kallani@alliedtelecom.net"
      }
    }
  ]
}
```
