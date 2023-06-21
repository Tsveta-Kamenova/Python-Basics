import math
year = str(input())
holyday = int(input())
weekends = int(input())

weekends_sofia = 48 - weekends
saturday_games = 0.75 * weekends_sofia
sunday_games = weekends
holyday_games = holyday * 2 / 3
games = saturday_games + sunday_games + holyday_games

if year == "leap":
    games = games * 1.15
    games = math.floor(games)
else:
    games = math.floor(games)
print(games)


