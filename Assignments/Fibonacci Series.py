try:
  q=int(input())
  
except:
  print("Invalid Input")

else:
  p=list()
  a=0
  b=1
  c=0


  for i in range (q):
    p.append(c)
    print(c)
    c=a+b
    a=b
    b=c
  print(p)
