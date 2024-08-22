---
description: my_api.get.users_stats()
---

# 🧾 GET - User Call Stats

Pulls a single users call statistics for a specified period of time. 

### Parameters&#x20;

* user\_id (str): Target user ID you would like to pull call statistics for.
* start_date (str): Start date of desired time period. Date must follow format 'YYYY-MM-DD'
* end_date (str, optional): End date of desired time period. Date must follow format 'YYYY-MM-DD'.\
If this date is the same as Start date you do not need this parameter. Defaults to None.
* start_time (_type_, optional): Start time of desired time period. Time must follow formate 'HH:MM:SS'. \
If you do not need to filter by time and want the whole day leave this parameter. Defaults to "00:00:00". MAX Request is 3 months.
* end_time (_type_, optional): End time of desired time period. Time must follow formate 'HH:MM:SS'. \
If you do not need to filter by time and want the whole day leave this parameter. Defaults to "23:59:59". MAX Request is 3 months.
* time_zone (str, optional): A specified time you would like to see call records in. \
Time zone must follow format 'GMT', 'EST', 'PST'. Defaults to "Z" (UTC Time Zone).




### Returns

* Dict: Users call record statistics for specified time period.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.users_stats{
    "userIds",
    "startTime",
    "endTime"
}

```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "userId": null,
  "total": 0,
  "totalAnsweredAndMissed": null,
  "answeredTotal": null,
  "missedTotal": null,
  "busyTotal": null,
  "redirectTotal": null,
  "receivedTotal": null,
  "receivedMissed": null,
  "receivedAnswered": null,
  "placedTotal": null,
  "placedMissed": null,
  "placedAnswered": null
}

```