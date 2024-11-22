# Bulk Build Group Admins

This script will build multiple group admins and assign policy settings to all built. 

The policy confifuration is for customers with access to your odin portal but can be modified to fit needs.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear.api import Api

my_api = Api("base_url", "username", "ENV-PASSWORD")
magic.authenticate()

# CHANGE ME
service_provider_id = 'ServiceProviderID'
group_id = 'GroupID'
group_domain = '@domain' #'@' is needed 
users = ['first_name.last_name','first_name.last_name'] # follow formatting as its used further down the script.

# Customer admin account 
policy = {
    "profileAccess": "Read-Only",
    "userAccess": "Full Profile",    
    "adminAccess": "Read-Only",    
    "departmentAccess": "Full",    
    "accessDeviceAccess": "Read-Only",    
    "enhancedServiceInstanceAccess": "Modify-Only",    
    "featureAccessCodeAccess": "Read-Only",    
    "phoneNumberExtensionAccess": "Read-Only",    
    "callingLineIdNumberAccess": "Full",    
    "serviceAccess": "Read-Only",    
    "trunkGroupAccess": "Read-Only Resources",    
    "sessionAdmissionControlAccess": "Read-Only",    
    "officeZoneAccess": "Read-Only",    
    "numberActivationAccess": "None",    
    "dialableCallerIDAccess": "Full",}
    
    # create admins
    for user in users:        
        gen_password = my_api.get.password_generate(service_provider_id, group_id)["password"]       
        
        payload = {        
            "firstName": user.split('.')[0],         
            "lastName": user.split('.')[1],        
            "password": gen_password    
            }        
            
        magic.post.group_admin(        
            service_provider_id=service_provider_id,        
            group_id=group_id,        
            user_id=user+group_domain,        
            password=gen_password,        
            payload=payload    
            )    
    
    #apply policy 
    magic.post.group_admin_policies_bulk(    
        user_ids=[user+group_domain for user in users],    
        policy_config=policy
    )
```
{% endcode %}