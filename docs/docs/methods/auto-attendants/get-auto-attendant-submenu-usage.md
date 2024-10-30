---
description: my_api.get.auto_attendant_submenu_usage()
---

#  🖲️ GET - Auto Attendant Submenu Usage

Returns the type of the specified Auto Attendant (AA) submenu. NOTE: This method does not return any usage data. 

### Parameters&#x20;

* service_user_id (str): The servivce user ID of the AA being queried.
* submenu_id (str): The submenu ID of the submenu being queried. 

### Returns

* List: Returns a list containing a single dict of the submenu. 

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.auto_attendant_submenus(
    service_user_id="test_aa@domain.net", 
    submenu_id="Submenu 1"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
    {
        "type": "Business Hours Menu",
        "submenuId": null
    }
]

```
