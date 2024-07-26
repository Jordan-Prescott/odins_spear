# 🔢 Group Users Call Statistics

Generates CSV file detailing all users in a single groups outgoing and incoming call statistics for a specified time range.

{% hint style="danger" %}
Data is only guaranteed for 3 months, if your requesting over 3 months all data may not be saved and output should be reviewed. This is an Odin limitation.&#x20;
{% endhint %}

{% hint style="info" %}
This feature can take a good amount of time to complete depending on the size of your group. For example a group containing 3000 users will take around an hour to complete.&#x20;

This is being worked on and we hope to speed it up for you soon! Thank you.
{% endhint %}

We have found that customers like to review how busy their users are and identify any that are not in use so they are lower their bill. This report identifies exactly that showing all users call statistics over a maximum guaranteed period of 3 months. If a user has not made a call in that time this can be easily spotted as the row will consist of only 0's (See example out below).

### Example Output

<figure><img src="../../../.gitbook/assets/image (30).png" alt=""><figcaption><p>Output Example</p></figcaption></figure>

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise where group is hosted.&#x20;
* group\_id (str): Target Group you would like to know user statistics for.&#x20;
* start\_date (str): Start date of desired time period. Date must follow format 'YYYY-MM-DD'&#x20;
* end\_date (str, optional): End date of desired time period. Date must follow format 'YYYY-MM-DD'.\
  If this date is the same as Start date you do not need this parameter. Defaults to None.&#x20;
* start\_time (_type_, optional): Start time of desired time period. Time must follow formate 'HH:MM:SS'. If you do not need to filter by time and want the whole day leave this parameter. Defaults to "00:00:00". MAX Request is 3 months.&#x20;
* end\_time (_type_, optional): End time of desired time period. Time must follow formate 'HH:MM:SS'. If you do not need to filter by time and want the whole day leave this parameter. Defaults to "23:59:59". MAX Request is 3 months.&#x20;
* time\_zone (str, optional): A specified time you would like to see call records in.&#x20;

### Return

* None: This will generate a CSV file with the report in the folder 'os\_reports'. Check this folder once script has completed.

The script makes use of the following methods:

```python
api.get.users()
api.get.users_stats()
api.get.user_services()
```

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear.api import Api

my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# Whole day in date range
my_api.reporter.group_users_call_statistics(
    "serviceProviderID",
    "groupID",
    "11-04-2024",
    "14-06-2024",
)

# Specific time during day and in EST timezone
my_api.reporter.group_users_call_statistics(
    "serviceProviderID",
    "groupID",
    "11-04-2024",
    "14-06-2024",
    start_time = "09:00:00",
    end_time: str = "17:00:00",
    time_zone: str = "EST"
)
```
{% endcode %}

### Terminal Output

{% code overflow="wrap" fullWidth="false" %}
```
Start.
Fetching list of users in GroupID.
Fetching individual stats for each user. This may take several minutes.: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 90/90 [01:34<00:00,  1.04s/it]
Formatting individual stats for each user.: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 90/90 [00:00<00:00, 42144.40it/s]

End.
```
{% endcode %}
