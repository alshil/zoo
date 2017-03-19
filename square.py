## На вход принимается название фигуры, значения ее сторон, 
## рассчитывается площадь.

figure_name = str (input("название фигуры "))
if figure_name == "треугольник":
	a = float (input ("1 сторона "))
	b = float (input ("2 сторона "))
	c = float (input ("3 сторона "))
## Ниже проверяется основное правило треугольника
	if a + b > c or b + c > a or c + a > b:
		p = (a + b + c) / 2
		print (p * (p -a) * (p - b) * (p -c) **0.5 )
	else:
		print ("Неверные параметры.Сумма двух сторон всегда больше третьей стороны")
elif figure_name == "прямоугольник":
	a = float (input ("1 сторона "))
	b = float (input ("2 сторона "))
	print (a * b)
else figure_name == "круг":  ## ругается на эту строчку!
	radius = float (input("радиус окружности ")
	pi = 3.14
	print ((radius ** 2) * pi)
