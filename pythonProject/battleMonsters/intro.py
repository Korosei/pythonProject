import engine as e


def menu(command, state):
    if state == "new":
        if command == 1:
            player_name = input("Welcome to Battle Monsters. What is your name? ")

            e.set_name(player_name)
            print(
                f"{player_name} lets get started. The rules of the game are simple. You battle against " +
                "a monster until either that monster reaches 0 hp or the monsters in your party reach 0 hp. " +
                "You start with only 1 monster but after every victory you can recruit the defeated monster.")
            print("While not in battle you can choose which monster you'll start the next battle with, view your " +
                  "parties"
                  " stats, and load/save the game. Anytime while in battle you can enter -1 to quit. " +
                  "Now what would you like to do?\n")
        elif command == 2:
            e.load_game()
            print(f"Game loaded. Welcome back {e.player.name}\n")
        elif command == 3:
            print("Thanks for playing!")
            quit()
    else:
        try:
            print()
            if command == 1:  # Battle Start
                e.monster_battle()
            elif command == 2:  # Save Game
                e.save_game()
                print("Game saved.\n")
            elif command == 3:
                e.load_game()
                print(f"Game loaded. Welcome back {e.player.name}\n")
            elif command == 4:
                e.display_party()
            elif command == 5:
                print(e.display_monsters())
                index = int(input("Enter the number of the monster you want to start with: "))
                print(e.swap_starter(index))
                print("ran")
            elif command == 6:
                e.skills_info()
            elif command == 7:
                print("Thanks for playing!")
                quit()
            else:
                raise ValueError
        except ValueError:
            print("That isn't an option.")


def display_menu(state):
    print("Main Menu: ")
    if state == "new":
        print("1. New Game\n2. Load Game\n3. Exit ")
    else:
        print("1. Battle\n2. Save Game\n3. Load Game\n4. View Party\n5. Change starting monster\n6. View Skills" 
              "\n7. Exit ")


display_menu("new")
cmd = int(input("> "))
menu(cmd, "new")

while True:
    display_menu("")
    cmd = int(input("> "))
    menu(cmd, "")