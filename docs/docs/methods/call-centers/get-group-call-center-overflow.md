---
description: my_api.get.group_call_center_overflow()
---

#  📞 GET - Group Call Center Overflow

Retrieves the forwarding number for a user when all call center agents are busy, along with any associated audio messages.

### Parameters&#x20;

* service_user_id (str): Target Call Center ID

### Returns

* Dict: Call Centers overflow configuration.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_call_center_overflow(
    service_user_id="TestCallCenter@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "serviceUserId": "TTestCallCenter@domain.com",
  "action": "Busy",
  "transferPhoneNumber": null,
  "overflowAfterTimeout": true,
  "timeoutSeconds": 30,
  "playAnnouncementBeforeOverflowProcessing": true,
  "audioMessageSource": "Default",
  "videoMessageSource": "Default",
  "audioUrlList": [],
  "videoUrlList": [],
  "audioFileList": [],
  "videoFileList": []
}
```
