
def hourminute(x):
	if x < 60:
		print("0:",x)
	else: 
		hours=x/60
		mins=x%60
		print(int(hours),":",mins)
num = int(input("enter the minutes:"))
hourminute(num)
