---
description: my_api.delete.service_provider_dns()
---

# 2️⃣ DELETE - Service Provider DNs

Removes range of numbers from a Service Proiver or Enterprise.

{% hint style="danger" %}
format of number must follow: "+{country code}-{number}"
{% endhint %}

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the group is located.&#x20;
* start\_of\_range\_number (str): Starting number in range to remove from group.&#x20;
* end\_of\_range\_number (str): Ending number in range to remove from group.

### Returns

* None: This method does not return any specific value.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.delete.service_provider_dns(
    "serviceProviderId",
    start_of_range_number= "+1-1234567891", 
    end_of_range_number= "+1-1234567895"
)
```
{% endcode %}
