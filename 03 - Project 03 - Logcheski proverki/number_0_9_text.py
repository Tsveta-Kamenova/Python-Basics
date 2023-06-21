import math

number = int(input())

number_list = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]

if number <= 9:
	print(number_list[number])
else:
	print("number too big")
