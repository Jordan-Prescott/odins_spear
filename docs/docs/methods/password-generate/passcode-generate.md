---
description: my_api.get.passcode_generate()
---

# 🗝️ GET - Passcode Generate

Generates a single passcode following group rules.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where Group is located.&#x20;
* group\_id (str): Group ID to generate passcode for.

### Returns

* dict: Multiple passwords generated according to the groups rules.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.passcode_generate(
    "serviceProviderId",
    "groupID",
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "passcode": "68204751"
}
```
