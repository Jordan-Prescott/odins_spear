---
description: api.put.user_group_id_update()
---
# 🤝 PUT - User Group ID Update

Moves the specified User to another Group under the same Enterprise.

### Parameters&#x20;

* user\_id (str): Target user ID of the user you would like to move
* new\_group\_id (str): Target Group ID you would like to move the user to
* evaluate\_only (bool): Runs without actually moving user, just provides error codes.

### Returns

* Dict: Information about the User, alongside the new updated group ID

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.user_group_id_update(
    "user_ID@userId.com",
    "userIdbutbetter@userId.com",
    False
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
    "serviceProviderId": "ServiceProv",
    "groupId": "GRPID",
    "userId": "ODINSPEARISAWESOME@thephones.com",
    "lastName": "John",
    "firstName": "Doe",
    "callingLineIdLastName": "John",
    "callingLineIdFirstName": "Doe",
    "hiraganaLastName": "John",
    "hiraganaFirstName": "Doe",
    "language": "English",
    "timeZone": "America/New_York",
    "timeZoneDisplayName": "(GMT-04:00) (US) Eastern Time",
    "defaultAlias": "odinspear@thephones.com",
    "countryCode": "1",
    "allowVideo": true,
    "callingLineIdPhoneNumber": "",
    "phoneNumber": "",
    "extension": "",
    "domain": "thephones.com",
    "endpointType": "none",
    "aliases": [],
    "accessDeviceEndpoint": {
        "contacts": []
    },
    "trunkAddressing": {
        "trunkGroupDeviceEndpoint": {
            "contacts": []
        }
    },
    "department": {
        "serviceProviderId": "",
        "groupId": "",
        "name": ""
    },
    "emailAddress": "",
    "nationalPrefix": "",
    "phoneNumberActivated": false,
    "isEnterprise": true,
    "passwordExpiresDays": "-2147483648"
}
```