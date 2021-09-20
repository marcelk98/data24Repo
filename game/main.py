import random

# Taking Inputs
mammals = ["hyena", "field mouse"]
birds = ["pigeon", "eagle"]
reptiles = ["viper", "crocodile"]
amphibians = ["Bullfrog", "airy frog"]

m_questions = ["alike humans", "mixed size","under water", "on land"]

guess_number = 0

while guess_number<4:
    user = input("From which category would you like to guess from ? : ")
    if user == "mammals":
        print(random.choice(m_questions))

    # taking guessing number as input
    user_guess = str(input("Enter your animal:- "))

    # Condition testing
    if user_guess in mammals:
        print("Congratulations you did it")
        # Once guessed, loop will break
        break
    elif user_guess not in mammals:
        print("You guessed wrong!")
        guess_number += 1

    if guess_number == 4:
        print("You have ran out of tries")

