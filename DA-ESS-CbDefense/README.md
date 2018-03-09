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
-  (Host Name Matching as per )(https://developer.carbonblack.com/reference/cb-defense/1/rest-api/#device-status) to filter results

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

