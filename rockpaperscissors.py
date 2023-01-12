import random
options=["rock","paper","scissors"]
gameStart=False
gameNum=input("How many games would you like to play? ")
w=0
l=0

def game(user,comp,w,l):     
    i=0
    comp=options[random.randrange(0,3)]
    while user not in options and i<3:
      print("invalid answer.")  
      user=input("Choose from the list: "+str(options)+" ").lower()
      i=i+1
      if user in options :
        i=4
    if user in options :
        print("Computer chooses",comp)
      
        if comp==user :
          print("It's a draw!")
        elif comp=="rock" and user=="paper" :
          print("you win!")
          w=w+1
        elif comp=="paper" and user=="scissors" :
          print("you win!")
          w=w+1
        elif comp=="scissors" and user=="rock" :
          print("you win!")
          w=w+1
        else :
          print("you lose")
          l=l+1
          
        
  
while gameStart==False :
  if gameNum.isdigit() :
    if int(gameNum)>0 :
      break
    elif int(gameNum)==0 :
      print("ok bye")
      break
  else :
    gameNum=input("Not a valid number. How many games would you like to play? ")
playerNum=input("How many players from 0 to 1? ")
if int(playerNum)==1 :
  for i in range(0,int(gameNum)) :
    player1=input("Choose from the list: "+str(options)+" ")
    player2=options[random.randrange(0,3)]
    game(player1,player2,w,l)
elif int(playerNum)==2 :
  for i in range(0,int(gameNum)) :
    player1=input("Choose from the list: "+str(options)+" ")
    player2=options[random.randrange(0,3)]
    game(player1,player2,w,l)
  
print("Wins:",w,"\nLosses:",l)
  