from datetime import datetime, timedelta, date, time

today = date.today()
start_of_day = datetime.combine(today, time.min)
end_of_day = datetime.combine(today, time.max)
# start_time += timedelta(seconds=15)
# end_time += timedelta(seconds=15)

def datetime_to_iso8601(datetime_object):
  return datetime_object.isoformat(timespec="seconds") + "+05:00"
