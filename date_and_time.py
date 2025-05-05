import datetime
import pytz

# DATE

# d = datetime.date(2016, 7, 24)
# tday = datetime.date.today()
# # print(d)
# # print(tday)
# # print(tday.year)
# # print(tday.weekday())
# # print(tday.isoweekday())

# # tdelta = datetime.timedelta(days=7)
# # print(tday + tdelta)

# bday = datetime.date(2025, 10, 12)
# till_bday = bday - tday
# print(till_bday.days)

#TIME
# t = datetime.time(9, 30, 45, 100000)
# print(t)
# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
# print(dt)
# timedelta = datetime.timedelta(days=7)
# print(dt + timedelta)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# # Add timezone examples
# dt_utc = datetime.datetime.now(tz=pytz.UTC)
# print(f"UTC time: {dt_utc}")

# # Convert to different timezone
# eastern = pytz.timezone('US/Eastern')
# dt_eastern = dt_utc.astimezone(eastern)
# print(f"Eastern time: {dt_eastern}")

# # Your local timezone
# local_tz = pytz.timezone('Asia/Kathmandu')  # Change to your timezone
# dt_local = dt_utc.astimezone(local_tz)
# print(f"Local time: {dt_local}")

dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_mtn= datetime.datetime.now()
dt_local = dt_mtn.astimezone(pytz.timezone('Asia/Kathmandu'))
print(dt_local)