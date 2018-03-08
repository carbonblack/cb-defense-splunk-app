# Overview
Welcome to the Cb Defense App for Splunk.

This app gives Slunk administrators the ability to leverage the market's leading NGAV solution.

Features: 
- Environment Overview 
- Threat Search 
- Policy Action Search
- Login Map
- Device Search 

Adaptive Response framework and Splunk Threat Intelligence Framework integration - can create Notable Events from CbD Data.

Currently supported (V1.0.0) AR actions: 
- Change Cb Defense Sensor Policy
    - Lets the Splunk operator change the assinged security policy of one or more CbD devices based from Ip Address, hostname, deviceId etc

#Installation:

Download the app from SplunkBase, or build from the source available on github.

# Setup & Configuration

##(basic)

Use the gear icon from the Splunk left hand nav bar to 'manage apps' - select Cb Defense and click 'setup'

Enter the (sans protocol, https is implied and enforced) URI for your Cb Defense API endpoint. 

Enter your API Key (Must be type API or Live Response )

Enter your Connector Id (Must be type API or Live Response)

##(advanced)

The app comes loaded with a macro `cbdefense` in default/macros.conf that defines Carbon Black Defense events.
In order to support all use cases, it defaults to :
 `index=* sourcetype=(carbonblack:defense:json)`

If you would like to only search specific indexes, change the macro (UI accessible, or on disk).

For instance, if you would like to use the 'carbonblack' index change the macro to indicate index="carbonblack".


#Adaptive Response Configuration 

The Change Cb Defense Sensor Policy Adaptive Response action has 3 important configuration options:
 - 'inputtype' either Ip Address, deviceId , hostname, or hostname exact
    - This option specifies the intended indicator in the incoming result set
 - 'fieldname' - the field in your result set to target, for instance deviceInfo.deviceId
    - ex , when inputtype = deviceId, fieldname = deviceInfo.deviceId the modular action will try to find a sensor by the deviceId in the 'deviceInfo.deviceId' of the incoming result set
 -  Policy Name - the Cb Defense Policy to be applied to the targeted sensors. For instance 'default' or 'Restrictive_Windows_Workstation'
    - note: If you try to change from policy A to policy A for sensor B , it will always succeed. 

# Resources
- Support
    - Contact support@carbonblack.com 
    - [link](https://www.carbonblack.com/resources/support/)
    - [Carbon Black Developer Network](https://developer.carbonblack.com)
    - [Developer Relations User Exchange Forum](https://community.carbonblack.com/community/resources/developer-relations) 
        - Leave feedback, request help, etc 
    - [Github](https://github.com/carbonblack/cb-defense-splunk-app)
        - This project is open souce and Cb Developer Network loves open collaboration!
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
