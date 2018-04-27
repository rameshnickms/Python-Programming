try:
  a=int(input())
  line=(input())
except:
  print("Invalid Input")
else:
  x = line.split(' ')
  y=[]
  if(a == len(x)):
    for i in x:
      y.append(int(i))
    print(min((y)))
  else:
    print("Invalid Input")
