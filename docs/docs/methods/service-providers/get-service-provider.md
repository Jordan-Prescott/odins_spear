---
description: my_api.get.service_provider()
---

# 🏢️ GET - Service Provider

Retrieves information about the specified Service Provider / Enterprise.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider / Enterprise to retreive information on.&#x20;

### Returns

* Dict: A Dictionary about the Service Provider such as it's default domain and resellerID.

### How To Use:

The below code will pull information for the specified Service Provider.

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.service_provider(
    "SERVICE123",
)
```
{% endcode %}

### Example Returned Data of Device (Formatted)

```json
{
  "isEnterprise": true,
  "defaultDomain": "website.com",
  "serviceProviderName": "ent odin mock",
  "supportEmail": "email@domain.com",
  "contact": {
    "contactName": "Contact Team",
    "contactNumber": "111-111-1111",
    "contactEmail": "email@domain.com"
  },
  "address": {
    "addressLine1": "111 This St",
    "city": "Somecity",
    "stateOrProvince": "New York",
    "zipOrPostalCode": "12345",
    "country": "TE"
  },
  "useServiceProviderLanguages": false,
  "serviceProviderId": "SERVICE123"
}
```