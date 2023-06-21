days = int(input())

total_min = 0
total_distance = 0
unit_km = "km"
unit_m = "m"
cals = 0

for i in range(1, days + 1):
    min_per_day = int(input())
    distance_per_day = float(input())
    unit = str(input())

    total_min += min_per_day
    cals = total_min*20

    if unit == unit_km:
        total_distance += distance_per_day
    elif unit == unit_m:
        distance_per_day = distance_per_day/1000
        total_distance += distance_per_day

print("He ran " + "%.2f"%total_distance + "km for " + str(total_min) +
      " minutes and burned " + str(cals) + " calories.")

