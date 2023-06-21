sleeve = float(input())
front = float(input())
fabric_type = str(input())
tie = str(input())

shirt = (sleeve+front)*2*1.1
shirt_m = shirt/100

if fabric_type == "Linen":
    price = 15*shirt_m + 10
elif fabric_type == "Cotton":
    price = 12*shirt_m + 10
elif fabric_type == "Denim":
    price = 20*shirt_m + 10
elif fabric_type == "Twill":
    price = 16*shirt_m + 10
elif fabric_type == "Flannel":
    price = 11*shirt_m + 10

if tie == "Yes":
    price_final = price*1.2
else:
    price_final = price

price_final = "%.2f" % price_final
print("The price of the shirt is: " + price_final + "lv.")