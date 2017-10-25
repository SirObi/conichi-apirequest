import requests
import hmac
import hashlib

class ConichiAPIRequest():
    '''Creates new request object. Customer key and API secret
    are required to successfully authenticate with Conichi API'''
    def __init__(self, customer_key, api_secret):
        self.customer_key = <customer key goes here>
        self.api_secret = <api secret goes here>
        self.get_uuid(customer_key, api_secret)

    def get_uuid(customer_key, api_secret):


# The goal here is to make a request that contains several headers.
# One of these headers should be the password, encrypted with the
# HMAC algorithm and


# The customer key is something that uniquely identifies the customer,
# i.e. their email address.
