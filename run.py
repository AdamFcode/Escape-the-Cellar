"""
Import time, sys and colorama
Time for time.delay function
Used to stagger printing and
keep presented text legible
Sys for exiting app in replay function
Colorama to style printed text
"""
import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Declare name as empty string

name = ""


def user_name():
    """
    Request name from user
    Store in global variable for
    recall later
    Return the adv_start function
    """
    global name
    name = input(Fore.MAGENTA +
                 Style.BRIGHT +
                 "Before we began, your name, little one?\n")
    print("\n")
    time.sleep(1)
    print(Fore.MAGENTA +
          Style.BRIGHT +
          f"{name}? A lovely name. Allow us to eat it...")
    time.sleep(1)
    print(Fore.MAGENTA +
          Style.BRIGHT +
          "Escape, and you may get it back. Let's begin...")
    time.sleep(2)
    adv_start()


# Function to open, read and close the story txt files


def read_story(filepath):
    """
    Opens the selected txt file
    Iterates through the file and prints content
    Printed in colour with delay between lines
    Closes document
    """
    with open(filepath, encoding="utf-8") as f:
        for char in f:
            print(Fore.MAGENTA + Style.BRIGHT + char, end="")
            time.sleep(0.75)


# Function to open read and close title cards
# Prints quicker than read-story function


def title_read(filepath):
    """
    Performs same function as read_story
    Prints the content quicker than read_story
    Required for ascii title cards
    """
    with open(filepath, encoding="utf-8") as f:
        for char in f:
            print(Fore.GREEN + Back.MAGENTA + Style.BRIGHT + char, end="")
            time.sleep(0.15)


# Function to start the game


def adv_start():
    """
    Prints the title and intro
    Asks user whether they wish to play
    Provides input for answer
    If yes advances to path_selection
    If no it exits the app
    If input is invalid returns error message
    Error leads to adv_start restarting.
    """
    title_read("assets/text-files/title.txt")
    time.sleep(2)
    read_story("assets/text-files/intro-play.txt")
    try:
        story_choice = int(input("Please select 1 or 2:\n"))
        if story_choice == 1:
            path_select()
        elif story_choice == 2:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "That's really too bad. Enjoy an eternity of darkness...\n"
            )
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "I am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            adv_start()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        adv_start()


# User selects their choice of path


def path_select():
    """
    Prints path selection file
    Requests user input for path selection
    Valid input decides next pathway
    Invalid input returns error message
    Error message restarts path_select function
    """
    read_story("assets/text-files/path-select.txt")
    try:
        story_choice = int(input("Please select 1 or 2:\n"))
        if story_choice == 1:
            meet_gargoyles()
        elif story_choice == 2:
            meet_troll()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "I am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            path_select()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        path_select()


# Users chooses the downstairs route (Path A)
# User meets a Troll


def meet_troll():
    """
    Prints troll confrontation
    Requests input for 3 choices
    Input leads to either advancement,
    game over, or another input
    Second input leads to game over
    regardless of choice
    Incorrect input returns error message
    Error message returns meet_troll function
    """
    read_story("assets/text-files/meet-troll.txt")
    try:
        story_choice = int(input("Please select 1, 2 or 3:\n"))
        if story_choice == 1:
            read_story("assets/text-files/defeat-troll.txt")
            time.sleep(2)
            riddle_path_one()
        elif story_choice == 2:
            read_story("assets/text-files/stun-troll.txt")
            time.sleep(2)
            troll_stunned = int(input("Please select 1 or 2\n"))
            try:
                if troll_stunned == 1 or 2:
                    read_story("assets/text-files/killed-by-troll.txt")
                    stun_kill()
            except ValueError:
                print(
                    Fore.MAGENTA
                    + Style.BRIGHT
                    + "I am afraid that we cannot allow that selection."
                    " Please choose again.\n"
                )
                time.sleep(2)
                meet_troll()
        elif story_choice == 3:
            read_story("assets/text-files/killed-by-troll.txt")
            time.sleep(1)
            title_read("assets/text-files/fail.txt")
            lose_name()
            time.sleep(2)
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "\nI am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            meet_troll()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        meet_troll()


# User meets the Riddler on path 1


def riddle_path_one():
    """
    Prints riddle for path 1
    Requests input for 2 choices
    Input leads to either advancement
    or another input.
    Second input leads to game over
    regardless of choice
    Incorrect input returns error message
    Error message returns riddle_path_one function
    """
    read_story("assets/text-files/riddle-path-one.txt")
    try:
        story_choice = int(input("Please select 1 or 2:\n"))
        if story_choice == 1:
            read_story("assets/text-files/riddle-right.txt")
            time.sleep(2)
            meet_cerberus()
        elif story_choice == 2:
            riddle_incorrect()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "\nI am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            riddle_path_one()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        riddle_path_one()


# The user meets a three-headed dog from hell


