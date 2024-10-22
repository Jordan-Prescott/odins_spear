# 🔎 Find Alias

Locates alias if assigned to Broadworks entity.

The script searches through various entity types including Auto Attendants (AA), Hunt Groups (HG), and Call Centers (CC), as well as individual Users. It employs a retry mechanism for instances where initial attempts to fetch entity details fail.

The search is conducted in two phases:

1. Collecting details of AAs, HGs, and CCs and checking for the aliases.
2. If not found, search through the users for the alias.

If the alias is found, the method returns a dict specifying the type of entity and its name or userID. If the alias is not found after checking all entities, an AOAliasNotFound exception is raised.

The script makes use of the following methods:

```python
api.get.auto_attendants()
api.get.auto_attendant()
api.get.group_hunt_groups()
api.get.group_hunt_group()
api.get.call_centers()
api.get.call_center()
api.get.users()
```

### Parameters&#x20;

* service\_provider\_id: Service Prodiver where group is hosted.
* group\_id: Group where alias is located.
* alias: Alias number to identify e.g. 0

### Return

* dict: Returns dictionary with type, userserviceid, name and alias.

### Raise

* AOALiasNotFound: If the alias is not found AOAliasNotFound error raised

### How To Use:

{% code overflow="wrap" %}
```python
from odin_api import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# find alias method
print(my_api.scripter.find_alias('Service Provider ID', 'Group ID', alias=12))
```
{% endcode %}

### Formatted Output

```json
{
   "type":"HG",
   "service_user_id":"TESTHG",
   "name":"Test HG",
   "aliases":[
      "12@PROXYADDRESS"
   ]
}
```