#Depends on the figure name an app calculates figure`s square

import math

figure_name = str(input("figure name "))
if figure_name == "triangle":
	a = float(input ("1 side "))
	b = float(input ("2 side "))
	c = float(input ("3 sideа "))
	if a + b > c or b + c > a or c + a > b:
		p = (a + b + c) / 2
		print(p * (p -a) * (p - b) * (p -c) **0.5)
	else:
		print("Wrong parametrs. A sum of 2 sides is always bigger than a one`s length")
elif figure_name == "rectangle":
	a = float(input("1 side "))
	b = float(input("2 side "))
	print(a * b)
else: 
	r = float(input("radius ")
	print((r ** 2) * math.pi)
