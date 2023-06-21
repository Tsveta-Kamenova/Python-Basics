num = int(input())

max_num = -9223372036854775807

for i in range(1, num+1):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    else:
        pass
print(max_num)