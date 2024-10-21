#wap to find factorial of given number

n=int(input("Enter n = "))
fact=0

for i in range(1,n+1):
    fact=fact*i
print("factorial is = ",fact)