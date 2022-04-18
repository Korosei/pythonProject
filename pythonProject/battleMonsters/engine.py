import random
import monsters as m
import character as c
from skills import skills_info
import pickle

player = c.Character("")
difficulty_level = 0


def add_mon(monster):
    player.add_monster(monster)


def set_name(name):
    player.name = name


def swap_starter(index):
    index = index-1
    m_list = player.monsters_list
    try:
        if index == -1:
            swap_str = "Starting monster not changed."
        elif index == 0:
            swap_str = f"{m_list[0].name} is already your starting monster."
        elif -1 < index < len(m_list):
            m_list[0], m_list[index] = m_list[index], m_list[0]
            swap_str = f"{m_list[0].name} is now your starting monster."
        else:
            raise ValueError
    except ValueError:
        swap_str = "That isn't a valid option"

    return swap_str


def battle_calculator(monster, m1_dmg, enemy_monster, m2_dmg):
    total_damage = m1_dmg + m2_dmg
    if m1_dmg < 0 and m2_dmg < 0:
        pass
    elif m1_dmg < 0 and total_damage < 0:
        print(f"{monster.name} takes 0 damage.")
    elif m1_dmg < 0:
        monster.hp -= total_damage
        print(f"{monster.name} takes {total_damage}.")
    elif m2_dmg < 0 and total_damage < 0:
        print(f"{enemy_monster.name} takes 0 damage.")
    elif m2_dmg < 0:
        print(f"{enemy_monster.name} takes {total_damage}.")
        enemy_monster.hp -= total_damage
    else:
        if m2_dmg != 0:
            print(f"{monster.name} takes {m2_dmg}.")
        print(f"{enemy_monster.name} takes {m1_dmg}.")
        monster.hp -= m2_dmg
        enemy_monster.hp -= m1_dmg


def random_battler(monster, enemy_name):
    if monster.mp > 15:
        skill_num = random.randint(1, 4)
    elif monster.mp > 5:
        skill_num = random.randint(1, 3)
    else:
        skill_num = random.randint(1, 2)
    dmg, rd_str = skill_use(skill_num, monster, enemy_name)
    return dmg, rd_str


def skill_use(command, monster, enemy_name):
    skill_choice = ["hit", "guard", "skill_one", "skill_two"]
    while True:
        if 0 < command < 5:
            func = getattr(monster, skill_choice[command-1])
            dmg, skill_str = func(enemy_name)
            break
        else:
            display_skills(monster.name)
            command = int(input("> "))

    return dmg, skill_str


def player_skills(command, monster, enemy_monster):
    func = getattr(player, "use_skill")
    while True:
        try:
            if command == 1:
                print(func(command, monster))
                monster.hp = monster.def_hp
                return 1
            elif command == 2:
                boost, b_str = func(command, monster)
                print(b_str)
                monster.atk += boost
                monster.defense += boost
                return 2
            elif command == 3:
                dmg, d_str = func(command, enemy_monster)
                print(d_str)
                enemy_monster.hp -= dmg
                return 3
            elif command == 4:
                print(func(command, enemy_monster))
                return 4
            elif command == -1:
                quit()
            else:
                raise ValueError
        except ValueError:
            display_skills(player.name)
            command = int(input("> "))


def display_skills(char):
    if char is player.name:
        skill = player.skill_list
    else:
        skill = char.skills_list()

    for num, attack in enumerate(skill):
        if num + 1 == 3:
            print()
        print(f"{num + 1}. {attack}\t", end="")
    print()


def display_monsters():
    d_str = f"{player.name}'s party:\n"
    for num, monster in enumerate(player.monsters_list):
        d_str += f"{num+1}. {monster.name} ({monster.hp}/{monster.def_hp})\n"

    return d_str


def display_party():
    print(f"{player.name}'s Party: ")
    for monster in player.monsters_list:
        print(monster, end="")
        skills = getattr(monster, "skills_list")
        print(skills(), "\n")


def reset_party():
    for monster in player.monsters_list:
        monster.reset_stats()


