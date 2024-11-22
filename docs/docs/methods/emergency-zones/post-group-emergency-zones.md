# 🗃️ POST - Group Emergency Zones

Updates the IP address(es) for the Emergency Zone configured in the group. 

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the Emergency Zone to be updated exists.
* group\_id (str): Group ID where the Emergency Zone to be updated exists.
* ip\_addresses (list): A list of IP address ranges (dicts) to be added to the Emergency Zone. If the IP address to be applied is not a range, the min and max values should be the same.

### Returns

* Dict: Emergency Zone profile with updated IP addresses.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.post.group_emergency_zones(
    service_provider_id = "my_service_proviider_id", 
    group_id = "my_group_id", 
    ip_addresses = [
        {
            "min": "123.45.0.67",
            "max": "123.45.0.68"
        }, 
        {
            "min": "11.0.0.0",
            "max": "11.0.0.0"
        }
    ]
)
```

### Example Data Returned (Formatted)

```json
{
    "isActive": "True", 
    "emergencyZonesProhibition": "Prohibit all registrations and call originations", 
    "sendEmergencyCallNotifyEmail": "False", 
    "serviceProviderId": "my_service_provider_id", 
    "groupId": "my_group_id", 
    "ipAddresses": [
        {
            "min": "11.0.0.0", 
            "max": "11.0.0.0"
            },
        {
            "min": "123.45.0.67", 
            "max": "123.45.0.68"
            }
        ]
    }
```