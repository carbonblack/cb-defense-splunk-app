Cb Defense Add-on for Splunk
Current Version: 2.0.0 

The Cb Defense App for Splunk allows administrators to forward events and notifications from the industry's leading NGAV solution into Splunk for correlation and analysis.
NEW FOR 2.0.0 Release: Re-worked UI and proxy settings. Configure multiple CbD inputs rather than being limited to just one.

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
Set the internval to 300, or faster if you prefer.
Enter the API hostname for your Cb Defense instance in the url field - for most customers this will be "api5.conferdeploy.net". If unsure, contact your support representative.
Make sure to ommit the https://, https:// urls are required.
Enter your SIEM type api key and connector ID in the input boxes. 
The Cb Defense app for Splunk uses Splunk’s encrypted credential storage facility to store the API token for your Cb Defense server, so the API key is stored securely on the Splunk server.
