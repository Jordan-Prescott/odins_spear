---
description: my_api.put.auto_attendant()
---

# 🍅 Auto Attendant

In this method, you can update your AAs&#x20;

### Parameters&#x20;

* auto\_attendant\_user\_ids (list): List of service user IDs (AA IDs), the status given will be applied to these.
* status (bool): Boolean value of True (Activate) or False (Deactivate) which will be applied to list of AAs.

### Return

* JSON Data: This method returns json representation of AA updated.

### How To Use:

The below code will set the AA to deactivated.

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

auto_attendants = [
    "basic_aa@domain.com"
]

my_api.put.auto_attendants_status(
    auto_attendant_user_ids= auto_attendants,
    status= False
)
```
{% endcode %}

#### Result:

<figure><img src="../../../../.gitbook/assets/image.png" alt=""><figcaption><p>Basic AA updated to deactivated.</p></figcaption></figure>

