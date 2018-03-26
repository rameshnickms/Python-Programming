try:
  a,b,c=input().split()
  p=int(a)
  q=int(b)
  r=int(c)
except:
  print("Invalid Input")
else:
  if(p>q):
    if(p>r):
      print(p)
    else:
      print(r)
  elif(q>r):
    print(q)
  else:
    print(r)
