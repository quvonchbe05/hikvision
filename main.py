import time
from util.send_request import send_request
from util.date import start_time, end_time
from uuid import uuid4


url = "http://212.115.112.48:8080/ISAPI/AccessControl/AcsEvent?format=json"
username = "admin"
password = "Parol0212"

json_data = {
    "AcsEventCond": {
        "searchID": None,
        "searchResultPosition": 1,
        "maxResults": 1000,
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
    old_result = 0
    while True:
        response = send_request(url, username, password, json_data)
        result = response_dates(response)
        json_data['AcsEventCond']['searchID'] = str(uuid4())
        print(len(result))
        if not result:
            pass
        elif old_result != len(result):
            if old_result != 0:
                difference = len(result) - old_result
                print(
                    f"""
                    Oldingi natija: {old_result}
                    Xozirgi natija: {len(result)}
                    """
                )
                print(result[-difference:])
                print("Amal bajarildi!")

            old_result = len(result)

        time.sleep(1)


if __name__ == "__main__":
    main()
