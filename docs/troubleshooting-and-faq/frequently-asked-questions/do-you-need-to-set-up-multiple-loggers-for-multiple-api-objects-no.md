# 1️⃣ Do You Need To Set Up Multiple Loggers For Multiple API Objects? No.

The Logger object is a Singleton and can only be created once across multiple API objects for your multiple Broadwork instances. All API calls for all your API objects will be sent to the same places you defined in one API object.&#x20;

The reason here is it allows administrators to see all uses of the library in one space. However, if there is a need to separate this so logs for different systems can be sent to different locations please contact us to discuss below.

{% content-ref url="../../contact.md" %}
[contact.md](../../contact.md)
{% endcontent-ref %}

### How To Use:

Like normal create your api objects however, before authentication use the set up handler methods on **one** of your objects to specify locations the logs should be sent.&#x20;

```python
from odins_spear import api

may_api_1= api.Api(base_url="https://base_url_1/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
may_api_2= api.Api(base_url="https://base_url_2/api/vx", username="john.smith", password="ODIN_INSTANCE_2")
may_api_3= api.Api(base_url="https://base_url_3/api/vx", username="john.smith", password="ODIN_INSTANCE_3")

my_api_1.logger.set_up_sys_log_handler('yourURL', 1234)
my_api_1.logger.set_up_file_handler('yourPath')

my_api_1.authenticate()
my_api_2.authenticate()
my_api_3.authenticate()
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

