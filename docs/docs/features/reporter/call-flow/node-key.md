# 🔑 Node Key

## Call Flow Nodes

<figure><img src="../../../../.gitbook/assets/call_flow.jpg" alt=""><figcaption><p>Simple call flow example of calls to the main number attached to an Auto Attendant</p></figcaption></figure>

<table><thead><tr><th width="170">Node</th><th width="176">Shape/ Colour</th><th>Details</th></tr></thead><tbody><tr><td>Start/ Entry Node</td><td>Black Box Pointed Edges</td><td>This highlights the start of the flow. This is simply to guide the user to the first Broadworks Entity in the call flow. </td></tr><tr><td>Auto Attendant (AA)</td><td>Dark Green Record</td><td>This node shows the extension number in the middle of the node and also shows the key number it forwards calls to on each edge. In the above example key 2 forwards to 104.</td></tr><tr><td>Call Center (CC)</td><td>Purple Record</td><td>This node represents a Call Center that will contain agents. Each edge will show the type of routing to the connecting node. For example in the above the Call Center 'OF' - OverFlows to 2001.</td></tr><tr><td>Hunt Group (HG)</td><td>Pink Record</td><td>This is a Hunt Group which will contain users. Like the CC node it will also highlight the type of call forwarding to whatever the next connecting node is. In the above the  Hunt Group 2001 'CFNR' Call Forward Not Reachable to 102.</td></tr><tr><td>User (U)</td><td>Yellow Record</td><td>This node is a User and like the CC and HG it will show the type of call forwarding to the connecting node. In the above user 104 'CFB' Call Forwards Busy to HG 2001.</td></tr><tr><td>Exit Node</td><td>White Circle with Black Border</td><td>These nodes indicate calls leave the Broadworks system. In the above AA 3001 forwards calls to '0123456789' on key 3 exiting the system.</td></tr></tbody></table>

{% hint style="info" %}
What the CFB does 'CFB' stand for! You can find all the abbreviations documented in the Abbreviation Key page. Link below.
{% endhint %}

{% content-ref url="abbreviation-key.md" %}
[abbreviation-key.md](abbreviation-key.md)
{% endcontent-ref %}
