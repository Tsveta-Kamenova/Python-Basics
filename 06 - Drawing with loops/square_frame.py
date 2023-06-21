n = int(input())
dash = n-2

print("+" + " -"*dash + " +")
for row in range(0, n-2):
    print("|" + " -"*dash + " |")
print("+" + " -"*dash + " +")
