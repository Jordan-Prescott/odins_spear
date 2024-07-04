---
description: my_api.get.sip_password_generate()
---

# 🗝️ GET - SIP Password Generate

Generates a single SIP password.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where Group is located.&#x20;
* group\_id (str): Group ID to generate SIP password for.

### Returns

* dict: Single SIP password generated according to the groups rules.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.sip_password_generate(
    "serviceProviderId",
    "groupID",
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "password": "8!01T_8Hk{R6"
}
```
