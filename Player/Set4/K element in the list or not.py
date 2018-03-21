try:
  a,b=(input().split())
  p=int(a)
  q=int(b)
except:
  print("Invalid Input")
  
else:
  e=input().split()
  if(len(e)==p):
    if str(q) in e:
      print("Yes")
    else:
      print("No")
  else:
    print("Invalid Input")
