# 🤖 Scripter

The Scripter object gives you access to pre-written scripts for common tasks and features not built in Odin's web portal such as locating an alias.

Each API object creates its own Scripter object on instantiation, the Scripter object can then be accessed through the API object.

{% code overflow="wrap" %}
```python
from odin_api import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.scripter.{script}
```
{% endcode %}

{% hint style="info" %}
For each script detail please see script documentation.
{% endhint %}
