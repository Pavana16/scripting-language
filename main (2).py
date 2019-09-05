class student:                                   #create class
    def __init__(self,name,age,marks):          #create constructor
        self.name = name
        self.age = age
        self.marks = marks[:]
        
    def display(self):                         #member function to display
        print("name:",self.name)
        print("age:",self.age)
        i=1 
        for mark in self.marks:
            print("marks of subj1",i,"=",mark)
            i += 1
            
marks = []                                     
def accept():
        name = input("enter the name of student:")
        age = input("enter the age:")
        print("enter the sub")
        i=1
        for i in range(3):
            marks.append(input())
            
        return name,age,marks
            
name, age, marks = accept()
p1 = student(name,age,marks)
    
marks = []
    
name,age,marks = accept()
p2 = student(name,age,marks)
    
print(p1.display())                     #calling the display function
print()
print(p2.display())


