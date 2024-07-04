---
description: my_api.get.password_generate()
---

# 🔓 GET - Password Generate

Generates a single passwords following the groups rules.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where Group is located.
* group\_id (str): Group ID to generate password for.

### Returns

* dict: Single password generated according to the groups rules..

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.password_generate(
    "serviceProviderId",
    "groupID",
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "password": "?+^8RZ40MeC3+:i.BQ"
}
```
