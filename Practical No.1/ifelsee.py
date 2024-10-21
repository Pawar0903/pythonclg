#wap to find largest of three numbers

n1=int(input("Enter num1=  "))
n2=int(input("Enter num=  "))
n3=int(input("Enter num3=  "))

if(n1>n2 and n1>n3):
    print("num1 is greater",n1)
elif(n2>n1 and n2>n3):
        print("n2 is greater",n2)
else:
    print("n3 is greater",n3)
    