city = input()
sells = float(input())

comission = 0

if city == "Sofia":
    if 0 <= sells <= 500:
        comission = 0.05*sells
    if 500 < sells <= 1000:
        comission = 0.07*sells
    if 1000 < sells <= 10000:
        comission = 0.08*sells
    if sells > 10000:
        comission = 0.12*sells
if city == "Varna":
    if 0 <= sells <= 500:
        comission = 0.045*sells
    if 500 < sells <= 1000:
        comission = 0.075*sells
    if 1000 < sells <= 10000:
        comission = 0.10*sells
    if sells > 10000:
        comission = 0.13*sells
if city == "Plovdiv":
    if 0 <= sells <= 500:
        comission = 0.055*sells
    if 500 < sells <= 1000:
        comission = 0.08*sells
    if 1000 < sells <= 10000:
        comission = 0.12*sells
    if sells > 10000:
        comission = 0.145*sells
if sells < 0 or city != "Sofia" and city != "Varna" and city != "Plovdiv":
    print("error")
else:
    print("%.2f" % comission)