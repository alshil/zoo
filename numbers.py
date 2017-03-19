## You can enter 3 numbers.
## An app will show the bigest number first, 
## than a smaller one and the smallest.

a = int (input ("Enter the first number "))
b = int (input ("Enter the second number "))
c = int (input ("Enter the third number "))
if a > b and a > c and b > c:
	print (a + '/n' + b + '/n' + c)
elif c < a < b:
	print (b)
	print (a)
	print (c)
elif b < a < c:
	print (c)
	print (a) 
	print (b)	
elif a < b < c:
	print (c)
	print (b)
	print (a)
elif a < c < b:
	print (b)
	print (c)
	print (a)
else:
	print (a)
	print (c)
	print (b)
