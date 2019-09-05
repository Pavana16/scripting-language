x = -3

if x > 0.0:
	print("Positive")

elif x < 0.0:
	print("Negative")
	x = -1.0*x

else:
	print("Zero")

#Alternative way

if x > 0:
	print("+ve")

else:
	if x < 0:
		print("-ve")
		x = -1.0*x
	else:
		print("0")
