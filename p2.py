#temperature converter python program
temp = []
def conversion(option):
	
	if(option == 1):
		
		temp=input("enter the temperature in celsisus\n")
		f = (temp × 9/5) + 32 
		print("the temperature in fahrenheit is:",f)
	elif(option == 2):
		print("enter the temperature in fahrenheit\n")
		F=input()
		C = (F - 32) x 5/9 
		print("the temperature in celsius is:",C)
	else:
		print("invalid option\n")
	

while true:
	option = input("enter 1 to convert Celsius to Fahrenheit,2 to Convert Fahrenheit to Celsius")
	conversion(option)
