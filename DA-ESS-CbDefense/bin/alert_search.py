from cbhelpers import CbSearchCommand2
from cbapi.defense import Device
import traceback
import time

import sys
from splunklib.searchcommands import dispatch, Configuration
import logging
log = logging.getLogger(__name__)


@Configuration()
class DeviceSearchCommand(CbSearchCommand2):
    def generate_result(self, data):
        squashed_data = data
        return {'sourcetype': 'carbonblack:defense:json', '_time': time.time(),
                'source': self.cb_url, '_raw': squashed_data}

    def transform(self, results):
        if not self.setup_complete:
            yield self.error_event("Error: {0}".format(self.error_text))
            return  # explicitly stop the generator on prepare() error

        try:
            if not self.query:
                yield self.error_event("Requires query with alert ID. Example: |alertsearch query=IAAQH4CH")
                return

            result = self.cb.get_object("/integrationServices/v3/alert/{0}".format(self.query))
            yield self.generate_result(result)

        except Exception as e:
            yield self.error_event("error searching for {0} in Cb Defense: {1}".format(self.query, str(e)),
                                   stacktrace=traceback.format_stack())
            return

if __name__ == '__main__':
    try:
        dispatch(DeviceSearchCommand, sys.argv, sys.stdin, sys.stdout, __name__)
    except Exception as e:
        log.exception("during dispatch")
