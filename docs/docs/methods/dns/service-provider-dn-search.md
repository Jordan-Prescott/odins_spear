---
description: my_api.get.service_provider_dn_search()
---

# 5️⃣ GET - Service Provider DN Search

Searches for numbers assigned to Service Provider/ Enterprise and allows search criteria and limiting result.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where group is hosted.&#x20;
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

my_api.get.service_provider_dn_search(
    "serviceProviderId",
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
    "phoneNumbers": "+1-9589582000",
    "department": null,
    "activated": true,
    "userId": "9589582000@as3.xdp.broadsoft.com",
    "lastName": "mock-2000",
    "firstName": "mock-2000",
    "extension": "2000",
    "emailAddress": null,
    "userType": "Normal",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "odin.mock.ent1",
    "groupId": "odin.mock.grp1",
    "userIdShort": "9589582000",
    "domain": "as3.xdp.broadsoft.com",
    "dns": {
      "min": "+1-9589582000",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-9589582001",
    "department": null,
    "activated": true,
    "userId": "9589582001@as3.xdp.broadsoft.com",
    "lastName": "mock-2001",
    "firstName": "mock-2001",
    "extension": "2001",
    "emailAddress": null,
    "userType": "Normal",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "odin.mock.ent1",
    "groupId": "odin.mock.grp1",
    "userIdShort": "9589582001",
    "domain": "as3.xdp.broadsoft.com",
    "dns": {
      "min": "+1-9589582001",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-9589582002",
    "department": null,
    "activated": true,
    "userId": "9589582002@as3.xdp.broadsoft.com",
    "lastName": "mock-2002",
    "firstName": "mock-2002",
    "extension": "2002",
    "emailAddress": null,
    "userType": "Normal",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "odin.mock.ent1",
    "groupId": "odin.mock.grp1",
    "userIdShort": "9589582002",
    "domain": "as3.xdp.broadsoft.com",
    "dns": {
      "min": "+1-9589582002",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-9589582003",
    "department": null,
    "activated": true,
    "userId": "9589582003@as3.xdp.broadsoft.com",
    "lastName": "mock-2003",
    "firstName": "mock-2003",
    "extension": "2003",
    "emailAddress": null,
    "userType": "Normal",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "odin.mock.ent1",
    "groupId": "odin.mock.grp1",
    "userIdShort": "9589582003",
    "domain": "as3.xdp.broadsoft.com",
    "dns": {
      "min": "+1-9589582003",
      "max": "",
      "activated": true
    }
  },
  {
    "phoneNumbers": "+1-9589582004",
    "department": null,
    "activated": true,
    "userId": "9589582004@as3.xdp.broadsoft.com",
    "lastName": "mock-2004",
    "firstName": "mock-2004",
    "extension": "2004",
    "emailAddress": null,
    "userType": "Normal",
    "countryCode": 1,
    "nationalPrefix": null,
    "serviceProviderId": "odin.mock.ent1",
    "groupId": "odin.mock.grp1",
    "userIdShort": "9589582004",
    "domain": "as3.xdp.broadsoft.com",
    "dns": {
      "min": "+1-9589582004",
      "max": "",
      "activated": true
    }
  }
]
```
