---
description: my_api.get.user_call_forwarding_selective_criteria()
---

# 🚗 GET - Call Forward selective criteria

Retrieves the Forwarding Selective status for a specified User, alongside the criteria's assigned.

### Parameters&#x20;

* user\_id (str): Target User ID
* criteria_name (str): Target Criteria Name


### Returns

* Dict: Forwarding enabled status and the specified Criterias Settings.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_call_forwarding_selective_criteria{
    "criteriaName",
    "userId"
}


```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "forwardToNumberSelection": "Forward To Default Number",
  "fromDnCriteria": {
    "fromDnCriteriaSelection": "Any",
    "includeAnonymousCallers": "false",
    "includeUnavailableCallers": "false",
    "phoneNumbers": []
  },
  "userId": "test-mock/aa1",
  "criteriaName": "Test123"
}

```