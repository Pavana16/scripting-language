from datetime import date 

def ageconvert(year,dd,mm):
	today = date.today() 
	age = today.year - year - ((today.month, today.day) < (mm, dd)) 
	print(age)
	return age
x=input("enter the dob da-mo-year")
year=int(x[5:])
dd=int(x[:1])
mm=int(x[3:4])

ageconvert(year,dd,mm)

