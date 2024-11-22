---
description: api.delete.user()
---
# ❌ DELETE - Delete User

Removes the specified user from the platform entirely.

{% hint style="danger" %}
**Warning:** This action will permanently delete the user and all associated attributes, including unassigning phone numbers. Once deleted, this action cannot be undone unless a prior backup exists. Proceed with caution.
{% endhint %}

### Parameters&#x20;

* user\_id (str): Target user ID of the user you would like to delete

### Returns

* Nothing

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.delete.user(
    "user_ID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[]
```