fruit = input()
day = input()
quantity = float(input())

price = 0

day = day.lower()
fruit = fruit.lower()

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    if fruit == "banana":
        price = quantity*2.5
    if fruit == "apple":
        price = quantity*1.2
    if fruit == "orange":
        price = quantity*0.85
    if fruit == "grapefruit":
        price = quantity*1.45
    if fruit == "kiwi":
        price = quantity*2.7
    if fruit == "pineapple":
        price = quantity*5.5
    if fruit == "grapes":
        price = quantity*3.85
    else:
        print("error")
elif day == "saturday" or day == "sunday":
    if fruit == "banana":
        price = quantity*2.7
    if fruit =="apple":
        price = quantity*1.25
    if fruit == "orange":
        price = quantity*0.9
    if fruit == "grapefruit":
        price = quantity*1.6
    if fruit == "kiwi":
        price = quantity*3
    if fruit == "pineapple":
        price = quantity*5.6
    if fruit == "grapes":
        price = quantity*4.2
    else:
        print("error")

else:
    print("error")
if price == 0:
    pass
else:
    print("%.2f" % price)


