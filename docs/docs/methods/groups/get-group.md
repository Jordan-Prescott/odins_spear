---
description: my_api.get.group()
---

# 🤝 GET - Group

Returns the specificied Group's settings and information

### Parameters&#x20;

* service_provider\_id (str): Target Service Provider ID
* group\_id (str): Target Group ID

### Returns

* Dict: Returns information about the specified group, such as the DID, userCount and Domain.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group{
     "serviceProviderId",
     "groupId"
}


```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "defaultDomain": "domain.com",
  "userLimit": 25,
  "userCount": 8,
  "groupName": "grp.test",
  "callingLineIdName": "test solutions",
  "callingLineIdPhoneNumber": "+12345678900",
  "callingLineIdDisplayPhoneNumber": 2345678900,
  "timeZone": "America/New_York",
  "timeZoneDisplayName": "(GMT-05:00) (US) Eastern Time",
  "locationDialingCode": 234,
  "contact": {
    "contactName": "test name",
    "contactNumber": "513-123-1234",
    "contactEmail": "testname@domain.com"
  },
  "serviceProviderId": "ent.test",
  "groupId": "grp.test"
}

```