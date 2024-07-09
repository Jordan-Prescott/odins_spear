# 📜 Logger

The Logger object logs API calls made using Odin's Spear.&#x20;

Details logged are: Date/ Time, Name (Odin's Spear), User (You the developer), response code, endpoint.&#x20;

Logs are sent to os.log by default but can be changed in set\_up\_file\_handler() method. Logs can also be sent to an external syslog server using the set\_up\_sys\_log\_handler method.

{% code overflow="wrap" %}
```python
from odin_api import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.logger.set_up_file_handler()
my_api.logger.set_up_syslog_handler()
```
{% endcode %}
