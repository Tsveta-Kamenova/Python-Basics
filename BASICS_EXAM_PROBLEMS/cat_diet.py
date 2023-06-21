fats = int(input())
protein = int(input())
carbs = int(input())
sum_calories = int(input())
water = int(input())

fats_gr = fats/100*sum_calories/9
protein_gr = protein/100*sum_calories/4
carbs_gr = carbs/100*sum_calories/4

food_gr = fats_gr + protein_gr + carbs_gr
calories = sum_calories/food_gr
calories_real = (100-water)/100*calories

print("%.4f" % calories_real)