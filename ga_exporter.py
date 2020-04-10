import time
import os
import json
import requests
from oauth2client.service_account import ServiceAccountCredentials
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY


class GarCollector(object):

    def collect(self):
        c = GaugeMetricFamily('ActiveDaimlerUsers', 'Currently active users on daimler.epam.com')
        c.add_metric("ActiveUsers", self.get_active_users())
        yield c

    def get_active_users(self):
        with open(KEY_FILE_LOCATION, "r") as read_json:
            keyfile_dict = json.loads(read_json.read())
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, scopes=[
            'https://www.googleapis.com/auth/analytics.readonly'])
        session = requests.Session()
        session.headers = {'Authorization': 'Bearer ' + credentials.get_access_token().access_token}

        url_kwargs = {
            'view_id': VIEW_ID,
            'get_args': 'metrics=rt:activeUsers'
        }
        response = session.get(
            'https://www.googleapis.com/analytics/v3/data/realtime?ids=ga:{view_id}&{get_args}'.format(**url_kwargs))
        response.raise_for_status()
        result = response.json()
        active_users = result['totalsForAllResults']['rt:activeUsers']
        return active_users


if __name__ == '__main__':
    KEY_FILE_LOCATION = os.getenv('KEY_FILE_LOCATION')
    VIEW_ID = os.getenv('VIEW_ID')

    start_http_server(9177)
    REGISTRY.register(GarCollector())
    while True:
        time.sleep(5)

