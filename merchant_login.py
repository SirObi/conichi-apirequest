import requests
import json

def login_merchant(consumer_key, email, password):
    '''Authenticates with conichi API and returns merchant data as JSON'''
    url = "https://dev.conichi.com/api/v3/merchant/login"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--" % (email, password)
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'x-consumer-key': "3bntJRRHv7Rv5mFd",
        'cache-control': "no-cache",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    response_text = json.loads(response.text)
    return response_text

    # TODO: Add error handling for failed login request

def get_merchant_uuid(consumer_key, email, password):
    '''Returns merchant session UUID'''
    response_text = login_merchant(consumer_key, email, password)
    uuid = response_text["session"]["uuid"]
    return uuid
