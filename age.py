from datetime import date 

def ageconvert(x):
	today = date.today() 
	age = today.year - x.year - ((today.month,today.day) < (x.month,x.day)) 
	
	return age

year=int(input("enter the year"))
mm=int(input("enter the month"))
dd=int(input("enter the date"))

print(ageconvert(date(year,mm,dd)),"years")

