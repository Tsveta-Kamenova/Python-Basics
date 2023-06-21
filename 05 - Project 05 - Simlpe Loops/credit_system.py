courses = int(input())
sum_mark = 0
sum_credits = 0
for i in range(1, courses + 1):
    number = int(input())
    mark = number % 10
    credits = number // 10
    if mark == 2:
        credits = 0
    elif mark == 3:
        credits = 0.5*credits
    elif mark == 4:
        credits = 0.7*credits
    elif mark == 5:
        credits = 0.85*credits
    elif mark == 6:
        pass
    sum_mark += mark
    sum_credits += credits
mid_mark = sum_mark/courses

print("%.2f"%sum_credits)
print("%.2f"%mid_mark)


