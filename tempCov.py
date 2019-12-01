'''
(C * 9/5) + 32
(f-32)* 5/9
'''
def c2f(temp):
    return ((temp*9.0)/5.0)+32
def f2c(temp):
    return (temp-32)*5.0/9.0
def history(l):
    for i in l:
            print(i[0],"->",i[1])
    
l1=list()

while True:
    print("-"*40,"\nMenu\n"+"-"*40,"\n1 for C->F\n2 for F->C\n3 to diplay previous conversions\n0 to quit")
    sel=int(input("Enter : "))
    if sel==1:
        temp=float(input("Enter Temp in C : "))
        x1=str(temp)+" C"
        x2=str(c2f(temp))+" F"
        print("Temp :",x2)
        l1.append((x1,x2))
        
    elif sel==2:
        temp=float(input("Enter Temp in F : "))
        x1=str(temp)+" F"
        x2=str(f2c(temp))+" C"
        print("Temp :",x2)
        l1.append((x1,x2))
    
    elif sel==3:
        history(l1)

    elif sel==0:
        print("----Thank You----")
        break
    else:
        print("Invalid Input")
