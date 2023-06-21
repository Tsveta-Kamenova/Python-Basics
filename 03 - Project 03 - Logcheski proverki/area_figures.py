# 1. read figure type
# 2. check if:
#   a: square -> read "a"
#   b: rectangle -

import math

figure_type = input()

a = float(input())
area = 0

if figure_type == "square":
    area = a * a
elif figure_type == "rectangle":
    b = float(input())
    area = a * b
elif figure_type =="circle":
    area = math.pi * math.pow(a,2)
elif figure_type == "triangle":
    height = float(input())
    area = (a * height)/2
print ("%.3f" % area)