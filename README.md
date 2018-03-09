# Overview

Cb Defense integration with Splunk has two principle components:

See the README in the respective sub-folder for more detailed installation and configuration information for each.

##Cb Defense Add-on for Splunk:
    - The Cb Defense Add-On for Splunk pulls CbD Notification data into Splunk via REST API. 
    - Parses events into well-formated JSON, index's them into splunk.
    - To simly get CbD notifications into splunk, this Add-on is all that is required. 
        
##Cb Defense App for Splunk: 
    - The Cb Defense App for Splunk contains a suite of comprehensive visualizations for Splunk operators and administrators to use
     to visualize the status of their environment
    - Custom 'devicesearch' and 'policysearch' commands to retrieve policy and device Information via REST API 
    - The Cb Defense App for Splunk is fully integrated with the Add-on for splunk - install the Add-On first.
    - The Cb Defense App for Splunk also integrates with the Splunk Enterprise Security Framework and Adaptive Response Framework
    - Current AR actions:
        - Reassign Cb Defense Device Policy
        - roadmap: Many more 