e=0
try:
  a=input()
  p=int(a)
except:
  print("Invalid Input")
else:
  for i in range (2,p-1):
    if(p%i == 0):
      e=1
      break
    else:
      continue
  if(e == 1 or p == 1):
    print("no")
  else:
    print("yes")
