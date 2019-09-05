#demo classes in python
#concept:use of delete attribute of obj and obj itself

class Person:
	def __init__(self,name,age):	#constructor of the class Person
		 self.name=name;
		 self.age=age;

p1 = Person('supandi',14)

print("\n the name of person1 is:",p1.name)
print("\n the age of person1 is:",p1.age)

print("\n ***printing after deleting age attribute ***\n")

del p1.age						#deleting age attribute
print("\n the name of person1 is:",p1.name)

print("\nprinting after deleting p1")
del p1
print("\n the name of the person:",p1.name)       	#gives an error



