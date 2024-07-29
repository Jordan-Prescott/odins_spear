---
description: my_api.get.bulk_call_forwarding_no_answer()
---

# 🚗 GET - Bulk Call Forward No Answer

Retrieves the Forwarding No Answer status for all users within a specified group

### Parameters&#x20;

* service_provider\_id (str): Target Service Provider where group is hosted
* group\_id (str): Target Group ID

### Returns

* List: Forwarding enabled status, the Number to be Forwarded to, and User information.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.bulk_call_forwarding_no_answer{
    "serviceProviderId",
    "groupId"
}


```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {
    "service": {
      "assigned": true,
      "serviceName": "Call Forwarding No Answer"
    },
    "user": {
      "userId": "9709580001@domain.com",
      "lastName": "Mock1",
      "firstName": "Mock1",
      "department": "test Mock Dept (test.mock.grp1)",
      "phoneNumber": "+1-9709580001",
      "phoneNumberActivated": true,
      "emailAddress": null,
      "hiraganaLastName": "Mock1",
      "hiraganaFirstName": "Mock1",
      "inTrunkGroup": false,
      "extension": "0001",
      "domain": "domain.com"
    },
    "data": {
      "isActive": true,
      "forwardToPhoneNumber": 5133334444,
      "numberOfRings": 4,
      "userId": "9709580001@domain.com"
    }
  },
  {
    "service": {
      "assigned": true,
      "serviceName": "Call Forwarding No Answer"
    },
    "user": {
      "userId": "9709580002@domain.com",
      "lastName": "User2last",
      "firstName": "User2first",
      "department": "test Mock Dept (test.mock.grp1)",
      "phoneNumber": "+1-9709580002",
      "phoneNumberActivated": true,
      "emailAddress": null,
      "hiraganaLastName": "User2last",
      "hiraganaFirstName": "User2first",
      "inTrunkGroup": false,
      "extension": "0002",
      "domain": "domain.com"
    },
    "data": {
      "isActive": true,
      "forwardToPhoneNumber": 5133334444,
      "numberOfRings": 4,
      "userId": "9709580002@domain.com"
    }
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Call Forwarding No Answer"
    },
    "user": {
      "userId": "9709580003@domain.com",
      "lastName": "User3last",
      "firstName": "User3first",
      "department": "test Mock Dept (test.mock.grp1)",
      "phoneNumber": "+1-9709580003",
      "phoneNumberActivated": true,
      "emailAddress": null,
      "hiraganaLastName": "User3last",
      "hiraganaFirstName": "User3first",
      "inTrunkGroup": false,
      "extension": "0003",
      "domain": "domain.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Call Forwarding No Answer"
    },
    "user": {
      "userId": "9709580004@domain.com",
      "lastName": "User4last",
      "firstName": "User4first",
      "department": "test Mock Dept (test.mock.grp1)",
      "phoneNumber": "+1-9709580004",
      "phoneNumberActivated": true,
      "emailAddress": null,
      "hiraganaLastName": "User4last",
      "hiraganaFirstName": "User4first",
      "inTrunkGroup": false,
      "extension": "0004",
      "domain": "domain.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Call Forwarding No Answer"
    },
    "user": {
      "userId": "9709580005@domain",
      "lastName": "User5last",
      "firstName": "User5first",
      "department": "test Mock Dept (test.mock.grp1)",
      "phoneNumber": "+1-9709580005",
      "phoneNumberActivated": true,
      "emailAddress": null,
      "hiraganaLastName": "User5last",
      "hiraganaFirstName": "User5first",
      "inTrunkGroup": false,
      "extension": "0005",
      "domain": "domain.com"
    },
    "data": {}
  }
]
```