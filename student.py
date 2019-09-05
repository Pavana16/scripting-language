students = {
	"1MS17IS100": "Rosie",
	"1MS17IS101": "Ashok",
  	"1MS17IS102": "Rekha",
  	"1MS17IS103": "Roshan"
}

list1 = ["value1", "value2", "value3", "value4"]

list2 = []

j=0

#Printing student names
for i in students:
	print("Key is: ", i," Value is: ", students[i])
	list1[j] = students[i]
	#list2[j] = i
	j = j+1

print(list1)
#print(list2)

print(students.keys())
print(students.values())
print(students.items())
