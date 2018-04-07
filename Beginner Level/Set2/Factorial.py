fact=1
try:
  a=input()
  b=int(a)
except:
  print("Invalid Input")
  
else:
  for i in range (1,b+1):
    fact*=i
    
  print(fact)
  
  
