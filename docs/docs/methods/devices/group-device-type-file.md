---
description: my_api.put.group_device_type_file()
---

# 📂 PUT - Group Device Type File

Set config file for all devices of a spceific type at the group level.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where target device is located.&#x20;
* device\_type (str): The device type you would like to apply the changes to.
* updates (dict): Cupdates (dict): Updates to apply to the target device.

### Returns

* None: This method does not return any specific value.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

updates = {
    "fileSource": "Custom",
    "fileFormat": "user%BWMACADDRESS%.cfg",
    "deviceType": "Polycom IP5000",
    "fileContent": "PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJ5ZXMiPz4NCjwhLS0gRGVmYXVsdCBNYXN0ZXIgU0lQIENvbmZpZ3VyYXRpb24gRmlsZS0tPg0KPCEtLSBGb3IgaW5mb3JtYXRpb24gb24gY29uZmlndXJpbmcgUG9seWNvbSBWb0lQIHBob25lcyBwbGVhc2UgcmVmZXIgdG8gdGhlIC0tPg0KPCEtLSBDb25maWd1cmF0aW9uIEZpbGUgTWFuYWdlbWVudCB3aGl0ZSBwYXBlciBhdmFpbGFibGUgZnJvbTogLS0+DQo8IS0tIGh0dHA6Ly93d3cucG9seWNvbS5jb20vY29tbW9uL2RvY3VtZW50cy93aGl0ZXBhcGVycy9jb25maWd1cmF0aW9uX2ZpbGVfbWFuYWdlbWVudF9vbl9zb3VuZHBvaW50X2lwX3Bob25lcy5wZGYgLS0+DQo8IS0tICRSQ1NmaWxlOiAwMDAwMDAwMDAwMDAuY2ZnLHYgJCAgJFJldmlzaW9uOiAxLjIzLjguMyAkIC0tPg0KPEFQUExJQ0FUSU9OIEFQUF9GSUxFX1BBVEg9IiVBUFBfVkVSU0lPTiUuc2lwLmxkIiBDT05GSUdfRklMRVM9InBob25lJUJXREVWSUNFSUQlLmNmZyxzeXMuY2ZnIiBNSVNDX0ZJTEVTPSIiIExPR19GSUxFX0RJUkVDVE9SWT0iIiBPVkVSUklERVNfRElSRUNUT1JZPSIiIENPTlRBQ1RTX0RJUkVDVE9SWT0iIiBMSUNFTlNFX0RJUkVDVE9SWT0iIj4NCg0KICAgPEFQUExJQ0FUSU9OX1ZWWDMwMCBBUFBfRklMRV9QQVRIX1ZWWDMwMD0iJUFQUF9WRVJTSU9OX1ZWWC0zMDAtNDAwJS5zaXAubGQiIENPTkZJR19GSUxFU19WVlgzMDA9InBob25lJUJXREVWSUNFSUQlLmNmZyxzeXMuY2ZnIi8+DQogICA8QVBQTElDQVRJT05fVlZYNDAwIEFQUF9GSUxFX1BBVEhfVlZYNDAwPSIlQVBQX1ZFUlNJT05fVlZYLTMwMC00MDAlLnNpcC5sZCIgQ09ORklHX0ZJTEVTX1ZWWDQwMD0icGhvbmUlQldERVZJQ0VJRCUuY2ZnLHN5cy5jZmciLz4NCiAgIDxBUFBMSUNBVElPTl9WVlg1MDAgQVBQX0ZJTEVfUEFUSF9WVlg1MDA9IiVBUFBfVkVSU0lPTl9WVlgtNTAwLTYwMCUuc2lwLmxkIiBDT05GSUdfRklMRVNfVlZYNTAwPSJwaG9uZSVCV0RFVklDRUlEJS5jZmcsc3lzLmNmZyIvPg0KICAgPEFQUExJQ0FUSU9OX1ZWWDYwMCBBUFBfRklMRV9QQVRIX1ZWWDYwMD0iJUFQUF9WRVJTSU9OX1ZWWC01MDAtNjAwJS5zaXAubGQiIENPTkZJR19GSUxFU19WVlg2MDA9InBob25lJUJXREVWSUNFSUQlLmNmZyxzeXMuY2ZnIi8+DQo8L0FQUExJQ0FUSU9OPg=="
}


my_api.put.group_device_type_file(
    "service Provider ID",
    "group Id",
    "Device Type",
    updates= updates
)
```
