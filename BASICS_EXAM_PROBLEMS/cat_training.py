start_hr = int(input())
arrive_hr = int(input())
arrive_min = int(input())
day = str(input())
bonus = 0

if arrive_hr + 1 <= start_hr:
    bonus = 1.5
elif arrive_hr == start_hr and arrive_min <= 30:
    bonus = 1
else:
    bonus = 0.5

if day == "Monday" or day=="Wednesday" or day=="Friday":
    bonus += 0.6
elif day == "Tuesday" or day=="Thursday" or day=="Saturday":
    bonus += 0.8
elif day == "Sunday":
    bonus += 2

bonus = "%.2f" % bonus

print(bonus)