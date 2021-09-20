import random

words = "marcel", "data"

def word_selection(list):
    random.choice(list)
    return list

def print_scaffold(guesses, wd): # prints the scaffold
      if (guesses == 0):
            print("_________")
            print("|    |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________")
      elif (guesses == 1):
            print("_________")
            print("|    |")
            print("|    O")
            print("|")
            print("|")
            print("|")
            print("|________")
      elif (guesses == 2):
            print("_________")
            print("|    |")
            print("|    O")
            print("|    |")
            print("|    |")
            print("|")
            print("|________")
      elif (guesses == 3):
            print("_________")
            print("|    |")
            print("|    O")
            print("|   \|")
            print("|    |")
            print("|")
            print("|________")
      elif (guesses == 4):
            print("_________")
            print("|    |")
            print("|    O")
            print("|   \|/")
            print("|    |")
            print("|")
            print("|________")
      elif (guesses == 5):
            print("_________")
            print("|    |")
            print("|    O")
            print("|   \|/")
            print("|    |")
            print("|   / ")
            print("|________")
      elif (guesses == 6):
            print("_________")
            print("|    |")
            print("|    O")
            print("|   \|/")
            print("|    |")
            print("|   / \ ")
            print("|________")
            print("\n")
            print("The word was %s." %wd)
            print("\n")
            print("\nYOU LOSE! TRY AGAIN!")
            print("\nWould you like to play again, type 1 for yes or 2 for no?")
            again = str(input("> "))
            again = again.lower()
            if again == "1":
              hangMan()
            return
def hangMan():
    guesses = 0
    word = word_selection(words)
    word_list = list(words)
    blanks = "_" * len(words)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []
    print("Let's play\n")
    print_scaffold(guesses, word)
    print("\n")
    print("" + ' '.join(blanks_list))
    print("\n")
    print("Guess a letter.\n")
    while guesses < 6:
        guess = str(input(": "))
        guess = guess.lower()
        if len(guess) > 1:
            print("Enter only one letter!")
        elif guess == "":
            print("Don't you want to play? Enter only one letter!")
        elif guess in guess_list:
            print("You already guessed that letter! Here is what you've guessed:")
            print(' '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(words):
                if guess == words[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1
            if new_blanks_list == blanks_list:
                print("Your letter isn't here.")
                guesses = guesses + 1
                print_scaffold(guesses, word)
                if guesses < 6:
                    print("Guess again.")
                    print(' '.join(blanks_list))
            elif word_list != blanks_list:
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))
                if word_list == blanks_list:
                    print("\nYou won!")
                    print("\n")
                    print("Would you like to play again?")
                    print("Type 1 for yes or 2 for no.")
                    again = str(input("> "))
                    if again == "1":
                        hangMan()
                    quit()
                else:
                    print("You have guessed! Guess another word!")

hangMan()

