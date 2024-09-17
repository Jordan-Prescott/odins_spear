---
description: my_api.get.bulk_call_forwarding_busy()
---

# 🚗 GET - Bulk Call Forward Busy

Retrieves the Forwarding Busy status for the specified User.

### Parameters&#x20;


* service_provider\_id (str): Target Service Provider where group is hosted
* group\_id (str): Target Group ID


### Returns

* Dict: Forwarding enabled status, and the Number to be Forwarded to.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.bulk_call_forwarding_busy{
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
      "serviceName": "Call Forwarding Busy"
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
      "isActive": false,
      "userId": "9709580001@domain.com"
    }
  },
  {
    "service": {
      "assigned": true,
      "serviceName": "Call Forwarding Busy"
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
      "isActive": false,
      "userId": "9709580002@domain.com"
    }
  }
]

```