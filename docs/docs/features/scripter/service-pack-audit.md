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

* dict: Returns dict containing service packs assigned in the group.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

print(
    my_api.scripter.service_pack_audit(
        "ServiceProviderId",
        "GroupId"
    )
)
```
Terminal Output:
```
Analysing Service Packs...: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 114/114 [00:00<?, ?it/s] 
{"servicePackServices": [{"servicePackName": "Admin-A", "usage": 21, "description": null}, {"servicePackName": "Unity-R", "usage": 4, "description": null}, {"servicePackName": "WBX-B", "usage": 45, "description": "Webex for BroadWorks Basic"}

```

### Example returned data (formatted):

```json


   "servicePackServices":[
      {
         "servicePackName":"Admin-A",
         "usage":21,
         "description":null
      },
      {
         "servicePackName":"Unity-R",
         "usage":4,
         "description":null
      },
      {
         "servicePackName":"WBX-B",
         "usage":45,
         "description":"Webex for BroadWorks Basic"
      }
   ]
```
