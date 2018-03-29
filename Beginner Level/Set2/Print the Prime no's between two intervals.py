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
  j=2
  for i in range (d+1,c):
    while(1):
      if(i%j == 0):
        if(i == j):
          x.append(str(i))
          j=2
          break
        else:
          j=2
          break
      else:
        j+=1
  print(" ".join(x))
