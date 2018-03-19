d=list()
a=(input())
c=(len(a))

for i in range (c):
  d.append((a.count(a[i])))
  
for i in range (len(d)):
  for j in range(len(d)):
    if (d[i]<d[j]):
      l=d[i]
    else :
      b=d[i]
      d[i]=d[j]
      d[j]=b
     
for i in range (c):
  if(d[0]==(a.count(a[i]))):
    print(a[i])
    break
