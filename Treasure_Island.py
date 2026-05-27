print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your goal is to find the treasure.")
print("You are at a cross-road. Where do you want to go?")
player_turn_decision=input("Type \"left\" for left, \"right\" for right:\n")
if player_turn_decision == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    print("So, what would you like to do now? Swim across or wait for boat?")
    player_action_decision=input("Type \"swim\" to swim across or \"wait\" to wait for boat:\n")
    if player_action_decision == "wait":
        print("You arrive at the island unharmed. On the island, you find a home with three doors: red, blue and yellow. Which dor would you choose?")
        player_door_decision=input("Type \"red\" for red, \"blue\" for blue, \"yellow\" for yellow:\n")
        if player_door_decision == "yellow":
            print(" You found the treasure. You won the treasure! Congratulations!!")
        elif player_door_decision == "blue":
            print("You enter a room of beats, the beasts attack you! Game Over:(")
        else:
            print("It's a room full of fire! Game Over:(")
    else:
        print("You get attacked by an angry grout in the lake! Game Over:(")
else:
    print("You fell into a hole! Game Over:(")
