---
description: my_api.post.service_provider_dns()
---

# 4️⃣ POST - Service Provider DNs

Adds a range of numbers to a Service Provider/ Enterprise. Range of numbers must be complete and format of number must follow: +{country code}-{number}.

{% hint style="info" %}
Adding a singular number - Set both the start and end of range parameters as the same number.
{% endhint %}

{% hint style="danger" %}
format of number must follow: +{country code}-{number} and the range must be complete.
{% endhint %}

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the target group is located.
* start\_of\_range\_number (str): Starting number in range to add to group.
* end\_of\_range\_number (str): Ending number in range to add to group.

### Returns

* None: This method does not return any specific value.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.post.service_provider_dns(
    "serviceProviderId",
    start_of_range_number="+1-1234567891,
    end_of_range_number="+1-1234567892
)
```
{% endcode %}
