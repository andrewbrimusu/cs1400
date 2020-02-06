import time

currTime = time.time()

print("currTime: ",currTime)

sec = int(currTime)

print("sec: ", sec)

currSec = sec % 60

print("currSec: ", currSec)

totalMinutes = sec // 60

print("totalMinutes: ", totalMinutes)

currentMinute = totalMinutes % 60

print("currentMinute: ", currentMinute)

totalHours = totalMinutes // 60

print("totalHours: ",totalHours)

currentHour = totalHours % 24

print("currentHour: ",currentHour)

mountainTime = -7
print("current time is: ", currentHour+mountainTime,":",currentMinute,":",currSec,sep="")