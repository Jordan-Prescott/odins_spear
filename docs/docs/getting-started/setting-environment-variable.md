# ⚠️ Setting Environment Variable

In the library to send requests an API object is built which needs your Odin username and password. The username is passed in as a variable however the password parameter is the key to your local environment variable where the value is your password. The API object will pull this password from your local machine and use it to authenticate.&#x20;

The reason for this is if you decide to save a Python file using the odin\_api library, it is best practice to not save passwords in these files in case they are exposed.

Before using the library set up an environment variable in your local machine and when instantiating an API object use the key in the password parameter. Below is an example where I set a variable and use it in the library.

Setting environment variable (Windows):

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

Passing environment variable to API object:

<pre class="language-python" data-overflow="wrap"><code class="lang-python"><strong>from odins_spear import api
</strong>
magic = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
</code></pre>

## Guide on setting environmental variables:&#x20;

{% embed url="https://chlee.co/how-to-setup-environment-variables-for-windows-mac-and-linux/" %}
