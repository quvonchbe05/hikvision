from datetime import datetime, timedelta, date, time
import pytz

tz = pytz.timezone("Asia/Tashkent")

today = date.today()
start_of_day = tz.localize(datetime.combine(today, time.min))
end_of_day = tz.localize(datetime.combine(today, time.max))
# start_time += timedelta(seconds=15)
# end_time += timedelta(seconds=15)

def datetime_to_iso8601(datetime_object):
  return datetime_object.isoformat(timespec="seconds")
