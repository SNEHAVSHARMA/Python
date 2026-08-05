import random
word_list=["apple","girl","beach","country"]
chosen_word=random.choice(word_list)                 #chooses a random word from the list
print(chosen_word)
guess_letter=input("Guess a letter:").lower()        #makes lower case
print(guess_letter)

for letter in chosen_word:                           
    if(letter==guess_letter):
        print("Right")
    else:
        print("Wrong")
