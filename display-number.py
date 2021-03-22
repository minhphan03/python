def displayNumber(x)
	n= 1
	if x > 7:
		while x>7:
		print("{}, {}, {}, {}, {}, {}, {}".format(n,n+1,n+2,n+3,n+4,n+5,n+6))
		n = n+7
		x = x-7
	while x>0:
		print('{},'.format(n),end=' ')
		n = n+1
		x = x-1

displayNumber(13)

