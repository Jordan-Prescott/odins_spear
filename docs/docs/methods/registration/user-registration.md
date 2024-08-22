---
description: my_api.get.user_registration()
---

# 💚 GET - User Registration

Gets a users devices and if those devices are registered. This includes soft phones.

{% hint style="info" %}
If registrations is an empty list this means the user has no active registrations.&#x20;
{% endhint %}

### Parameters&#x20;

* user\_id (str): Target user ID to check registration

### Returns

* dict: All users devices and details on device such as registration.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_registration(
    "testUserId@domain.com"
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "registrations": [
    {
      "deviceLevel": "Group",
      "deviceName": "ECG_0004f2accaf7",
      "order": 1,
      "uRI": "sip:2026951172@10.2.2.45:5060;transport=udp;jtr=22-1808",
      "expiration": "Thu May 23 08:33:00 EDT 2019",
      "line/Port": "2026951172@alliedtelecom.net",
      "endpointType": "Primary",
      "publicNetAddress": null,
      "publicPort": null,
      "privateNetAddress": null,
      "privatePort": null,
      "userAgent": "Polycom/5.4.1.14510 PolycomVVX-VVX_500-UA/5.4.1.14510",
      "lockoutStarted": null,
      "lockoutExpires": null,
      "lockoutCount": 0,
      "accessInfo": null
    }
  ],
  "userId": "test.user1@alliedtelecom.net"
}
```
