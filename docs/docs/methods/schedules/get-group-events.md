---
description: my_api.get.group_events()
---

# 📅 GET - Group Events

Retrieves the Business Schedule's Events for the specified group.

### Parameters&#x20;

* service\_provider\_id (str): Target Service Provider ID
* group\_id (str): Target Group ID
* name (str): Name of the target Busisness Schedule
* type (str): The type of the Business Schedule (Time, Holiday)

### Returns

* List: List of each Business Schedule Event, including startTime and endTime.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_events(
    "serviceProviderID",
    "groupID",
    "eventName",
    "Holiday"
)
```
{% endcode %}

### Example Response (Formatted)

```json
[
  {
    "eventName": "Test / Event",
    "startTime": "2018-09-15T00:00:00",
    "endTime": "2018-09-16T00:00:00",
    "allDayEvent": true,
    "name": "Test1234",
    "type": "Holiday",
    "serviceProviderId": "serviceProvider",
    "groupId": "groupID",
    "rrule": "DTSTART:20180915T040000Z\nRRULE:FREQ=DAILY"
  }
]
```
