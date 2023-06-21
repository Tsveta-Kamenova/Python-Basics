#read the input

product = input()
city = input()
quantity = float(input())

#if city -> price

result = 0

if city == "Sofia":
    if product == "coffee":
        result = quantity*0.5
    elif product == "water":
        result = quantity*0.8
    elif product == "beer":
        result = quantity*1.2
    elif product == "sweets":
        result = quantity*1.45
    elif product == "peanuts":
        result = quantity*1.6
elif city == "Plovdiv":
    if product == "coffee":
        result = quantity*0.4
    elif product == "water":
        result = quantity*0.7
    elif product == "beer":
        result = quantity*1.15
    elif product == "sweets":
        result = quantity*1.3
    elif product == "peanuts":
        result = quantity*1.5
elif city == "Varna":
    if product == "coffee":
        result = quantity*0.45
    elif product == "water":
        result = quantity*0.7
    elif product == "beer":
        result = quantity*1.1
    elif product == "sweets":
        result = quantity*1.35
    elif product == "peanuts":
        result = quantity*1.55
result = "%.2f" % result
print(result)
