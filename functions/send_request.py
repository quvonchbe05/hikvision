import requests
from requests.auth import HTTPDigestAuth


def send_request(url, username, password, json_data):
    digest_auth = HTTPDigestAuth(username, password)
    response = requests.post(url, json=json_data, auth=digest_auth)
    return response
