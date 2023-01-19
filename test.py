boolean=True
while boolean:
  try:
    gameNum=input("How many games would you like to play? ")
    gameNum=int(gameNum)
    if gameNum>0:
      boolean=False
  except ValueError:
    print("Not a valid number.")