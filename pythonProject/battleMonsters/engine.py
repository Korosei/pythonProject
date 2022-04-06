import random
import monsters as m
import character as c

player = c.Character("")
difficulty_level = 0


def set_name(name):
    player.name = name


def battle_calculator(monster, m1_dmg, enemy_monster, m2_dmg):
    total_damage = m1_dmg + m2_dmg
    if m1_dmg < 0 and m2_dmg < 0:
        pass
    elif m1_dmg < 0 and total_damage < 0:
        print(f"{monster.name} takes 0 damage.")
    elif m1_dmg < 0:
        monster.curr_hp -= total_damage
        print(f"{monster.name} takes {total_damage}.")
    elif m2_dmg < 0 and total_damage < 0:
        print(f"{enemy_monster.name} takes 0 damage.")
    elif m2_dmg < 0:
        print(f"{enemy_monster.name} takes {total_damage}.")
        enemy_monster.curr_hp -= total_damage
    else:
        if m2_dmg != 0:
            print(f"{monster.name} takes {m2_dmg}.")
        print(f"{enemy_monster.name} takes {m1_dmg}.")
        monster.curr_hp -= m2_dmg
        enemy_monster.curr_hp -= m1_dmg


def random_battler(monster, enemy_name):
    skill_num = random.randint(1, 4)
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
            error_msg()
            display_skills(monster.name)
            command = int(input())

    return dmg, skill_str


def player_skills(command, monster, enemy_monster):
    func = getattr(player, "use_skill")
    while True:
        try:
            if command == 1:
                print(func(command, monster.name))
                monster.curr_hp = monster.max_hp
            elif command == 2:
                boost, b_str = func(command, monster.name)
                print(b_str)
                monster.curr_atk += boost
                monster.curr_defense += boost
                return 2
            elif command == 3:
                dmg, d_str = func(command, enemy_monster.name)
                print(d_str)
                enemy_monster.curr_hp -= dmg
            elif command == 4:
                print(func(command, enemy_monster.name))
                return 4
            else:
                raise ValueError
        except ValueError:
            error_msg()
            display_skills(player.name)
            command = int(input())
        return 0


def display_skills(name):
    if name is player.name:
        skill = player.skill_list
    else:
        skill = m.get_skills(name)

    for num, attack in enumerate(skill):
        if num + 1 == 3:
            print()
        print(f"{num + 1}. {attack}\t", end="")
    print()


def display_monsters():
    for num, monster in enumerate(player.monsters_list):
        print(f"{num+1}. {monster.name} ({monster.curr_hp}/{monster.max_hp})")


def monster_battle():
    m1 = player.monsters_list[0]
    m2 = m.RandomMonster()
    m2.increase_stats(difficulty_level)
    player_skill = 1
    boost_turns = 2
    is_boosted = False
    is_flashed = False

    while True:
        try:
            command = int(input("Please choose an action \n1. Attack\t2. Skill\n3. Stats\t4. Swap\n> "))
            if command == 1:

                if is_boosted and boost_turns != 0:
                    boost_turns -= 1
                else:
                    m1.curr_atk = m1.def_atk
                    m1.curr_defense = m1.def_defense
                    is_boosted = False

                display_skills(m1.name)
                try:
                    command = int(input())
                    m1_dmg, m1_str = skill_use(command, m1, m2.name)
                    if is_flashed:
                        m2_dmg, m2_str = 0, ""
                        is_flashed = False
                    else:
                        m2_dmg, m2_str = random_battler(m2, m1.name)
                    print(m1_str, m2_str)
                    battle_calculator(m1, m1_dmg, m2, m2_dmg)

                    m1_dead = True if m1.curr_hp < 0 else False
                    m2_dead = True if m2.curr_hp < 0 else False
                    if m2_dead:
                        print(f"{m2.name} has been defeated. Would you like to recruit {m2.name} into your party? Y/N")
                        while True:
                            try:
                                recruit = input().strip()
                                if recruit[0].lower() == "y":
                                    m2.decrease_stats(difficulty_level)
                                    player.add_monster(m2)
                                    break
                                elif recruit[0].lower() == "n":
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print(f"Would you like to recruit {m2.name} into your party? Y/N")

                        break
                    if m1_dead:
                        print("You lose")
                        break
                except ValueError:
                    error_msg()
            elif command == 2:
                if not player_skill:
                    print("You can only use one skill per match.")
                    continue
                try:
                    display_skills(player.name)
                    command = int(input())
                    r_command = player_skills(command, m1, m2)
                    if r_command == 2:
                        is_boosted = True
                    if r_command == 4:
                        is_flashed = True
                    player_skill = 0
                except ValueError:
                    error_msg()
            elif command == 3:
                print(m1)
                print(m2)
            elif command == 4:
                if len(player.monsters_list) == 1:
                    print("You don't have any other monsters.")
                else:
                    print("Enter the number of the monster you want to swap to: ")
                    display_monsters()
                    while True:
                        try:
                            cmd = int(input().strip())-1
                            monster = player.monsters_list[cmd]

                            if monster is m1:
                                print(f"{monster.name} is already out. Cancel swapping? Y/N")
                                try:
                                    cmd = input.strip()
                                    if cmd[0].lower() == "y":
                                        break
                                    elif cmd[0].lower() == "n":
                                        continue
                                    else:
                                        raise ValueError
                                except ValueError:
                                    print(f"{m1.name} is already out. Cancel swapping? Y/N")
                            else:
                                m1 = monster
                        except (IndexError, ValueError):
                            print("Enter the number of the monster you want to swap to: ")
            else:
                error_msg()
            if command == -1:
                break
        except ValueError:
            error_msg()


def error_msg():
    print("Command must be 1, 2, 3, or 4. Press -1 to quit.")

