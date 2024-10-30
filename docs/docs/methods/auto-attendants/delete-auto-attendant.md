---
description: my_api.delete.auto_attendant()
---

#  🚮 DELETE - Auto Attendant

Removes an Auto Attendant (AA) from a group. 

### Parameters&#x20;

* service_user_id(str): The service user ID of the AA to be deleted.

### Returns

* Dict: Returns the profile of the deleted AA.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.delete.auto_attendant(
    service_user_id="test_aa@domain.net"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "serviceInstanceProfile": {
    "name": "Test AA",
    "callingLineIdLastName": "AA",
    "callingLineIdFirstName": "Test",
    "hiraganaLastName": "AA",
    "hiraganaFirstName": "Test",
    "language": "English",
    "timeZone": "Europe/London",
    "timeZoneDisplayName": "(GMT) Greenwich Mean Time",
    "aliases": []
  },
  "type": "Standard",
  "firstDigitTimeoutSeconds": 1,
  "enableVideo": False,
  "extensionDialingScope": "Group",
  "nameDialingScope": "Group",
  "nameDialingEntries": "LastName + FirstName",
  "businessHoursMenu": {
    "announcementSelection": "Default",
    "enableFirstMenuLevelExtensionDialing": False,
    "keys": [
      {
        "key": "0",
        "action": "Transfer To Operator",
        "description": None,
        "phoneNumber": None,
        "submenuId": None
      },
      {
        "key": "1",
        "action": "Extension Dialing",
        "description": None,
        "phoneNumber": None,
        "submenuId": None
      },
      {
        "key": "2",
        "action": "Name Dialing",
        "description": None,
        "phoneNumber": None,
        "submenuId": None
      }
    ]
  },
  "afterHoursMenu": {
    "announcementSelection": "Default",
    "enableFirstMenuLevelExtensionDialing": False,
    "keys": [
      {
        "key": "0",
        "action": "Transfer To Operator",
        "description": None,
        "phoneNumber": None,
        "submenuId": None
      },
      {
        "key": "1",
        "action": "Extension Dialing",
        "description": None,
        "phoneNumber": None,
        "submenuId": None
      },
      {
        "key": "2",
        "action": "Name Dialing",
        "description": None,
        "phoneNumber": None,
        "submenuId": None
      }
    ]
  },
  "holidayMenu": {
    "announcementSelection": "Default",
    "enableFirstMenuLevelExtensionDialing": False,
    "keys": [
      {
        "key": "0",
        "action": "Transfer To Operator",
        "description": None,
        "phoneNumber": None,
        "submenuId": None
      },
      {
        "key": "1",
        "action": "Extension Dialing",
        "description": None,
        "phoneNumber": None,
        "submenuId": None
      },
      {
        "key": "2",
        "action": "Name Dialing",
        "description": None,
        "phoneNumber": None,
        "submenuId": None
      }
    ]
  },
  "serviceUserId": "test_aa@domain.net",
  "resellerId": None,
  "serviceProviderId": "my_service_provider_id",
  "groupId": "my_group_id",
  "isEnterprise": True
}


```
