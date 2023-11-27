import random as rand
 
  i = 0
    while i < len(backpack)
        print(backpack[i])
        i += 1

def main():

    print("Hello traveler, you have been captured. To escape this maze you will have to choose the right door.")
    playername = input("What is your name?")
    playerhp = 100
    playerstrength = 10 

    backpack = ["svärd","brygd","fackla"]

  


    print(f"""Hello {playername} you have {playerstrength} strength and {playerhp} hp.
            We have done some research in the maze and there is a lot of different creatures roaming different areas of the maze. 
            You will fight against Skeletons, mutaded bats, flesh eating hog.
            You will have to fight them or they will kill you. 
            There is also crates and trapes all around the maze.""")


    while playerhp >= 0:
        print("""What do you want to do?
            1 = choose a door
            2 = Check the backpack
            3 = Check the stats """)
        
        val = input()

        if val == "1":
            print("""Which door?
                  1 = door one
                  2 = door twop
                  3 = door three""")
            val = input()

            if val == "1":
                
            elif val == "2":
                print("Hejdå")
            
            else:
                print("Godmorgon")
        
        elif val == "2":
            print(backpack)
        
        elif val == "3":
            print("Stats")¨
        else:


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


