---
description: api.logger.set_up_file_handler()
---

# 📂 Sending Logs To A File

By default the library will send your logs to the a file name `os.log` in your current working directory . However, if you would like to change the location where your logs are saved you can use this method. The method takes in the `path` argument which is the path to the location the file you would like to store your log file.&#x20;

### Parameters&#x20;

* path (str, optional): Path to file to send logs. Defaults to 'os.log'. Defaults to 'os.log'

### Return

* None: This method does not return anything.

### How To Use:

When creating your API object it will set up the logger automatically and start to send logs of API calls made to `os.logg`. When authenticating your API object this sends a call to the API and will Logger will send this to `os.logg`. Therefore, if you plan to send the logs to a different location specify this before authenticating.

```python
from odins_spear import api

may_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")

my_api.logger.set_up_file_hander('yourPath')

my_api.authenticate()
```

### Example logs.

```log
2024-04-25 15:39:33,919 | Odin's Spear | Username | 400 | /service-providers/trunk-groups/call-capacity?serviceProviderId=ServicePrividerID
2024-04-25 15:48:05,673 | Odin's Spear | Username | 200 | /auth/token
2024-04-25 15:48:06,447 | Odin's Spear | Username | 400 | /service-providers/trunk-groups/call-capacity?serviceProviderId=ServicePrividerID
2024-04-25 15:48:07,215 | Odin's Spear | Username | 200 | /service-providers/trunk-groups/call-capacity?serviceProviderId=ServicePrividerID
2024-04-25 15:48:08,513 | Odin's Spear | Username | 200 | /groups?serviceProviderId=ServicePrividerID
2024-04-25 15:48:09,484 | Odin's Spear | Username | 400 | /groups/trunk-groups/call-capacity?serviceProviderId=ServicePrividerID&groupId=groupId
2024-04-25 15:48:10,305 | Odin's Spear | Username | 400 | /groups/trunk-groups/call-capacity?serviceProviderId=ServicePrividerID&groupId=groupId
```

