# 🤵 POST - Group Admin

Builds a group-level administrator.

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the admin should be built.
* group\_id (str): Group ID where the admin should be built
* user\_id (str): User Id of the admin.
* password (str): Password for the administrator profile. Note get.password_generate() can be used to get this.
* payload (dict, optional): Admin configuration data. 

### Returns

* Dict: Returns the admin profile. 

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.post.group_admin(
    "my_service_provider_id",
    "my_group_id",
    "john_smith@domain.net", 
    "password123"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
    "userId": "john.smith@domain.net", 
    "serviceProviderId": "my_service_provider_id", 
    "groupId": "my_group_id", 
    "language": "English", 
    "locale": "en_US", 
    "encoding": "ISO-8859-1"
}
```