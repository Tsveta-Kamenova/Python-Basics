dni = int(input())
sladkari = int(input())
torti = int(input())
gofr = int(input())
chinki = int(input())

torta_cena = 45
gofr_cena = 5.80
chinki_cena = 3.20

parichki = dni*sladkari*(torti*torta_cena + gofr*gofr_cena + chinki*chinki_cena)

razhodi = parichki/8

parichki = parichki - razhodi

print("%.2f"% parichki)