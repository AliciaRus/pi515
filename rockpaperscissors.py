import random
options=["rock","paper","scissors"]
w=0
l=0
print("Welcome to Rock, Paper, Scissors!")
gameNum=input("How many games would you like to play? ")

def game(user,comp):     
    i=0
    global w
    global l
    comp=options[random.randrange(0,3)]
    while user not in options and i<3:
      print("invalid answer.")  
      user=input("Choose from the list: "+str(options)+" ").lower()
      i=i+1
      if user in options :
        i=4
    if user in options :
        print(playerName,"chooses",user)
        print("player2 chooses",comp)
        if comp==user :
          print("It's a draw!")
        elif comp=="rock" and user=="paper" :
          print(playerName,"wins!")
          w=w+1
        elif comp=="paper" and user=="scissors" :
          print(playerName,"wins!")
          w=w+1
        elif comp=="scissors" and user=="rock" :
          print(playerName,"wins!")
          w=w+1
        else :
          print(playerName,"loses.")
          l=l+1
        print("\n")
          
        
  
while True :
  if gameNum.isdigit() :
    if int(gameNum)>0 :
      break
    elif int(gameNum)==0 :
      print("play anyway")
      break
  else :
    gameNum=input("Not a valid number. How many games would you like to play? ")
playerNum=input("How many players, 0 or 1? ")
while True :
  if playerNum=="1" or playerNum=="0" :
    break
  else :
    gameNum=input("Not a valid number. How many games would you like to play? ")
print("\n")
if int(playerNum)==1 :
  playerName=input("Enter your username: ")
  for i in range(0,int(gameNum)) :
    player1=input("Choose from the list: "+str(options)+" ").lower()
    player2=options[random.randrange(0,3)]
    game(player1,player2)
elif int(playerNum)==0 :
  playerName="computer"
  for i in range(0,int(gameNum)) :
    player1=options[random.randrange(0,3)]
    player2=options[random.randrange(0,3)]
    game(player1,player2)
  
print(playerName+"'s wins:",w,"\n"+playerName+"'s losses:",l)
  