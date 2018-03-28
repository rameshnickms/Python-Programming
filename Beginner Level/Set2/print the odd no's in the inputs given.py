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
      continue
    else:
      x.append(str(i))
  print(" ".join(x))
