# 🔎 Find Alias (Script)

Locates alias if assigned to Broadworks entity.

The script searches through various entity types including Auto Attendants (AA), Hunt Groups (HG), and Call Centers (CC), as well as individual Users. It employs a retry mechanism for instances where initial attempts to fetch entity details fail.

The search is conducted in two phases:

1. Collecting details of AAs, HGs, and CCs and checking for the aliases.
2. If not found, search through the users for the alias.

If the alias is found, the method returns a string specifying the type of entity and its name or userID. If the alias is not found after checking all entities, an AOAliasNotFound exception is raised.

### Parameters&#x20;

* service\_provider\_id: Service Prodiver where group is hosted.
* group\_id: Group where alias is located.
* alias: Alias number to identify e.g. 0

### Return

* Returns type and name/ userId of entity where alias located.

### Raise

* AOALiasNotFound: If the alias is not found AOAliasNotFound error raised

### How To Use:

{% code overflow="wrap" %}
```python
from odin_api import api

magic = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
magic.authenticate()

magic.scripter.{script}

# find alias method
print(magic.scripter.find_alias('Service Provider ID', 'Group ID', alias=11))
```
{% endcode %}

### Terminal Output

{% code overflow="wrap" fullWidth="false" %}
```
Fetching AA, HG, and CC details: 100%|██████████████████████████████████████████████████████████████████████████
Searching AA, HG, and CC for alias 11: 100%|████████████████████████████████████████████████████████████████████
2024-01-03 13:05:33,003 - INFO - Fetched users.
Searching Users for alias: 11:  38%|███████████████████████████████████████████████▎                            

        Alias (11) found: User - FourteenIPUK2015@voip.14ip.net
        
```
{% endcode %}
