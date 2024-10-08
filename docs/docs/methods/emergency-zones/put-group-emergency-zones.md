# ⚠️ PUT - Group Emergency Zones

Updates the Emergency Zone configuration in the group. 

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the Emergency Zone to be updated exists.
* group\_id (str): Group ID where the Emergency Zone to be updated exists.
* is\_active (bool, optional): Whether the Emergency Zone service is active or not. Defaults to True
* zone\_rules (str, optional): The rules of the Emergency Zone. This will either be "Prohibit all registrations and call originations" or "Prohibit emergency call originations".
* emergency\_notification\_email (str, optional): The email address where emergency call notifications should be sent. 
* ip\_addresses (list, optional): A list of IP address ranges (dicts) to be added to the Emergency Zone. If the IP address to be applied is not a range, the min and max values should be the same.

### Returns

* Dict: Updated Emergency Zone configuration.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.put.group_emergency_zones(
    service_provider_id = "my_service_proviider_id", 
    group_id = "my_group_id", 
    zone_rules = "Prohibit emergency call originations", 
    emergency_notification_email = "john.smith@domain.com",
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
    "emergencyZonesProhibition": "Prohibit emergency call originations", 
    "sendEmergencyCallNotifyEmail": "True", 
    "emergencyCallNotifyEmailAddress": "john.smith@domain.com", 
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