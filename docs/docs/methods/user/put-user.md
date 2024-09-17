---
description: api.put.user()
---

# 👩‍💻 PUT - User

Updates specified User's options, such as extension, name and etc.

Note: Available options to change can be seen through: get.user_by_id()

### Parameters&#x20;

* service_provider_id (str): Target Service Provider where group is located
* group_id (str): Target Group ID where user is located
* user_id (str): Target User ID
* updates (dict): The updates to be applied to the list of Users e.g {"extension":"9999"}

### Returns

* Dict: Returns the changes made including User ID and updates.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.user(
    "my_service_provider",
    "my_group_id", 
    "john.smith@testdomain.net",
    {
    "address": {
        "addressLine1": "Bldg 1",
        "addressLine2": "Suite 2",
        "city": "Cincinnat",
        "stateOrProvince": "Ohio",
        "zipOrPostalCode": "45204",
        "country": "US"
    }
}
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {
    "serviceProviderId": "my_service_provider_id",
    "groupId": "my_group_id",
    "userId": "john.smith@testdomain.net",
    "lastName": "Smith",
    "firstName": "John",
    "callingLineIdLastName": "Smith",
    "callingLineIdFirstName": "John",
    "hiraganaLastName": "Smith",
    "hiraganaFirstName": "John",
    "extension": "1234",
    "language": "English",
    "timeZone": "Europe/London",
    "timeZoneDisplayName": "(GMT+01:00) Greenwich Mean Time",
    "defaultAlias": "john.smith@testdomain.net",
    "address": {
        "addressLine1": "Bldg 1",
        "addressLine2": "Suite 2",
        "city": "Cincinnat",
        "stateOrProvince": "Ohio",
        "zipOrPostalCode": "45204",
        "country": "US"
    },
    "countryCode": "1",
    "allowVideo": true,
    "callingLineIdPhoneNumber": "",
    "phoneNumber": "",
    "domain": "testdomain.net",
    "endpointType": "none",
    "aliases": ["11@testdomain.net"],
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
    "passwordExpiresDays": "-107"
}

]

```
