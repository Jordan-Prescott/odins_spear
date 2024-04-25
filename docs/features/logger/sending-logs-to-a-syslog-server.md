---
description: api.logger.set_up_sys_log_handler()
---

# ☁️ Sending Logs To A Syslog Server

Logger lets you send your logs externally to a server which can be handy for system administrators that need accountability. When making calls to Odin's API **not all** calls are logged in the event history in the web portal. Using this feature can ensure you get the full benefits of the library and have complete accountability of the team.

### Parameters&#x20;

* url (str): IP/ URL to syslog server e.g. 1.1.1.1 or mysyslogserver.com/&#x20;
* port\_number (int): Port number the logs will sent on to URL

### Return

* None: This method does not return anything.

### How To Use:

When creating your API object it will set up the logger automatically and start to send logs of API calls made to `os.logg`. When authenticating your API object this sends a call to the API and will Logger will send this to `os.logg`. Therefore, to capture all logs including the authentication call this method before authenticating.

```python
from odins_spear import api

may_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")

my_api.logger.set_up_sys_log_handler('yourURL', 1234)

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

