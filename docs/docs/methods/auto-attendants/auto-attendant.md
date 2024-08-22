---
description: my_api.put.auto_attendant()
---

# 🍅 PUT - Auto Attendant

In this method, you can update your AAs&#x20;

### Parameters&#x20;

* service_provider_id (str): Service Provider ID where Group is hosted.
* group_id (str): Group ID where target Auto Attendant is located.
* auto_attendant_user_id (str): Target Auto Attendant User ID.
* updates (dict): Updates to be applied to Auto Attendant.

### Return

* Dict: Updated version of the Auto Attendant with updates applied. 

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_changes = {
    "serviceInstanceProfile": {
    "name": "Name of Auto Attendant",
    "callingLineIdLastName": "Auto Attendant",
    "callingLineIdFirstName": "Main",
    "hiraganaLastName": "mock-aa-test-1",
    "hiraganaFirstName": "Auto Attendant",
    "language": "English",
    "timeZone": "America/Denver",
    "timeZoneDisplayName": "(GMT-06:00) (US) Mountain Time",
    "aliases": []
  },
  "type": "Basic",
  "enableVideo": False,
  "extensionDialingScope": "Group",
  "nameDialingScope": "Group",
}

my_api.put.auto_attendant(
    service_provider_id="serviceProviderID",
    group_id="groupID"
    auto_attendant_user_id="AAUserID",
    updates=my_changes
)
```
{% endcode %}

#### Result:

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption><p>Basic AA updated to deactivated.</p></figcaption></figure>

