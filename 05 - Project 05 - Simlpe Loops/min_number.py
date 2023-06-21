num = int(input())

min_num = +9223372036854775807

for i in range(1, num+1):
    current_num = int(input())
    if current_num < min_num:
        min_num = current_num
    else:
        pass
print(min_num)