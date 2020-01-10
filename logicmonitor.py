import requests
import hashlib
import base64
import time
import hmac
import json

from urllib.parse import urlencode

"""
Wrapper around the LogicMonitor API to simplify interacting with the service
Requires the requests library to be installed
"""


class LM():
    # Set up account info for use in later operations

    def __init__(self, account_name, access_id, access_key):
        self.account_name = account_name
        self.access_id = access_id
        self.access_key = access_key

    # Builds authentication headers.  Unique for every API call
    def login(self, method, path='', data=''):
        # Get current time in milliseconds
        epoch = str(int(time.time() * 1000))

        # Concatenate Request details
        request_vars = method + epoch + data + path

        # Construct signature
        hmac_val = hmac.new(self.access_key.encode(),
                            msg=request_vars.encode(),
                            digestmod=hashlib.sha256).hexdigest()
        signature = base64.b64encode(hmac_val.encode()).decode()

        # Construct headers
        auth = f'LMv1 {self.access_id}:{signature}:{epoch}'
        headers = {'Content-Type': 'application/json', 'Authorization': auth}

        return headers

    # Does a http GET to the specified endpoint
    def get(self, path='', query=''):
        headers = self.login('GET', path=path)

        # URL encode the query parameters
        if query:
            encoded = urlencode(query)
            query = f'?{encoded}'

        # Construct URL
        url = f'https://{self.account_name}.logicmonitor.com/santaba/rest{path}{query}'

        # Make request
        response = requests.get(url, headers=headers)

        return response.json()

    # Does a http POST to the specified endpoint
    def post(self, path='', data={}):
        # Because the LM api is extremely picky and doesn't accept true json
        data = json.dumps(data)

        headers = self.login('POST', path=path, data=data)

        # Construct URL
        url = f'https://{self.account_name}.logicmonitor.com/santaba/rest{path}'

        # Make request
        response = requests.post(url, data=data, headers=headers)

        return response.json()

    # Does a http DELETE to the specified endpoint
    def delete(self, path=''):
        headers = self.login('DELETE', path=path)

        # Construct URL
        url = f'https://{self.account_name}.logicmonitor.com/santaba/rest{path}'

        # Make request
        response = requests.delete(url, headers=headers)

        return response.json()
