word = input()
a = 1
e = 2
i = 3
o = 4
u = 5

sum = 0

for c in word:
    if c == "a":
        sum += a
    if c == "e":
        sum += e
    if c == "i":
        sum += i
    if c == "o":
        sum += o
    if c == "u":
        sum += u
    else:
        pass
print(sum)