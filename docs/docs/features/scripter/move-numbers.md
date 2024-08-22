---
description: my_api.scripter.move_numbers()
---

# 🔢 Move Numbers

Moves a list of numbers from existing group to another group on the same broadworks instance. This can move numbers between Service Provider/ Enterprise and groups in the same Service Provider/ Enterprise.

{% hint style="warning" %}
```python
Numbers need to be strings and follow this format: +{country code}-{number}.
```
{% endhint %}



The script makes use of the following methods:

```python
api.delete.group_dns()
api.delete.service_provider_dns()
api.post.group_dns_assign_bulk()
api.post.group_dns()
```

### Parameters&#x20;

* current\_service\_provider\_id (str): Current Service Provider/ Enterprise where numbers are located.
* current\_group\_id (str): Current Group ID where numbers are located.&#x20;
* target\_service\_provider\_id (str): Target Service Provider/ Enterprise to move the numbers to.
* target\_group\_id (str): Target Group to move numbers to.&#x20;
* start\_of\_number\_range (str): Starting number in range of numbers you would like to move.
* end\_of\_number\_range (str): Ending nummber in range of numbers you would like to move. If you need to move only one number do not enter a value for this paramter. Defaults to None.

### Return

* Bool: Returns a True value once complete.&#x20;

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# Moving the range 234567891-3 from GroupID-A to GroupID-B
api.scripter.move_numbers(
    current_service_provider_id="ServiceProviderID-A",
    current_group_id="GroupID-A",
    target_service_provider_id="ServiceProverID-B",
    target_group_id="GroupID-B",
    start_of_range_number="+1-234567891",
    end_of_range_number="+1-234567892"
)


# Moving the number 234567891 from GroupID-A to GroupID-B
api.scripter.move_numbers(
    current_service_provider_id="ServiceProviderID-A",
    current_group_id="GroupID-A",
    target_service_provider_id="ServiceProverID-B",
    target_group_id="GroupID-B",
    start_of_range_number="+1-234567891"
)
```
