import math
x11=int(input("X1 value:"))
y11=int(input("Y1 value:"))
x22=int(input("X2 value:"))
y22=int(input("Y2 value:"))
x33=int(input("X3 value:"))
y33=int(input("Y3 value:"))
a1=x22-x11
b1=y22-y11
a2=x33-x22
b2=y33-y22
a3=x33-x11
b3=y33-y11
ans11=math.sqrt(a1*a1+b1*b1)
ans22=math.sqrt(a2*a2+b2*b2)
ans33=math.sqrt(a3*a3+b3*b3)
if(ans33==(ans11+ans22)):
	print("Yes")
else:
	print("No")
