import requests
from requests.auth import HTTPDigestAuth


def send_request(url, username, password, json_data):
    digest_auth = HTTPDigestAuth(username, password)
    response = requests.post(url, json=json_data, auth=digest_auth)
    return response






# def get_data_between_current_time_and_15_minutes(data):
#     current_time = datetime.datetime.now()
#     fifteen_minutes_ago = current_time - datetime.timedelta(seconds=1)
#     filtered_data = []
#     for entry in data:
#         time_str = entry['time']
#         time_obj = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S+05:00')
#         if time_obj >= fifteen_minutes_ago:
#             filtered_data.append(entry)
#     return filtered_data

