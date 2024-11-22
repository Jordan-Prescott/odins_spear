---
description: api.scripter.locate_free_extension()
---

# Locate Free Extension

Locates the lowest value free extension given the provided range of extension numbers.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise ID where Group is located which hosts needed free extensions
* group\_id (str): Group ID where target extensions are located.
* range\_start (int): integral value specifying the starting range for free extensions.
* range\_end (int): integral value specifying the ending range for free extensions.

### Return

* dict: First free extension in the range. 

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

print(
    my_api.scripter.locate_free_extension(
        service_provider_id="ServiceProviderID",
        group_id="GroupID",
        range_start=2000,
        range_end=3000
    )
)
```
{% endcode %}

### Retuned Data (Formatted)

{% code overflow="wrap" fullWidth="false" %}
```
    {
    'extension': 2000 
    }
```
{% endcode %}
