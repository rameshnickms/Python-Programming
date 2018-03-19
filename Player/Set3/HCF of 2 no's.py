
def HCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
try:
  num1 = int(input())
  num2 = int(input())

except:
  print("Invalid Input")
  
else:
  print(HCF(num1, num2))
