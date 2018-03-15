a=input()
try:
  b=int(a)
except:
  print("Invalid Input")
  exit()
if(b>0):
  print('positive')
elif(b<0):
  print('negative')
else:
  print('zero')
