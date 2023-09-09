from datetime import datetime, date, time


def datetime_to_iso8601(datetime_object):
    return datetime_object.isoformat(timespec="seconds")


today = date.today()
start_time = f"{datetime_to_iso8601(datetime.combine(today, time.min))}-05:00"
end_time = f"{datetime_to_iso8601(datetime.combine(today, time.max))}-05:00"
