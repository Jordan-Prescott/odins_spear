---
description: my_api.get.group_call_center_forced_forwarding()
---

#  📞 GET - Group Call Center Forced Forwarding

Retrieves the forwarding number for a call center if it is set to forward calls, along with any associated audio messages.

### Parameters&#x20;

* service_user_id (str): Target Call Center ID

### Returns

* Dict: Number to be Forwarded to, alongside any Audio Messages.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_call_center_forced_forwarding(
    service_user_id="TestCallCenter@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "serviceUserId": "TestCallCenter@domain.com",
  "enabled": false,
  "forwardToPhoneNumber": null,
  "allowEnableViaFAC": true,
  "playAnnouncementBeforeForwarding": false,
  "audioMessageSource": "File",
  "videoMessageSource": "Default",
  "audioUrlList": [],
  "videoUrlList": [],
  "audioFileList": [
    {
      "name": "HandoverMusic.wav",
      "mediaType": "WAV",
      "level": "User"
    }
  ],
  "videoFileList": []
}
```