def monster_battle():
    m1 = player.monsters_list[0]
    m2 = m.RandomMonster()
    m2.increase_stats(difficulty_level)
    player_skill = 1
    boost_turns = 2
    is_boosted = False
    player_flashed = False
    enemy_flashed = False

    while True:
        try:
            print(f"{m1.name} ({m1.hp}/{m1.def_hp}) vs {m2.name} ({m2.hp}/{m2.def_hp})")
            command = int(input("Please choose an action \n1. Attack\t2. Skill\n3. Stats\t4. Swap\n> "))
            if command == 1:

                if is_boosted and boost_turns != 0:
                    boost_turns -= 1
                else:
                    m1.atk = m1.def_atk
                    m1.defense = m1.def_defense
                    is_boosted = False

                display_skills(m1)
                try:
                    command = int(input("> "))
                    if player_flashed:
                        m1_dmg, m1_str = 0, ""
                        player_flashed = False
                    else:
                        if (command == 4 and m1.mp < 20) or (command == 3 and m1.mp < 5):
                            print(f"{m1.name} doesn't have enough mp.")
                            continue
                        else:
                            m1_dmg, m1_str = skill_use(command, m1, m2)

                    if enemy_flashed:
                        m2_dmg, m2_str = 0, ""
                        enemy_flashed = False
                    else:
                        m2_dmg, m2_str = random_battler(m2, m1)
                    print(m1_str, m2_str)
                    battle_calculator(m1, m1_dmg, m2, m2_dmg)

                    m1_dead = True if m1.hp < 0 else False
                    m2_dead = True if m2.hp < 0 else False
                    if m2_dead:
                        while True:
                            try:
                                print(f"{m2.name} has been defeated. Would you like to recruit {m2.name} "
                                      f"into your party? Y/N")
                                recruit = input("> ").strip()
                                if recruit[0].lower() == "y":
                                    player.add_monster(m2)
                                    print(f"{m2.name} has been recruited.")
                                    break
                                elif recruit[0].lower() == "n":
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                continue
                        break
                    if m1_dead:
                        print(f"{m1.name} has died.")
                        m_list = player.monsters_list
                        if len(m_list) > 0:
                            for mon in m_list:
                                if mon.hp > 0:
                                    m1 = mon
                                    break
                        print("You have no other monsters to battle with. Game over.")
                        break
                except ValueError:
                    continue
            elif command == 2:
                if not player_skill:
                    print("You can only use one skill per match.")
                    continue
                try:
                    display_skills(player.name)
                    command = int(input("> "))
                    r_command = player_skills(command, m1, m2)
                    if r_command == 2:
                        is_boosted = True
                    if r_command == 4:
                        enemy_flashed = True
                    player_skill = 0
                except ValueError:
                    display_skills(player.name)
            elif command == 3:
                print(m1, end="")
                print(m1.skills_list(), "\n")
            elif command == 4:
                if len(player.monsters_list) == 1:
                    print("You don't have any other monsters.")
                else:
                    display_monsters()
                    print("Enter the number of the monster you want to swap to: ")
                    while True:
                        try:
                            cmd = int(input().strip())-1
                            monster = player.monsters_list[cmd]

                            if monster is m1:
                                print(f"{monster.name} is already out. Cancel swapping? Y/N\n> ")
                                try:
                                    cmd = input().strip()
                                    if cmd.lower() == "y":
                                        break
                                    elif cmd.lower() == "n":
                                        continue
                                    else:
                                        raise ValueError
                                except ValueError:
                                    continue
                            elif monster.hp == 0:
                                print(f"{monster.name} is dead.")
                            else:
                                m1 = monster
                        except (IndexError, ValueError):
                            display_monsters()
                            print("Enter the number of the monster you want to swap to: ")
            elif command == -1:
                quit()
            else:
                continue
        except ValueError:
            continue

    reset_party()


def save_game():
    m_list = player.monsters_list
    save = [player.name, m_list, difficulty_level]
    with open("battle_save.txt", 'wb') as bs:
        pickle.dump(save, bs)


def load_game():
    global difficulty_level
    with open("battle_save.txt", "rb") as bs:
        load = pickle.load(bs)
    player.name, player.monsters_list, difficulty_level = load


def print_skills():
    skills_info()
