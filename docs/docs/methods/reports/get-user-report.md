---
description: my_api.get.user_report()
---

# 📈 GET - User Report

Retrieves a detailed report of the specified user including services and service packs assigned.

### Parameters&#x20;

* user_id (str): Target User ID&#x20;

### Returns

* dict: Detailed report of user including services and service packs.

### How To Use:

The following code snippet demonstrates how to fetch a list of all Service Providers:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_report("USER12345@domain")
```
{% endcode %}

### Example Returned Data of Device (Formatted)

```json
{
   "serviceProviderId":"SERVICE123",
   "groupId":"Group1",
   "userId":"user@domain.com",
   "lastName":"Surname",
   "firstName":"Name Name",
   "callingLineIdLastName":"Surname",
   "callingLineIdFirstName":"Name Name",
   "hiraganaLastName":"Surname",
   "hiraganaFirstName":"Name Name",
   "extension":"1234",
   "department":{
      "serviceProviderId":"SERVICE123",
      "groupId":"Group1",
      "name":"Name Name"
   },
   "departmentFullPath":"Office Office",
   "language":"English",
   "timeZone":"Europe/Paris",
   "timeZoneDisplayName":"(GMT+02:00) (Europe) Central Time",
   "defaultAlias":"alias@domain.com",
   "accessDeviceEndpoint":{
      "accessDevice":{
         "deviceType":"Phone Phone",
         "protocol":"SIP 2.0",
         "macAddress":"DEADBEEFCAFE",
         "numberOfPorts":{
            "quantity":"12"
         },
         "numberOfAssignedPorts":1,
         "status":"Online",
         "configurationMode":"Default",
         "transportProtocol":"Unspecified",
         "useCustomUserNamePassword":false,
         "version":"5.9.7.3480",
         "deviceName":"deviceName",
         "serviceProviderId":"ServiceID",
         "groupId":"GroupID",
         "deviceLevel":"Group",
         "accessDeviceCredentials":{
            "userName":"None"
         },
         "tags":[
            
         ],
         "relatedServices":[
            
         ]
      },
      },
      "linePort":"LINEPORT123@lineport.com",
      "staticRegistrationCapable":"false",
      "useDomain":"true",
      "supportVisualDeviceManagement":"false",
      "contacts":[
         
      ]
   },
   "countryCode":"00",
   "nationalPrefix":"",
   "allowVideo":true,
   "callingLineIdPhoneNumber":"",
   "phoneNumber":"",
   "domain":"domain.com",
   "endpointType":"accessDeviceEndpoint",
   "aliases":[
      
   ],
   "trunkAddressing":{
      "trunkGroupDeviceEndpoint":{
         "contacts":[
            
         ]
      }
   },
   "departmentName":"Name Name",
   "emailAddress":"",
   "phoneNumberActivated":"None",
   "isEnterprise":true,
   "passwordExpiresDays":"00000000",
   "inTrunkGroup":"None",
   "premiumServices":[
      
   ],
   "userServices":[
      
   ],
   "servicePacks":[
      "Pack-1"
   ],
   "userLinePorts":[
      "LINEPORT123@lineport.com"
   ]
}
```