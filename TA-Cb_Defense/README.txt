Cb Defense Add-on for Splunk
Current Version: 2.0.0

The Cb Defense App for Splunk allows administrators to forward events and notifications from the industry's leading NGAV solution into Splunk for correlation and analysis.
NEW FOR 2.0.0 Release:
   - Re-worked UI and proxy settings.
   - Configure multiple CbD inputs rather than being limited to just one.
Requirements
This app requires Cb Defense and Splunk version 6.4 or above.

No additional hardware requirements are necessary for running this app above the standard requirements for both Carbon Black and Splunk.

Getting Started
Once the Cb Defense app for Splunk is installed, then you must configure it to connect to your Cb Defense server. This is done by using the Cb Defense REST API. For more information on the Cb Defense REST API and how to generate an API key and Connector ID, see the Cb Developer Network website and the Cb Defense Users Guide.

To configure the Cb Defense app for Splunk to connect to your Cb Defense server:

Start the Cb Defense App in Splunk
(Optional Proxy Configuration)
Go to the "Configuration" tab - "Proxy Settings" page and fill in the information if using a proxy.
(Requisite configuration of Modular Input)
Go to the "Inputs" tab and create a new input called "cbdefense" (name is not significant).
Set the interval to 300, or faster if you prefer.
Enter the API hostname for your Cb Defense instance in the url field - for most customers this will be "api5.conferdeploy.net". If unsure, contact your support representative.
Make sure to omit the https://, https:// urls are required.
Enter your SIEM type api key and connector ID in the input boxes.
The Cb Defense app for Splunk uses Splunk’s encrypted credential storage facility to store the API token for your Cb Defense server, so the API key is stored securely on the Splunk server.

Example Notifications:
{"eventTime": 1518208676297, "policyAction": {"applicationName": "svchost.exe", "action": null, "reputation": "TRUSTED_WHITE_LIST", "sha256Hash": "121118a0f5e0e8c933efd28c9901e54e42792619a8a3a6d11e1f0025a7324bc2"}, "eventDescription": "[jason-splunk-test-action-deny] [Confer has blocked a threat for you.] [An executable was RUN_BLOCK on a device registered to zestep@carbonblack.com.] [Group: Restrictive_Windows_Workstation] [Device: zewinsevsensor] [SHA256: 121118a0f5e0e8c933efd28c9901e54e42792619a8a3a6d11e1f0025a7324bc2]\n", "url": "https://defense-eap01.conferdeploy.net/investigate?s[searchWindow]=ALL&s[c][QUERY_STRING_TYPE][0]=029f675a0aa611e882c127a75a4ef2d2&s[c][DEVICE_ID][0]=6494", "deviceInfo": {"deviceName": "zewinsevsensor", "targetPriorityCode": 0, "internalIpAddress": "172.17.178.130", "deviceHostName": null, "groupName": "Restrictive_Windows_Workstation", "externalIpAddress": "144.121.23.203", "deviceType": "WINDOWS", "deviceId": 6494, "targetPriorityType": "MEDIUM", "email": "zestep@carbonblack.com", "deviceVersion": null}, "ruleName": "jason-splunk-test-action-deny", "type": "POLICY_ACTION"}
{"eventTime": 1517856821797, "eventDescription": "[jason-splunk-test-alert] [Confer has detected a threat against your company.] [https://defense-eap01.conferdeploy.net#device/6494/incident/XY8IRCCP] [A known virus was detected running. A Deny Policy Action was applied] [Incident id: XY8IRCCP] [Threat score: 4] [Group: Restrictive_Windows_Workstation] [Email: zestep@carbonblack.com] [Name: zewinsevsensor] [Type and OS: WINDOWS Windows 7 x86 SP: 1] [Severity: Threat]\n", "url": "https://defense-eap01.conferdeploy.net/investigate?s[searchWindow]=ALL&s[c][DEVICE_ID][0]=6494&s[c][INCIDENT_ID][0]=XY8IRCCP", "deviceInfo": {"deviceName": "zewinsevsensor", "targetPriorityCode": 0, "internalIpAddress": "172.17.178.130", "deviceHostName": null, "groupName": "Restrictive_Windows_Workstation", "externalIpAddress": "144.121.23.203", "deviceType": "WINDOWS", "deviceId": 6494, "targetPriorityType": "MEDIUM", "email": "zestep@carbonblack.com", "deviceVersion": "Windows 7 x86 SP: 1"}, "ruleName": "jason-splunk-test-alert", "type": "THREAT", "threatInfo": {"indicators": [{"applicationName": "explorer.exe", "indicatorName": "POLICY_DENY", "sha256Hash": "11d69fb388ff59e5ba6ca217ca04ecde6a38fa8fb306aa5f1b72e22bb7c3a25a"}, {"applicationName": "explorer.exe", "indicatorName": "CODE_DROP", "sha256Hash": "11d69fb388ff59e5ba6ca217ca04ecde6a38fa8fb306aa5f1b72e22bb7c3a25a"}, {"applicationName": "svchost.exe", "indicatorName": "POLICY_DENY", "sha256Hash": "121118a0f5e0e8c933efd28c9901e54e42792619a8a3a6d11e1f0025a7324bc2"}, {"applicationName": "explorer.exe", "indicatorName": "DETECTED_MALWARE_APP", "sha256Hash": "11d69fb388ff59e5ba6ca217ca04ecde6a38fa8fb306aa5f1b72e22bb7c3a25a"}, {"applicationName": "explorer.exe", "indicatorName": "MALWARE_DROP", "sha256Hash": "11d69fb388ff59e5ba6ca217ca04ecde6a38fa8fb306aa5f1b72e22bb7c3a25a"}, {"applicationName": "explorer.exe", "indicatorName": "RUN_MALWARE_APP", "sha256Hash": "11d69fb388ff59e5ba6ca217ca04ecde6a38fa8fb306aa5f1b72e22bb7c3a25a"}], "time": 1517857014951, "incidentId": "XY8IRCCP", "score": 4, "summary": "A known virus was detected running. A Deny Policy Action was applied"}}
{"eventTime": 1517863503153, "policyAction": {"applicationName": "svchost.exe", "action": null, "reputation": "TRUSTED_WHITE_LIST", "sha256Hash": "1d35014d937e02ee090a0cfc903ee6e6b1b65c832694519f2b4dc4c74d3eb0fd"}, "eventDescription": "[jason-splunk-test-action-deny] [Confer has blocked a threat for you.] [An executable was RUN_BLOCK on a device registered to jgarman+po@carbonblack.com.] [Group: jan09-demo] [Device: WIN-IA9NQ1GN8OI] [SHA256: 1d35014d937e02ee090a0cfc903ee6e6b1b65c832694519f2b4dc4c74d3eb0fd]\n", "url": "https://defense-eap01.conferdeploy.net/investigate?s[searchWindow]=ALL&s[c][QUERY_STRING_TYPE][0]=f05da5560ab411e8834a939ef3e75232&s[c][DEVICE_ID][0]=5798", "deviceInfo": {"deviceName": "WIN-IA9NQ1GN8OI", "targetPriorityCode": 0, "internalIpAddress": "172.22.5.141", "deviceHostName": null, "groupName": "jan09-demo", "externalIpAddress": "70.106.217.80", "deviceType": "WINDOWS", "deviceId": 5798, "targetPriorityType": "LOW", "email": "jgarman+po@carbonblack.com", "deviceVersion": null}, "ruleName": "jason-splunk-test-action-deny", "type": "POLICY_ACTION"}
