---
description: my_api.delete.auto_attendant_submenu()
---

#  🛑 DELETE - Auto Attendant Submenu

Removes an Auto Attendant (AA) Submenu from the AA configuration. Submenus are only a feature of the 'Auto Attendant - Standard' service. These are not available on Basic AAs.

### Parameters&#x20;

* service_user_id(str): The service user ID of the AA.
* submenu_id (str): The ID of the Submenu to be removed from the AA. 

### Returns

* None: This method does not return any specific value.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.delete.auto_attendant_submenu(
    service_user_id="test_aa@domain.net", 
    submenu_id="Menu 1"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[]


```
