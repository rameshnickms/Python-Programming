a=0
try:
  b=(input())
  a=int(b)
except:
  if(b == 'a' or b== 'e' or b=='i' or b=='o' or b=='u'):
    print("Vowel")
  else:
    print("Consonant")

else:
  print("Invalid Input")
  
