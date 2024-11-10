import random  #imporing the random module to choose random word from the list

list_of_words = ["hello", "world","i", "am", "Nazeema"]  #Predefined list 


def hangman():      #Defining the function with the name hangman 

    word = random.choice(list_of_words)     #Choosing random word from the list 

    guessed_word = ["_"] * len(word)  #Creating a list of underscores to represent unguesses letters in word

    guessed_letters = set()       #Kepping the track of guessed letters

    attempts = 6    #Setting the numbers of attempts a player has to guess the word 

    print("Welcome to Hangman!")
    print("Try to guess the word!")



    while attempts > 0:
        print("Word:", " ".join(guessed_word))

        print("Attempts left:", attempts)

        print("Guessed letters:", " ".join(sorted(guessed_letters)))


        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try another one.")

            continue

        guessed_letters.add(guess) 

        if guess in word:
            print("Good guess!")

            for index,letter in enumerate(word):
                
                if letter == guess:
                    guessed_word[index] = guess 
        else:
            attempts = attempts - 1 
            print("Wrong guess")       

        if "_"  not in guessed_word:
            print("congratulations! You guessed the word:", word)
            break   

    if attempts == 0:
        print("You've run out of attempts!The word was:", word)



hangman()           #Calling the function      
              

