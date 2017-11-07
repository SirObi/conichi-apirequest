import requests
import hmac
import hashlib
import json
import merchant_login
import base64

# The function below belongs in the class
# It was taken out for debugging purposes
def body_digest(body):
    body_json = json.dumps(body)
    body_hash = base64.b64encode(hmac.new("something", body, hashlib.sha256).digest())
    body_hash = body_hash.replace('/', '_')
    body_hash = body_hash.replace('+', '-')
    return body_hash
    
class ConichiMerchantRequest():
    '''Creates new Conichi request object. Authenticates with conichi API
    and makes user UUID available to created object'''
    def __init__(self, consumer_key, api_secret, email, password):
        self.consumer_key = consumer_key
        self._api_secret = api_secret
        self._email = email
        self._password = password
        self._uuid = merchant_login.get_merchant_uuid(consumer_key, email, password)



    def send_request(self):
        print self._uuid


#new_request = ConichiMerchantRequest(consumer_key, api_secret, email, password)
#new_request.send_request()
#print new_request._uuid



# The goal here is to make a request that contains several headers.
# One of these headers should be the password, encrypted with the
# HMAC algorithm and


# The customer key is something that uniquely identifies the customer,
# i.e. their email address.

# What I don't know:
# Do you need HMAC in order to authenticate?
# No. It's only necessary when sending requests.
# That's why you're able to authenticate through Postman, without usin HMAC
# I don't know whether the username (login) also has to be encrypted
# Answer: No.
# I don't know whether I only need to include the password and login in the login request
# A login request should contain:
# - url
# - method
# - body, (this is where the username and password go in):
# { user: marc,
# password: marchorne
# }
# - customer key
# - api key encrypted with HMAC
# Additional required headers:
# - timestamp (protection against old requests)
# - bodyhash (ensures it's the right request)
# - HMAC version (which encoding algorithm has been used)
# I don't know what the full url of the API I need to call is
# Base url
# https://dev.conichi.com/api/v3
# https://app.conichi.com/api/v3
