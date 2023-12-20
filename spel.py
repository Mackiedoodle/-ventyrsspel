import random as rand
import time

class monstercreator:
    def __init__(self, hp, strength, color, name):
        self.hp = hp
        self.strength = strength
        self.color = color 
        self.name = name

class playercreator:
    def __init__(self, hp, strength):
        self.hp = hp 
        self.strength = strength 
    


class itemcreator:
    def __init__(self, itemname, itemstrength, ):
        self.itemstrength = itemstrength
        self.itemname = itemname

def randomitemcreator():
    list = ("Katana", "Battle Axe", "Baguette", "nunchucks", "Pocket knife") 
    return itemcreator(rand.choice(list), rand.randint(1,3))
        

    
    

def strid(player,):
    monster = monstercreator(rand.randint(40,130), rand.randint(7,25), rand.choice(["darkred", "brown", "albino"]), rand.choice(["serpent", "mutaded bat", "flesh eating hog"]))
    if player.strength >= monster.strength:
        print(f"let's go, You defeated the monster!!")
        backpack = []
        backpack.append(itemcreator(rand.choice(["Katana", "Battle Axe", "Baguette", "nunchucks", "Pocket knife", "Mystical Dagger", "Flameable Torch", "Double-Edged Sword"]), rand.randint(7,25)))
        loot = randomitemcreator()
        print(f"You found a {loot.itemname} with {loot.itemstrength} strength in the remainings of the monster!")
        player.strength += loot.itemstrength
    else:
        print("You lost the battle against the monster, get better gear to defeat him next time")
        time.sleep(2)
        print("You are not at max health anymore, check your stats to see your hp and be careful!")
        player.hp -= 15
    

    return



def trap(player):
    trapodds = rand.randint(1,5)
    if trapodds == 1 or trapodds == 2 or trapodds == 3:
        print("You fell in to the trap and lost 15hp... ")
        print("HEYY, you have to be more careful in the future!!  ")
        player.hp -= 15
        return player
    else:
        print("OMG YOU ARE SO LUCKY you managed to get away from the trap!!")




def main():
    global backpack 

    backpack = []
    backpack.append(itemcreator(rand.choice(["Mystical Dagger", "Flameable Torch", "Double-Edged Sword"]), rand.randint(7,25)))
    winning_strength = 100

    print("Hello traveler, you have been captured in this maze. To escape you will have to choose the right door at defeat the creature that captured you..")
    playername = input("What is your name?")
    player = playercreator(60, 17) 
    

  
    

    print(f"""Hello {playername} you have {player.strength} strength and {player.hp} hp.
            We have done some research in the maze and there is a lot of different creatures roaming different areas of the maze. 
            There is huge serpents, mutaded bats and flesh eating hogs.
            You will have to fight them or they will kill you.""") 
    time.sleep(6)

    print("""You will also discover crates which contains loot that you can use in battles. The maze is also full of traps so keep your eyes open.
         In order to escape the maze you must get to 100 strength points.""")

    
           

    time.sleep(7)


    while player.hp > 0 and player.strength < winning_strength:
        print("""What do you want to do?
            1 = Choose a door
            2 = Check the backpack
            3 = Check the stats """)
        
        val = input()

        if val == "1":
            doorchoser(player)
        
        elif val == "2":
            for x in range(len(backpack)):
                print(f"You have a {backpack[x].itemname} with {backpack[x].itemstrength} strength.")

                
            print("Press ENTER to go back")
            input()

        elif val == "3":
            print(f"Player Stats - HP: {player.hp}, Strength: {player.strength}")

        else:
            print("Please enter valid input")

    if player.strength >= winning_strength: 
        print("""You have gained enough strength to escape the maze.
                 You win!
                 GAME COMPLETE""")
        
    if player.hp <= 0: print("You lost all your health, GAME OVER")


def doorchoser(player):

    print("""Which door?
        1 = door one
        2 = door two
        3 = door three""")
    
    val = input()

    

    if val == "1" or val == "2" or val == "3":
        slumptal = rand.randint(1,3)
        if slumptal == 1:
            monster = monstercreator(rand.randint(40, 130), rand.randint(7, 25), rand.choice(["darkred", "brown", "albino"]),
                                     rand.choice(["serpents", "mutaded bat", "flesh eating hog"]))
            print(f"It's a {monster.color} {monster.name} with {monster.hp} hp and {monster.strength} strength!!")
            strid(player)
        
        elif slumptal == 2:
            print("OOoh look it's a crate!")
            loot = randomitemcreator()
            backpack.append(loot) 
            player.strength += loot.itemstrength
            print(f"""You found a {loot.itemname} with {loot.itemstrength} strength!!
                  That's just great now your strength is higher.""")
        elif slumptal == 3:
            print("Oh no whatchout it's a trap!")
            trap(player)
        else:
            print("Please enter a valid input")
            doorchoser()




main()





