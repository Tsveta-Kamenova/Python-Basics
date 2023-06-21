hour = int(input())
min = int(input())

min_new = min + 15
hour_new = hour

if min_new > 59:
    min_new = min + 15 - 60
    if hour == 23:
        hour_new = 0
    else:
        hour_new = hour + 1

elif hour == 23:
    hour_new = hour
    min_new = min + 15

if min_new <= 9:
    print(str(hour_new) + ":0" + str(min_new))
else:
    print(str(hour_new) + ":" + str(min_new))