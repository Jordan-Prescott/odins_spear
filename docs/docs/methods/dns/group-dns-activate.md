---
description: my_api.put.group_dns_activate()
---

# 1️⃣ PUT - Group DNs Activate

Update activation state of a list of numbers assigned to a group.

{% hint style="danger" %}
format of number must follow: "+{country code}-{number}"
{% endhint %}

### Parameters&#x20;

* service\_provider\_id (str): Service provider ID where the group is located.&#x20;
* group\_id (str): Group ID where numbers are hosted.&#x20;
* activated (bool): True to activate number and False to deactivate.&#x20;
* numbers (list): List of target numbers to update. These must be strings and follow correct format.

### Returns

* JSON: All numbers assigned to group with activation state.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

numbers = [
    "+1-1234567891",
    "+1-1234567892",
    "+1-1234567893",
]

my_api.put.group_dns_activate(
    "serviceProviderId",
    "groupID",
    activated =True,
    numbers =numbers
)
```
{% endcode %}

### Example Returned Data (Formatted)

```json
{
  "serviceProviderId": "ent.odin",
  "groupId": "grp.odin",
  "dns": [
    {
      "assigned": true,
      "activated": true,
      "min": "+1-2345678900",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-2345678908",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5123875553",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-5131004000",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-5132011000",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-5132198500",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-5132337654",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5132337655",
      "max": null
    },
    {
      "assigned": true,
      "activated": false,
      "min": "+1-5132655005",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-5132655006",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5132655007",
      "max": "+1-5132655010"
    },
    {
      "assigned": true,
      "activated": false,
      "min": "+1-5132851520",
      "max": "+1-5132851521"
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-5133825000",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-5134031000",
      "max": "+1-5134031001"
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5134031002",
      "max": "+1-5134031003"
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-5134221000",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5134221001",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-5134221002",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5136549851",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5136549856",
      "max": "+1-5136549859"
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5136569842",
      "max": "+1-5136569844"
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5136569851",
      "max": "+1-5136569852"
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5136569856",
      "max": "+1-5136569859"
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5138881000",
      "max": "+1-5138881004"
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5139228863",
      "max": "+1-5139228870"
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5223875553",
      "max": "+1-5223875554"
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-5551001000",
      "max": "+1-5551001001"
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-8783449000",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-8783449001",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-8783449002",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-8783449003",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-8783449004",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-9135559716",
      "max": null
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-9871515000",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-9871515001",
      "max": "+1-9871515002"
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-9871515003",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-9871515004",
      "max": "+1-9871515006"
    },
    {
      "assigned": true,
      "activated": true,
      "min": "+1-9871515007",
      "max": null
    },
    {
      "assigned": false,
      "activated": true,
      "min": "+1-9871515008",
      "max": "+1-9871515010"
    }
  ]
}
```
