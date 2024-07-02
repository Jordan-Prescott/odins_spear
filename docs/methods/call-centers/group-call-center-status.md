---
description: my_api.put.group_call_centers_status()
---

# 🟢 PUT - Group Call Center Status

In this method, you can control the status of your Call Centers (CC) by activating and deactivating them. The method takes in two parameters, they are a list of the CC service user IDs and a status which is a boolean value of True (Active) or False (Deactivate).

### Parameters&#x20;

* call\_center\_user\_ids(list): List of service user IDs (CC IDs), the status given will be applied to these.
* status (bool): The boolean value of True (Activate) or False (Deactivate) which will be applied to list of AAs.

### Returns

* None: This method does not return any specific value.

### How To Use:

The below code will set the AA to deactivated.

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

call_centers = [
    "basic_cc@domain.com"
]

my_api.put.group_call_centers_status(
    call_center_user_ids = call_centers,
    status= False
)
```
{% endcode %}

#### Result:

<figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

