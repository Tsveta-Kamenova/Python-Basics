numbers = int(input())
p1 = 0
p2 = 0
p3 = 0

for i in range(1, numbers+1):
    current_num = int(input())
    if current_num % 2 == 0:
        p1 += 1
    if current_num % 3 == 0:
        p2 += 1
    if current_num % 4 == 0:
        p3 += 1
p1 = p1 * 100 / numbers
p2 = p2 * 100 / numbers
p3 = p3 * 100 / numbers

print("%.2f" % p1 + "%")
print("%.2f" % p2 + "%")
print("%.2f" % p3 + "%")