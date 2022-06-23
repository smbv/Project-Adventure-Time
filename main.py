# Filename: Project 2: Adventure Time.py
# NAMES: Sofía M. Barrera Vega, Nestor S. Frontera Rocher
# STUDENT ID: 802-21-5180
# SECTION: 91L

def Project2():
  #KEYS 
  CMD_MENU = 'm'
  CMD_SLAY = 'b'
  CMD_CLOSE = 'c'
  CMD_EAST = 'e'
  CMD_BRIBE = 'f'
  CMD_GET = 'g'
  CMD_LOCK = 'l'
  CMD_NORTH = 'n'
  CMD_OPEN = 'o'
  CMD_PUT = 'p'
  CMD_QUIT = 'q'
  CMD_SOUTH = 's'
  CMD_CROWD = 't'
  CMD_UNLOCK = 'u'
  CMD_WEST = 'w'
  CMD_SECRET = 'z'
  CMD_TALK = 'a'
  ROOM_FRONT_GATE = 0
  ROOM_MEETING_GROUNDS = 1
  ROOM_ARMORY = 2
  ROOM_TOWN_HALL = 3
  ROOM_DUNGEON = 4
  ROOM_SECRET = 5
  ROOM_NAMES = ("Front Gate", "Meeting Grounds", "Armory", "Town Hall", "Dungeon","Secret")
  flag_monster_alive = True
  flag_crowd_rambling = False #tv_on
  chest_unlocked = False
  KEY = False
  coins = False
  Tresure = False
  guard_bribed = False
  locker_unlocked = False
  locker_open = False
  Locker_treasure = False
  Vault_Unlocked = False
  Vault_Open = False
  sweetroll = False
  talked = False
  location = 0
  turns_taken = 0
  j = ''
  x = ''
  y = ''
  z = ''

  print("CIIC 3015 Autumn 2021 Project 2: Adventure Time")
  print()
  print("\033[1;31;01mDisclaimer: This project is not meant to insult anyone. It was made just for fun. Everything said is meant to be taken as a joke. Any similarities with real-life in the story are purely coincidental. \033[0;0m")
  print()
  print("|---------------------------------------------------|\n"
        "| START GAME                Press m for controls    |\n"            
        "|---------------------------------------------------|\n"
        "| What a beautiful day it is. You had just woken up |\n"  
        "| and decided to go on an adventure. Let's go!      |\n"        
        "|---------------------------------------------------|")
  print()
      
  while flag_monster_alive:
    print("----------------------------------------------------\n"
          "| Location: ", ROOM_NAMES[location])
    cmd = input("> ")
    turns_taken += 1
    if cmd == CMD_QUIT:
        print("----------------------------------------------------\n"
        "| Giving up already, huh? As expected of you. Pathetic.")
        print(turns_taken, "turns played.")
        return False
    if cmd == CMD_MENU: 
      print("----------------------------------------------------")
      print("|\033[1;31;01m Controls: \033[0;0m")
      print("|\033[1;36;01m  South: s, North: n, East: e, West: w, ???: z  \033[0;0m")
      print("|\033[1;35;01m  Crowd: t, Bribe: f, Get: g, Put: p, ???: a  \033[0;0m")
      print("|\033[1;32;01m  Open: o, Unlock: u, Lock: l, Close: c, Slay: b  \033[0;0m")
      print("|\033[5;31;01m  AND IF YOU ARE A WEAK Quit: q  \033[0;0m")
      continue
    if location == ROOM_FRONT_GATE:
        if cmd == CMD_EAST:
            print("| You have entered the Meeting Grounds.")
            location = ROOM_MEETING_GROUNDS
            print("| The village gathers.")
            print("| You notice a guard standing in front of the Dungeon Gate.\n" 
                    "As you are thinking of a way to enter, you completely space out while staring at the guard. The guard is now flustered and  desperately trying to avoid eye contact with you.")
            print("| Good job! Your social awkwardness made the guard uncomfortable.")
            if flag_crowd_rambling == True:
              print("| The crowd is talking.")
            elif flag_crowd_rambling == False:
              print("| The crowd is quiet.")
            continue
        elif cmd == CMD_NORTH:
            print("| What are you doing? Trying to escape your work? Me too, buddy. But you cannot waste your time, you still have a mission to do!")
            continue

        elif cmd == CMD_SOUTH:
            print("| What are you doing? Trying to escape your work? Me too, buddy. But you cannot waste your time, you still have a mission to do!")
            continue
        elif cmd == CMD_WEST:
            print("| What are you doing? Trying to escape your work? Me too, buddy. But you cannot waste your time, you still have a mission to do!")
            continue
    if location == ROOM_MEETING_GROUNDS:
        if cmd == CMD_CROWD:
            if flag_crowd_rambling:
                print("| The crowd is being silenced.")
            else:
                print("| The crowd started rambling.")
            flag_crowd_rambling = not flag_crowd_rambling
            continue
        if cmd == CMD_BRIBE:
            if flag_crowd_rambling == True:
              if coins == True:
                if guard_bribed == False:
                  print("| You offered the coins to the guard and tried to bribe him. Now look at what you did, you've hurt his feelings. He leaves his station all ashamed and culrs up in a corner sobbing.")
                  guard_bribed = True
                  continue
                elif guard_bribed == True:
                  print("| The guard is still crying in the corner. You already 'bribed' him. Do you want to make him feel even worse? You are a sick, sick fellow.")
                  continue
              elif coins == False:
                print("| I don't know if you're bold or just plain stupid. How is a basement dweller like you going to bribe the guard without coins?")
                continue
            
            elif flag_crowd_rambling == False:
                print("| It seems the crowd is quiet. The silence makes the guard a little shy.")
                continue

        if cmd == CMD_WEST:
            #outside
            print("| What are you doing going outside? Trying to escape your work? Me too, buddy. But you cannot waste your time, you still have a mission to do!") 
            continue

        if cmd == CMD_EAST:
            print("| You have entered the Town Hall.")
            print("| You see a dusty chest in the corner of the room.") 
            location = ROOM_TOWN_HALL
            continue

        if cmd == CMD_SOUTH:
            # armory
            print("| You have entered the Armory.") 
            print("| You see a strange locker with a key hole.")
            print("| Want use the key to unlock it?")
            location = ROOM_ARMORY
            continue

        if cmd == CMD_NORTH:
          #dugenon
            if guard_bribed == True:
                print("| You have entered the Dungeon.") 
                print("| A huge powerful creature ready to fight approaches you.")
                print("| After some time you notice a shiny treasure. You can't help but be attracted to it and pick it up.")
                location = ROOM_DUNGEON
                continue
            elif guard_bribed == False:
                print("| Guard: 'YOU SHALL NOT PASS!'") 
                print("| The guard is surprinsingly stubborn and does not let you pass. What to do?") 
                continue

    if location == ROOM_TOWN_HALL:
        if cmd == CMD_OPEN:
            print("| What's the combination for the chest?")
            print("| I can see you're struggling. Here, I'll be nice for once and give you a little hint. I'm getting tired of seeing you fail.")
            print("| Hint: collatz sequence after 42") 
            x += str(input("| What are the first two  digits? "))
            y += str(input("| What are the second two  digits? "))
            z += str(input("| What are the third two  digits? "))
            if x == "21" and y == "64" and z == "32":
                print("| Nice job! You did the bare minimum.") #tobechanged
                print("| You see a key glowing inside.")
                print("| Want to grab it?")
                chest_unlocked = True
                continue
            else:
                print("| WRONG. TRY AGAIN.") 
                print("| Look, man. Do you want me to give you the answer? It's just sad at this point. ")
                x = ''
                y = ''
                z = ''
                continue
        elif cmd == CMD_CLOSE:
            if chest_unlocked == False:
                print("| It is already closed.") 
                continue
            elif chest_unlocked == True:
                print("| You have closed the chest.") 
                chest_unlocked = False
                continue
        elif cmd == CMD_GET:
            
            if chest_unlocked == True:
              if KEY == False:
                KEY = True
                print("| Wow. That is a shiny key. Wonder what it could be used for.") #change?
                continue
              elif KEY == True:
                print("| You already have the key on you. I am starting to think you are more than stupid.")
                continue
            elif chest_unlocked == False:
                print("| It appears you forgot a vital step, unlocking the chest. Noob lmao.")
                continue
        elif cmd == CMD_PUT:
            if chest_unlocked == True:
                KEY = False
                print("| The key goes back to the safe.") 
                continue
            if chest_unlocked == False:
                print("| Did you just to try to noclip? I know you are a bit slow but you should know that you cannot put the key in the closed safe.") 
                continue
        elif cmd == CMD_LOCK:
            chest_unlocked = False
            continue

        if cmd == CMD_EAST:
            print("| I think it's time you leave the basement. It's starting to affect your common sense. You cannot exit through the wall.")#best one
            continue 

        elif cmd == CMD_NORTH:
            print("| Are you visually impared? This is a WALL, NOT an exit. In case you were not aware, it is not possible to exit through the wall.")
            continue

        elif cmd == CMD_SOUTH:
            print("| Do you ever go out? You DO know that it is impossible to exit through the wall? RIGHT?!")
            continue

        elif cmd == CMD_WEST:
            print(("| Congratulations! You have managed to complete the very basic task of exiting a door and have now entered the Meeting Grounds."))
            location = ROOM_MEETING_GROUNDS
            print("| You notice a guard standing in front of the Dungeon Gate. As you are thinking of a way to enter, you completely space out while staring at the guard. The guard is now flustered and desperately trying to avoid eye contact with you.")
            print("| Good job! Your social awkwardness made the guard uncomfortable.")
            if flag_crowd_rambling == True:
              print("| The crowd is talking.")
            elif flag_crowd_rambling == False:
              print("| The crowd is quiet.")
            continue
    if location == ROOM_ARMORY:
        if cmd == CMD_UNLOCK:
            if KEY == True:
                locker_unlocked = True
                print("| You have unlocked the locker!")
                continue
            elif KEY == False:
                print("| Why are you trying to open the locker without a key? Do I have to keep repeating myself? GET. THE. DAMN. KEY.")
                continue
        if cmd == CMD_OPEN:
            if locker_unlocked == True:
                locker_open = True
                print("| You have open the locker!")
                print("| You see a lot of gold coins.")
                print("| Want to put some in your bag?")
                continue
            elif locker_unlocked == False:
                print("| Surprise! The locker is indeed locked. How are you going to open it?")
                continue
        if cmd == CMD_CLOSE:
            if locker_open == False:
                print("| Did you just try to close the ALREADY CLOSED locker? Dissapointed but not surprised.") 
                continue
            elif locker_open == True:
              locker_open = False
              print("| Great job! You have completed another easy task that should not have taken you so much time to get done.")
              print("| The locker is now locked.")
              continue
        if cmd == CMD_GET:
            if locker_open == True:
              if coins == False:
                coins = True
                print("| Oh, look at that! It's gold coins. Your broke self can't help but to grab them.")
                continue
              elif coins == True:
                print("| It seems you have some coins in your pockets. There is no need to take more, greedy noob.")
                continue
            elif locker_open == False:
                print("| It appears you forgot a vital step, opening the locker. Get good.") 
                continue
        if cmd == CMD_PUT:
            if locker_open == True:
                if Tresure == True:
                    if Locker_treasure == False:
                        Tresure = False
                        Locker_treasure = True
                        continue
                    elif Locker_treasure == True:
                        print("| Forgot you already stored the treasure? Imagine being you. Cringe.")
                        continue
                elif Tresure == False:
                    print("| Were you dropped as a child? You have not collected the treasure.")
                    continue
            elif locker_open == False:
                print("| How are you going to store the treasure if the locker is closed? My expectations of you were low but damn.")
                continue

        if cmd == CMD_LOCK:
            if locker_open == True:
                print("| I'm already getting tired of insulting you. You forgot to close the locker first. ffs.") 
                continue
            elif locker_open == False:
                print("| FINALLY! I was starting to run out of insults. You have successfully locked the locker.")
                locker_unlocked = False 
                continue

        if cmd == CMD_EAST:
            print("| I think it is time you leave the basement. It's starting to affect your common sense. You cannot exit through the wall.")
            continue

        elif cmd == CMD_NORTH:
            location = ROOM_MEETING_GROUNDS
            print("| Congratulations! You have managed to complete the very basic task of exiting a door and have now entered the meeting grounds.") 
            print("| You notice a guard standing in front of the Dungeon Gate. As you are thinking of a way to enter, you completely space out while staring at the guard. The guard is now flustered and desperately trying to avoid eye contact with you.")
            print("| Good job! Your social awkwardness made the guard uncomfortable.")
            if flag_crowd_rambling == True:
              print("| The crowd is talking.")
            elif flag_crowd_rambling == False:
              print("| The crowd is quiet.")
            continue

        elif cmd == CMD_SOUTH:
            print("| Do you ever go out? You DO know that it is impossible to exit through the wall? RIGHT?!")
            continue

        elif cmd == CMD_WEST:
            print("| Are you visually impared? This is a WALL, NOT an exit. In case you were not aware, it is not possible to exit through the wall.")
            continue


    if location == ROOM_DUNGEON:
        if cmd == CMD_GET:
            if Tresure == True:
                print("| Are you trying to get more? Don't be greedy. You already got the treasure, bro.")
                continue
            elif Tresure == False:
                Tresure = True
                Locker_treasure = False
                print("| Hey, would you look at that, you actually made progress. I knew you could do it!")
                print("| You collected the treasure.")
                print("| You should probably store the treasure away in your locker.") 
                continue
        if cmd == CMD_SLAY:
            if flag_crowd_rambling == False:
                if locker_open == False:
                    if locker_unlocked == False:
                        if KEY == False:
                            if chest_unlocked == False:
                                if Tresure == False:
                                    if Locker_treasure == True:
                                        print("| Congratulations! You have slayed an innocent gentle creature for no reason!")
                                        print("| The sick, cruel humans of the village cheer for you.")
                                        print("| You hear a faint noise in the distance. As you get closer and closer to the sound you notice three adorable and now motherless baby dragons crying")
                                        flag_monster_alive = False

                                    elif Locker_treasure == False:
                                        print("| You should put that away.")
                                        continue
                                elif Tresure == True:
                                    print("| You should put that away.")
                                    continue
                            elif chest_unlocked == True:
                                print("| You should lock the chest.")
                                continue
                        elif KEY == True:
                            print("| You still have the key.")
                            continue
                    elif locker_unlocked == True:
                        print("| You should lock the locker.")
                        continue
                elif locker_open == True:
                    print("| Come on! You know should close the locker before that.") 
                    continue
            elif flag_crowd_rambling == True:
                print("| You must find a way to shut up all of these people so you can concentrate on the fight.")
                continue
        if cmd == CMD_EAST:
            print("| Are you visually impared? This is a WALL, NOT an exit. In case you were not aware, it is not possible to exit through the wall.")
            continue

        elif cmd == CMD_NORTH:
            print("| Do you ever go out? You DO know that it is impossible to exit through the wall? RIGHT?!")
            continue

        elif cmd == CMD_SOUTH:
            location = ROOM_MEETING_GROUNDS
            print("| Congratulations! You have managed to complete the very basic task of exiting a door and have now entered the meeting grounds.")
            print("| You notice a guard standing in front of the Dungeon Gate. As you are thinking of a way to enter, you completely space out while staring at the guard. The guard is now flustered and desperately trying to avoid eye contact with you.")
            print("| Good job! Your social awkwardness made the guard uncomfortable.")
            if flag_crowd_rambling == True:
              print("| The crowd is talking.")
            elif flag_crowd_rambling == False:
              print("| The crowd is quiet.")
            continue

        elif cmd == CMD_WEST:
            print("| I think it is time you leave the basement. It's starting to affect your common sense. You cannot exit through the wall.")
            continue

        elif cmd == CMD_SECRET:
          print("| Woah! You have discovered a secret hatch. You might not be so useless after all, huh.")#make it nicer? 
          #Like that? -Sof
          print("| You see a vault with an Atari controller plugged into it.")
          print("| This is your chance to prove you're not a complete idiot. Want to try your luck and solve it?")
          location = ROOM_SECRET
          continue

    if location == ROOM_SECRET:
        if cmd == CMD_UNLOCK:
          print("| You stare at the controller, dumbfounded.")
          print("| Let's see if you are smart enough to write the secret code.")
          print("| I will give you a small hint because you found our secret room.")
          print("| Hint: It's a famous code used in old video games.")
          j += str(input("| Type the entire code here. Remember to use spaces: "))
          j = j.lower()
          j = j.rstrip()
          j = j.lstrip()
          if j == "up up down down left right left right b a start":
            print("| Impressive! You have managed to unlock it. ")
            print("| *you hear a voice from the vault.*")
            print("| 'I used to be an adventurer like you, then I took an arrow in the knee...'")#10/10 line
            Vault_Unlocked = True
            continue
        
          else:
            print("| WRONGGGGGGGG")
            print("| How can you even call yourself a gamer if you don't know this? It is so simple. I can't believe you had me believing you were not stupid. How can you just fail? How just how?")
            j = ''
            continue
        if cmd == CMD_OPEN:
          if Vault_Unlocked == True:
            print("| EY! You did it. You opened the heavy vault door.")
            print("| As you are walking, you encounter a Whiterun guard standing on the corner playing some Doom on a computer.")
            print("| Want to talk to him?")
            Vault_Open = True
            continue
          elif Vault_Unlocked == False:
            print("| We went throught this already. THE VAULT IS LOCKED!")
            continue
        if cmd == CMD_TALK:
          if Vault_Open == True:
            print("| Whiterun guard:'HEY THERE!'")
            print("| Whiterun guard:'I see you have been working hard up there. Have this as your reward.'")
            print("| Will you accept his gift?")
            talked = True
            continue
          elif Vault_Open == False:
            print("| You can't walk through walls.")
            continue
        if cmd == CMD_GET:
          if Vault_Unlocked == True:
            if Vault_Open == True:
              if talked == True:
                print("| CONGRATS! YOU OBTAINED A WARM TASTY SWEETROLL FOR YOUR ADVENTURE <3")
                print("| You unlocked the secret achivement of the game, 'Sweetroll'")
                print("| You can show this off with your friends. Oh right, I forgot you don't have any.")
                print("| You can now go back to the main game.")
                sweetroll = True
                continue
              elif talked == False:
                print("| You should go talk with that nice looking, sexy guard with those strong arms I would let him take me to jail and... Oh, my. I got a little bit distracted there, uhm.")
                continue
            elif Vault_Open == False: 
              print("| At this point I am just begging you to please use your brain.")
              continue
          elif Vault_Unlocked == False:
            print("| Nice try, dumbass.")
            continue

        if cmd == CMD_SECRET:
          print("| You left the secret room.")
          location = ROOM_DUNGEON
          continue
        
    if flag_monster_alive == True:
        print("| Illegal command, genius.")
        print(turns_taken, "| turns played.")
        return False
    elif flag_monster_alive == False:
        print("| Congratulations, you have won the game! You gained absolutely nothing and wasted your time. Hope you had fun!")
        print(turns_taken, "turns played.", "On god it took u that long to finish the game?")
        return True
Project2()