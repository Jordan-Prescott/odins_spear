---
description: api.post.user()
---

# 📮 POST - User

Creates a new user in the specified group with the configuration defined in the payload.

### Parameters&#x20;

* service_provider_id (str): Service provider ID where Group is loctaed.
* group_id (str): Group ID where new user will be built.
* user_id (str): Complete User ID including group domain of new user.
* first_name (str): First name of new user.
* last_name (str): Last name of new user.
* extension (str): Extension number of new user.
* web_auth_password (str): Web authentication password. Note get.password_generate() can be used to get this.
* payload (dict): User configuration.

### Returns

* Dict: New user entity.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_user_payload = {

}

my_api.post.user(
    "my_service_provider_id", 
    "my_group_id", 
    "john.smith@testdomain.net",
    "John", 
    "Smith",
    "1234", 
    "my_web_auth_password123!", 
    my_user_payload
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {"serviceProviderId": "my_service_provider_id", 
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
  "countryCode": "1", 
  "allowVideo": true, 
  "callingLineIdPhoneNumber": "", 
  "phoneNumber": "", 
  "domain": "testdomain.net", 
  "endpointType": "none", 
  "aliases": [], 
  "accessDeviceEndpoint": {
    "contacts": []
  },
  "trunkAddressing": {
    "trunkGroupDeviceEndpoint": {"contacts": []}
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
]

```
