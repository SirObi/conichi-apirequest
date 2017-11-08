import requests
import hmac
import hashlib
import json
import base64
import time
import math
import pprint
import merchant_login


class ConichiMerchantRequest():
    '''Creates new Conichi request object. Authenticates with conichi API
    and saves session UUID on the created object'''
    def __init__(self, api_key, api_secret, email, password):
        self.api_key = api_key
        self._api_secret = api_secret
        self._email = email
        self._password = password
        self._uuid = merchant_login.get_merchant_uuid(api_key, email, password)

    def _body_digest(self, body):
        '''Takes request body and outputs a 64-character-long hash.
        This hash is a necessary component of the final hash'''
        apisecret = self._api_secret
        body_hash = base64.b64encode(hmac.new(apisecret, body,
                                              hashlib.sha256).digest())
        body_hash = body_hash.replace('/', '_')
        body_hash = body_hash.replace('+', '-')
        return body_hash

    def _normalized_string(self, method, url, body, current_timestamp):
        '''Concatenates additional parameters required for final hash'''
        uuid = self._uuid
        body_hash = self._body_digest(body)
        normalized_string = (uuid + '\n' + method + '\n' + url + '\n' +
                             body_hash + '\n' + current_timestamp)

        return normalized_string

    def _final_digest(self, normalized_string):
        '''Creates hmac required by conichi API'''
        apisecret = self._api_secret
        new_hmac = base64.b64encode(hmac.new(apisecret, normalized_string,
                                             hashlib.sha256).digest())
        new_hmac = new_hmac.replace('/', '_')
        new_hmac = new_hmac.replace('+', '-')
        return new_hmac

    def send_request(self, method, body, url):
        '''Sends request signed with user's API secret'''
        body = json.dumps(body)
        body_hash = self._body_digest(body)
        current_timestamp = str(int(math.floor(time.time())))
        normalized_string = self._normalized_string(method, url, body,
                                                    current_timestamp)
        new_hmac = self._final_digest(normalized_string)

        headers = {
            'User-Agent': 'python',
            'X-Consumer-Key': self.api_key,
            'X-Session-UUID': self._uuid,
            'X-HMAC': new_hmac,
            'X-HMAC-Version': 'HMAC-SHA256',
            'X-HMAC-Timestamp': current_timestamp,
            'X-Body-Hash': body_hash
        }

        response = requests.request(method, url, data=body, headers=headers)
        pprint.pprint(response.json())
        return response.json()


# Base urls
# https://dev.conichi.com/api/v3
# https://app.conichi.com/api/v3
