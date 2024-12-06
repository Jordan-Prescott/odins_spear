---
description: my_api.get.user_alternate_numbers()
---

# 1️⃣ GET - User Alternate Numbers

Fetches a list of a user/ service such as Auto Attendant, Hunt Group, or Call Centres alternate numebrs.

### Parameters&#x20;

* user\_id (str): Target user/ service\_user\_id

### Returns

* Dict: List of all alternate numbers assigned to the user/ service.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_alternate_numbers(
    "9546547216@microv-works.com"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "userId": "9546547216@microv-works.com",
  "distinctiveRing": false,
  "alternateEntries": [
    {
      "phoneNumber": "5131111112",
      "extension": "1112",
      "ringPattern": "Short-Short-Long",
      "alternateEntryId": 1
    },
    {
      "phoneNumber": null,
      "extension": null,
      "ringPattern": null,
      "alternateEntryId": 2
    },
    {
      "phoneNumber": null,
      "extension": null,
      "ringPattern": null,
      "alternateEntryId": 3
    },
    {
      "phoneNumber": null,
      "extension": null,
      "ringPattern": null,
      "alternateEntryId": 4
    },
    {
      "phoneNumber": null,
      "extension": null,
      "ringPattern": null,
      "alternateEntryId": 5
    },
    {
      "phoneNumber": null,
      "extension": null,
      "ringPattern": null,
      "alternateEntryId": 6
    },
    {
      "phoneNumber": null,
      "extension": null,
      "ringPattern": null,
      "alternateEntryId": 7
    },
    {
      "phoneNumber": null,
      "extension": null,
      "ringPattern": null,
      "alternateEntryId": 8
    },
    {
      "phoneNumber": null,
      "extension": null,
      "ringPattern": null,
      "alternateEntryId": 9
    },
    {
      "phoneNumber": null,
      "extension": null,
      "ringPattern": null,
      "alternateEntryId": 10
    }
  ]
}
```
