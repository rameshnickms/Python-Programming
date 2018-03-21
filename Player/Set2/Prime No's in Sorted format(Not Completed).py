p=list()

try:
  a=int(input())
  
except:
  print("Invalid Input")
  
else:
  i=2
  j=2
  while(i<=a):
    if(a%i == 0):
      print(i)
      if(i%j == 0):
        
        if(i == j):
          print(i)
          p.append(i)
          j-=1
    i+=1
