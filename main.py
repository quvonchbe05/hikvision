import time, json, requests, datetime
from functions.send_request import send_request
from functions.date import datetime_to_iso8601, start_of_day, end_of_day, tz

def data_filtering(data):
    json_data = json.loads(data.content)
    if "AcsEvent" in json_data:
        if "InfoList" in json_data["AcsEvent"]:
            info_list = json_data["AcsEvent"]["InfoList"]
            filtered_data = []
            for info in info_list:
                if len(info.keys()) == 14:
                    filtered_data.append(info)
                
            with open('data/data.json', 'w') as file:
                json.dump(filtered_data, file, indent=4)
        else:        
            with open('data/data.json', 'w') as file:
                json.dump('[]', file, indent=4)
                    
        return "success!"
    else:
        return data.content
    
def filter_duplicate_employeeNoString(data):
    unique_data = []
    seen_employeeNoStrings = set()
    for entry in data:
        employeeNoString = entry['employeeNoString']
        if employeeNoString not in seen_employeeNoStrings:
            unique_data.append(entry)
            seen_employeeNoStrings.add(employeeNoString)
    return unique_data


def get_data_between_current_time_and_15_minutes(data):
    current_time = datetime.datetime.now(tz)
    fifteen_minutes_ago = current_time - datetime.timedelta(seconds=10)
    filtered_data = []
    for entry in data:
        time_str = entry['time']
        time_obj = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S+05:00').astimezone(tz)
        if time_obj >= fifteen_minutes_ago:
            filtered_data.append(entry)
    return filtered_data


def main():
    url = "http://192.168.0.102/ISAPI/AccessControl/AcsEvent?format=json"
    username = "admin"
    password = "Parol0212"

    while True:
        json_data = {
            "AcsEventCond": {
                "searchID":"adbc47f1-d88e-41fb-a152-86a72ce9fb9b",
                "searchResultPosition":1,
                "maxResults":100,
                "major":5,
                "minor":75,
                "startTime": f"{datetime_to_iso8601(start_of_day)}",
                "endTime": f"{datetime_to_iso8601(end_of_day)}",
                "timeReverseOrder": True
            }
        }
        
        response = send_request(url, username, password, json_data)
        result = data_filtering(response)
        
        data = json.load(open('data/data.json', 'r'))
        filtered_data = filter_duplicate_employeeNoString(data)
        between = get_data_between_current_time_and_15_minutes(filtered_data)
        
        with open('data/filtered_data.json', 'w') as f:
            json.dump(between, f, indent=4)
            
        print(result)
        
        between_data = json.load(open('data/filtered_data.json', 'r'))
        print(between_data)
        request_to_go = requests.post('https://tizim.astrolab.uz/v1/ac', json=between_data)
        print(request_to_go)
        time.sleep(10)

if __name__ == "__main__":
    main()