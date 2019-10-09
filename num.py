x=int(input("enter the 1st number"))
one=x
y=int(input("enter the 2nd number"))
two=y

def odd(one,two):
	newlist = []
	for i in range(one,two):
		if i % 2 !=0:
			newlist.append(i)
	
	print(newlist)
	return newlist	
	
odd(one,two)	

