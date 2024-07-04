---
description: my_api.get.system_dn()
---

# 6️⃣ GET - System DNs

Searches for number from System level. This will return where the number is located on the system. It will show the Service Provider/ Enterprise, Group ID, and User ID the number is assigned to.

### Parameters&#x20;

* dn (int): Target number excluding country code e.g. 123456789

### Returns

* List: List of dictionaries containing details of each number that fit the search criteria.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.system_dn(
    123456789
)
```
{% endcode %}
