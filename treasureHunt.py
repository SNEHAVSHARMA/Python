print("Welcome to treasure hunt!")
ways=input("You have 2 doors, which one do you choose? Left/Right")
if ways=="left":
    lake=input("There is a lake, Do you like to swim or wait?")
    if lake=="wait":
        door=input("There are 3 doors of colour red,yellow and green. which one do you choose?")
        if door=="yellow":
            print("Congratulations! You win!!")
        else:
            print("you are bitten by the snake....You lost")
    else:
        print("You are eaten by the crocodile....You lost")
else:
    print("You are burnt in the fire....You lost")
