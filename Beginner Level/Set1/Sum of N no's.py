sum=0
try:
  a=input()
  b=int(a)
except:
  print("Invalid Input")
else:
  for i in range(b+1):
    sum+=i
  print(sum)
