try:
  p,q,r=input().split()
  a=int(p)
  e=int(q)
  o=int(r)
  
except:
  print("Invalid Input")
  
else:
  s=((a*e*o)/100)
  print(int(s))
