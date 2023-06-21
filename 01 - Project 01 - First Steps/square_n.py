n = int(input())

print("*"*n)

for i in range(1, (n-2)+1):
    print("*" + " "*(n-2) + "*")

print("*"*n)