h = int(input())
x = int(input())
y = int(input())

x1_rec1 = 0
y1_rec1 = 0
x2_rec1 = 3*h
y2_rec1 = h

x1_rec2 = h
y1_rec2 = h
x2_rec2 = 2*h
y2_rec2 = 4*h

if x2_rec1 > x > x1_rec1 and y2_rec1 > y > y1_rec1:
    print("Inside")
elif x2_rec2 > x > x1_rec2 and y2_rec2 > y > y1_rec2:
    print("Inside")
elif (x2_rec1 == x or x == x1_rec1) and (y2_rec1 >= y or y >= y1_rec1):
    print("Border")
elif (x2_rec1 >= x or x >= x1_rec1) and (y2_rec1 == y or y == y1_rec1):
    print("Border")
else:
    print("Outside")