import math

kg_nachalo = int(input())
m_hlqb_kg_br = int(input())
p_cena_hlqb_br = float(input())
b_br_hlqb_prodadeno = int(input())
s_br_sladki_prodadeno = int(input())

den_income = b_br_hlqb_prodadeno*p_cena_hlqb_br
testo_hlqb = b_br_hlqb_prodadeno*m_hlqb_kg_br
testo_sladki = testo_hlqb+kg_nachalo-testo_hlqb
p_cena_sladki_br = p_cena_hlqb_br*1.25
m_sladki_kg_br = 0.8*m_hlqb_kg_br
testo_sladki_izpolzvano = s_br_sladki_prodadeno*m_sladki_kg_br
nosht_income = s_br_sladki_prodadeno*p_cena_sladki_br
razhodi_testo = (kg_nachalo/1000+testo_hlqb/1000)*4
income = (den_income+nosht_income) - razhodi_testo
#c = float(str(round(income,2)))
#c = "%.2f"%c
c = round(income+10**(-len(str(income))-1),2)
#c = round(income,1)
#c = income
dough = testo_hlqb+testo_sladki_izpolzvano
d = int(dough)

print("Pure income: " + str(c) + " lv.")
print("Dough used: " + str(d)+ " g.")

