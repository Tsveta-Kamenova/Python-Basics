n = int(input())
tochki = n-1
skobki_1 = n
skobki_2 = n
rows = 4 + 2*n + 2
for i in range (1,2):
    print(tochki*"." + "|" + n*"\/" + "|" + tochki*".")
    print(tochki * "." + "|" + n * "~~" + "|" + tochki * ".")

for j in range(0, skobki_1):
    print(tochki*"."+"|"+j*" "+(skobki_1)*"{}"+j*" "+"|"+tochki*".")
    skobki_1-=1

print(tochki * "." + "|" +(n-2)*" "+"MEOW"+ (n-2)*" " + "|" + tochki * ".")
print(tochki * "." + "|" + (n-2)*" "+"FOOD" + (n-2)*" " + "|" + tochki * ".")

for j in range(1, skobki_2+1):
    print(tochki*"."+"|"+(skobki_2-1)*" "+j*"{}"+(skobki_2-1)*" "+"|"+tochki*".")
    skobki_2-=1

for i in range (1,2):
    print(tochki * "." + "|" + n * "~~" + "|" + tochki * ".")
    print(tochki * "." + "|" + n * "\/" + "|" + tochki * ".")

