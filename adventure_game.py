import time
import random

enemies = ['Moxi', 'Ragnarok', 'RedLine']
chest = ['Golden Scar', 'M16', 'Heavy Sniper']


def pause(wait):
    print(wait)
    time.sleep(2.5)


def pause2(wait):
    print(wait)
    time.sleep(1.5)


def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        time.sleep(1)


def beginning():
    pause("You are waiting for the battle plane in 'paradise palms'")
    pause("Waiting to go to 'Tilted Towers',\
 a big city in the Battle Royale arena.")
    pause('You are taking the journey the long way!')
    pause2('You are almost there!!')
    countdown(3)


beginning()


def start_game():
    print("\n\n\n")
    pause2("well, you have arrived.")
    pause("You find yourself standing in 'Tilted Towers', \
 the Volcano erupted and destroyed most of it.")
    pause("In front of you is the 'High Rise Building', \
 Get in and get the 'Llama crystal'.")
    tk_inp_house()


def back_to_tilted():
    pause("welcome back!!")
    at_tiltedtowers()


def tk_inp_house():
    answer = input('\nType "start" to enter the building: ').lower()
    if answer == "start":
        at_tiltedtowers()
    else:
        print("\nYou have entered an invalid value.")
        tk_inp_house()


weapon = random.choice(chest)


def at_tiltedtowers():
    print("\n\n\n")
    pause("You are in front of the\
 gate of the building\
 but you don't know what to do.")
    pause("You entered the building, you\
 look everywhere till you find out a big chest.")
    pause('You are about to open it out when\
 you heard foot steps coming from outside.')
    pause("\nYou quickly open the chest to find out a " + "' " + weapon + " '")
    pause('Uh Oh!\nThe door is opened')
    enemy = random.choice(enemies)
    pause("\nOh No! " + enemy + ' is too close')
    if enemy == "Moxi":
        moxi_fight()
    elif enemy == "Ragnarok":
        ragnarok_fight()
    elif enemy == "RedLine":
        redline_fight()


def defeated():
    pause('Unfortunately , you are defeated.')
    try_again()


def won():
    pause('Congratulations ! You Have Won, You have got the Llama crystal!!')
    try_again()


def try_again():
    answer = input('Would you like try again ? (yes/no)').lower()
    if answer == 'yes':
        pause('Loading....')
        countdown(3)
        start_game()
    elif answer == 'no':
        print("Thanks for playing")
    else:
        print("Invalid Value")
        try_again()


def moxi_fight():
    answer = input("Choose (1) to fight or (2) to run away ?")
    if answer == "1":
        pause("Pick up your " + weapon)
        pause("AtLeast, you are trying!")
        if weapon == "Golden Scar":
            pause2("You have got Golden scar, it's a strong weapon \
 don't worry.")
            won()
        elif weapon == "M16":
            pause2("One headshot with your M16 is enough.")
            won()
        elif weapon == "Heavy Sniper":
            pause("Moxi is the fastest ever,\
you can't kill her with a sniper!")
            defeated()
    elif answer == "2":
        back_to_tilted()
    else:
        print("Enter a valid number.")
        moxi_fight()


def ragnarok_fight():
    answer = input("Choose (1) to fight or (2) to run away ?")
    if answer == "1":
        pause("Pick up your " + weapon)
        pause("Ragnarok is really strong enemy, but keep going.")
        if weapon == "Golden Scar":
            pause2("This Scar is the most suitable weapon\
 to defeat ragnarok, it's a strong weapon.")
            won()
        elif weapon == "M16":
            pause2("M16 is a strong weapon, but\
 unfortunately ragnarok is stronger.")
            defeated()
        elif weapon == "Heavy Sniper":
            pause("Ragnarok has smashed your weapon.")
            defeated()
    elif answer == "2":
        back_to_tilted()
    else:
        print("Enter a valid number.")
        ragnarok_fight()


def redline_fight():
    answer = input("Choose (1) to fight or (2) to run away ?  ")
    if answer == "1":
        pause("Pick up your " + weapon)
        pause("No Way!! It's RedLine bro, you are dead.")
        defeated()
    elif answer == "2":
        back_to_tilted()
    else:
        print("Enter a valid number.")
        redline_fight()


start_game()
