import random as rand
 
#  backpack är inte klar än
backpack = ["svärd","brygd","fackla"]

   # inte klar med monster
def monster()
    monsterhp = rand.randint(40,130)
    monsterstrength = rand.randint(7,25)
    monstercolor = rand.choice("darkred", "brown", "albino")
#  strid är inte färdigt än
def strid(playerhp, monsterhp):
    if playerhp >= monsterhp:
        print("du vann")
    else:
        print("du förlorade")
# ej klar behind_door
def behind_door(playerhp, monsterhp, playerstrength, monsterstrength, backpack):
    händelser = list[monster, crate, trap]

def main():

    print("Hello traveler, you have been captured. To escape this maze you will have to choose the right door.")
    playername = input("What is your name?")
    playerhp = 100
    playerstrength = 10 
    
    i = 0

    while i < len(backpack):
        print(backpack[i])
        i += 1

  


    print(f"""Hello {playername} you have {playerstrength} strength and {playerhp} hp.
            We have done some research in the maze and there is a lot of different creatures roaming different areas of the maze. 
            There is huge serpents, mutaded bats, flesh eating hogs.
            You will have to fight them or they will kill you. 
            You will also discover crates which contains loot that you can use in battles. The maze is also full of traps so keep your eyes open.""")


    while playerhp >= 0:
        print("""What do you want to do?
            1 = choose a door
            2 = Check the backpack
            3 = Check the stats """)
        
        val = input()

        if val == "1":
            doorchoser()



def doorchoser():

    print("""Which door?
        1 = door one
        2 = door two
        3 = door three""")
    
    val = input()

    

    if val == "1" or val == "2" or val == "3":
        slumptal = rand.randint(1,3)
        if slumptal == 1:
            print("It's a MONSTER!!! you have to fight it.")
            strid(playerhp, monsterhp)
        elif slumptal == 2:
            print("OOoh look it's a crate!")
        else:
            print("Oh no whatout it's a trap")    
   


main()
    # hjältestr=10
    # Fiendestr=7
    # Hjälteliv=100

    # strid(Hjältestr, Fiendestr, Hjälteliv)
    # Hjälteliv = strid(hs, fs, hl)
    # if hs>=fs:
    # Print("Du vann")
    # return
    # else:
    # print("du förlorade 1 hp")
    # hl-=1
    # return hl
    # )

    # def strid(playerhp, playerstrength, enemystrength):
    # print(f"You have {playerstrength} strength.")


