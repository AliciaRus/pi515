# numList=[0,0,0,0,0,0]
# min=10000
# max=-10000
# for x in numList :
#   if (min<x):
#       print(x)
#   elif(min>x):
#     print(x, "This is the smallest so far")
#     min=x
#   if (max<x):
#     max=x
    
# print(min, " is the minimum, ", max, " is the maximum")

# flavors = ["chocolate", "vanilla", "cookies and cream", "strawberry", "mint chocolate chip"]

# flavors2 = ["chocolate", "vanilla", "cookie dough", "strawberry", "cookies and cream"]

# print("chocolate" in flavors2)
# print("vanilla" in flavors2)
# print("cookies and cream" in flavors2)
# print("strawberry" in flavors2)
# print("mint chocolate chip" in flavors2)

# flavors.append(flavors2[2])
# print(flavors)

# flavors = flavors + flavors2
# flavors.remove("mint chocolate chip")
# print(flavors)


# subjects=["english","math","history","art","psychology"]
# for subject in subjects :
#   length=(len(subjects))
#   if subject=="history" :
#     print (subject+"(U.S. history)")
#   else :
#     print(subject) 
# print(length)

# wordList=["hippopotamus","elephant"]

# for x in wordList :
#   for letter in x :
#     print(letter)
# holidayList=["Valentine's Day","Halloween","Christmas","Thanksgiving","New Years Day","St. Patricks Day","Easter"]

# def func(holiday):
#   print("My favorite holiday is " + holiday)

# for x in holidayList :
#   func(x)

gift_counters=[0,0]
for gitf in range (1,13):
  for x in range(gift):
    gift[x] += x+1

print(gift_counters)
total=0

for counter in gift_counters:
  total = total + counter

print("total number of gifts:",total)