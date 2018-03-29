x=list()
a=input()
arm=0
try:
  p=int(a)
  q=p
except:
  print("Invalid Input")
else:
  while(p>0):        #Reversing part
    rem=p%10
    p=int(p/10)
    x.append(rem)
  for i in range (0,len(x)):
    arm+=(x[i]**3)
 
  if(arm == q):     #Checking part
    print("yes")
  else:
    print("no")
