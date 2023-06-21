cats = int(input())

for i in range(1, cats+1):
    name = str(input())
    family_name = str(input())
    birth = int(input())
    b = ''.join([s[:1] for s in name.split(' ')])
    b = ord(b)
    c = ''.join([s[:1] for s in family_name.split(' ')])
    c = ord(c)
    a = birth
    d = i

    print(a, end="")
    print(b, end="")
    print(c, end="")
    print(d, end="")
    print("")