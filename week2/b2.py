import math


pi = 3.14

width  = int(input("Input width: "))
height = int(input("Input height: "))
recArea = width * height
cirArea = min(width, height) / 2 ** 2 * pi
print(f"Area left: {recArea - cirArea}")