import datetime
import time

from datetime import datetime


"""This file is used to test date related build in functions."""

current_datetime = datetime.now()
y=datetime.isocalendar(current_datetime)[0]
w=datetime.isocalendar(current_datetime)[1]
wd=datetime.isocalendar(current_datetime)[2]
d=datetime.fromisocalendar(y,w,wd).date()
print(d)
# print("Current Date and Time:", current_datetime) #current date time
# timestamp = datetime.timestamp(current_datetime) #timestamp

# print("Timestamp:", timestamp, "\nDate time:",current_datetime)
# time.sleep(3)

# ts_to_date=datetime.fromtimestamp(timestamp)
# print("from timestamp:",ts_to_date)