---
description: api.scripter.service_pack_audit()
---

# ✅ Service Pack Audit

A stripped down version of group audit focussing only on the service packs assigned within the group. This only shows the service packs assigned and total count of unlike group audit which details the users this is assigned to.

The script makes use of the following methods:

<pre class="language-python"><code class="lang-python"><strong>api.get.group_services()
</strong></code></pre>

### Parameters&#x20;

* service\_provider\_id: Service Provider ID or Enterprise ID containing the Group ID.
* group\_id: Group ID to generate the report for.

### Return

* JSON: A JSON formatted report of service packs assigned in the group.

### How To Use:

```python
from odins_spear import api

may_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

print(
    my_api.scripter.service_pack_audit(
        "ServiceProviderId",
        "GroupId"
    )
)
```

### Example returned data (formatted):

```json

{
    "service_pack_services": [
        {
            "servicePackName": "Standard pack 1",
            "usage": 20,
            "description": "Standard pack 1"
        },
        {
            "servicePackName": "Premium pack 1",
            "usage": 1,
            "description": "Premium pack 1"
        },
        {
            "servicePackName": "Service pack 2",
            "usage": 13,
            "description": "Service pack 2"
        }
    ]
}
```
