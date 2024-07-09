# ⚙️ Create API Object

The API object is the core object of the library, all functionality is accessed through this object. The first step is to create the object and pass it the base URL of the API, your username, and the environment variable.&#x20;

{% code overflow="wrap" lineNumbers="true" %}
```python
from odins_spear import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
```
{% endcode %}

Once you have built the object the next step is to authenticate it, this authorizes the object to interact with the Odin API it is the equivalent of you logging in through the web portal. To authenticate this call the .authenticate() method on the object.&#x20;

<pre class="language-python" data-overflow="wrap" data-line-numbers><code class="lang-python"><strong>from odins_spear import api
</strong><strong>
</strong><strong>my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
</strong>my_api.authenticate()
</code></pre>

This method can raise an OAApiAuthenticationFail error, which means that the API has failed to authenticate and it will give you some details on potential issues. If this does not raise an error the API object is authenticated and now authorized to use all other methods.&#x20;

{% hint style="info" %}
More than one object can be built for multiple odin instances.
{% endhint %}

#### Check out API object details:

[Broken link](broken-reference "mention")
