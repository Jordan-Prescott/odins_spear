---
description: my_api.scripter.remove_numbers()
---

# 🔢 Remove Numbers

Removes a singular or range of numbers from the entire Broadworks instance.

{% hint style="warning" %}
```python
Numbers need to be strings and follow this format: +{country code}-{number}.
```
{% endhint %}

The script makes use of the following methods:

```python
api.delete.group_dns()
api.delete.service_provider_dns()
```

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise ID where Group is located which hosts target numbers.&#x20;
* group\_id (str): Group ID where target numbers are located.&#x20;
* start\_of\_number\_range (str): Starting number in range of numbers you would like to remove.&#x20;
* end\_of\_number\_range (str): Ending nummber in range of numbers you would like to remove. If you need to remove only one number do not enter a value for this paramter. Defaults to None.

### Return

* Bool: Returns a True value once complete.&#x20;

### How To Use:

<pre class="language-python"><code class="lang-python">from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

<strong># Removes the range 234567891-3 from Broadworks instance.
</strong>api.scripter.move_numbers(
    service_provider_id="ServiceProviderID-A",
    group_id="GroupID-A",
    start_of_range_number="+1-234567891",
    end_of_range_number="+1-234567892"
)

# Removes the range 234567891 from Broadworks instance.
api.scripter.move_numbers(
    service_provider_id="ServiceProviderID-A",
    group_id="GroupID-A",
    start_of_range_number="+1-234567891"
)
</code></pre>
