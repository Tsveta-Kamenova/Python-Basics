food_kg = int(input())
leftovers = 0
eaten = 0
sum_eaten = 0

while True:
    try:
        eaten = int(input())
        sum_eaten += eaten
    except ValueError:
        break
leftovers = food_kg*1000 - sum_eaten

if leftovers >= 0:
    print("Food is enough! Leftovers: " + str(leftovers) + " grams.")
else:
    leftovers = abs(leftovers)
    print("Food is not enough. You need " + str(leftovers) + " grams more.")