def meet_cerberus():
    """
    Prints cerberus confrontation
    Requests input for 3 choices
    Input leads to either advancement,
    game over, or another input
    Second input leads to game over
    regardless of choice
    Incorrect input returns error message
    Error message returns meet_cerberus function
    """
    read_story("assets/text-files/meet-cerberus.txt")
    try:
        story_choice = int(input("Please select 1, 2 or 3:\n"))
        if story_choice == 1:
            read_story("assets/text-files/stun-cerberus.txt")
            time.sleep(2)
            try:
                cerberus_stunned = int(input("Please select 1 or 2\n"))
                if cerberus_stunned == 1 or 2:
                    read_story("assets/text-files/killed-by-cerberus.txt")
                    stun_kill()
            except ValueError:
                print(
                    Fore.MAGENTA
                    + Style.BRIGHT
                    + "I am afraid that we cannot allow that selection."
                    " Please choose again.\n"
                )
                time.sleep(2)
                meet_cerberus()
        elif story_choice == 2:
            read_story("assets/text-files/killed-by-cerberus.txt")
            time.sleep(1)
            title_read("assets/text-files/fail.txt")
            lose_name()
            time.sleep(2)
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
        elif story_choice == 3:
            read_story("assets/text-files/defeat-cerberus.txt")
            time.sleep(2)
            elevator()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "\nI am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            meet_cerberus()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        meet_cerberus()


# User is presented with an opportunity to escape via elevator


def elevator():
    """
    Prints elevator escape opportunity
    Requests input of 2 choices
    One leads to game over
    Other leads to win condition
    Invalid input returns error message
    Error message returns elevator function
    """
    read_story("assets/text-files/elevator.txt")
    try:
        story_choice = int(input("Please select 1 or 2:\n"))
        if story_choice == 1:
            read_story("assets/text-files/elevator-escape.txt")
            time.sleep(1)
            title_read("assets/text-files/congrats.txt")
            win_name()
            time.sleep(2)
            read_story("assets/text-files/win.txt")
            time.sleep(2)
            replay()
        elif story_choice == 2:
            read_story("assets/text-files/elevator-death.txt")
            time.sleep(1)
            title_read("assets/text-files/fail.txt")
            lose_name()
            time.sleep(2)
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "\nI am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            elevator()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        elevator()

# User chooses the upstairs route (Path B)
# User meets some Gargoyles


def meet_gargoyles():
    """
    Prints gargoyles confrontation
    Requests input for 3 choices
    Input leads to either advancement,
    game over, or another input
    Second input leads to game over
    regardless of choice
    Incorrect input returns error message
    Error message returns meet_gargoyles function
    """
    read_story("assets/text-files/meet-gargoyle.txt")
    try:
        story_choice = int(input("Please select 1, 2 or 3:\n"))
        if story_choice == 1:
            read_story("assets/text-files/killed-by-gargoyles.txt")
            time.sleep(1)
            title_read("assets/text-files/fail.txt")
            lose_name()
            time.sleep(2)
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
        elif story_choice == 2:
            read_story("assets/text-files/stun-gargoyles.txt")
            time.sleep(2)
            try:
                gargoyle_stunned = int(input("Please select 1 or 2:\n"))
                if gargoyle_stunned == 1 or 2:
                    read_story("assets/text-files/killed-by-gargoyles.txt")
                    stun_kill()
            except ValueError:
                print(
                    Fore.MAGENTA
                    + Style.BRIGHT
                    + "I am afraid that we cannot allow that selection."
                    " Please choose again.\n"
                )
                time.sleep(2)
                meet_gargoyles()
        elif story_choice == 3:
            read_story("assets/text-files/defeat-gargoyles.txt")
            time.sleep(2)
            riddle_path_two()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "\nI am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            meet_gargoyles()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        meet_gargoyles()


# User meets the riddler on path 2


def riddle_path_two():
    """
    Prints riddle path 2
    Requests input for 2 choices
    Input leads to either advancement
    or another input.
    Second input leads to game over
    regardless of choice
    Incorrect input returns error message
    Error message returns riddle_path_two function
    """
    read_story("assets/text-files/riddle-path-two.txt")
    try:
        story_choice = int(input("Please select 1 or 2:\n"))
        if story_choice == 1:
            read_story("assets/text-files/riddle-right.txt")
            time.sleep(2)
            meet_witch()
        elif story_choice == 2:
            riddle_incorrect()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "\nI am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            riddle_path_two()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        riddle_path_two()

# User meets a witch


