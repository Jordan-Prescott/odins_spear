---
description: my_api.get.passcodes_generate()
---

# 🗝️ GET - Passcodes Generate

Generates a multiple passcodes to the limit set in pararmeters.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where Group is located.&#x20;
* group\_id (str): Group ID to generate passcodes for.&#x20;
* limit (int, optional): Number of passwords api will return. Defaults to 10.

### Returns

* Dict: Multiple passwords generated according to the groups rules.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.passcodes_generate(
    "serviceProviderId",
    "groupID",
    limit =10
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "passcodes": [
    "52184637",
    "73586940",
    "27648093",
    "14608397",
    "35810742",
    "64907832",
    "47692380",
    "69307485",
    "95013267",
    "78210935"
  ]
}
```
