type_projection = input()
row_num = int(input())
column_num = int(input())
income = float()

tickets = row_num * column_num

if type_projection == "Premiere":
    income = tickets * 12
elif type_projection == "Normal":
    income = tickets * 7.5
elif type_projection == "Discount":
    income = tickets * 5
print(("%.2f" % income) + " leva")