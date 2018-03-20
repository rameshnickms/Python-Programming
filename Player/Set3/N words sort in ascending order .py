n=input()
k=list()
try:
  a=int(n)
  
except:
  print("Invalid Input")
  
  
else:
  #print(k)
  l=input().split()
  #print(l)
  l.sort()
  #print(len(l))
  if(len(l) == a):
    print ( ' ' .join(l))
  else:
    print("Invalid Input")
