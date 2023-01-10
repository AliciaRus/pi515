import random
options=["rock","paper","scissors"]
comp=options[random.randrange(0,3)]
user=input("Choose from the list: "+str(options)+" ")
i=0
while user not in options and i<3:
  print("invalid answer.")  
  user=input("Choose from the list: "+str(options)+" ").lower()
  i=i+1
  if user in options :
    print(comp)


#   if comp==input :
#     print("draw!")
#   elif comp=="rock" & input=="paper" :
#     print("you win!")
#   elif comp=="paper" & input=="scissors" :
#     print("you win!")
#   elif comp=="scissors" & input=="rock" :
#     print("you win!")
#   else :
#     print("you lose")