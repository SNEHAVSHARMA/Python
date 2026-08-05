import random
print("Welcome to play rock,paper and scissor")
user_choice=int(input("Choose 0 for rock, 1 for paper, 2 for scissor: "))
comp_choice=random.randint(0,2)
print(f"Computer chose: {comp_choice}")

if comp_choice==2 and user_choice==1:
    print("You lost!")
elif comp_choice==1 and user_choice==0:
    print("You lost!")
elif comp_choice==0 and user_choice==2:
    print("You lost!")
elif user_choice==2 and comp_choice==1:
    print("You win!")
elif user_choice==1 and comp_choice==0:
    print("You win!")
elif user_choice==0 and comp_choice==2:
    print("You win!")
elif user_choice==comp_choice:
    print("draw")
else:
    print("Invalid number")


