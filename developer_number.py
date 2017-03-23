## App counts the number of developers sitting in the room
## and pronounce the number correctly in russian

developer_number = int (input ())
if 0 <= developer_number <= 1000: #Enter a number of developers
	if developer_number % 10 == 1 and developer_number != 11:
	    print (developer_number, " программист")
	elif developer_number % 10 == 2:
		print (developer_number, "программиста")
	elif developer_number % 10 == 3:
		print (developer_number, "программиста")
	elif developer_number % 10 == 4:
		print (developer_number, "программиста")
	elif developer_number % 10 == 5:
		print (developer_number, "программистов")
	elif developer_number % 10 == 6:
		print (developer_number, "программистов")
	elif developer_number % 10 == 7:
		print (developer_number, "программистов")
	elif developer_number % 10 == 8:
		print (developer_number, "программистов")
	elif developer_number % 10 == 9:
		print (developer_number, "программистов")
	elif developer_number % 10 == 0:
		print (developer_number, "программистов")
	else:
		print (developer_number, "программистов")
else:
	print ("Print a number between 0 - 1000") 
