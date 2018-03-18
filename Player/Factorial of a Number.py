a=input()
sum=1
try:
  b=int(a)
  
except:
  print("Invalid Input")
  
else:
  if(b<=20):
    
    for i in range(1,b+1):
      sum*=i
    
    print(sum)
    
  else:
    print("Input is out of Range")
