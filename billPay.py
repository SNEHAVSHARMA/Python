import random
friends=["Bob","Alice","Ram","Steve","Ruby"]
print("Bill should be paid by: ")
# pay=random.randint(0,4)
# if pay==0:                    #option 1
#     print("Bob")
# elif pay==1:
#     print("Alice")
# elif pay==2:
#     print("Ram")
# elif pay==3:
#     print("Steve")
# else:
#     print("Ruby")

#print(random.choice(friends))   #option 2

pay=random.randint(0,4)
print(friends[pay])       #option3
