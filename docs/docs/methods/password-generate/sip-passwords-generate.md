---
description: my_api.get.sip_passwords_generate()
---

# 🗝️ GET - SIP Passwords Generate

Generates multiple SIP passwords to the limit set in parameters. Defaults to 10.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where Group is located.&#x20;
* group\_id (str): Group ID to generate SIP password for.&#x20;
* limit (int, optional): Number of passwords api will return. Defaults to 10.

### Returns

* dict: Mutliple SIP passwords generated according to the groups rules.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.sip_passwords_generate(
    "serviceProviderId",
    "groupID",
    limit= 15
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "passwords": [
    "A9y2Rk[L:E2+94JW{6",
    "#OZmK3-HI7s9).N4WJ",
    "*_Z#6@J2cUBf3?-7W0",
    "X{_z%O+06LXJVC7K19",
    "!*DFJ1O(^B3041#:Zb",
    "7#*6+)Q*A3:L6$e1UT",
    "!w_PI-H691N7w+qBO^",
    "@j4r2R[{HB2^pO7IL9",
    "fT3{_!2n8NJN19:fF}",
    "41nQT{Az6j2#%uE8!F",
    "8T_9R%14?W5r1^8aA[",
    "2R!lK3]K2:6n^DJbO1",
    "_O]C26c{4Pg7A$*X.N",
    "*Ilr1E0We_:G$qN59@",
    "#%9cH$0B3QH0qJaZ{4",
    ".V$F2?(U_Lx6%Y_83R",
    "q:85a4^xTZ0*C_HE!c",
    "Zc-C+6]4N)5I0$eFC7",
    "S9[87y$RZ3jU8C?A0_",
    "SpYM([1yT2%5N2F0M*",
    "_4W_8x?Q:6EH3(D9Ow",
    "?Z$HqF2tZ6__S7+9z?",
    "3]]5wP)M$^OD8#1DK?",
    "?gPK16q7B7o@#.:0uQ",
    "8%yFK*N{I5QUi^7$I9",
    "S_X^810L)n@z3_Ia.e",
    "WR*6h_{bA2*{HC4O(1",
    "?@0%AWS13mOE_%bY-5",
    "2ZN^*:M@89Sq+T1xD_",
    ":89]WM@5SqJ.B@s}h4",
    "F%s2_68TKGH269^?DE",
    "8GR+{d5_-t6a7AlNJY",
    "-Lij5}8$KV2+IAd46X",
    "7?orTIST(53*X21RA%",
    "Y1![Pp0:_U4Bo_ZlI2",
    "4oK.[2*Rt$NB8PH1VQ",
    "19MDr}%03R*}U.A(7J",
    "NJI[L.]o5341P82If(",
    "FL49D^__5V?d:6{pI7",
    "ZB28wCp-*P?lS!19D0",
    "SC!XOI%u]97GO?I5$2",
    "_UYPC4^Sc}3.Z86X+F",
    "9diO_?QD7v166s.Y3!",
    "KA4]r8$Y.#5:J9Nzwj",
    "D0r.Q4K2x%G[8w_XP)"
  ]
}{
  "password": "8!01T_8Hk{R6"
}
```
