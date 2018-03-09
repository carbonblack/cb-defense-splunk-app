# Overview

Cb Defense integration with Splunk has two principal components: the *Cb Defense Add-on for Splunk* and the *Cb Defense App for Splunk*. To get started with the integration, you will want to install the *Cb Defense Add-on for Splunk* to pull the Cb Defense data into your Splunk server. The Add-on provides a one-way integration between Cb Defense and Splunk, periodically polling the Cb Defense cloud to retrieve alert notifications and index those notifications in your Splunk server.

The *Cb Defense App for Splunk* enables a more powerful two-way integration with Cb Defense. It includes additional custom search commands, macros as well as  dashboards & visualizations  to help Splunk operators view and manipulate Cb Defense event data in real time. The initial 1.0.0  release includes  basic integration with the splunk Adaptive Response framework.  Splunk operators can configure Cb Defense environment responses to alerts, correlated searches,  ad-hoc notable events in the Splunk Enterprise Security app (via the REST API for CB Defense). 

See the README in the respective sub-folder for more detailed installation and configuration information for each.

(TA-Cb_Defense/ for the Add-on and DA-ESS-CbDefense/ for the Application)