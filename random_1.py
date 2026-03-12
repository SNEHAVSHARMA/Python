import random

# a=random.randint(1,10)  #gives any random integer btw 1 and 10 (including both)
# print(a)

# b=random.random()   #float btw 0 to 1
# print(b)
# c=random.random()*20  #float btw 0 to 20
# print(c)
# d=random.uniform(10,20)  #float btw 10 and 20
# print(d)


#printing heads/tails
flip=random.randint(0,1)
if flip==0:
    print("heads")
else:
    print("tails")