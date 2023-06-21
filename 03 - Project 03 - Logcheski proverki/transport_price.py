km = int(input())
period = str(input())

taxi_price = float()
bus_price = float()
train_price = float()

if km < 20 and period == "day":
    taxi_price = 0.7 + 0.79*km
elif km < 20 and period == "night":
    taxi_price = 0.7 + 0.90*km
if taxi_price != 0:
    print(taxi_price)

if 100 > km >= 20:
    bus_price = 0.09*km
    print(bus_price)
elif km >= 100:
    train_price = 0.06*km
    print(train_price)
