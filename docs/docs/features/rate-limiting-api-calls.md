# 🛑 Rate Limiting API Calls

The API object has a default parameter of 'rate\_limit' set to True which limits the amounts of API calls the library will make to 5 calls per 1 second. If the limit is reach the system will wait for the limit to pass before executing the next 5 calls.&#x20;

This limiting will ease the pressure on the API and hopefully stopping any negative impact on systems such as significant resource drainage leading to outages or poor performance.&#x20;

{% hint style="info" %}
Odin does not imply any limitations on the usage of their API and this feature is a precaution.&#x20;
{% endhint %}

## Disabling Rate Limiting

The limitation is applied by default however this can be removed by passing in the `rate_limit` argument set to `False` when instantiating an API object.

{% hint style="danger" %}
This will remove the limitation of 5 calls per 1 second allowing the library to send as many API requests as it can.
{% endhint %}

```python
my_api = Api(base_url="https://yourSystemsURL/api/v2", username="John.Smith", 
               password="ENV_VARIABLE", rate_limit=False)
```
