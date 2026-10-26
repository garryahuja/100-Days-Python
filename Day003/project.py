print(r'''
--------------------------------------------------------------------------

@                               _                                  ,,
 \\   _   @'                    ( )_                       .      _  \\
  \\_( )_//                    / Y |                   .      /--( )_//
    | Y/--                    /\   /               .        '//  \~ \
    |_/       _ / o"         ( _\ /            .                   - \
  _ //\      | | |    .       \_\\\        .                     //  \\--,
 /_// /      | | |      .    / \ \\\ .                           \\
/ // /_______|_|_|__________/_/_\ \_______________________________\\______
-------------------------------------------- Play Cricket ----------------

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road = input("You're at a cross road. Where do you want to go?\n\t Type \"left\" or \"right\"\n")
road_actual = road.lower()
if road_actual == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake.\n Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")
    lake_actual = lake.lower()
    if lake_actual == "wait":
        house = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?\n")
        house_actual = house.lower()
        if house_actual == "red":
            print("It's a room full of dangerous fast bowlers. Game Over.")
        elif house_actual == "yellow":
            print("You found the treasure! You win!")
        elif house_actual == "blue":
            print("You entered a room full of mystery spinners. Game Over.")
        else:
            print("Game Over.")
    elif lake_actual == "swim":
        print("You get attacked by an angry tout. Game Over.")
elif road_actual == "right":
    print("You fell into a cricket ground. Game Over.")
else:
    print("You fell into a cricket ground. Game Over.")