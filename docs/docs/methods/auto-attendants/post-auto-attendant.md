---
description: my_api.post.auto_attendant()
---

#  ✍️ POST - Auto Attendant

Builds an Auto Attendant (AA) from the given payload.

### Parameters&#x20;

* service_provider_id (str): Service Provider ID of the group where the AA should be built.
* group_id (str): Group ID where the AA should be built.
* service_user_id (str): Service User ID of the AA (including the domain). 
* aa_name (str): Name of the AA
* aa_type (str, optional): Type of AA: "Basic" or "Standard". Will default to "Basic". NOTE: The "Auto Attendant - Standard" service must be enabled on the group in order for the aa_type to be set to "Standard".
* payload (dict, optional): Additional AA configuration data.

### Returns

* Dict: Returns the AA profile.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.post.auto_attendant(
    service_provider_id="my_service_provider_id",
    group_id="my_group_id", 
    service_user_id="test_user101@domain.net", 
    aa_name="Test AA" ,
    aa_type="Basic"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "serviceInstanceProfile": {
    "name": "Test AA",
    "callingLineIdLastName": "Test AA",
    "callingLineIdFirstName": "Test AA",
    "hiraganaLastName": "Test AA",
    "hiraganaFirstName": "Auto Attendant",
    "language": "English",
    "timeZone": "Europe/London",
    "timeZoneDisplayName": "(GMT+01:00) Greenwich Mean Time",
    "aliases": []
  },
  "type": "Basic",
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
  "serviceUserId": "test_user101@jrdneva.ev.com",
  "resellerId": None,
  "serviceProviderId": "TestLab",
  "groupId": "JRDNEVA",
  "isEnterprise": True
}


```
