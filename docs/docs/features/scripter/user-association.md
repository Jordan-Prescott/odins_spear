---
description: api.scripter.user_association()
---

# 🔗 User Association

This script is to identify a user's associations with Call Centers (CC), Hunt Groups (HG), and Pick Up Groups. Additionally, this returns other key information of the user such as extension, phone number, and services and feature packs assigned as this data can be useful when reviewing which CC and HG they are associated to for example if an agent in a CC has a higher feature pack than needed for work in x CC.

This script uses the below methods to achieve this:

```python
api.get.call_pickup_group_user()
api.get.group_hunt_group_user()
api.get.user_call_center()
api.get.user_report()
```

### Parameters&#x20;

* service\_provider\_id: Service Provider where the group is hosted.
* group\_id: Group where the User is located.
* user\_id: Target user ID.

### Return

* str: Formatted output of the user showing all CC, HG, and Pick Up user is assigned to.&#x20;

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.scripter.user_association(
    "ServiceProviderID", 
    "GroupID", 
    "UserID"
)
```
{% endcode %}

### Terminal Output

{% code overflow="wrap" fullWidth="false" %}
```
User Data:
        User Id: userId@domain.com
        First Name: John
        Last Name: Smith
        Extension: 101
        Phone Number: 0123456789
        Services: Custom Ringback User
        Feature Packs: Feature Pack X, Feature Pack Y
        Hunt Groups: Accounts, Sales, Reception
        Call Centers: Technical Support, Service Support
        Pick Up Group: Tech and Service
```
{% endcode %}
