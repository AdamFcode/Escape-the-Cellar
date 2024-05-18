import time

# Function to open, read and close the story txt files
def read_story(filepath):
    f = open(filepath, "r")
    #Iterates through the lines in txt file with delay
    for char in f: 
        print(char, end='')
        time.sleep(.75)
    f.close()

# Function to start the game
def adv_start():
    read_story("assets/text-files/intro-play.txt")
    story_choice = int(input("Please select 1 or 2:\n"))
    if story_choice == 1:
        path_select()
    elif story_choice == 2:
        print("That's really too bad. Enjoy an eternity of darkness...\n")
    else:
        print("I am afraid that we cannot allow that selection. Please choose again.\n")
        time.sleep(3)
        return adv_start()

# User selects their choice of path
def path_select():
    read_story("assets/text-files/path-select.txt")
    story_choice = int(input("Please select 1 or 2:\n"))
    if story_choice == 1:
        meet_gargoyles()
    elif story_choice == 2:
        meet_troll()
    else:
        print("I am afraid that we cannot allow that selection. Please choose again.\n")
        time.sleep(3)
        return path_select()

# User meets a Troll
def meet_troll():
    read_story("assets/text-files/meet-troll.txt")
    story_choice = int(input("Please select 1, 2 or 3:\n"))
    if story_choice == 1:
        read_story("assets/text-files/defeat-troll.txt")
        time.sleep(3)
        riddle_path_one()
    elif story_choice == 2:
        read_story("assets/text-files/stun-troll.txt")
        time.sleep(3)
        troll_stunned = int(input("Please select 1 or 2\n"))
        if troll_stunned == 1 or 2:
            read_story("assets/text-files/killed-by-troll.txt")
            time.sleep(3)
            read_story("assets/text-files/lose.txt")
            play_again = int(input("Please select 1 or 2:\n"))
            if play_again == 1:
                adv_start()
            elif play_again == 2:
                exit()
            else:
                print("We shall take your inability to take instructions as a no...\n")
                time.sleep(3)
                exit()
    elif story_choice == 3:
        read_story("assets/text-files/killed-by-troll.txt")
        time.sleep(3)
        read_story("assets/text-files/lose.txt")
        play_again = int(input("Please select 1 or 2:\n"))
        if play_again == 1:
            adv_start()
        elif play_again == 2:
            print("Coward...\n")
            time.sleep(3)
            exit()
        else:
            print("We shall take your inability to take instructions as a no...\n")
            time.sleep(3)
            exit()
    else:
        print("I am afraid that we cannot allow that selection. Please choose again.\n")
        time.sleep(3)
        meet_troll()

adv_start()

