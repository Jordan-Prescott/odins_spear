# 🗃️ POST - Group Emergency Zones

Updates the IP address(es) for the Emergency Zone configured in the group. 

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the Emergency Zone to be updated exists.
* group\_id (str): Group ID where the Emergency Zone to be updated exists.
* ip\_addresses (str): A list of IP address ranges (dicts) to be added to the Emergency Zone. If the IP address to be applied is not a range, the min and max values should be the same.

### Returns

* Dict: Returns the device profile. 

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

payload = {