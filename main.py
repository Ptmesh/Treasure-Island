print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island...\nYour mission is to find the legendary treasure of Captain Blackbeard.")

direction = input("\nYou find yourself standing at a crossroad in a dense jungle. To your left is a narrow path with ancient trees and strange whispers. To your right, a misty trail leads into the unknown. Which path do you choose? Press 'R' for right or 'L' for left: ")

if direction == "L":
    decision = input("\nYou cautiously step onto the left path, the whispers growing louder with every step. Suddenly, you come across a murky pond. Do you 'S' swim across or 'W' wait and observe? ")
    if decision == "W":
        door = input("\nAfter a tense wait, the whispers fade, and you find yourself in front of three mysterious doors. A red door, a blue door, and a golden door shimmering in the dim light. Which door do you choose? 'R' for red, 'B' for blue, or 'Y' for yellow: ")
        if door == "Y":
            print("As you open the golden door, a blinding light fills the chamber. Congratulations! You've found the legendary treasure of Captain Ptmesh , the richest pirate in history.")
        else:
            print("You open the door cautiously, but it leads to a dead-end. The treasure remains hidden. Game over.")
    else:
        print("You dive into the murky waters, but something sinister lurks beneath. You never emerge. Game over.")
else:
    print("You embark on the misty trail, excitement pulsating through your veins. Suddenly, the ground gives way, and you plummet into darkness. Game over.")
