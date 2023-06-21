age = int(input())
washing_mashine = float(input())
gift_price = int(input())

money = 0
sum = 0
gifts = 0
brother = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money += 10
        sum += money
        brother += 1
    else:
        gifts += 1

gift_money = gifts*gift_price

sum = sum + gift_money - brother
diff = sum - washing_mashine


if diff >= 0:
    diff = "%.2f" % diff
    print("Yes! " + str(diff))
else:
    diff = abs(diff)
    diff = "%.2f" % diff
    print("No! " + str(diff))