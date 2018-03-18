
a=input()

try:
  c=int(a)
except:
    
  b=len(a)
  if(b<=6):
    print(a[::-1])
  

else:
  print("Invalid Input")
