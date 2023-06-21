n = int(input())
is_n_even = n % 2 == 0
rows = 0
star = 0

if is_n_even:
    rows = n - 1
    star = 2
    dash_mid = 2
    rows_half = (n - 2) // 2
else:
    rows = n
    star = 1
    dash_mid = 1
    rows_half = (n - 2) // 2 + 1

dash_end = (n-star) // 2
print("-"*dash_end + "*"*star + "-"*dash_end)

for i in range(0, rows_half):
    star = 1
    dash_end = (n - star*2 - dash_mid) // 2
    print("-"*dash_end + "*"*star + "-"*dash_mid + "*"*star + "-"*dash_end)
    dash_mid += 2
dash_mid = n-4
for i in range(0, rows_half-1):
    star = 1
    dash_end = (n - star*2 - dash_mid) // 2
    print("-"*dash_end + "*"*star + "-"*dash_mid + "*"*star + "-"*dash_end)
    dash_mid -= 2

if is_n_even:
    star = 2
else:
    star = 1

dash_end = (n-star) // 2
if n >= 3:
    print("-"*dash_end + "*"*star + "-"*dash_end)

