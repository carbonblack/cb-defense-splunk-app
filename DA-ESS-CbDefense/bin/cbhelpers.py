from cbapi import CbApi
from cbapi.defense import CbDefenseAPI
from cbapi.errors import ApiError, ServerError

from splunklib.searchcommands import GeneratingCommand, Option, Configuration, EventingCommand
import json
import time
import logging
import traceback
import os

import logging


class CredentialMissingError(Exception):
    pass

try:
    from splunk.clilib.bundle_paths import make_splunkhome_path
except ImportError:
    from splunk.appserver.mrsparkle.lib.util import make_splunkhome_path


def get_creds(splunk_service):
    api_credentials = splunk_service.storage_passwords["credential:DA-ESS-CbDefense_realm:admin:"]

    api_secret_key = api_credentials.clear_password

    cb_server = splunk_service.confs["DA-ESS-CbDefense_settings"]["api"]['api_url']
    api_id = splunk_service.confs["DA-ESS-CbDefense_settings"]["api"]['api_id']

    if not cb_server or not api_secret_key or not api_id:
        raise CredentialMissingError(
            "Please visit the Set Up Page for the Cb DefenseApp for Splunk to set the API URL, API secret key & API Id for your Cb Defense server.")

    return cb_server, api_secret_key, api_id



def get_cbapi(splunk_service):
    cb_server, api_secret_key, api_id = get_creds(splunk_service)
    return CbDefenseAPI(token="{0}/{1}".format(api_secret_key,api_id), url=cb_server)


class CbSearchCommand2(EventingCommand):
    query = Option(name="query", require=False)
    max_result_rows = Option(name="maxresultrows", default=1000)

    field_names = []
    search_cls = None

    def __init__(self):
        super(CbSearchCommand2, self).__init__()
        self.setup_complete = False
        self.cb = None
        self.cb_url = "<unknown>"
        self.error_text = "<unknown>"

    def error_event(self, comment, stacktrace=None):
        error_text = {"Error": comment}
        if stacktrace is not None:
            error_text["stacktrace"] = stacktrace

        return {'sourcetype': 'carbonblack:defense:json', '_time': time.time(), 'source': self.cb_url,
                '_raw': json.dumps(error_text)}

    def prepare(self):
        try:
            self.cb = get_cbapi(self.service)
            self.cb_url = self.cb.credentials.url
        except KeyError:
            self.error_text = "API key not set. Check that the Cb Defenseserver is set up in the Cb DefenseApp for Splunk configuration page."
        except (ApiError, ServerError) as e:
            self.error_text = "Could not contact Cb Defenseserver: {0}".format(str(e))
        except CredentialMissingError as e:
            self.error_text = "Setup not complete: {0}".format(str(e))
        except Exception as e:
            self.error_text = "Unknown error reading API key from credential storage: {0}".format(str(e))
        else:
            self.setup_complete = True

    def process_data(self, data_dict):
        """
        If you want to modify the data dictionary before returning to splunk, override this. // BSJ 2016-08-30
        """
        return data_dict

    def squash_data(self, data_dict):
        for x in data_dict.keys():
            v = data_dict[x]
            data_dict[x] = str(v)
            if (type(v) is dict or isinstance(v,dict)):
                data_dict[x] = self.squash_data(v)
            elif (isinstance(v,list)):
                data_dict[x] = [ self.squash_data(e) if isinstance(e,dict) else str(e) for e in v]
            else:
                data_dict[x] = str(v)
        return data_dict

    def generate_result(self, data):
        rawdata = dict((field_name, getattr(data, field_name, "")) for field_name in self.field_names)
        squashed_data = self.squash_data(self.process_data(rawdata))
        return {'sourcetype': 'carbonblack:defense:json', '_time': time.time(),
                'source': self.cb_url, '_raw': squashed_data}

    def transform(self, results):
        if not self.setup_complete:
            yield self.error_event("Error: {0}".format(self.error_text))
            return  # explicitly stop the generator on prepare() error

        try:
            query = self.cb.select(self.search_cls)
            if self.query and not self.query.isspace() and len(self.query.split(":")) >= 2:
                query = query.where(self.query)

            for result in query[:int(self.max_result_rows)]:
                self.logger.info("yielding {0} {1}".format(self.search_cls.__name__, result._model_unique_id))
                yield self.generate_result(result)

        except Exception as e:
            yield self.error_event("error searching for {0} in Cb Defense: {1}".format(self.query, str(e)),
                                   stacktrace=traceback.format_stack())
            return


def setup_logger():
    """
   Setup a logger for the REST handler.
   """

    logger = logging.getLogger('da-ess-cbDefense')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.handlers.RotatingFileHandler(
        make_splunkhome_path(['var', 'log', 'splunk', 'da-ess-cbDefense.log']),
        maxBytes=25000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s %(lineno)d %(levelname)s %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
