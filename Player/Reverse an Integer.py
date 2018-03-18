try:
  N=int(input())
except:
  print("Invalid Input")

else:
  Rev = 0    
  while(N > 0):    
      Reminder = N %10    
      Rev = (Rev *10) + Reminder    
      N = N //10    
     
  print(Rev) 
