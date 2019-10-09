
def hourminute(x):
	hour=0
	num=x
	if num>=60:
		num=int(num)-60
		hour=hour+1
	print(hour)
