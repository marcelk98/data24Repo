import random

class Main_character():
    def __init__(self,gear, magic):
        self.gear = gear
        self.magic = magic
        self.health = 150
        self.alive = True

    def damage(self):
        hit = random.randrange(10,50)
        while self.health > 149:
            print("The creature have hit" + " " + player + "with an axe" + " " + "for" + str(hit))
            self.health -= hit
        if self.health < 1:
            self.alive == False
            print("You have died "
                  "RIP" + " " + player)
            exit()

class Enemy(Main_character):
    def __init__(self, name, weapon):
        self.weapon = weapon
        self.health2 = 100
        self.alive = True
        self.name = name

    def attack(self):
        hit = random.randrange(10,50)
        magic_hit = random.randrange(20,60)
        gear = ["flame sword", "bow", "magic spear"]
        magic = ["charge", "teleport", "fury"]

        attack_sel = int(input("select 1 for normal attack or 2 for magic attack"))
        if attack_sel == 1:
            print(player + "have attacked" + self.name + "with"+" "+random.choice(gear) + str(hit))
            self.health2 -= hit

        elif attack_sel == 2:
            print(player + "have attacked" + self.name + "with"+" "+random.choice(magic) + str(magic_hit))
            self.health2 -= hit*2

        if self.health2 < 1:
            print("You have killed it")
            cont = input("Wanna to take over this world or move on?")
            if cont == "yes":
                self.health2 = 100
                print ("You will now face the creature ruling this land to take it over!!")
                while foe.alive == True:
                    foe.attack()

            elif cont == "no":
                self.health2 = 100
                print("You will now fast travel to a new world!!")
                self.alive == True
                while foe.alive == True:
                    foe.attack()
class map:
    def __repr__(self):
        return """
         
         CONQUER THE UNCHARTED LANDS
        
YOU SPAWN HERE
  .·´  Magic forest
 (¸¸.·´  .·´  
       .·´Old town 
      (¸¸.·´  .·´ 
            .·´ Swamp 
           (¸¸.·´  .·´  
                 .·´Abandoned fields 
                (¸¸.·´  .·´  
                      .·´Haunted graveyard 
                    (¸¸.·´  .·´  
                          YOUR JOURNEY ENDS HERE (if you survive)"""
print(map())
player = str(input("\nEnter your hero's name: "))

# location = int(input("""Select your journey path!
#                                1 - Magic forest
#                                2 - Old town
#                                3 - Swamp
#                                4 - Abandoned fields"""))
# if location == 1:
#     print("you are currently travelling the Magic forrest")
# elif location == 2:
#     print("you are currently travelling an Old town")
# elif location == 3:
#     print("You are currently travelling the Swamp")
# elif location == 4:
#     print("Your are currently travelling throughout the Abandoned fields")

gear = ["flame sword", "bow", "magic spear"]
magic = ["charge", "teleport", "fury"]
foe_names = ["Troll", "Witch", "Wearwolf", "Vampire"]
foe_weapons = ["Great axe", "Rusty pipe", "Magic bomb","Wild attack"]
foe = Enemy(random.choice(foe_names), random.choice(foe_weapons))
main = Main_character(random.choice(gear), random.choice(magic))


print("You are equipped with" +" " + main.gear+ " "+ main.magic)
print("\n First location to conquer is the Magic forest")
print(player +" "+ "have encountered" + " " + foe.name + " "+"wielding" +" "+ foe.weapon)



while foe.alive == True:
    kill = input("\n press Enter to start an attack!")
    if kill == "":
        foe.attack()
        main.damage()
















