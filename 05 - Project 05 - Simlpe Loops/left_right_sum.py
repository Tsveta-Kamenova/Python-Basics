numbers = int(input())

sum_left = 0
sum_right = 0

for l in range(0, numbers):
    current_num_left = int(input())
    sum_left += current_num_left
for r in range(0, numbers):
    current_num_right = int(input())
    sum_right += current_num_right
if (sum_left == sum_right):
    print("Yes, sum = %d" % sum_right)
else:
    print("No, diff = %d" % abs(sum_left - sum_right))