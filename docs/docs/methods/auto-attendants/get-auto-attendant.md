---
description: my_api.get.auto_attendant()
---

#  🤙🏼 GET - Auto Attendant

Returns detailed information of a singel Auto Attendant.

### Parameters&#x20;

* service_user_id (str): User ID of target Auto Attendant.

### Returns

* dict: Detailed information of target Auto Attendant.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()


my_api.get.auto_attendant(
    service_user_id="auto_attendant_user_id"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "serviceInstanceProfile": {
    "name": "mock-aa-test-1",
    "callingLineIdLastName": "mock-aa-test-1",
    "callingLineIdFirstName": "mock-aa-test-1",
    "hiraganaLastName": "mock-aa-test-1",
    "hiraganaFirstName": "Auto Attendant",
    "language": "English",
    "timeZone": "America/Denver",
    "timeZoneDisplayName": "(GMT-06:00) (US) Mountain Time",
    "aliases": []
  },
  "type": "Basic",
  "enableVideo": false,
  "extensionDialingScope": "Group",
  "nameDialingScope": "Group",
  "nameDialingEntries": "LastName + FirstName",
  "businessHoursMenu": {
    "announcementSelection": "Default",
    "enableFirstMenuLevelExtensionDialing": false,
    "keys": [
      {
        "key": "0",
        "action": "Transfer To Operator",
        "description": null,
        "phoneNumber": null,
        "submenuId": null
      },
      {
        "key": "1",
        "action": "Extension Dialing",
        "description": null,
        "phoneNumber": null,
        "submenuId": null
      },
      {
        "key": "2",
        "action": "Name Dialing",
        "description": null,
        "phoneNumber": null,
        "submenuId": null
      }
    ]
  },
  "afterHoursMenu": {
    "announcementSelection": "Default",
    "enableFirstMenuLevelExtensionDialing": false,
    "keys": [
      {
        "key": "0",
        "action": "Transfer To Operator",
        "description": null,
        "phoneNumber": null,
        "submenuId": null
      },
      {
        "key": "1",
        "action": "Extension Dialing",
        "description": null,
        "phoneNumber": null,
        "submenuId": null
      },
      {
        "key": "2",
        "action": "Name Dialing",
        "description": null,
        "phoneNumber": null,
        "submenuId": null
      }
    ]
  },
  "serviceUserId": "mock-aa-test-1",
  "serviceProviderId": "odin.mock.ent1",
  "groupId": "odin.mock.grp1",
  "isEnterprise": true
}
```
