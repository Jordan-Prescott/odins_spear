---
description: my_api.get.group_dn_search()
---

# 2️⃣ GET - Group DN Search

Searches for numbers assigned to group and allows search criteria and limiting result.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where group is hosted.&#x20;
* group\_id (str): Group ID of target group where numbers are located.&#x20;
* dn (int): Number/ part of number to search for.
* filter\_type (str, optional): Options: equal to, starts with, or contains. Defaults to None. limit (int, optional): Limits the amount of values API returns. Defaults to None.

### Returns

* List: List of numbers matching search criteria

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_dn_search(
    "serviceProviderId",
    "groupID",
    dn= "01942",
    filter_type= "contains",
    limit= 10
)
```
{% endcode %}

### Example Returned Data (Formatted)

```json
[
  {
    "phoneNumbers": "+1-2345678900",
    "department": null,
    "activated": false,
    "userId": "group.paging2@parkbenchsolutions.com",
    "lastName": "group.paging2",
    "firstName": "Group Paging",
    "extension": "78900",
    "emailAddress": null,
    "userType": "Group Paging",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "group.paging2@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-2345678900",
      "max": "",
      "activated": false
    }
  },
  {
    "phoneNumbers": "+1-2345678905",
    "department": null,
    "activated": true,
    "userId": "huntgroup1@parkbenchsolutions.com",
    "lastName": "huntgroup1",
    "firstName": "Hunt Group",
    "extension": "",
    "emailAddress": null,
    "userType": "Hunt Group",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "huntgroup1@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-2345678905",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-5132224003",
    "department": null,
    "activated": false,
    "userId": "aavis1@parkbenchsolutions.com",
    "lastName": "aavis1",
    "firstName": "Auto Attendant",
    "extension": "24003",
    "emailAddress": null,
    "userType": "Auto Attendant",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "aavis1@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-5132224003",
      "max": "",
      "activated": false
    }
  },
  {
    "phoneNumbers": "+1-5134004003",
    "department": null,
    "activated": true,
    "userId": "6106424235X4020@parkbenchsolutions.com",
    "lastName": 4003,
    "firstName": 4003,
    "extension": "04003",
    "emailAddress": "developer@parkbenchsolutions.com",
    "userType": "Normal",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "6106424235X4020@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-5134004003",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-5135564000",
    "department": null,
    "activated": true,
    "userId": "5135564000@parkbenchsolutions.com",
    "lastName": "Demo user",
    "firstName": "Marc",
    "extension": "64000",
    "emailAddress": null,
    "userType": "Normal",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "5135564000@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-5135564000",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-8135551001",
    "department": null,
    "activated": true,
    "userId": "flexible1@parkbenchsolutions.com",
    "lastName": "flexible1",
    "firstName": "Flexible Seating Host",
    "extension": "51001",
    "emailAddress": null,
    "userType": "Flexible Seating Host",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "flexible1@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-8135551001",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-8135551002",
    "department": null,
    "activated": true,
    "userId": "4001@parkbenchsolutions.com",
    "lastName": 4001,
    "firstName": 4001,
    "extension": "51401",
    "emailAddress": "developer@parkbenchsolutions.com",
    "userType": "Normal",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "4001@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-8135551002",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-8135551006 - +1-8135551008",
    "department": null,
    "activated": true,
    "userId": "huntgroup1@parkbenchsolutions.com",
    "lastName": "huntgroup1",
    "firstName": "Hunt Group",
    "extension": "",
    "emailAddress": null,
    "userType": "Hunt Group",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "huntgroup1@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-8135551006",
      "max": "+1-8135551008",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-8595551020",
    "department": null,
    "activated": true,
    "userId": "aatest1@parkbenchsolutions.com",
    "lastName": "aatest11",
    "firstName": "Auto Attendant",
    "extension": "51020",
    "emailAddress": null,
    "userType": "Auto Attendant",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "aatest1@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-8595551020",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-8595551024",
    "department": null,
    "activated": true,
    "userId": "group.paging1@parkbenchsolutions.com",
    "lastName": "group.paging1",
    "firstName": "Group Paging",
    "extension": "51024",
    "emailAddress": null,
    "userType": "Group Paging",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "group.paging1@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-8595551024",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-8595551401",
    "department": null,
    "activated": true,
    "userId": "4001@parkbenchsolutions.com",
    "lastName": 4001,
    "firstName": 4001,
    "extension": "51401",
    "emailAddress": "developer@parkbenchsolutions.com",
    "userType": "Normal",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "4001@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-8595551401",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-8595551402",
    "department": null,
    "activated": true,
    "userId": "flexible2@parkbenchsolutions.com",
    "lastName": "flexible2",
    "firstName": "Flexible Seating Host",
    "extension": "51402",
    "emailAddress": null,
    "userType": "Flexible Seating Host",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userIdShort": "flexible2@parkbenchsolutions.com",
    "domain": "parkbenchsolutions.com",
    "dns": {
      "min": "+1-8595551402",
      "max": "",
      "activated": true
    }
  }
]
```
