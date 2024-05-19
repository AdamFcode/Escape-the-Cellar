# Time imported for time.sleep function
import time
# Colorama imported for coloured text
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Function to open, read and close the story txt files
def read_story(filepath):
    f = open(filepath, "r")
    # Iterates through the lines in txt file with delay
    for char in f: 
        print(Fore.MAGENTA + Style.BRIGHT + char, end='')
        time.sleep(.75)
    # Closes the file after reading it
    f.close()

# Function to start the game
def adv_start():
    read_story("assets/text-files/intro-play.txt")
    story_choice = int(input("Please select 1 or 2:\n"))
    if story_choice == 1:
        path_select()
    elif story_choice == 2:
        print(Fore.MAGENTA + Style.BRIGHT + "That's really too bad. Enjoy an eternity of darkness...\n")
    else:
        print(Fore.MAGENTA + Style.BRIGHT + "I am afraid that we cannot allow that selection. Please choose again.\n")
        time.sleep(2)
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
        print(Fore.MAGENTA + Style.BRIGHT + "I am afraid that we cannot allow that selection. Please choose again.\n")
        time.sleep(2)
        return path_select()

# User meets a Troll
def meet_troll():
    read_story("assets/text-files/meet-troll.txt")
    story_choice = int(input("Please select 1, 2 or 3:\n"))
    if story_choice == 1:
        read_story("assets/text-files/defeat-troll.txt")
        time.sleep(2)
        riddle_path_one()
    elif story_choice == 2:
        read_story("assets/text-files/stun-troll.txt")
        time.sleep(2)
        troll_stunned = int(input("Please select 1 or 2\n"))
        if troll_stunned == 1 or 2:
            read_story("assets/text-files/killed-by-troll.txt")
            time.sleep(2)
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
    elif story_choice == 3:
        read_story("assets/text-files/killed-by-troll.txt")
        time.sleep(2)
        read_story("assets/text-files/lose.txt")
        time.sleep(2)
        replay()
    else:
        print(Fore.MAGENTA + Style.BRIGHT + "\nI am afraid that we cannot allow that selection. Please choose again.\n")
        time.sleep(2)
        meet_troll()

#User meets the Riddler on path 1
def riddle_path_one():
    read_story("assets/text-files/riddle-path-one.txt")
    story_choice = int(input("Please select 1 or 2:\n"))
    if story_choice == 1:
        read_story("assets/text-files/riddle-right.txt")
        time.sleep(2)
        meet_cerberus()
    elif story_choice == 2:
        read_story("assets/text-files/riddle-wrong.txt")
        time.sleep(2)
        riddle_wrong = int(input("Please select 1 or 2:\n"))
        if riddle_wrong == 1 or 2:
            read_story("assets/text-files/killed-by-riddle.txt")
            time.sleep(2) 
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
    else:
        print(Fore.MAGENTA + Style.BRIGHT + "\nI am afraid that we cannot allow that selection. Please choose again.\n")
        time.sleep(2)
        riddle_path_one()

# The user meets a three-headed dog from hell
def meet_cerberus():
    read_story("assets/text-files/meet-cerberus.txt")
    story_choice = int(input("Please select 1, 2 or 3:\n"))
    if story_choice == 1:
        read_story("assets/text-files/stun-cerberus.txt")
        time.sleep(2)
        cerberus_stunned = int(input("Please select 1 or 2\n"))
        if cerberus_stunned == 1 or 2:
            read_story("assets/text-files/killed-by-cerberus.txt")
            time.sleep(2)
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
    elif story_choice == 2:
        read_story("assets/text-files/killed-by-cerberus.txt")
        time.sleep(2)
        read_story("assets/text-files/lose.txt")
        time.sleep(2)
        replay()
    elif story_choice == 3:
        read_story("assets/text-files/defeat-cerberus.txt")
        time.sleep(2)
        elevator()
    else:
        print(Fore.MAGENTA + Style.BRIGHT + "\nI am afraid that we cannot allow that selection. Please choose again.\n")
        time.sleep(2)
        meet_cerberus()

#User is presented with an opportunity to escape via elevator
def elevator():
    read_story("assets/text-files/elevator.txt")
    story_choice = int(input("Please select 1 or 2:\n"))
    if story_choice == 1:
        read_story("assets/text-files/elevator-escape.txt")
        time.sleep(2)
        read_story("assets/text-files/win.txt")
        time.sleep(2)
    elif story_choice == 2:
        read_story("assets/text-files/elevator-death.txt")
        time.sleep(2)
        read_story("assets/text-files/lose.txt")
        time.sleep(2)
        replay()
    else:
        print(Fore.MAGENTA + Style.BRIGHT + "\nI am afraid that we cannot allow that selection. Please choose again.\n")
        time.sleep(2)
        elevator()

# Function to offer user the option to replay
def replay():
    play_again = int(input("Please select 1 or 2:\n"))
    if play_again == 1:
        adv_start()
    elif play_again == 2:
        print(Fore.MAGENTA + Style.BRIGHT + "\nCoward...\n")
        time.sleep(2)
        exit()
    else:
        print(Fore.MAGENTA + Style.BRIGHT + "\nWe shall take your inability to take instructions as a no...\n")
        time.sleep(2)
        exit()

adv_start()


