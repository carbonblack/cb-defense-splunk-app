# Overview
Welcome to the Cb Defense App for Splunk.

The Cb Defense App for Splunk integrates Cb Defense with Splunk Enterprise! Please ensure that the [Cb Defense Add-on for Splunk](https://splunkbase.splunk.com/app/3545/) is installed before installing this app, as this app requires the Add-on to function. 

The V1.0.0 Release includes pre-built visualizations from Cb's Internal Threat researchers:
Providing a thorough overview of Cb Defense environments as well as dashboards to  search through threat and policy notifications, view and manipulate device status, etc.

# Main Features

- Cb Defense Overview Dashboard
  - Comprehensive Overview of your Cb Defense data in Splunk
  - view total detections, policy actions, rare applications
  - triage threats by severity
- Threat Search
  - geoip map of threats based on severity
  - additional table of threat information
  - searchable (SPL) to isolate threat events of interest
- Policy Action Search
  - geoip map of Policy Actions by reputation
  - tabular display of policy activities
  - searchable (SPL) to isolate policy events of interest
- Login Map (Splunk)
  - geoip map and table of Logins (attempted and successful)  to Splunk instances
- Device Search
  - powered by the `devicesearch` custom search command
  - uses the Cb Defense REST API to retrieve device status information
  - geoip map of devices by external IPs + table of the same
  - enter a [device query](https://developer.carbonblack.com/reference/cb-defense/1/rest-api/#device-status) to filter results like ‘hostname:WIN-1984VBRULES’ or ‘ipAddress:172.17.178.1’
  
## Adaptive Response framework and Splunk Enterprise Security integration. 

Currently supported adaptive response actions:
- *Change Cb Defense Sensor Policy*: Change the assigned security policy of one or more Cb Defense devices based on :  IP address, hostname or deviceId in an event
- Fully integrated with existing alert & notable event framework in Splunk Enterprise Security. 
-  [Host Name Matching as per ](https://developer.carbonblack.com/reference/cb-defense/1/rest-api/#device-status)
    - use 'hostnameexact' inptutype for exact matching and 'hostname' for in-exact 

# Requirements:

(hard) - Cb Defense Add-on for Splunk

# Installation & Setup/Configuration

Download the app from Splunkbase, or build from the source available on github.

##(basic)

Use the gear icon from the Splunk left hand navigation bar to 'manage apps' - select Cb Defense and click 'setup'

Enter the (sans protocol, https is implied and enforced) base URL  for your Cb Defense API endpoint. For instance, “api-eap01.conferdeploy.net” not https://api-eap01.conferdeploy.net/integrationServices/V3/Notifications

Enter your API Key (Must be type API or Live Response ) in the API Key input field.

Enter your Connector Id (Must be type API or Live Response) in the Connector ID input Field. 

##(advanced)

The app comes loaded with a search macro `cbdefense` in default/macros.conf that defines Carbon Black Defense events. This is used to power most of the visualizations. 
In order to support all use cases, it defaults to :
`index=* sourcetype=(carbonblack:defense:json)`

If you would like to only search specific indexes, change the macro (UI accessible, or on disk).

For instance, if you would like to use the 'carbonblack' index change the macro to indicate index="carbonblack".

#Adaptive Response Configuration

The Change Cb Defense Change Sensor Policy Adaptive Response action has 3 important configuration options:
- 'inputtype' either Ip Address, deviceId , hostname, or hostname exact
  - This option specifies the intended indicator in the incoming result set
  - The indicator can be an ‘Ip Address’ (IPV4) , a deviceId (an integer) or a hostname (choose hostnameexact for exact-matching - otherwise hostnames will be matched as per the Cb Defense Rest API)
- 'fieldname' - the field in your result set to target, for instance deviceInfo.deviceId
  - ex , when inputtype = deviceId, fieldname = deviceInfo.deviceId the modular action will try to find a sensor by the deviceId in the 'deviceInfo.deviceId' of the incoming result set
-  Policy Name - the Cb Defense Policy to be applied to the targeted sensors. The policy must exist.  For instance 'default' or 'Restrictive_Windows_Workstation' .  
 - note: If you try to change from policy A to policy A for sensor B , it will always succeed.
##example data and configuration
`{"eventTime": 1517863503153, "policyAction": {"applicationName": "svchost.exe", "action": null, "reputation": "TRUSTED_WHITE_LIST", "sha256Hash": "1d35014d937e02ee090a0cfc903ee6e6b1b65c832694519f2b4dc4c74d3eb0fd"}, "eventDescription": "[jason-splunk-test-action-deny] [Confer has blocked a threat for you.] [An executable was RUN_BLOCK on a device registered to jgarman+po@carbonblack.com.] [Group: jan09-demo] [Device: WIN-IA9NQ1GN8OI] [SHA256: 1d35014d937e02ee090a0cfc903ee6e6b1b65c832694519f2b4dc4c74d3eb0fd]\n", "url": "https://defense-eap01.conferdeploy.net/investigate?s[searchWindow]=ALL&s[c][QUERY_STRING_TYPE][0]=f05da5560ab411e8834a939ef3e75232&s[c][DEVICE_ID][0]=5798", "deviceInfo": {"deviceName": "WIN-IA9NQ1GN8OI", "targetPriorityCode": 0, "internalIpAddress": "172.22.5.141", "deviceHostName": null, "groupName": "jan09-demo", "externalIpAddress": "70.106.217.80", "deviceType": "WINDOWS", "deviceId": 5798, "targetPriorityType": "LOW", "email": "jgarman+po@carbonblack.com", "deviceVersion": null}, "ruleName": "jason-splunk-test-action-deny", "type": "POLICY_ACTION"}
`
We can change sensor policy by hostname using inputtype = hostname or hostnameexact, and targetig the 'deviceInfo.deviceName' field. 
To target the deviceId, use deviceInfo.deviceId and inputtype = hostname
In general, Splunk operators are not limited to using only the dataprovided by the Cb Defense Add-on for Splunk - but must configure the Adaptive Response action appropriately. 

#Debugging and Logging information
The Add-On log level and debugging configuration is seperate from the App. If you're having problems getting data into Splunk, raise the log level in the Add-On and check the add-on logs. 

The App logs to the $SPLUNK_HOME/var/log directory.
Log files of interest:

- log file for the adaptive response action is changepolicy_modalert.log
`2018-03-03 22:37:44,340+0000 INFO sendmodaction - signature="Successfully created splunk events" action_name="changepolicy" sid="1520116660.228" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520116560_122" rid="0" orig_rid="1748" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc" event_count="1"
2018-03-03 23:06:38,595+0000 INFO sendmodaction - signature="Invoking modular action" action_name="changepolicy" sid="1520118396.496" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520118300_338" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc"
2018-03-03 23:06:38,631+0000 INFO Changing policy for device WIN-IA9NQ1GN8OI by hostnameexact to policy default
2018-03-03 23:06:39,636+0000 INFO Sensor WIN-IA9NQ1GN8OI now assigned to policy default
2018-03-03 23:06:39,636+0000 INFO sendmodaction - signature="Successfully Changed Policy" action_name="changepolicy" sid="1520118396.496" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520118300_338" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc" action_status="success"
2018-03-03 23:06:48,907+0000 INFO sendmodaction - signature="Invoking modular action" action_name="changepolicy" sid="1520118405.497" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520118300_338" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc"
2018-03-03 23:06:48,936+0000 INFO Changing policy for device WIN-IA9NQ1GN8OI by hostname to policy default
2018-03-03 23:06:50,732+0000 INFO Sensor WIN-IA9NQ1GN8OI now assigned to policy default
2018-03-03 23:06:50,732+0000 INFO sendmodaction - signature="Successfully Changed Policy" action_name="changepolicy" sid="1520118405.497" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520118300_338" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc" action_status="success"
2018-03-04 00:48:57,592+0000 INFO sendmodaction - signature="Invoking modular action" action_name="changepolicy" sid="1520124534.353" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520124420_250" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc"
2018-03-04 00:48:57,625+0000 INFO Changing policy for device 5798 by deviceId to policy default
2018-03-04 00:48:58,017+0000 INFO Sensor 5798 now assigned to policy default
2018-03-04 00:48:58,017+0000 INFO sendmodaction - signature="Successfully Changed Policy" action_name="changepolicy" sid="1520124534.353" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520124420_250" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc" action_status="success"
2018-03-04 00:49:18,329+0000 INFO sendmodaction - signature="Invoking modular action" action_name="changepolicy" sid="1520124556.368" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520124420_250" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc"
2018-03-04 00:49:18,351+0000 INFO Changing policy for device WIN-IA9NQ1GN8OI by hostname to policy default
2018-03-04 00:49:18,774+0000 INFO Sensor WIN-IA9NQ1GN8OI now assigned to policy default
2018-03-04 00:49:18,774+0000 INFO sendmodaction - signature="Successfully Changed Policy" action_name="changepolicy" sid="1520124556.368" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520124420_250" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc" action_status="success"
2018-03-06 22:56:43,576+0000 INFO sendmodaction - signature="Invoking modular action" action_name="changepolicy" sid="1520377000.1444" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520376780_790" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc"
2018-03-06 22:56:43,630+0000 INFO Changing policy for device 5798 by deviceId to policy default
2018-03-06 22:56:44,452+0000 INFO Sensor 5798 now assigned to policy default
2018-03-06 22:56:44,452+0000 INFO sendmodaction - signature="Successfully Changed Policy" action_name="changepolicy" sid="1520377000.1444" orig_sid="scheduler__admin__SplunkEnterpriseSecuritySuite__RMD57618d27410fa6840_at_1520376780_790" rid="0" orig_rid="1749" app="SplunkEnterpriseSecuritySuite" user="system" action_mode="adhoc" action_status="success"
`                                                                                                                                                                                                         

# Resources
- Support
  - Contact support@carbonblack.com
  - [link](https://www.carbonblack.com/resources/support/)
  - [Carbon Black Developer Network](https://developer.carbonblack.com)
  - [Developer Relations User Exchange Forum](https://community.carbonblack.com/community/resources/developer-relations)
      - Leave feedback, request help, etc
  - [Github](https://github.com/carbonblack/cb-defense-splunk-app)
      - This project is open source and Cb Developer Network loves open collaboration!
      - Open an issue for a bug, submit PR with your changes to UI, etc
  - [For more ideas check out the Cb Integration Network](https://community.carbonblack.com/community/ecosystem)
- Technology Used
  - python - [CB-API for python](https://cbapi.readthedocs.io/en/latest/)
  - Splunk - [Splunk Setup Page Developer Guidance](https://splunkbase.splunk.com/app/3728/)
  - CSS
  - HTML
  - JavaScript
      - Backbone JS
          - [Main Website](http://backbonejs.org/)
          - [On GitHub](https://github.com/jashkenas/backbone/)
          - [Views are the only feature used](http://backbonejs.org/#View)
      - JQuery
          - [Main Website](http://jquery.com/)
          - [On GitHub](https://github.com/jquery/jquery/)
      - Splunk JavaScript Software Development Kit
          - [API Documentation](http://docs.splunk.com/Documentation/JavaScriptSDK) (docs.splunk.com)
          - [On GitHub](https://github.com/splunk/splunk-sdk-javascript)
          - [Main Website](http://dev.splunk.com/javascript) (dev.splunk.com)
# Credits
This project is maintained and delivered by the Carbon Black Developer Relations team / Developer Network.
JG, JM , ZE & SM 2017.
Contact us !!! dev-support@carbonblack.com !!! for help , or to suggest a new integration with Cb.
Additional credits to Cb's Jimmy Astle for providing excellent source visualizations and direction.

