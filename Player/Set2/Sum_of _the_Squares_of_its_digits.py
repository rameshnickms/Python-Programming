try:
  a=int(input())
except:
  print("Invalid Input")
else:
  sum=0
  while(a>0):
    b=(a%10)
    c=(int(a/10))
    sum+=b**2
    a=c
  print(sum)
  
  
