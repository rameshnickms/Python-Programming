try:
  a=int(input())
except:
  print("Invalid Input")
else:
  sum=0
  if(a>=1 and a<=1000000000000000000):
    while(a>0):
      b=(a%10)
      c=(int(a/10))
      sum+=b**2
      a=c
    print(sum)
  
  else:
    print("Invalid Input")
