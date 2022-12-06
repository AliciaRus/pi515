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

flavors = ["chocolate", "vanilla", "cookies and cream", "strawberry", "mint chocolate chip"]

flavors2 = ["chocolate", "vanilla", "cookie dough", "strawberry", "cookies and cream"]

print("chocolate" in flavors2)
print("vanilla" in flavors2)
print("cookies and cream" in flavors2)
print("strawberry" in flavors2)
print("mint chocolate chip" in flavors2)

flavors.append(flavors2[2])
print(flavors)

flavors = flavors + flavors2
flavors.remove("mint chocolate chip")
print(flavors)