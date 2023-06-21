bit = int(input())
kit = float(input())
com = float(input())

bit_lv = 1168
kit_lv = 1.76*0.15
euro_lv = 1.95

parichki = bit*bit_lv + kit*kit_lv
parichki_euro = parichki/1.95

kraj = parichki_euro*(1-com/100)
print("%.2f"%kraj)
