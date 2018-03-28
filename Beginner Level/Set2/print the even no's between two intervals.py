x=list()
a,b=input().split()
try:
  p=int(a)
  q=int(b)
except:
  print("Invalid Input")
else:
  c=max(p,q)
  d=min(p,q)
  for i in range (d+1,c):
    if(i%2 == 0):
      x.append(str(i))
    else:
      continue
  print(" ".join(x))
