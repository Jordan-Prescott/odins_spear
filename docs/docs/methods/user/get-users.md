---
description: api.get.users()
---

# 👯 GET - Users

Returns list of users depending on filter criteria you set. See supported filters and filter examples on how to use.&#x20;

### Parameters&#x20;

* service\_provider\_id (str, optional): Service or Enterprise ID, top level object. Defaults to None.
* group\_id (str, optional): Group ID where user is hosted. Defaults to None.&#x20;
* filter (str, optional): Filter criteria, supported filters below. Defaults to None.&#x20;
* filter\_type (str, optional): Options: equal to, starts with, or contains. Defaults to None.&#x20;
* filter\_value (str, optional): Value filtering on e.g. firstName. Defaults to None.&#x20;
* limit (int, optional): Limits the amount of values API returns. Defaults to None.

### Returns

* Dict: Python dictionary of the users details

## Supported Filters

* macAddress: search by device&#x20;
* lastName: filter by lastName&#x20;
* firstName: filter by firstName&#x20;
* dn: filter by dn&#x20;
* emailAddress: filter by emailAddress&#x20;
* userId: filter by userId&#x20;
* extension: filter by extension

### Examples:

#### Get all users in Enterprise ent1

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.users(
    servive_provider_id= "ent1"
)
```

#### Get all users in Group grp1&#x20;

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.users(
    servive_provider_id= "ent1",
    group_id= "grp1"
)
```

