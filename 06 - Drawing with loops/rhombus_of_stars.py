n = int(input())
#for row in range (1,n+1):
    #print(" "*(n-row)+"* "*row)
#for row in range (1,n):
    #print(" "*row + "* "*(n-row))

star = "*"
space = " "
second_part_star = n-1

for row in range (1,2*n):
    if row <= n:
        space = n-row
        star = row
        print(" "*space + "* "*star)
    else:
        space = row - n
        print(" "*space + "* "*second_part_star)
        second_part_star -= 1
