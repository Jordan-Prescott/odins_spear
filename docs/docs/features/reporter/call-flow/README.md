# 🤙 Call Flow

Generates a visual call flow for a dedicated number for example calls to 0.

There is now no need to spend hours interrogating how calls to 0 flows through your Braodworks/ Odin system building a call flow for management or to send to customers. This can now be done in seconds with Odins Spear Reporter. Give this feature the number (0), the number type (DN, Extension, Alias), and what its attached to (User, Hunt Group etc) and the feature will generate a flow like the below for you!

{% hint style="warning" %}
You will need to download Graphviz in order to use this feature. Follow the instruction here [graphviz.md](graphviz.md "mention")
{% endhint %}

<figure><img src="../../../../.gitbook/assets/call_flow.jpg" alt=""><figcaption><p>Simple call flow example of calls to the main number attached to an Auto Attendant</p></figcaption></figure>

### Making Sense of The Graph

What is does a red circle with 3001 in it mean and what does 'CFB' stand for? To make sense of the graph you will need to see the Node Key and the Abbreviation Key found below:

{% content-ref url="node-key.md" %}
[node-key.md](node-key.md)
{% endcontent-ref %}

{% content-ref url="abbreviation-key.md" %}
[abbreviation-key.md](abbreviation-key.md)
{% endcontent-ref %}

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise where group is hosted.&#x20;
* group\_id (str): Group ID where target number for call flow is located.&#x20;
* number (str): Target number for call flow. NOTE: do not include the area code e.g. "123456789"
* number\_type (str): Type of number, options: "dn": Direct Number, "extension": Extension, "alias": Alias
* broadworks\_entity\_type (str): Broadworks entity type target number is associated with.\
  Options: "auto\_attendant": Auto Attendant, "call\_center": Call Center, "hunt\_group": Hunt Group, "user": User

### Return

* None: This will generate a SVG file with the call flow in the folder 'os\_reports'. Check this folder once script has complete.

The script makes use of the following methods:

```python
api.get.service_provider()
api.get.group()
api.get.auto_attendants()
api.get.auto_attendant()
api.get.users()
api.get.bulk_call_forwarding_always()
api.get.bulk_call_forwarding_busy()
api.get.bulk_call_forwarding_no_answer()
api.get.bulk_call_forwarding_not_reachable()
api.get.user_call_forwarding_always()
api.get.user_call_forwarding_busy()
api.get.user_call_forwarding_no_answer()
api.get.user_call_forwarding_no_answer()
api.get.group_call_center()
api.get.group_call_centers()
api.get.group_call_center()
api.get.group_call_center_overflow()
api.get.group_call_center_stranded_calls()
api.get.group_call_center_stranded_calls_unavailable()
api.get.group_call_center_forced_forwarding()
api.get.group_hunt_groups()
api.get.group_hunt_group()
```

### How To Use:

{% code overflow="wrap" %}
```python
from odin_api import api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# Generates a call flow chart for the number 123456789.
my_api.reporter.call_flow(
    "serviceProviderId",
    "groupId",
    "123456789",
    "dn",
    "user"
)
```
{% endcode %}

### Terminal Output

{% code overflow="wrap" fullWidth="false" %}
```
Start.

Fetching Service Provider & Group details.
Fetching all Auto Attendants.: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.27it/s]
Fetching all Users.: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 11/11 [00:06<00:00,  1.82it/s]
Fetching all Call Centers.: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:04<00:00,  4.30s/it]
Fetching all Hunt Groups.: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 5/5 [00:05<00:00,  1.13s/it]
Gathering nodes in flow.
Generating report.
Saving report.

End.
```
{% endcode %}
