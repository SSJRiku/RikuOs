import random
import time


def boot():
  print("loading...")
  time.sleep(0.5)
  print("..........")
  time.sleep(0.5)
  print("..........")
  time.sleep(0.5)
  print("..........")
  time.sleep(0.5)

  print("Riku OS succesfuly loaded")

def animation():
 print ("-")
 time.sleep(0.4)
 print (" -")
 time.sleep(0.4)
 print ("  -")
 time.sleep(0.4)
 print ("   -")
 time.sleep(0.4)


def run():

 a = True
 animation()
 time.sleep(0.4)

 print("Welcome to Riku os")

 time.sleep(0.4)

 while a == True :
   print("choose what you want to do")
   time.sleep(0.2)
   x=int(input("1.Guess the number / 2.calculator / 3.Rock, paper, scissors  / 4.Close : "))
   time.sleep(0.4)

   if x == 1:
     rando_num_gen()
   elif x == 2 :
     calculator()
   elif x == 3 :
     rps_game()
   elif x == 4 :
     a = False
def calculator():
 print("welecome to the calculator")
 time.sleep(0.4)
 a=int(input("choose the first number: "))
 time.sleep(0.4)
 b=int(input("choose the second number: "))
 time.sleep(0.4)

 print("Choose the operator")
 c=int(input("1.addition 2.substraction 3.multiplication 4.divison: "))
 time.sleep(0.2)

 
 if c == 1:
   print(a + b)
 elif c == 2:
   print(a - b)
 elif c == 3:
   print(a * b)
 elif c == 4:
   print (a / b)

def rando_num_gen():
 a= random.randint(1,10)
 print("Welcome to the random number generator")

 tries = 3
 time.sleep(0.4)
 while tries>0 : 

   print("Guess the number from 1 to 10")
   b=int(input())
   time.sleep(0.4)

   if (a == b):
     print("you guessed correctly")
     tries = 0
   elif(a > b):
     print("your number is too small")
     tries -= 1
     print("you have " + str(tries) + " tries left")

   elif(a < b) :
     print("your number is to big")
     tries -= 1
     print("you have " + str(tries) + " tries left")
 
 print("the number was " + str(a))

def rps_game():
    
    def get_input(posibilities):
        #gets the input
        human_choice = input("Enter rock,paper or scissors: ")
        #checks if the input isn't valid
        while human_choice.lower().strip() not in posibilities:
            human_choice = input("Enter rock,paper or scissors: ")
        return human_choice

    def check_winner(human_choice, computer_choice):
        statement = ""
        if human_choice == "rock" and computer_choice == "scissors":
            statement = "win"
        elif human_choice == "paper" and computer_choice == "rock":
            statement = "win"
        elif human_choice == "scissors" and computer_choice == "paper":
            statement = "win"
        elif human_choice == computer_choice:
            statement = "tie"
        else:
            statement = "lose"
        return statement

    def print_statement(statement):
        if statement == "win":
          print("You won")
        elif statement == "tie":
          print("it was a tie")
        else:
          print("Ha you lost, noob")

    def get_computer_choice(posibilities):
        computer_choice = random.choice(posibilities)
        print(f"The computer chose {computer_choice}")
        return computer_choice
        
    def rock_paper_scissors_game():
        print("welcome to Rock, paper. scissors")
        time.sleep(0.5)
        posibilities = ["rock", "paper", "scissors"]
        human_choice = get_input(posibilities)
        computer_choice = get_computer_choice(posibilities)
        statement = check_winner(human_choice, computer_choice)
        print_statement(statement)

    rock_paper_scissors_game()

boot()
run()
