rev=0
rem=0
try:
  a=input()
  p=int(a)
  q=p
except:
  print("Invalid Input")
else:
  while(p>0):
    rem=p%10
    p=int(p/10)
    rev=(rev*10)+rem
  if(rev == q):
    print("yes")
  else:
    print("no")
    
