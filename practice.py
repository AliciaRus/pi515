numList=[0,0,0,0,0,0]
min=10000
max=-10000
for x in numList :
  if (min<x):
      print(x)
  elif(min>x):
    print(x, "This is the smallest so far")
    min=x
  if (max<x):
    max=x
    
print(min, " is the minimum, ", max, " is the maximum")
