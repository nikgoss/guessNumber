from logo import art
import random


easyLevel =10
hardLevel = 5

def checkAnswer(com, user, turns):
  if (com==user):
    print (f"You guessed it right. You won. The computer also picked {com}")
    return turns-1
  elif (com<user):
    print ("Too low")
    return turns-1
  else:
    print("Too High")
    return turns-1

def difficulty():
  print("Guess a number between 1 and 100. Good Luck.\n Easy = 10 chances \n Hard = 5 chances\n")
  level=input("Choose your level. Type 'easy' or 'hard': ").lower()

  if level=='easy':
    return easyLevel
  else:
    return hardLevel

def game():
  print(art)
  print("Code written by Tashi Tsering Sherpa")
  computerPick = random.randint(1,100)
  print("Computer Picked:",computerPick)

  turns = difficulty()
  guess = 0

  while guess != computerPick:
    print(f"You have {turns} remaining")

    guess = int(input("Make a guess: "))

    turns = checkAnswer(guess,computerPick,turns)
    if turns<1:
      print("you lost")
      return
    elif guess != computerPick:
      print("Guess Again.")
game()
