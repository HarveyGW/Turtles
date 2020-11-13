import turtle
from random import randrange
from colorama import Fore

def TurtleKeys():
  turtle.setup(400,500)
  wn = turtle.Screen() 
  wn.bgcolor("Blue")
  turtl = turtle.Turtle() 
  
  def h1():
    turtl.forward(30)
  
  def h2():
    turtl.left(45)
  
  def h3():
    turtl.right(45)
  
  def h4():
    wn.bye() 
  wn.onkey(h1, "Up")
  wn.onkey(h2, "Left")
  wn.onkey(h3, "Right")
  wn.onkey(h4, "q")
  wn.listen()
  wn.mainloop()


def TurtleRandom(bg):
  #Takes in bg = background colour

  turtle.setup(400,500)
  wn = turtle.Screen() 
  wn.bgcolor(bg)
  turt = turtle.Turtle() 
  bob = turtle.Turtle()

  turt.color('red')
  bob.color('blue')

  turtList=[]
  nestedTurt=[]
  bobList=[]
  nestedBob=[]

  while 1:
    
    leftRandTurt = randrange(25,100)
    forwardRandTurt = randrange(25,100)

    nestedTurt.append(leftRandTurt)
    nestedTurt.append(forwardRandTurt)

    turtList.append(nestedTurt)
    
    turt.forward(forwardRandTurt)
    turt.left(leftRandTurt)

    leftRandBob = randrange(25,100)
    forwardRandBob = randrange(25,100)

    nestedBob.append(leftRandBob)
    nestedBob.append(forwardRandBob)

    bobList.append(nestedBob)

    bob.forward(leftRandBob)
    bob.left(leftRandBob)

    print(Fore.RED + "LeftRandTurt Value: " + str(leftRandTurt))
    print(Fore.RED + "forwardRandTurt Value: " + str(forwardRandTurt))
    print(Fore.RED + "nestedTurt: " + str(nestedTurt))
    print(Fore.BLUE + "LeftRandBob Value: " + str(leftRandBob))
    print(Fore.BLUE + "forwardRandBob Value: " + str(forwardRandBob))
    print(Fore.BLUE + "nestedBob: " + str(nestedBob))
    
    nestedBob.clear()
    nestedTurt.clear()


def NoSides(length, sides):
  #DefaultLength = 120
  
  angle = 360/sides
  for i in range(sides):
    turtle.forward(length)
    turtle.right(angle)

  

def main():
  a=input(Fore.LIGHTRED_EX+"Which Would You Like To Do?:"+"\n"+Fore.BLACK+"1.Control Turtle With Keys"+"\n"+"2.Random Turtles"+"\n"+"3.Draw Shapes"+"\n"+Fore.LIGHTRED_EX+"Enter The Corresponding Number"+"\n")

  if a == "1":
    TurtleKeys()
  elif a == "2":
    TurtleRandom(input("Enter A Colour For The Background (Preferebly A Hex Code): "))
  elif a == "3":
    l=int(input("Enter The Length Of The Shapes Sides: "))
    s=int(input("Enter The Number Of Sides You Want To Draw: "))
    NoSides(l,s)

if __name__=='__main__':
  main()