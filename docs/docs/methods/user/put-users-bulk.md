---
description: api.put.users_bulk()
---

# 👩‍👩‍👧‍👧 PUT - Users Bulk

Updates specified list of User's options, such as extension, name and etc.

Note: Available options to change can be seen through: get.user_by_id()

### Parameters&#x20;

* users (list): List of specified User IDs to update
* updates (dict): The updates to be applied to the list of Users e.g {"extension":"9999"}

### Returns

* Dict: Returns the changes made including the list of User IDs and updates.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_users = [
  "john.smith@testdomain.net",
  "jane.smith@testdomain.net"
]

my_user_payload = {
    "address": {
        "addressLine1": "Bldg 1",
        "addressLine2": "Suite 2",
        "city": "Cincinnat",
        "stateOrProvince": "Ohio",
        "zipOrPostalCode": "45204",
        "country": "US"
    }
}

my_api.put.users_bulk(
    my_users,
    my_user_payload
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {
  "users": [
    {"userId": "john.smith@testdomain.net"}, 
    {"userId": "jane.smith@testdomain.net"}
    ], 
  "data": {
    "address": {
      "addressLine1": "Bldg 1", 
      "addressLine2": "Suite 2", 
      "city": "Cincinnat", 
      "stateOrProvince": "Ohio", 
      "zipOrPostalCode": "45204", 
      "country": "US"
      }
     }
  }
]

```
