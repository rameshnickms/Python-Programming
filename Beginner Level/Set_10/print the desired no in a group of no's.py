try:
  p,q=input().split()
  a=int(p)
  e=int(q)
except:
  print("Invalid Input")
  
else:
  b=input().split()
  if(a == len(b)):
    print(b[e-1])
  else:
    print("Invalid Input")
