 # two add two numbers
a= input("enter the number")
b=input("enter another number")
cal=input("press 1 to add ,press 2 to substract,press 3 to mul")
if (cal==1):
 ans=a+b
 print("the addition of two numbers is ",ans)
elif(cal==2):
 ans=a-b
 print("the substraction of numbers is ",ans)
elif(cal==3):
 ans=a*b
 print(ans)
else:
 print("invalid choice")
