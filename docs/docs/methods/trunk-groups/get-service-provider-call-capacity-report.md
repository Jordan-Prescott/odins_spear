---
description: api.get.service_provider_trunk_call_capacity_report()
---

# 📂 GET - Service Provider Call Capacity Report

Fetches trunk call capacity details of Service Provider/ Enterprise and all Groups in the SP/ ENT.

{% hint style="info" %}
Note the feature 'Service Provider Trunking Capacity' in Scripter also achieves this. Link below.
{% endhint %}

{% content-ref url="../../features/scripter/service-provider-trunking-capacity.md" %}
[service-provider-trunking-capacity.md](../../features/scripter/service-provider-trunking-capacity.md)
{% endcontent-ref %}

### Parameters&#x20;

* servive\_provider\_id (str): Target Service Provider/ Enterprise ID.

### Returns

* Dict: Breakdown of all trunk call capacity details of target Service Provider/ Enterprise and all Groups in the target SP/ ENT.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.service_provider_trunk_call_capacity_report(
    "ServiceProviderID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "serviceProviderId": "ent.odin",
  "serviceProviderTrunkCapacity": {
    "serviceProviderId": "ent.odin",
    "maxActiveCalls": 40,
    "burstingMaxActiveCalls": -1
  },
  "groups": [
    {
      "groupId": "connections.demo",
      "groupName": "connections.demo",
      "userLimit": 200,
      "service": {
        "serviceName": "Trunk Group",
        "authorized": true,
        "assigned": true,
        "limited": "Limited",
        "quantity": 1,
        "usage": 0,
        "licensed": true,
        "allowed": -1,
        "alias": "Trunk Group"
      },
      "groupTrunkCapacity": {
        "maxActiveCalls": 10,
        "maxAvailableActiveCalls": 40,
        "burstingMaxActiveCalls": 0,
        "burstingMaxAvailableActiveCalls": -1,
        "serviceProviderId": "ent.odin",
        "groupId": "connections.demo"
      }
    },
    {
      "groupId": "group.odin",
      "groupName": "odin Group",
      "userLimit": 100,
      "service": {
        "serviceName": "Trunk Group",
        "authorized": true,
        "assigned": true,
        "limited": "Unlimited",
        "quantity": -1,
        "usage": 4,
        "licensed": true,
        "allowed": -1,
        "alias": "Trunk Group"
      },
      "groupTrunkCapacity": {
        "maxActiveCalls": 15,
        "maxAvailableActiveCalls": 40,
        "burstingMaxActiveCalls": 0,
        "burstingMaxAvailableActiveCalls": -1,
        "serviceProviderId": "ent.odin",
        "groupId": "group.odin"
      }
    },
    {
      "groupId": "phonism.test",
      "groupName": "Phonism Test",
      "userLimit": 25,
      "service": {
        "serviceName": "Trunk Group",
        "authorized": true,
        "assigned": true,
        "limited": "Unlimited",
        "quantity": -1,
        "usage": 0,
        "licensed": true,
        "allowed": -1,
        "alias": "Trunk Group"
      },
      "groupTrunkCapacity": {
        "maxActiveCalls": 40,
        "maxAvailableActiveCalls": 40,
        "burstingMaxActiveCalls": 0,
        "burstingMaxAvailableActiveCalls": -1,
        "serviceProviderId": "ent.odin",
        "groupId": "phonism.test"
      }
    }
  ]
}
```
