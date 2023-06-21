price_whisky = float(input())
beer = float(input())
wine = float(input())
rakia = float(input())
whisky = float(input())

price_rakia = price_whisky*0.5
price_wine = price_rakia*0.6
price_beer = price_rakia*0.2

money = beer*price_beer + whisky*price_whisky + wine*price_wine + rakia*price_rakia
print("%.2f"%money)