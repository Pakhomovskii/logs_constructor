import datetime
import time
import enum

class Time(enum.Enum):
   now = datetime.datetime.now()
   strftime = time.strftime("%H:%M:%S")
   #TODO create more enums
