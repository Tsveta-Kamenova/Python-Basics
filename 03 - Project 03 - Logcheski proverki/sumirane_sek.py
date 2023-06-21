first_player = int(input())
second_player = int(input())
third_player = int(input())

sum_sec = first_player + second_player + third_player
min = sum_sec // 60
sec = sum_sec % 60

if sec <= 9:
    print(str(min) + ":0" + str(sec))
else:
    print(str(min) + ":" + str(sec))
