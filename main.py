import time
import requests
from util.send_request import send_request
from util.date import start_time, end_time
from uuid import uuid4


url = "http://212.115.112.48:8080/ISAPI/AccessControl/AcsEvent?format=json"
username = "admin"
password = "Parol0212"

json_data = {
    "AcsEventCond": {
        "searchID": "a1e5c03a-9da2-44df-812f-9bc0e57036f5",
        "searchResultPosition": 1,
        "maxResults": 100,
        "major": 5,
        "minor": 75,
        "startTime": start_time,
        "endTime": end_time,
        "timeReverseOrder": True,
    }
}


def response_dates(response):
    data = response.json()
    if "AcsEvent" not in data:
        return []

    info_list = data["AcsEvent"].get("InfoList", [])
    filtered_data = [info for info in info_list if len(info.keys()) == 14]

    return filtered_data


def main():
    old_result = None
    while True:
        response = send_request(url, username, password, json_data)
        result = response_dates(response)
        # json_data['AcsEventCond']['searchID'] = str(uuid4())
        # print(f"""
        #       new: {result[0]["time"]}
        #       old: {old_result}
        #       """)
        # print(response.content)
        # print(json_data)
        if not result:
            pass
        elif old_result != result[0]["time"]:
            if old_result != None:
                # print(
                #     f"""
                #     Oldingi natija: {old_result}
                #     Xozirgi natija: {result[0]["time"]}
                #     """
                # )
                result_user = result[0]
                print(result_user)
                to_go = requests.post('https://tizim.astrolab.uz/v1/ac', json=result_user)
                print(f"Status: {to_go.status_code}")
                print("Amal bajarildi!")

            old_result = result[0]["time"]

        time.sleep(1)


if __name__ == "__main__":
    main()