def meet_witch():
    """
    Prints witch confrontation
    Requests input for 3 choices
    Input leads to either advancement,
    game over, or another input
    Second input leads to game over
    regardless of choice
    Incorrect input returns error message
    Error message returns meet_witch function
    """
    read_story("assets/text-files/meet-witch.txt")
    try:
        story_choice = int(input("Please select 1, 2 or 3:\n"))
        if story_choice == 1:
            read_story("assets/text-files/killed-by-witch.txt")
            time.sleep(1)
            title_read("assets/text-files/fail.txt")
            lose_name()
            time.sleep(2)
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
        elif story_choice == 2:
            read_story("assets/text-files/stun-witch.txt")
            time.sleep(2)
            try:
                witch_stunned = int(input("Please select 1 or 2:\n"))
                if witch_stunned == 1 or 2:
                    read_story("assets/text-files/killed-by-witch.txt")
                    stun_kill()
            except ValueError:
                print(
                    Fore.MAGENTA
                    + Style.BRIGHT
                    + "I am afraid that we cannot allow that selection."
                    " Please choose again.\n"
                )
                time.sleep(2)
                meet_witch()
        elif story_choice == 3:
            read_story("assets/text-files/defeat-witch.txt")
            time.sleep(2)
            hatch()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "\nI am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            meet_witch()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        meet_witch()


# User is presented with an opportunity to escape via hatch


def hatch():
    """
    Prints hatch escape opportunity
    Requests input of 2 choices
    One leads to game over
    Other leads to win condition
    Invalid input returns error message
    Error message returns hatch function
    """
    read_story("assets/text-files/hatch.txt")
    try:
        story_choice = int(input("Please select 1 or 2:\n"))
        if story_choice == 1:
            read_story("assets/text-files/hatch-death.txt")
            time.sleep(1)
            title_read("assets/text-files/fail.txt")
            lose_name()
            time.sleep(2)
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
        elif story_choice == 2:
            read_story("assets/text-files/hatch-escape.txt")
            time.sleep(1)
            title_read("assets/text-files/congrats.txt")
            win_name()
            time.sleep(2)
            read_story("assets/text-files/win.txt")
            time.sleep(2)
            replay()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "\nI am afraid that we cannot allow that selection."
                " Please choose again.\n"
            )
            time.sleep(2)
            hatch()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        hatch()

# Function to offer user the option to replay


def replay():
    """
    Called directly after lose or win text file
    Requests input for play again question
    as presented in those files
    If yes returns user to adv_start function
    If no exits the app
    Incorrect input returns tongue in cheek message
    and exits the app
    """
    try:
        play_again = int(input("Please select 1 or 2:\n"))
        if play_again == 1:
            adv_start()
        elif play_again == 2:
            print(Fore.MAGENTA + Style.BRIGHT + "\nCoward...\n")
            time.sleep(2)
            sys.exit()
        else:
            print(
                Fore.MAGENTA
                + Style.BRIGHT
                + "\nWe shall take your inability to"
                " take instructions as a no...\n"
            )
            time.sleep(2)
            sys.exit()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
            )
        time.sleep(2)
        replay()


# Function called after incorrect riddle answer


def riddle_incorrect():
    """
    Called when riddle selection on either
    path is incorrect.
    Requests choice of 1 or 2 from user
    Returns game over regardless of choice
    Game over condition calls the replay function
    """
    read_story("assets/text-files/riddle-wrong.txt")
    time.sleep(2)
    try:
        riddle_wrong = int(input("Please select 1 or 2:\n"))
        if riddle_wrong == 1 or 2:
            read_story("assets/text-files/killed-by-riddle.txt")
            time.sleep(1)
            title_read("assets/text-files/fail.txt")
            lose_name()
            time.sleep(2)
            read_story("assets/text-files/lose.txt")
            time.sleep(2)
            replay()
    except ValueError:
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "I am afraid that we cannot allow that selection."
            " Please choose again.\n"
        )
        time.sleep(2)
        riddle_incorrect()


# Function called after an enemy has been stunned by the user


def stun_kill():
    """
    Called whenever a users choice stuns the enemy
    Prints fail and lose text files
    Prints sneering comment that
    returns users entered name
    Calls replay function
    """
    time.sleep(1)
    title_read("assets/text-files/fail.txt")
    lose_name()
    time.sleep(2)
    read_story("assets/text-files/lose.txt")
    time.sleep(2)
    replay()


# Function called when user loses (regards stored name)

def lose_name():
    """
    Prints personalised message referencing
    username on lose condition
    """
    time.sleep(1)
    print((Fore.MAGENTA +
          Style.BRIGHT +
          f"\nNow where is that name? Ah! {name}!"))
    time.sleep(1)
    print((Fore.MAGENTA +
          Style.BRIGHT +
          "NOM NOM NOM! Simply delicious!"))

# Function called when user wins(regards stored name)


def win_name():
    """
    Prints personalised message referencing
    username on win condition
    """
    time.sleep(1)
    print((Fore.MAGENTA +
          Style.BRIGHT +
          f"\nNow where is that name? Ah! {name}!"))
    time.sleep(1)
    print((Fore.MAGENTA +
          Style.BRIGHT +
          "A tasty morsel! But it is yours to keep!"))


def main():
    """
    Function to inititate the app for new user
    """
    user_name()


if __name__ == "__main__":
    main()
