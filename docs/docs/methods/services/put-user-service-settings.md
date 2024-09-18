---
description: my_api.put.user_service_settings()
---

# ⚙️ PUT - User Service Settings

This method updates a Broadwork entity's service settings. This uses a dicitonary as an input to apply changes, the structure of this dictionary should mirror the API's expected format for updating service settings.

For more information and other examples please visit [here](https://doc.odinapi.net/#95bdfa78-9ba1-4c31-b7e8-6b4d5a1d37ff)

Most broadworks User Service Settings have varying options and choices that can be made:

```JSON
"Call Forwarding Busy": {"isActive": false, "forwardToPhoneNumber": 12314}
```

```JSON
"Call Forwarding Selective": {"isActive": false,"playRingReminder": false,"criteria": []}
```

Here you can see the differences between two similar services. To update settings using this function you must follow this structure.

You can either follow the link above for examples, or see the exmaple responses below to copy and paste the format. Otherwise, you can also use the output of get.user_service_settings().

### Parameters&#x20;

* user\_id (str): User ID of the target Broadworks entity.
* settings (dict): A dictionary containing the new settings to be applied.

### Returns

* Dict: A dictionary representing the updated service settings for the specified user.

### How To Use:

```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# Enabling Call Forward Always to ext 1509

settings = {"Call Forwarding Always": {"isActive": false, "forwardToPhoneNumber": 1509}}

# Enabling Call Forward Not Reachable to 1509 after 20 rings

settings = {'Call Forwarding No Answer': {'isActive': True, 'numberOfRings': 20, 'forwardToPhoneNumber': 1509}}

my_api.put.user_service_settings(
    "userId@domain.com",
    settings
)
```
{% endcode %}

### Example Data Returned (Formatted)
```json
{
  "userId": "9871515000@odinapi.net",
  "Advice Of Charge": {
    "isActive": false,
    "aocType": "During Call"
  },
  "Alternate Numbers": {
    "distinctiveRing": true,
    "alternateEntries": [
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 1
      },
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 2
      },
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 3
      },
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 4
      },
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 5
      },
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 6
      },
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 7
      },
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 8
      },
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 9
      },
      {
        "phoneNumber": null,
        "extension": null,
        "ringPattern": null,
        "alternateEntryId": 10
      }
    ]
  },
  "Anonymous Call Rejection": {
    "isActive": false
  },
  "Authentication": {
    "userName": 9871515000,
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin"
  },
  "Automatic Callback": {
    "isActive": false
  },
  "Automatic Hold/Retrieve": {
    "isActive": false,
    "recallTimerSeconds": 120
  },
  "Barge-in Exempt": {
    "isActive": true
  },
  "BroadWorks Anywhere": {
    "alertAllLocationsForClickToDialCalls": false,
    "alertAllLocationsForGroupPagingCalls": false,
    "phoneNumbers": []
  },
  "BroadWorks Mobility": {
    "isActive": false,
    "phonesToRing": "Fixed",
    "alertClickToDialCalls": false,
    "alertGroupPagingCalls": false,
    "enableDiversionInhibitor": false,
    "requireAnswerConfirmation": false,
    "broadworksCallControl": false,
    "useSettingLevel": "Group",
    "denyCallOriginations": false,
    "denyCallTerminations": false
  },
  "Busy Lamp Field": {
    "enableCallParkNotification": false,
    "users": []
  },
  "Call Forwarding Always": {
    "isActive": false,
    "forwardToPhoneNumber": 1234,
    "isRingSplashActive": false
  },
  "Call Forwarding Always Secondary": {
    "isActive": false,
    "isRingSplashActive": false
  },
  "Call Forwarding Busy": {
    "isActive": false
  },
  "Call Forwarding No Answer": {
    "isActive": false,
    "forwardToPhoneNumber": 12314,
    "numberOfRings": 2
  },
  "Call Forwarding Not Reachable": {
    "isActive": false
  },
  "Call Forwarding Selective": {
    "isActive": false,
    "playRingReminder": false,
    "criteria": []
  },
  "Call Notify": {
    "criteria": []
  },
  "Call Recording": {
    "recordingOption": "Never",
    "pauseResumeNotification": "None",
    "enableCallRecordingAnnouncement": false,
    "enableRecordCallRepeatWarningTone": false,
    "recordCallRepeatWarningToneTimerSeconds": 15,
    "enableVoiceMailRecording": false
  },
  "Call Transfer": {
    "isRecallActive": false,
    "recallNumberOfRings": 4,
    "useDiversionInhibitorForBlindTransfer": false,
    "useDiversionInhibitorForConsultativeCalls": false,
    "enableBusyCampOn": false,
    "busyCampOnSeconds": 120
  },
  "Call Waiting": {
    "isActive": true,
    "disableCallingLineIdDelivery": false
  },
  "Calling Line ID Blocking Override": {
    "isActive": false
  },
  "Calling Line ID Delivery Blocking": {
    "isActive": false
  },
  "Calling Name Delivery": {
    "isActiveForExternalCalls": true,
    "isActiveForInternalCalls": true
  },
  "Calling Name Retrieval": {
    "isActive": false
  },
  "Calling Number Delivery": {
    "isActiveForExternalCalls": true,
    "isActiveForInternalCalls": true
  },
  "Calling Party Category": {
    "category": "Ordinary"
  },
  "Charge Number": {
    "useChargeNumberForEnhancedTranslations": false,
    "sendChargeNumberToNetwork": true
  },
  "Classmark": [],
  "CommPilot Express": {
    "availableInOffice": {
      "busySetting": {
        "action": "Transfer To Voice Mail"
      },
      "noAnswerSetting": {
        "action": "Transfer To Voice Mail"
      }
    },
    "availableOutOfOffice": {
      "incomingCalls": {
        "action": "Transfer To Voice Mail"
      },
      "incomingCallNotify": {
        "sendEmail": "false"
      }
    },
    "busy": {
      "incomingCalls": {
        "sendCallsToVoiceMailExceptExcludedNumbers": "false"
      },
      "voiceMailNotify": {
        "sendEmail": "false"
      }
    },
    "unavailable": {
      "incomingCalls": {
        "sendCallsToVoiceMailExceptExcludedNumbers": "false"
      },
      "voiceMailGreeting": "No Answer"
    }
  },
  "Communication Barring User-Control": {
    "lockoutStatus": false,
    "profileTable": []
  },
  "Connected Line Identification Restriction": {
    "isActive": false
  },
  "Direct Route": {
    "outgoingDTGPolicy": "Direct Route DTG",
    "outgoingTrunkIdentityPolicy": "Direct Route Trunk Identity",
    "routes": []
  },
  "Directed Call Pickup with Barge-in": {
    "enableBargeInWarningTone": true,
    "enableAutomaticTargetSelection": false
  },
  "Do Not Disturb": {
    "isActive": false,
    "ringSplash": false
  },
  "Executive-Assistant": {
    "enableDivert": false,
    "executives": []
  },
  "External Calling Line ID Delivery": {
    "isActive": true
  },
  "External Custom Ringback": {
    "isActive": false,
    "useSettingLevel": "Service Provider"
  },
  "Fax Messaging": {
    "isActive": false,
    "aliases": []
  },
  "Group Night Forwarding": {
    "nightForwarding": "Use Group",
    "groupNightForwarding": "On"
  },
  "Hoteling Guest": {
    "isActive": false,
    "enableAssociationLimit": true,
    "associationLimitHours": 12
  },
  "Hoteling Host": {
    "isActive": false,
    "enforceAssociationLimit": true,
    "associationLimitHours": 24,
    "accessLevel": "Group"
  },
  "In-Call Service Activation": {
    "isActive": false
  },
  "Integrated IMP": {
    "isActive": false
  },
  "Intercept User": {
    "isActive": false,
    "announcementSelection": "Default",
    "inboundCallMode": "Intercept All",
    "alternateBlockingAnnouncement": false,
    "exemptInboundMobilityCalls": false,
    "disableParallelRingingToNetworkLocations": false,
    "routeToVoiceMail": false,
    "playNewPhoneNumber": false,
    "transferOnZeroToPhoneNumber": false,
    "outboundCallMode": "Block All",
    "exemptOutboundMobilityCalls": false,
    "rerouteOutboundCalls": false
  },
  "Internal Calling Line ID Delivery": {
    "isActive": true
  },
  "MWI Delivery to Mobile Endpoint": {
    "isActive": false
  },
  "Malicious Call Trace": {
    "isActive": false,
    "traceTypeSelection": "Answered Incoming",
    "traceForTimePeriod": false
  },
  "Number Portability Announcement": {
    "enable": false
  },
  "Physical Location": {
    "isActive": false
  },
  "Pre-alerting Announcement": {
    "isActive": false,
    "audioSelection": "Default",
    "videoSelection": "Default",
    "criteria": []
  },
  "Preferred Carrier User": {
    "intraLataCarrier": {
      "useGroupPreferredCarrier": "false"
    },
    "interLataCarrier": {
      "useGroupPreferredCarrier": "false"
    },
    "internationalCarrier": {
      "useGroupPreferredCarrier": "false"
    }
  },
  "Prepaid": {
    "isActive": false
  },
  "Priority Alert": {
    "isActive": false,
    "criteria": []
  },
  "Privacy": {
    "enableDirectoryPrivacy": false,
    "enableAutoAttendantExtensionDialingPrivacy": false,
    "enableAutoAttendantNameDialingPrivacy": false,
    "enablePhoneStatusPrivacy": false,
    "permittedMonitors": []
  },
  "Push to Talk": {
    "allowAutoAnswer": true,
    "outgoingConnectionSelection": "Two Way",
    "accessListSelection": "Allow Calls From Selected Users",
    "users": []
  },
  "Remote Office": {
    "isActive": false
  },
  "Route List": {
    "treatOriginationsAndPBXRedirectionsAsScreened": true,
    "useRouteListIdentityForNonEmergencyCalls": true,
    "useRouteListIdentityForEmergencyCalls": true,
    "assignedNumberPrefixTable": [],
    "dns": []
  },
  "Security Classification": [],
  "Selective Call Acceptance": [],
  "Selective Call Rejection": [],
  "Sequential Ring": {
    "ringBaseLocationFirst": true,
    "baseLocationNumberOfRings": 2,
    "continueIfBaseLocationIsBusy": true,
    "callerMayStopSearch": true,
    "locations": [
      {
        "phoneNumber": "",
        "numberOfRings": 3,
        "answerConfirmationRequired": false
      },
      {
        "phoneNumber": "",
        "numberOfRings": 3,
        "answerConfirmationRequired": false
      },
      {
        "phoneNumber": "",
        "numberOfRings": 3,
        "answerConfirmationRequired": false
      },
      {
        "phoneNumber": "",
        "numberOfRings": 3,
        "answerConfirmationRequired": false
      },
      {
        "phoneNumber": "",
        "numberOfRings": 3,
        "answerConfirmationRequired": false
      }
    ],
    "criteria": []
  },
  "Shared Call Appearance": {
    "alertAllAppearancesForClickToDialCalls": false,
    "alertAllAppearancesForGroupPagingCalls": false,
    "maxAppearances": 35,
    "allowSCACallRetrieve": false,
    "enableMultipleCallArrangement": true,
    "multipleCallArrangementIsActive": true,
    "allowBridgingBetweenLocations": false,
    "bridgeWarningTone": "None",
    "enableCallParkNotification": false,
    "endpoints": []
  },
  "Silent Alerting": {
    "isActive": false
  },
  "Simultaneous Ring Personal": {
    "isActive": false,
    "doNotRingIfOnCall": true,
    "criteria": [],
    "locations": []
  },
  "Speed Dial 100": {
    "speedCodes": []
  },
  "Speed Dial 8": {
    "speedCodes": [
      {
        "speedCode": "2"
      },
      {
        "speedCode": "3"
      },
      {
        "speedCode": "4"
      },
      {
        "speedCode": "5"
      },
      {
        "speedCode": "6"
      },
      {
        "speedCode": "7"
      },
      {
        "speedCode": "8"
      },
      {
        "speedCode": "9"
      }
    ]
  },
  "Terminating Alternate Trunk Identity": [],
  "Third-Party Voice Mail Support": {
    "isActive": false,
    "busyRedirectToVoiceMail": true,
    "noAnswerRedirectToVoiceMail": true,
    "serverSelection": "Group Mail Server",
    "mailboxIdType": "User Or Group Phone Number",
    "noAnswerNumberOfRings": 2,
    "alwaysRedirectToVoiceMail": false,
    "outOfPrimaryZoneRedirectToVoiceMail": false
  },
  "Two-Stage Dialing": {
    "isActive": true,
    "allowActivationWithUserAddresses": false
  },
  "Video Add-On": {
    "isActive": false,
    "maxOriginatingCallDelaySeconds": 2
  },
  "Voice Messaging User": {
    "Voice Messaging User": {
      "isActive": false,
      "processing": "Unified Voice and Email Messaging",
      "voiceMessageDeliveryEmailAddress": "mreverman@parkbenchsolutions.com",
      "usePhoneMessageWaitingIndicator": true,
      "sendVoiceMessageNotifyEmail": false,
      "sendCarbonCopyVoiceMessage": false,
      "transferOnZeroToPhoneNumber": false,
      "alwaysRedirectToVoiceMail": false,
      "busyRedirectToVoiceMail": true,
      "noAnswerRedirectToVoiceMail": true,
      "outOfPrimaryZoneRedirectToVoiceMail": false,
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "userId": "9871515000@odinapi.net"
    },
    "Voice Messaging User Advanced": {
      "mailServerSelection": "Group Mail Server",
      "groupMailServerEmailAddress": "mreverman@parkbenchsolutions.com",
      "groupMailServerUserId": "vm9871515000",
      "useGroupDefaultMailServerFullMailboxLimit": true,
      "personalMailServerProtocol": "POP3",
      "personalMailServerRealDeleteForImap": false,
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "userId": "9871515000@odinapi.net"
    },
    "Voice Messaging User Greeting": {
      "busyAnnouncementSelection": "Default",
      "noAnswerAnnouncementSelection": "Default",
      "extendedAwayEnabled": false,
      "extendedAwayDisableMessageDeposit": true,
      "noAnswerNumberOfRings": 2,
      "disableMessageDeposit": false,
      "disableMessageDepositAction": "Disconnect",
      "userId": "9871515000@odinapi.net"
    },
    "Voice Messaging User Voice Portal": {
      "usePersonalizedName": true,
      "voicePortalAutoLogin": true,
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "userId": "9871515000@odinapi.net",
      "audioFile": {
        "description": "aa1 copy is a copy of the Let's go song",
        "mediaType": "WAV"
      }
    }
  },
  "Voice Portal Calling": {
    "isActive": false
  },
  "Zone Calling Restrictions": []
}
```
```