import random
import replit
import time
options=["rock","paper","scissors"]
w,l,w2,l2,d=0,0,0,0,0
boolean=True
print("Welcome to Rock, Paper, Scissors!")
def game(user,comp):     
    global w,l,w2,l2,d
    while user not in options:
      print("invalid answer.")  
      user=input("Choose rock, paper, or scissors: ").lower()
    if user in options :
        print(f"{playerName} chooses {user}")
        print(f"{playerName2} chooses {comp}")
        if comp==user :
          print("It's a draw!")
          d=d+1
        elif comp=="rock" and user=="paper" :
          print(f"{playerName} wins!")
          w=w+1
          l2=l2+1
        elif comp=="paper" and user=="scissors" :
          print(f"{playerName} wins!")
          w=w+1
          l2=l2+1
        elif comp=="scissors" and user=="rock" :
          print(f"{playerName} wins!")
          w=w+1
          l2=l2+1
        else :
          print(f"{playerName2} wins!")
          l=l+1
          w2=w2+1
        print("\n")
while boolean:
  try:
    gameNum=input("How many games would you like to play? ")
    gameNum=int(gameNum)
    if gameNum>0:
      boolean=False
  except ValueError:
    print("Not a valid number.")

  
# while True :
#   if gameNum.isdigit() :
#     if int(gameNum)>0 :
#       break
#   else :
#     gameNum=input("Not a valid number. How many games would you like to play? ")
playerNum=input("How many players, 0, 1, or 2? ")
while True :
  if playerNum=="1" or playerNum=="0" or playerNum=="2":
    break
  else :
    playerNum=input("Not a valid number. How many players?")
print("\n")
if int(playerNum)==1 :
  playerName=input("Enter your username: ")
  playerName2="computer"
  for i in range(0,int(gameNum)) :
    player1=input("Choose rock, paper, or scissors: ").lower()
    player2=options[random.randrange(0,3)]
    game(player1,player2)

elif int(playerNum)==0 :
  playerName="computer"
  playerName2="computer2"
  for i in range(0,int(gameNum)) :
    player1=options[random.randrange(0,3)]
    player2=options[random.randrange(0,3)]
    game(player1,player2)
elif int(playerNum)==2 :
  playerName=input("Player 1, Enter your username: ")
  playerName2=input("Player 2, Enter your username: ")
  for i in range(0,int(gameNum)) :
    print(f"Let {playerName} answer first.")
    player1=input(f"{playerName}, choose rock, paper, or scissors: ").lower()
    # time.sleep(3)
    replit.clear()
    print(f"Now let {playerName2} answer.")
    player2=input(f"{playerName2}, choose rock, paper, or scissors: ").lower()
    # time.sleep(3)
    replit.clear()
    game(player1,player2)
  
print(f"{playerName}'s wins: {w}\n{playerName}'s losses: {l}")
print(f"{playerName2}'s wins: {w2}\n{playerName2}'s losses: {l2}")
print("draws:",d)
if w>w2 :
  print(playerName,"wins!")
elif w<w2 :
  print(playerName2,"wins!")
else :
  print("It's a tie!")
