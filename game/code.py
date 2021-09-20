def event3(self):
    print(player, ",you are now in NO MAN'S LAND which have not been conquered before")
    print('\n' * 2)  # prints 80 line breaks
    print("As you enter the un-conquered land, you are equipped with" + " " + main_last_level.gear +
          "and" + " " + main_last_level.magic)
    print("As", player,
          "approaches the unholy temple to confront his final enemy, he is attacked by THE CARETAKER, he is a relict monster, servent of the gods"
    dodge = (player, "is critically damaged, PRESS T TO TAKE COVER IN THE TEMPLE: ")
    if dodge == "t":
        heal = input("PRESS G TO QUICKLY HEAL BEFORE THE CARETAKER FINDS OUT YOUR POSITION: ")
    if heal == "g":
        bomb = input("THE CARETAKER FOUND YOU!! PRESS B TO USE SMOKE BOMB IN YOUR ADVANTAGE: ")
    if bomb == "B":
        attack = input("THE CARETAKER IS DISORIENTED, QUICKLY PRESS H FOR A POWERFUL MAGIC ATTACK: ")
    if attack == "h":
        print('\n' * 2)
    print("***POWER INTENSIFIES***")
    print('\n' * 2)
    attack2 = input("THE CARETAKER IS ON BRINK OF DEATH, PRESS R TO DODGE HIS WRATH ATTACK AND DEAL FINAL BLOW")
    if attack2 == "r":
        print("***SUDDEN DODGE / / / /  ----------------> STRIKE***")
    print(player, "!!, HE IS MORE POWERFUL THAN EXPECTED, THE TEMPLE WILL BE SACRIFICED TO DEFEAT THE CARETAKER")
    final_strike = input("PRESS V TO EXPLODE TEMPLE PILLARS WHICH WILL CRUSH THE ENEMY ENSURING OUR VICTORY!!: ")
    if final_strike == "v":
        print("***MASSIVE EXPLOSION SOUNDS***")
    print('\n' * 3)
    print("IMPOSSIBLE HAVE HAPPENED", player, "HAVE CONQUERED NO MAN'S LAND")