#### Get up to 10 users in the system wit a last name that contains Smith

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.users(
    filter= "lastName",
    filter_type= "contains",
    filter_value= "Smith",
    limit= 10
)
```

#### Get the users in grp1 that have a phone number that starts with 513333

<pre class="language-python"><code class="lang-python">from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.users(
<strong>    servive_provider_id= "ent1",
</strong>    group_id= "grp1",    
    filter= "dn",
    filter_type= "contains",
    filter_value= "513333"
)
</code></pre>



### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_by_id(
    "user_ID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userId": "5136549857_s@odinapi.net",
    "lastName": 1,
    "firstName": "user_",
    "callingLineIdLastName": 1,
    "callingLineIdFirstName": "Marc",
    "hiraganaLastName": 1,
    "hiraganaFirstName": "user_",
    "phoneNumber": "5136549857",
    "extension": "9857",
    "callingLineIdPhoneNumber": "5136549857",
    "language": "English",
    "timeZone": "America/New_York",
    "timeZoneDisplayName": "(GMT-05:00) (US) Eastern Time",
    "defaultAlias": "5136549857_s@odinapi.net",
    "accessDeviceEndpoint": {
      "accessDevice": {
        "deviceType": "Polycom VVX 400 DM",
        "protocol": "SIP 2.0",
        "numberOfPorts": {
          "quantity": "12"
        },
        "numberOfAssignedPorts": 1,
        "status": "Online",
        "configurationMode": "Default",
        "transportProtocol": "TCP",
        "useCustomUserNamePassword": false,
        "deviceName": "5136549857",
        "deviceLevel": "Group",
        "accessDeviceCredentials": {
          "userName": null
        },
        "serviceProviderId": "ent.odin",
        "groupId": "grp.odin",
        "tags": [],
        "relatedServices": []
      },
      "linePort": "5136549857_s@odinapi.net",
      "staticRegistrationCapable": "false",
      "useDomain": "true",
      "supportVisualDeviceManagement": "false",
      "contacts": []
    },
    "countryCode": "1",
    "allowVideo": true,
    "domain": "odinapi.net",
    "endpointType": "accessDeviceEndpoint",
    "aliases": [],
    "trunkAddressing": {
      "trunkGroupDeviceEndpoint": {
        "contacts": []
      }
    },
    "isEnterprise": true,
    "passwordExpiresDays": "-2147483648"
  },
  {
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userId": "9871515000@odinapi.net",
    "lastName": "Reverman",
    "firstName": "Mark",
    "callingLineIdLastName": "Reverman",
    "callingLineIdFirstName": "Mark",
    "hiraganaLastName": "Reverman",
    "hiraganaFirstName": "Mark",
    "phoneNumber": "9871515000",
    "extension": "5000",
    "callingLineIdPhoneNumber": "9871515000",
    "department": {
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "name": "department1"
    },
    "departmentFullPath": "department1 (grp.odin)",
    "language": "English",
    "timeZone": "America/New_York",
    "timeZoneDisplayName": "(GMT-05:00) (US) Eastern Time",
    "defaultAlias": "9871515000@odinapi.net",
    "trunkAddressing": {
      "trunkGroupDeviceEndpoint": {
        "name": "9871515000",
        "linePort": "9871515000_trunk@odinapi.net",
        "staticRegistrationCapable": "true",
        "useDomain": "true",
        "isPilotUser": "false",
        "contacts": []
      }
    },
    "title": "Title Here",
    "pagerPhoneNumber": 9871515000,
    "mobilePhoneNumber": 9871515000,
    "emailAddress": "mreverman@parkbenchsolutions.com",
    "addressLocation": "1234 Main Street",
    "address": {
      "addressLine1": "Bldg 2",
      "addressLine2": "Suite 2",
      "city": "Cincinnati",
      "stateOrProvince": "Ohio",
      "zipOrPostalCode": "45204",
      "country": "US"
    },
    "countryCode": "1",
    "alternateUserId": [
      {
        "alternateUserId": "mreverman@gmail.com",
        "description": "mreverman@gmail.com"
      },
      {
        "alternateUserId": "mreverman@parkbenchsolutions.com",
        "description": "mreverman@parkbenchsolutions.com"
      }
    ],
    "allowVideo": true,
    "domain": "odinapi.net",
    "endpointType": "trunkAddressing",
    "aliases": [],
    "accessDeviceEndpoint": {
      "contacts": []
    },
    "isEnterprise": true,
    "passwordExpiresDays": 2147483647
  },
  {
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "userId": "9871515001@odinapi.net",
    "lastName": "Latsa",
    "firstName": "Scott",
    "callingLineIdLastName": "Latsa",
    "callingLineIdFirstName": "Scott",
    "hiraganaLastName": "Latsa",
    "hiraganaFirstName": "Scott",
    "phoneNumber": "9871515001",
    "extension": "5001",
    "callingLineIdPhoneNumber": "+19871514002",
    "language": "English",
    "timeZone": "America/New_York",
    "timeZoneDisplayName": "(GMT-05:00) (US) Eastern Time",
    "defaultAlias": "9871515001@odinapi.net",
    "accessDeviceEndpoint": {
      "accessDevice": {
        "deviceType": "Generic SIP Phone",
        "protocol": "SIP 2.0",
        "numberOfPorts": {
          "unlimited": "true"
        },
        "numberOfAssignedPorts": 1,
        "status": "Online",
        "transportProtocol": "Unspecified",
        "useCustomUserNamePassword": false,
        "version": "Kapanga Softphone Desktop Windows 1.00/2180b+1595505876_80E82C997FFA_A0510BEA6293_02004C4F4F50_005056C00001_005056C00008_0A002700000E_FABBC859EAB4_A0510BEA6290_A2510BEA628F",
        "deviceName": "generic_sip",
        "deviceLevel": "Group",
        "accessDeviceCredentials": {
          "userName": null
        },
        "serviceProviderId": "ent.odin",
        "groupId": "grp.odin",
        "tags": [],
        "relatedServices": []
      },
      "linePort": "9871515001@odinapi.net",
      "staticRegistrationCapable": "true",
      "useDomain": "true",
      "supportVisualDeviceManagement": "false",
      "contacts": []
    },
    "emailAddress": "slatsa@parkbenchsolutions.com",
    "countryCode": "1",
    "alternateUserId": {
      "alternateUserId": "scott.latsa@gmail.com",
      "description": "Test gamil.com for single sign on"
    },
    "allowVideo": true,
    "domain": "odinapi.net",
    "endpointType": "accessDeviceEndpoint",
    "aliases": [],
    "trunkAddressing": {
      "trunkGroupDeviceEndpoint": {
        "contacts": []
      }
    },
    "isEnterprise": true,
    "passwordExpiresDays": 2147483647
  }
]
```
