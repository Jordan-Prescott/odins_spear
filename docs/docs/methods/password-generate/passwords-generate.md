---
description: my_api.get.passwords_generate()
---

# 🔓 GET - Passwords Generate

Generates a single passwords following the groups rules.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where Group is located.&#x20;
* group\_id (str): Group ID to generate password for.&#x20;
* limit (int, optional): Number of passwords api will return. Defaults to 10.

### Returns

* dict: Multiple passwords generated according to the groups rules.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.passwords_generate(
    "serviceProviderId",
    "groupID",
    limit= 100
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "passwords": [
    ".:2hnk:VYW80G[!5@-",
    "?f-O6Ui$8*Nd3L[?2-",
    "5wGV8M[@I%1OE4-(3.",
    "I3%^O_8kC!9rSUG}4l",
    "27@{P4[leD9A_xWNY^",
    "4{)Y2Y.LM9G5c?7G}n",
    "$38VZF[kP%#691U^1_",
    "22T64[P-WE3_43gbe^",
    "7@*5cnG(S1I6XApW[O",
    "Pe9V4%@$3sb:R}5w}F",
    "n:3a97%W]8Y4$TQKO*",
    "V8]*YCJ#8^3gKr09sK",
    "gW^5[97fJ0)p@(1TZX",
    "X3M5z-?1_n:%OWR2I1",
    "9vNMTZV6e7?WW5#_n-",
    "AQ*8#$:baP7WIZ^*02",
    "w781U?%F]u226-WDcH",
    "ojK_XE%7#g^9J3E*4T",
    "73Va(51^Gh.A0R0U2_",
    "vXWBO4f)(82pR7?^Zy",
    "14Z4o7_Rl5}!6_-[HD",
    "fPy$2:*jJ[D59H7@2Q",
    "Z_OBT7Hn315rE_}7r+",
    "^W%1NDKq_8PX#^9Ra6",
    "P:.R[361M(0}GdDA6s",
    "WX3B?S_@5Cj?(20}^E",
    "Ryhp97CC}1$Q)EN6@Y",
    "3X+(B*Y]G_h%25%9LV",
    "4[22k#_PV8(AFFX_9u",
    "27]VHWWRB}1nfT*-4c",
    "(eR30NJ50*WL:8m^D+",
    "N.8(C7U9NvD$61^6:I",
    "53S0sE71_6B_H!?(BO",
    "YP6VM$*5!4j3}Oxy%9",
    "Po^683[I+75_*ZwK$H",
    ":51[Im6}6PfV#4[Z(N",
    "Up12k#:Gr{3}ED9_cQ",
    "8*UjFD^6.HH4v?d9w*",
    "%W5+584MkQ1$3cJ_lK",
    "9G5-348[RTj.!w0)oP",
    "p7}Y5--30]Z@Pt!DHf",
    "_pY8o]#TMD5IH-4a{1",
    "]!e5MW8J{w7:.VIp3@",
    "{)D003(-37V.8lZh{S",
    "0(CD$:.Yt50S8-PS27",
    "u+{U4xS8)^0LWH7S[X",
    ":[d!s_+3@R60BNIl9^",
    "#LA@m2[5.O@TkXP+68",
    "3dy5{b7}$Ak_0$ZJW^",
    "W?^3BN51M!uFIu{_9r",
    "g5UYF5_k9V30NX+(?2",
    "D7L{_!++1N}PuJ^46T",
    "*#DD:6K.L2q0S:YO_1",
    "XQ0@+7_G4P+6w3}WFL",
    "70$FWLl1r{QZ*O:4)3",
    "J1y3*q$UYN4T{o2p8@",
    "w@uBv!HP*5924N:TZ%",
    "n$6Qe_9+^X83aGWN_E",
    "m2_?3Q1!@y69E}*LgG",
    "5G2#T-YV.Cu!g84M2D"
  ]
}{
  "password": "?+^8RZ40MeC3+:i.BQ"
}
```
