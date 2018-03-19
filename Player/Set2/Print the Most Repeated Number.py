d=list()
a=(input())
c=(len(a))
print(c)
for i in range (c):
  d.append((a.count(a[i])))
  print(d)
for i in range (len(d)):
  for j in range(len(d)):
    if (d[i]<d[j]):
      l=d[i]
    else :
      b=d[i]
      d[i]=d[j]
      d[j]=b
      print(d) 
print(d[0])
