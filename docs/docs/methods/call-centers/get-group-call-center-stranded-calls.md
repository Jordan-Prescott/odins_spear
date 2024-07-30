---
description: my_api.get.group_call_center_stranded_calls()
---

# 🆘 GET - Group Call Center Stranded Calls

Retrieves the forwarding number for a user when a call center doesn't answer, along with any associated audio messages.

### Parameters&#x20;

* service_user_id (str): Target Call Center ID

### Returns

* Dict: Call Centers stranded call configuration.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.group_call_center_stranded_calls(
    service_user_id="TestCallCenter@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "serviceUserId": "TestCallCenter@domain.com",
  "action": "None",
  "transferPhoneNumber": null,
  "audioMessageSource": "File",
  "videoMessageSource": "Default",
  "audioUrlList": [],
  "videoUrlList": [],
  "audioFileList": [
    {
      "name": "StrandedCallAudio.wav",
      "mediaType": "WAV",
      "level": "User"
    }
  ],
  "videoFileList": []
}
```
