---
description: api.scripter.webex_builder()
---

# 💻 Webex Builder

This script will build a webex device for a user either as a primary device or as a Shared Call Appearance. 

An email and alternate user id is set, then an optional feature pack can be assigned for billing. 

Next, Integrated IMP is enabled in the user services (This is needed for the integration with Cisco). Furthermore, the device is built to the device profile you set using `device_type` parameter and then added to the user either as a primary device or SCA.

{% hint style="warning" %}
```
Before running ensure your user has correct licensing for Shared Call Appearance if secondary device. Furthermore, make sure all prerequisites for the group to have webex users have been taken.
```
{% endhint %}

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where group is hosted.
* group\_id (str): Group ID where target user is hosted. 
* user\_id (str): Target user to build and add webex device.
* device\_type (str): Name of the device profile to apply. 
* email (str): Email of user. This will be used to sign into the webex client.
* primary\_device (bool, optional): Setting to False will assign as SCA, True is primary. Defaults to True. 
* webex\_feature\_pack\_name (str, optional): Feature pack to assign for Webex services. Defaults to None.
* enable\_integrated\_imp (bool, optional): Enables Integrated IMP service for the user if True .Defaults to True.

### Return

* dict: Webex user/ device details. Includes webex client username and password, and if primary device, device type set. 

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.scripter.webex_builder(
    service_provider_id="serviceProviderId",
    group_id="groupId",
    user_id="userId",
    device_type="Businness Communicator - Mobile",
    email="test@test.com",
    primary_device=True,
    webex_feature_pack_name="Webex Mobile",
    enable_integrated_imp=True
)
```
{% endcode %}

### Retuned Data (Formatted)

{% code overflow="wrap" fullWidth="false" %}
```
    {
    'username': 'User.ID@Domain.wbx.com', 
    'password': '{YdQba', 
    'primary_device': True, 
    'device_type': 'Business Communicator - PC'
    }
```
{% endcode %}
