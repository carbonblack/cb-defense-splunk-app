import sys
import logging
import json
import gzip
import csv
import os

try:
    from splunk.clilib.bundle_paths import make_splunkhome_path
except ImportError:
    from splunk.appserver.mrsparkle.lib.util import make_splunkhome_path

sys.path.append(make_splunkhome_path(["etc", "apps", "Splunk_SA_CIM", "lib"]))
sys.path.append(make_splunkhome_path(["etc", "apps", "SA-Utils", "lib"]))

from cim_actions import ModularAction
from splunklib.client import Service
from cbhelpers import get_cbapi
from cbapi.defense.models import Policy,Device
from cbapi.errors import ServerError
import json

class ChangePolicyAction(ModularAction):
    def __init__(self, settings, logger, action_name=None):
        super(ChangePolicyAction, self).__init__(settings, logger, action_name)
        self.service = Service(token=self.session_key)

    def dowork(self, result):
        cb = get_cbapi(self.service)
        return self.do_genericevent(cb, result)

    def error(self, msg):
        self.addevent(msg, sourcetype="carbonblack:defense:action")
        logger.error(msg)

    def do_policychange(self, cb, device, policyName,inputtype):
        dryrun = self.configuration.get("dryrun", "1")
        try:
            dryrun = int(dryrun)
        except:
            dryrun = 1
        if dryrun == 1:
            logger.info("Dry run: would have changed policy for device {0} to {}.".format(device, policyName))
            self.addevent("Dry run changing policy for {0}.".format(device), sourcetype="carbonblack:defense:action")
            return True

        logger.info("Changing policy for device {0} by {1} to policy {2}".format(device,inputtype,policyName))

        if inputtype == "deviceId":
            devices = list(cb.select(Device).where("deviceId:%s" % device))
        if inputtype == "ipaddress":
            devices = list(cb.select(Device).where('ipAddress:%s' % device))
        if inputtype == "hostname":
            devices = list(cb.select(Device).where('hostName:%s' % device))
        if inputtype == "hostnameexact":
            devices = list(cb.select(Device).where('hostNameExact:%s' % device))

        try:
            for d in devices:
                d.policyName = policyName
                d.save()
        except:
            raise
        else:
            logger.info("Sensors {} now assigned to policy {}".format(devices, policyName))
            return True

    def do_genericevent(self, cb, result):
        """Attempt to ban an MD5 hash based on the field from the 'fieldname' in the Alert Action UI."""

        #get the configured policy Name
        policy_name = self.configuration.get("policyname", None)
        # attempt to retrieve the MD5 hash from the event
        field_name = self.configuration.get("fieldname", None)
        #attempt to get the input type
        input_type = self.configuration.get("inputtype", None)

        if not field_name:
            self.error("No field name specified in the configuration {0}".format(self.configuration))
            return False
        if not policy_name:
            self.error("No policy name specified in the configuration {0}".format(self.configuration))
            return False
        if not input_type:
            self.error("No policy name specified in the configuration {0}".format(self.configuration))
            return False

        device = result.get(field_name)
        if not device:
            device = result.get("orig_raw."+field_name)

        if not device:
            self.error("No value found in the result {1} for field name {0}".format(field_name,result))
            return False

        try:
            return self.do_policychange(cb, device, policy_name,input_type)
        except Exception as e:
            self.error("Could not change policy for : {0}".format(str(e)))
            logger.exception("Detailed error message")

        return False


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] != "--execute":
        print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)"
        sys.exit(1)

    try:
        logger = ModularAction.setup_logger('changepolicy_modalert')
        modaction = ChangePolicyAction(sys.stdin.read(), logger, 'changepolicy')
    except Exception as e:
        logger.critical(str(e))
        sys.exit(3)

    try:
        session_key = modaction.session_key

        modaction.addinfo()
        ## process results
        if not os.path.exists(modaction.results_file):
            logger.info("No results available to process: %s does not exist, exiting." % modaction.results_file)
            sys.exit(0)
        with gzip.open(modaction.results_file, 'rb') as fh:
            for num, result in enumerate(csv.DictReader(fh)):
                ## set rid to row # (0->n) if unset
                result.setdefault('rid', str(num))

                modaction.update(result)
                modaction.invoke()

                act_result = modaction.dowork(result)

                if act_result:
                    modaction.message('Successfully Changed Policy', status='success')
                else:
                    modaction.message('Failed to change Policy', status='failure', level=logging.ERROR)

                modaction.writeevents(source='carbonblackdefenseapi')

    except Exception as e:
        ## adding additional logging since adhoc search invocations do not write to stderr
        try:
            logger.critical(modaction.message(e, 'failure'))
        except:
            logger.critical(e)
        print >> sys.stderr, "ERROR Unexpected error: %s" % e
        sys.exit(3)

