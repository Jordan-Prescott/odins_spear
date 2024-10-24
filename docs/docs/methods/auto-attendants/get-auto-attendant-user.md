---
description: my_api.get.auto_attendant_user()
---

#  💁‍♀️ GET - Auto Attendant User

Returns detailed information about all Auto Attendants (AA) built in the same group as the specified user.

### Parameters&#x20;

* service_provider_id (str): Service Provider ID of the group where the user is built. 
* group_id (str): Group ID of the group where the user is built.
* user_id (str): User ID of the user being queried.
### Returns

* List: Returns a list of the AAs built in the group. 

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.auto_attendant_user(
    service_provider_id="my_service_provider_id",
    group_id="my_group_id", 
    user_id="test_user101@domain.net"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
  {
    "serviceUserId": "basic_aa@domain.com",
    "name": "basic aa",
    "video": False,
    "phoneNumber": None,
    "extension": "3001",
    "department": None,
    "isActive": True,
    "type": "Basic",
    "serviceInstanceProfile": {
      "name": "basic aa",
      "callingLineIdLastName": "aa",
      "callingLineIdFirstName": "basic",
      "hiraganaLastName": "basic aa",
      "hiraganaFirstName": "Auto Attendant",
      "extension": "3001",
      "language": "English",
      "timeZone": "Europe/London",
      "timeZoneDisplayName": "(GMT+01:00) Greenwich Mean Time",
      "aliases": []
    },
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
          "phoneNumber": "1001",
          "submenuId": None
        },
        {
          "key": "1",
          "action": "Transfer With Prompt",
          "description": None,
          "phoneNumber": "2001",
          "submenuId": None
        },
        {
          "key": "2",
          "action": "Transfer With Prompt",
          "description": None,
          "phoneNumber": "104",
          "submenuId": None
        },
        {
          "key": "3",
          "action": "Transfer Without Prompt",
          "description": None,
          "phoneNumber": "0123456789",
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
    }
  },
  {
    "serviceUserId": "odin_test@domain.com",
    "name": "Odin Test",
    "video": False,
    "phoneNumber": None,
    "extension": None,
    "department": None,
    "isActive": True,
    "type": "Standard",
    "serviceInstanceProfile": {
      "name": "Odin Test",
      "callingLineIdLastName": "Test",
      "callingLineIdFirstName": "Odin",
      "hiraganaLastName": "Odin Test",
      "hiraganaFirstName": "Auto Attendant",
      "language": "English",
      "timeZone": "Europe/London",
      "timeZoneDisplayName": "(GMT+01:00) Greenwich Mean Time",
      "aliases": []
    },
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
    }
  }
]

```
