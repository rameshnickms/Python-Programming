sum=0
try:
  a=int(input())
except:
  print("Invalid Input")
  
else:
  b=input().split()
  if(a == len(b)):
    for i in range (len(b)):
      sum+=int(b[i])
  
    print(sum)
  else:
    print("Invalid Input")


