---
description: my_api.put.system_device_file()
---

# 📁 PUT - System Device File

Update a config file for a single device at the system level.

### Parameters&#x20;

* device\_name (str): Device name of the target device.&#x20;
* updates (dict): Updates to apply to the target device.

### Returns

* None: This method does not return any specific value.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

updates = {
    "fileSource": "Custom",
    "fileFormat": "%BWMACADDRESS%.cfg",
    "fileContent": "PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJ5ZXMiPz4KPCEtLSBEZWZhdWx0IE1hc3RlciBTSVAgQ29uZmlndXJhdGlvbiBGaWxlLS0+CjwhLS0gRm9yIGluZm9ybWF0aW9uIG9uIGNvbmZpZ3VyaW5nIFBvbHljb20gVm9JUCBwaG9uZXMgcGxlYXNlIHJlZmVyIHRvIHRoZSAtLT4KPCEtLSBDb25maWd1cmF0aW9uIEZpbGUgTWFuYWdlbWVudCB3aGl0ZSBwYXBlciBhdmFpbGFibGUgZnJvbTogLS0+CjwhLS0gaHR0cDovL3d3dy5wb2x5Y29tLmNvbS9jb21tb24vZG9jdW1lbnRzL3doaXRlcGFwZXJzL2NvbmZpZ3VyYXRpb25fZmlsZV9tYW5hZ2VtZW50X29uX3NvdW5kcG9pbnRfaXBfcGhvbmVzLnBkZiAtLT4KPCEtLSAkUkNTZmlsZTogMDAwMDAwMDAwMDAwLmNmZyx2ICQgICRSZXZpc2lvbjogMS4yMy44LjMgJCAtLT4KPEFQUExJQ0FUSU9OIEFQUF9GSUxFX1BBVEg9ImZ0cDovLzE2Mi4yNTAuMjQwLjEzMS9maXJtd2FyZS8lZmlybXdhcmUlL3NpcC5sZCIgQ09ORklHX0ZJTEVTPSJ1c2VyJUJXTUFDQUREUkVTUyUuY2ZnLGZlYXR1cmVzJUJXTUFDQUREUkVTUyUuY2ZnLHN5c3RlbSVCV01BQ0FERFJFU1MlLmNmZywlQldNQUNBRERSRVNTJV9kZWN0LmNmZyIgTUlTQ19GSUxFUz0iIiBMT0dfRklMRV9ESVJFQ1RPUlk9IiIgT1ZFUlJJREVTX0RJUkVDVE9SWT0iIiBDT05UQUNUU19ESVJFQ1RPUlk9IiIgTElDRU5TRV9ESVJFQ1RPUlk9IiI+CjwvQVBQTElDQVRJT04+Cg=="
}


my_api.put.system_device_file(
    "device_name",
    updates=updates
)
```
