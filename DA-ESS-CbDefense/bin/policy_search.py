from cbhelpers import CbSearchCommand2
from cbapi.defense import Policy

import sys
from splunklib.searchcommands import dispatch, Configuration
import logging
log = logging.getLogger(__name__)


@Configuration()
class PolicySearchCommand(CbSearchCommand2):
    field_names = ['description','id','latestRevision','name','policy','priorityLevel','systemPolicy','version']
    search_cls = Policy

if __name__ == '__main__':
    try:
        dispatch(PolicySearchCommand, sys.argv, sys.stdin, sys.stdout, __name__)
    except Exception as e:
        log.exception("during dispatch")

#ider: count all sensors in policies - policy info page - bin sensors by policy     