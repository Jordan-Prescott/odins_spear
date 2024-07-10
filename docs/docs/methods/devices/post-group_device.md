# 🗃️ POST - Group Device

Adds a new device to a group. 

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the device should be built.
* group\_id (str): Group ID where the device should be built
* device\_name (str): Name of the new device
* device\_type (str): Type of device. 
* payload (dict, optional): Device configuration data. 

### Returns

* Dict: Returns the device profile. 

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

payload = {
    "deviceType": "Polycom Soundpoint IP 4000",
    "deviceName": "my-new-device-name",
    "deviceLevel": "Group",
    "useCustomUserNamePassword": true,
    "accessDeviceCredentials": {
        "userName": "9871515000",
        "password": "ym7#zIuA"
    },
    "netAddress": "111.111.111.111",
    "port": "2222",
    "outboundProxyServerNetAddress": "222.222.222.222",
    "stunServerNetAddress": "333.333.333.333",
    "macAddress": "CBFB0EBBF325",
    "serialNumber": "123456789",
    "description": "description",
    "physicalLocation": "usa",
    "transportProtocol": "UDP",
    "groupId": "grp.odin",
    "serviceProviderId": "ent.odin",
    "profile": "Intelligent Proxy Addressing",
    "staticRegistrationCapable": "false",
    "configType": "3 File Configuration",
    "protocolChoice": [
        "SIP 2.0"
    ],
    "isIpAddressOptional": "true",
    "useDomain": "true",
    "isMobilityManagerDevice": "false",
    "deviceConfigurationOption": "Device Management",
    "staticLineOrdering": "false",
    "deviceTypeLevel": "System",
    "tags": [],
    "relatedServices": [],
    "protocol": "SIP 2.0",
    "userName": "9871515000"
}


my_api.post.group_device(
    "service_provider_id",
    "group_id",
    "device_name", 
    "device_type",
    payload=payload
)
```
{% endcode %}

### Example Returned Data of Device (Formatted)

```json
{
  {
    "deviceType": "device_type",
    "protocol": "SIP 2.0",
    "numberOfPorts": {
        "unlimited": "true"
    },
    "numberOfAssignedPorts": 0,
    "status": "Online",
    "transportProtocol": "Unspecified",
    "useCustomUserNamePassword": false,
    "deviceName": "device_name",
    "serviceProviderId": "service_provider_id",
    "groupId": "group_id",
    "macAddress": "",
    "deviceLevel": "Group",
    "accessDeviceCredentials": {
        "userName": null
    },
    "tags": [],
    "relatedServices": []
}
}
```