a,b=input().split()
p=int(a)
q=int(b)
c=max(p,q)
d=min(p,q)
for i in range (d+1,c):
  if(i%2 == 0):
    #print(i)
    continue
  else:
    print(i)
   
