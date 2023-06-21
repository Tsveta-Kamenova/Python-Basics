number = int(input())
number_list = ["Error", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if number <= 7 and number > 0:
    print(number_list[number])
else:
    print("Error")