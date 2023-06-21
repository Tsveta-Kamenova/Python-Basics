numbers = int(input())

max_num: int = -9223372036854775807
sum = 0

for i in range(0, numbers):
    current_num = int(input())
    sum += current_num
    if current_num > max_num:
        max_num = current_num

if max_num == (sum-max_num):
    print("Yes")
    print("Sum = " + str(max_num))
else:
    print("No")
    print("Diff = " + str(abs((max_num-(sum-max_num)))))