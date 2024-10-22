---
description: my_api.scripter.bulk_password_reset()
---

# 🔑 Bulk Password Reset

Resets a list of users SIP passwords, Voicemail passcodes, or Web Authentication Password. Specifify in password\_type with the options of SIP = 'SIP', Voicemail = 'VM', or Web = "WEB" and the script will perform the necessary actions.

{% hint style="warning" %}
```
This script ONLY updates SIP passwords, Voicemail passcodes, or Web Authentication password..
```
{% endhint %}

The script makes use of the following methods:

```python
api.get.passwords_generate()
api.put.user_authentication_service()
api.get.passcodes_generate()
api.put.user_portal_passcode()
api.get.passwords_generate()
api.put.user_web_authentication_password()
```

### Parameters

* service\_provider\_id (str): Service Provider ID where group is hosted.
* group\_id (str): Group ID where target users are located.
* users (list): List of User IDs of the target users to reset the password.
* password\_type (str): Type of password to reset either 'SIP', 'VM', or 'WEB'. Only accepts these two options.

### Raises:

* OSInvalidPasswordType: Only valid password options are SIP, VM, WEB. If another is requested this will be raised.

### Return

* Jdict: Returns dictionary containing user ID and new password set.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()


users = [
    "testuser1@domain.com",
    "testuser2@domain.com",
    "testuser3@domain.com"
]

# changes SIP password for users
my_api.scripter.bulk_password_reset(
        "ServiceProviderID",
        "GroupID",
        users=users,
        password_type="SIP"   
    )
    
# changes Voicemail passcode for users
my_api.scripter.bulk_password_reset(
        "ServiceProviderID",
        "GroupID",
        users=users,
        password_type="VM"   
    )
    
# changes Web Authentication password for users
my_api.scripter.bulk_password_reset(
        "ServiceProviderID",
        "GroupID",
        users=users,
        password_type="WEB"   
    )
```

### Example Returned Data of SIP Passwords (Formatted)

```json
[
   {
      "userId":"User1@domain.com",
      "newPassword":"3h1U[-"
   },
   {
      "userId":"User2@domain.com",
      "newPassword":"e^Bv4c"
   },
   {
      "userId":"User3@domain.com",
      "newPassword":"4WK#:y"
   }
]
```
