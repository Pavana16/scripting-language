#A
	#read a list of elements.
	#create a new list having all the elements minus the duplicate.


def removeduplicates(list1):
	newlist = []
	for number in list1:
		if number not in newlist:
			newlist.append(number)
			
	print(newlist);
	return newlist
list1=[1,2,3,4,5,5,5,6,3,2]
removeduplicates(list1)

#can be done this way also
def removeduplicates(numbers):
	newlist = []
	for number in numbers:
		if number not in newlist:
			newlist.append(number)
			
	print(newlist);
	return newlist

removeduplicates([1,2,3,4,5,5,5,6,3,2])

#use one-line comprehensive of create a new list of even numbers.
#create another list reversing the elements.
S = [x**2 for x in range(10)] #read elementsin list
print(S);
m = [x for x in S if x%2 == 0]
m.reverse()
print(m);

#B
#write a python program to count the frequency of words in a given file
from collections import Counter
def count_word(fname):
	with open(fname) as f:
		return Counter(f.read().split())
		
print("number of words in the file :",count_word("text.txt"))

#c
#read a list of  numbers.uses a recursive function to find the maximum of 'n' numbers:
