x=input("enter the range ")
x=int(x)
a=0
b=1
print(a,b)
for i in range(2,x):
   c=a+b
   a=b
   b=c
   print(c)