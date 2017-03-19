## You can enter 3 numbers.
## An app will show the bigest number first, 
## than the smallest one 
## and a middle in the end.

a = int (input ("Enter the first number "))
b = int (input ("Enter the second number "))
c = int (input ("Enter the third number "))
if c < b < a:
	print (a)
	print (b)
	print (c)
elif c < a < b:
	print (b)
	print (c)
	print (a)
elif b < a < c:
	print (c)
	print (b) 
	print (a)	
elif a < b < c:
	print (c)
	print (a)
	print (b)
elif a < c < b:
	print (b)
	print (a)
	print (c)
else:
	print (a)
	print (b)
	print (c)
