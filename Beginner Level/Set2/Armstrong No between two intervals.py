arm=0
x=list()
y=list()
a,b=input().split()
try:
  p=int(a)
  q=int(b)
except:
  print("Invalid Input")
else:
  c=max(p,q)
  d=min(p,q)
  for w in range (d+1,c):
    x=[]
    arm=0
    j=w
    
    while(w>0):        #Reversing part
      rem=w%10
      w=int(w/10)
      x.append(rem)
    for i in range (0,len(x)):
      arm+=(x[i]**3)
    
    if(arm == j):
      y.append(str(arm))
    else:
      continue  
  print(' '.join(y))

