from cbhelpers import CbSearchCommand2
from cbapi.defense import Device

import sys
from splunklib.searchcommands import dispatch, Configuration
import logging
log = logging.getLogger(__name__)


@Configuration()
class DeviceSearchCommand(CbSearchCommand2):
    field_names = [ "activationCodeExpiryTime"
    , "assignedToId"
    ,"assignedToName"
    ,"avEngine"
    ,"avLastScanTime"
    ,"avMaster"
    , "avStatus"
    , "avUpdateServers"
    , "createTime"
    ,"deregisteredTime"
    ,"deviceGuid"
    ,"deviceId"
    ,"deviceOwnerId"
    ,"deviceSessionId"
    ,"deviceType"
    ,"email"
    ,"firstName"
    ,"firstVirusActivityTime"
    ,"lastContact"
    ,"lastExternalIpAddress"
    ,"lastInternalIpAddress"
    ,"lastLocation"
    ,"lastName"
    ,"lastReportedTime"
    ,"lastShutdownTime"
    ,"lastVirusActivityTime"
    ,"linuxKernelVersion"
    ,"messages"
    ,"middleName"
    ,"name"
    ,"organizationId"
    ,"organizationName"
    ,"osVersion"
    ,"passiveMode"
    ,"policyId"
    ,"policyName"
    ,"quarantined"
    ,"registeredTime"
    ,"rootedByAnalytics"
    ,"rootedByAnalyticsTime"
    ,"rootedBySensor"
    ,"rootedBySensorTime"
    ,"scanLastActionTime"
    ,"scanLastCompleteTime"
    ,"scanStatus"
    ,"sensorStates"
    ,"sensorVersion"
    ,"status"
    ,"targetPriorityType"
    ,"testId"
    ,"uninstalledTime"
    ,"vdiBaseDevice"
    ,"windowsPlatform"]
    search_cls = Device

if __name__ == '__main__':
    try:
        dispatch(DeviceSearchCommand, sys.argv, sys.stdin, sys.stdout, __name__)
    except Exception as e:
        log.exception("during dispatch")