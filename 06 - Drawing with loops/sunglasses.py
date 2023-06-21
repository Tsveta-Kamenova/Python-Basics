n = int(input())

star = 2*n
space = 5*n - 4*n
slash = 2*n - 2

is_n_even = n%2 == 0

print("*"*star + " "*space + "*"*star)

for row in range (1, n-1):
    if row == n//2 and not is_n_even:
        print("*" + "/" * slash + "*" + "|" * space + "*" + "/" * slash + "*")
    elif is_n_even and row == n//2 - 1:
        print("*" + "/" * slash + "*" + "|" * space + "*" + "/" * slash + "*")
    else:
        print("*" + "/" * slash + "*" + " " * space + "*" + "/" * slash + "*")
print("*"*star + " "*space + "*"*star)
