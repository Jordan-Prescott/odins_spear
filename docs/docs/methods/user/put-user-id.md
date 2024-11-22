---
description: api.put.user_id()
---
# 🆔 PUT - User ID

Updates the specified user's UserID, including domain.

{% hint style="warning" %}
**Warning:** This action may cause devices to become unregistered. When applying in bulk, please proceed with caution.
{% endhint %}

### Parameters&#x20;

* user\_id (str): Target user ID of the user you would like to change the UserID of.

### Returns

* Nothing

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.user_id(
    "user_ID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[]
```