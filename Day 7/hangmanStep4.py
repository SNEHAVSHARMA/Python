import random
word_list=["apple","girl","beach","country"]
chosen_word=random.choice(word_list)      
print(chosen_word)
word_length=len(chosen_word)

place_holder=""                     #an empty string
for position in range(word_length):             #prints no. of _ in the word
    place_holder += "_ "
print(place_holder)

lives=6
game_over=False
correct_letter=[]
while not game_over:
    guess_letter=input("Guess a letter:").lower()        #makes lower case
    print(guess_letter)
    display=""
    
    for letter in chosen_word:                  #prints the guessed letter in its position
        if letter==guess_letter:
            display += letter
            correct_letter.append(guess_letter)
        elif letter in correct_letter:
            display += letter
        else:
             display += " _ "
            
    print(display)

    if guess_letter not in chosen_word:
            lives -= 1
            print("Wrong guess! Lives left:",lives)
            if lives==0:
                game_over=True
                print("You Lose")
                
    if "_" not in display:
        print("You Win")
        game_over=True

    



