numbers = int(input())

sum_even = 0
sum_odd = 0

for i in range(0, numbers):
    current_num = int(input())
    if i % 2 == 0:
        sum_even += current_num
    else:
        sum_odd += current_num
if sum_odd == sum_even:
    print("Yes")
    print("Sum = " + str(sum_even))
else:
    print("No")
    print("Diff = " + str(abs(sum_even-sum_odd)))