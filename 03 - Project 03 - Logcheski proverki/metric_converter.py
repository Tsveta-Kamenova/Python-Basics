# 1. read number
# 2. convert input -> input unit
# a:m * ...
# b:mm * ...
# c:...

# 3. convert input unit -> output unit
# a:m
# b:mm
# c:...

number_input = float(input())
unit_input = str(input())
unit_output = str(input())

conversions = {
                "mm": {"mm": 1, "cm": 1/10, "m": 1/1000, "km": 1/1000000, "yd": 1.0936133/1000, "mi": 0.000621371192/1000, "in": 39.3700787/1000, "ft": 3.2808399/1000},
                "cm": {"mm": 10, "cm": 1, "m": 1/100, "km": 1/100000, "yd": 1.0936133/100, "mi": 0.000621371192/100, "in": 39.3700787/100, "ft": 3.2808399/100},
                "m":  {"mm": 1000, "cm": 100, "m": 1, "km": 1/1000, "yd": 1.0936133, "mi": 0.000621371192, "in": 39.3700787, "ft": 3.2808399},
                "km": {"mm": 1000000, "cm": 100000, "m": 1000, "km": 1, "yd": 1.0936133*1000, "mi": 0.000621371192*1000, "in": 39.3700787*1000, "ft": 3.2808399*1000},
                "mi": {"mm": 1000/0.000621371192, "cm": 100/0.000621371192, "m": 1/0.000621371192, "km": 1/1000/0.000621371192, "yd": 1.0936133/0.000621371192, "mi": 1, "in": 39.3700787/0.000621371192, "ft": 3.2808399/0.000621371192},
                "in": {"mm": 1000/39.3700787, "cm": 100/39.3700787, "m": 1/39.3700787, "km": 0.001/39.3700787, "yd": 1.0936133/39.3700787, "mi": 0.000621371192/39.3700787 , "in": 1, "ft": 3.2808399/39.3700787},
                "ft": {"mm": 1000/3.2808399, "cm": 100/3.2808399, "m": 1/3.2808399, "km": 0.001/3.2808399, "yd": 1.0936133/3.2808399, "mi": 0.000621371192/3.2808399, "in": 39.3700787/3.2808399, "ft": 1},
                "yd": {"mm": 1000/1.0936133, "cm": 100/1.0936133, "m": 1/1.0936133, "km": 0.001/1.0936133, "yd": 1, "mi": 0.000621371192/1.0936133, "in": 39.3700787/1.0936133, "ft": 3.2808399/1.0936133},
              }
convert = conversions[unit_input][unit_output]
answer = number_input * convert

print(str(answer) + " " + unit_output)


