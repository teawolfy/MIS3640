#Take One
import  time

time_sec = time.time()
mydate = time_sec
num_days = mydate // 3600 // 24
print(num_days, "days since epoch")

midnight_on_mydate = num_days * 24 * 3600

seconds_since_midnight = mydate - midnight_on_mydate

hours = seconds_since_midnight // 3600
minutes = (seconds_since_midnight - (hours * 3600)) // 60
seconds = seconds_since_midnight - (hours * 3600 + minutes * 60)

time_of_day = "%s:%s:%s" % (hours, minutes, seconds)

print(time_of_day, "on", num_days, "days since epoch")
