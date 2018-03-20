sum=0
try:
  a,b=(input().split())
  p=int(a)
  q=int(b)
except:
  print("Invalid Input")
  
else:
  e=input().split()
  if(len(e)==p):
    for i in range (q):
      sum+=int(e[i])
    print(sum)
  else:
    print("Invalid Input")
  
    
