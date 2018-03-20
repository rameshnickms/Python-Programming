
try:
  a,b=(input().split())
  p=int(a)
  q=int(b)
except:
  print("Invalid Input")
  
else:
  e=input().split()
  if(len(e)==p):
    h=len(e)
    f=e[(h-q):] + e[:(h-q)]
    print(' ' .join(f))
  else:
    print("Invalid Input")
    
  
