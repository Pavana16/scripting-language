#1
	list1=['pavana',20,'bangalore']
	print("the lis is:",list1)
	print("length of the string is:",len(list1))

	list2=['pavana krishna','msrit',2021,'bangalore']
	print("the second list is:",list2)
	print("length of second string is:",len(list2))

	#slice operator
	print("slice operator:")
	print(list2[1:3])

	#replace with fruit name
	list1[1]='orange'
	print("second element of list1 is replaced by a fruit",list1)

	#concatenation
	list3=list1+list2
	print("the concatenated list:",list3)	

#2
	mytuple=(16,5,19,4)
	print(mytuple[2])

#3
	mylist=list(mytuple)
	print(mylist)
	mylist[1]='pav'
	print(mylist)

