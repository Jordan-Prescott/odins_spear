---
description: my_api.put.auto_attendant_submenu()
---

# 📖 PUT - Auto Attendant Submenu

This method allows you to update the configuration of the submenus for your AAs. This method only allows you to update one submenu at a time but can be placed in a look to update all submenus you may have.&#x20;

### Parameters&#x20;

* auto\_attendant\_user\_id (str): Service user ID of your auto attendant.
* submenu\_id (str): Service user ID of your submenu.
* updates (dict): Updates your applying to your submenu.

### Return

* None: This method does not return any specific value.

### How To Use:

<pre class="language-python"><code class="lang-python">
my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_changes = {
                "announcementSelection":"Personal",
                "enableLevelExtensionDialing":False,
                "keys":[
                	{"key":"0","action":"Transfer To Operator","description":"Operator","phoneNumber":2025}
                ]
<strong>            }
</strong>
my_api.put.auto_attendant_submenu(
    auto_attendant_user_ids= "test@domain.com",
    submenu_id= "Test1"
    updates= my_changes
)
</code></pre>

#### Result:

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

&#x20;
