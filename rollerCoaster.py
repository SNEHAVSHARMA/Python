price=0
height=int(input("enter your height: "))
if height>=120:
    print("you can ride!")
    age=int(input("enter age: "))
    if age<13:
        price=300
        print(f"price: {price}")
    elif age<18:
        price=500
        print(f"price: {price}")
    else:
        price=1000
        print(f"price: {price}")
    photo = (input("do you want photo? "))
    if  photo=="yes":
        price += 300
        print(f"total price:{price}")
    
else:
    print("oops you cannot ride")