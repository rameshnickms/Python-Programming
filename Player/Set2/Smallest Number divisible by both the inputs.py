p,q=input().split()
try:
  a=int(p)
  b=int(q)
except:
  print("Invalid Input")
  
else:
  i=1
  while(1):
    if(((i%a)==0) and ((i%b)==0)):
      print(i)
      break
    i+=1
