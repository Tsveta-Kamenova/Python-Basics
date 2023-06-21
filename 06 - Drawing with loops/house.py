n = int(input())
roof = (n+1)//2
base = n - roof
star = 0

is_n_even = n % 2 == 0

if is_n_even:
    star = 2
    dash = (n - star) // 2
    print("-" * dash + "*" * star + "-" * dash)
else:
    star = 1
    dash = (n - star) // 2
    print("-" * dash + "*" * star + "-" * dash)

for row in range(1, roof):
    star += 2
    dash = (n - star) // 2
    print("-" * dash + "*" * star + "-" * dash)

for row in range(0,base):
    print("|" + "*"*(n-2) + "|")