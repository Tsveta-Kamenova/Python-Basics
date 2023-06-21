numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, numbers+1):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    if 200 <= current_num <= 399:
        p2 += 1
    if 400 <= current_num <= 599:
        p3 += 1
    if 600 <= current_num <= 799:
        p4 += 1
    if 800 <= current_num:
        p5 += 1
p1 = p1 * 100 / numbers
p2 = p2 * 100 / numbers
p3 = p3 * 100 / numbers
p4 = p4 * 100 / numbers
p5 = p5 * 100 / numbers

print("%.2f" % p1 + "%")
print("%.2f" % p2 + "%")
print("%.2f" % p3 + "%")
print("%.2f" % p4 + "%")
print("%.2f" % p5 + "%")