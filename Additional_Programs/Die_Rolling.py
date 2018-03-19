import random

def again(b):
    if(b==1 or b==5 or b==6):
      p=input("Roll again...y/n?")
      if(p=='y'):
        roll()
      else:
        print("Game Over!!!")
    else:
      print("Game Over!!")
      q=input("Want to Play again..y/n?")
      if(q=='y'):
        roll()
      else:
        print("Good Bye")
def roll():
  b=int(random.randint(1,6))
  print("Rolled no..",b)
  again(b)
while(1):
    a=input("Start Rolling y/n")
    if(a=='y'):
      roll()
      break
    else:
      print("Game Over!!!")
      break


