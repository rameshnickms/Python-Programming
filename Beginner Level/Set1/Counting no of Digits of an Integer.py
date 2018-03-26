s=0
try:
  a=input()
  b=int(a)
except:
  print("Invalid Input")
else:
  for i in str(b):
    s+=1
  print(s)
