a = int (input("первое число "))
b = str (input("операция "))
c = int (input("второе число "))
if b == "+":
	print (a + c)
elif b == "-":
	print (a - c)
elif b == "/":
	if c != 0:
		print (a / c)
	else:
		print ("Деление на 0!")	
		b = int (input ("второе число "))
		print (a / c)			
elif b == "*":
	print (a * c)
elif b == "mod":
	if c != 0:
		print (a % c)
	else:
		print ("Деление на 0!")
		b = int (input ("второе число" ))
		print (a % c)		
elif b == "pow":
	print (a ** c)
elif b == "dev":
	if c != 0:
		print (a // c)
	else:
		print ("Деление на 0!")
		b = int (input ("второе число "))
		print (a // c)
