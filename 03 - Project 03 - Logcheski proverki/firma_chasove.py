import math
hrs_needed = int(input())
days_we_have = int(input())
empl_spec = int(input())

work_hrs = 0.9 * days_we_have * 8

hrs_bonus = empl_spec * 2 * days_we_have

hrs_we_have = work_hrs + hrs_bonus
hrs_we_have = math.floor(hrs_we_have)

diff = abs(hrs_needed - hrs_we_have)

#diff = round(diff,0)
#diff = math.floor(diff)
#diff = math.ceil(diff)
#diff = "%.0f" % diff

if hrs_we_have >= hrs_needed:
	print("Yes!" + str(diff) + " hours left.")

else:
	print("Not enough time!" + str(diff) + " hours needed.")

