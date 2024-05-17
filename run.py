# Function to open, read and close the story txt files
def read_story(filepath):
    f = open(filepath, "r")
    print(f.read())
    f.close()

# Function to start the game
def adv_start():
    read_story("assets/text-files/intro-play.txt")
    story_choice = int(input("Please select 1 or 2:\n"))
    if story_choice == 1:
        path_select()
    elif story_choice == 2:
        print("That's really too bad. Enjoy an eternity of darkness...")
    else:
        print("I am afraid that we cannot allow that selection. Please choose again.\n")
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
        return path_select()

adv_start()

