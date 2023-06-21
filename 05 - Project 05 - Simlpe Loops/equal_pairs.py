# read pairs
# find sum of numbers in pairs
# compare two sequential pairs, only if there are more than 1 pair
# store max difference between two sequential pairs


pairs = int(input())

pair = 0
pair1 = 0
pair2 = 0
maxdiff = -9223372036854775807
maxdiff_current = 0

for i in range(1, pairs + 1):
    a = int(input())
    b = int(input())
    pair = a + b
    if i % 2 != 0:
        pair1 = pair
    else:
        pair2 = pair

    if i >= 2:
        maxdiff_current = abs(pair2 - pair1)

    if maxdiff_current > maxdiff:
        maxdiff = maxdiff_current

if pair1 == pair2 or pairs == 1:
    print("Yes, value=" + str(pair1))
else:
    print("No, maxdiff=" + str(maxdiff))
