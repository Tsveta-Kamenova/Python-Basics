hartiq = int(input())
plat = int(input())
lepilo = float(input())
procent = int(input())

hartiq_cena = 5.8
plat_cena = 7.2
lepilo_cena = 1.20

parichki = (hartiq*hartiq_cena + plat*plat_cena + lepilo*lepilo_cena)*(1-procent/100)

print(round(parichki,4))

