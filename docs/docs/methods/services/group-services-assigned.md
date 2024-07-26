---
description: my_api.get.group_services_assigned()
---

# 🧍 GET - Group Services Assigned

Get details of the user/service instances where a particular service is assigned.

### Parameters&#x20;

*    group\_id (str): GroupID being targeted
*    service_provider\_id (str): Service provider/Enterprise ID where the group is located.
*    service_name (str): Name of the service querying
*    service_type (str): Type of service. Either: serviceName or servicePackName

### Returns

* Dict: Users/Service Instances where the service is assigned.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# Get details of the user/service instances where a particular service is assigned.
my_api.get.group_services_assigned(
    "groupId",
    "serviceProviderId",
    "serviceType",
    "serviceName"
)
```
{% endcode %}



### Example Data Returned (Formatted)
```json
{
   "serviceProviderId":"Test-Enterprise-EU",
   "groupId":"TGDMS",
   "serviceType":"userServices",
   "serviceName":"Anonymous Call Rejection",
   "users":[
      
   ]
}
```
```
