x=input("enter the number")
x=int(x)
y=len(str(x))
num=x
result=0
while(x!=0):
    digit=x%10
    result=result+digit**y
    x=x//10
if(num==result):
    print("it is amstrong number ")
else:
    print("it is not an amstrong")