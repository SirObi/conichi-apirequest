import requests
import hmac
import hashlib

class ConichiAPIRequest():
    '''Creates new request object. Customer key and API secret
    are required to successfully authenticate with Conichi API'''
    def __init__(self, customer_key, api_secret):
        self.customer_key = customer_key
        self._api_secret = api_secret

    '''Not sure if the method below is necessary - I am not quite sure What
    Marc meant in the README by "getting the UUID after login". Is it
    the session UUID? Is it the merchant's UUID?'''
    def get_uuid(customer_key, _api_secret):
        pass


# The goal here is to make a request that contains several headers.
# One of these headers should be the password, encrypted with the
# HMAC algorithm and


# The customer key is something that uniquely identifies the customer,
# i.e. their email address.

# What I don't know:
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
