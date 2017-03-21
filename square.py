# Depends on the figure name an app calculates figure`s square
figure_name = str (input("figure name "))
if figure_name == "triangle":
	a = float (input ("1 side "))
	b = float (input ("2 side "))
	c = float (input ("3 sideа "))
	if a + b > c or b + c > a or c + a > b:
		p = (a + b + c) / 2
		print (p * (p -a) * (p - b) * (p -c) **0.5 )
	else:
		print ("Wrong parametrs.A sum of 2 sides is always bigger than a one`s length")
elif figure_name == "rectangle"
	a = float (input ("1 side "))
	b = float (input ("2 side "))
	print (a * b)
elif figure_name == "circle": 
	cir_radius = float (input("radius ")
	print (((cir_radius) **2) 3.14)
