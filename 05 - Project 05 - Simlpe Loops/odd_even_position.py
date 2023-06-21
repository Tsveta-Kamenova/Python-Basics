numbers = int(input())
odd_sum = 0
odd_min = +9223372036854775807
odd_max = -9223372036854775807
even_sum = 0
even_min = +9223372036854775807
even_max = -9223372036854775807

for i in range(1, numbers+1):
    current_num = float(input())
    if i % 2 == 0:
        even_sum += current_num
        if current_num < even_min:
            even_min = current_num
        if current_num > even_max:
            even_max = current_num
    else:
        odd_sum += current_num
        if current_num < odd_min:
            odd_min = current_num
        if current_num > odd_max:
            odd_max = current_num

print("OddSum=" + "%g" % float(odd_sum))

if odd_min == +9223372036854775807:
    print("OddMin=No")
else:
    print("OddMin=" + "%g" % float(odd_min))

if odd_max == -9223372036854775807:
    print("OddMax=No")
else:
    print("OddMax=" + "%g" % float(odd_max))

print("EvenSum=" + "%g" % float(even_sum))

if even_min == +9223372036854775807:
    print("EvenMin=No")
else:
    print("EvenMin=" + "%g" % float(even_min))

if even_max == -9223372036854775807:
    print("EvenMax=No")
else:
    print("EvenMax=" + "%g" % float(even_max))