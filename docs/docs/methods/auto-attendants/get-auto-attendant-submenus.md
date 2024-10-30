---
description: my_api.get.auto_attendant_submenus()
---

#  🎚️ GET - Auto Attendant Submenus

Returns a list of the submenus of the specified Auto Attendant (AA). Works with Standard AAs only, basic AAs do not have submenus.

### Parameters&#x20;

* service_user_id (str): The service user ID of the AA.

### Returns

* List: Returns a list of the submenus associated with the AA.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.auto_attendant_submenus(
    service_user_id="test_aa@domain.net"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
    {
        "submenuId": "Submenu 1",
        "isUsed": false,
        "serviceUserId": "test_aa@domain.com"
    },
    {
        "submenuId": "Submenu 2",
        "isUsed": false,
        "serviceUserId": "test_aa@domain.com"
    }
]

```
