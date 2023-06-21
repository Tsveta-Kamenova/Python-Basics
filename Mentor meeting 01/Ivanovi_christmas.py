budget = float(input())
pod_1 = float(input())
pod_2 = float(input())
pod_3 = float(input())

pomosht = budget - pod_1 - pod_2 - pod_3
pomosht = pomosht - 0.1*(pomosht)

print("%.2f"%pomosht)