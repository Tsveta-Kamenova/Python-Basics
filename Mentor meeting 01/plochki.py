pg_l = int(input())
l_pl = float(input())
w_pl = float(input())
l_pej = int(input())
w_pej = int(input())
t_pl = 0.2

area_pg = pg_l ** 2
area_pl = l_pl * w_pl
area_pej = l_pej * w_pej

area_pokr = area_pg - area_pej
broi_pl = area_pokr / area_pl

time = broi_pl * t_pl
print ("%.2f" % broi_pl)
print("%.2f" % time)
