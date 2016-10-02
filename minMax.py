largest=None
smallest=None

while True:
	num=raw_input("enter a number: ")
	if num=='done' :break
	
	try: num=int(num)
	except:
		print "Invalid input"
		continue
	
	if num<smallest or smallest is None:
		smallest=num
	elif num>largest or largest is None:
		largest=num
print "Mamximum is ",largest
print "Minimum is ",smallest

	
	
		

