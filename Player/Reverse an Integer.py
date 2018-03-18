try:
  N=int(input("Please Enter any Number: "))
except:
  print("Invalid Input")

else:
  Rev = 0    
  while(N > 0):    
      Reminder = N %10    
      Rev = (Rev *10) + Reminder    
      N = N //10    
     
  print("\n Reverse of entered number is = %d" %Rev) 
