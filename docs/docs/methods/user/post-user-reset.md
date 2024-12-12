---
description: api.post.user_reset()
---

# ⭕ POST - User Reset

{% hint style="danger" %}
**Warning:** This action will remove elemnts of a User, and once completed cannot be undone without prior backup. Proceed with caution.
{% endhint %}

Removes Call records, group services and Webex from the specified user.

### Parameters&#x20;

* user_id (str): Users Original Identifier
* remove_from_group_services (bool): Remove From Group Services
* remove_call_records (bool): Remove Call Record Instances
* remove_alternate_user_ids (bool): Remove Alternate User Identifiers
* remove_webex_person (bool): Remove Webex Entry
* cycle_service_packs (bool): Shift Service Packs
* reset_password_passcode (bool): Reset Password Forcing A New Login And Password

### Returns

* Nothing

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.post.user_reset(
    "user@domain.com", 
    True,
    False,
    True,
    True,
    False,
    False
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
N\A
```
