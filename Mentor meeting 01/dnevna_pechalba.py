days = int(input())
money_day = float(input())
kurs = float(input())

money_per_month = days * money_day
money_per_year = 14.5 * money_per_month

danyk = 0.25*money_per_year
dohod = money_per_year - danyk

dohod_lv = dohod*kurs
pechalba = dohod_lv/365

print("%.2f"% pechalba)