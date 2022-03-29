import random
import monsters as m
import character as c

player = c.Character("")
diff_increase = 0


def set_name(name):
    player.name = name


def battle_calculator(monster, m1_dmg, enemy_monster, m2_dmg):
    total_damage = m1_dmg + m2_dmg
    if m1_dmg < 0 and m2_dmg < 0:
        pass
    elif m1_dmg < 0 and total_damage < 0:
        print(f"{monster.name} takes 0 damage.")
    elif m1_dmg < 0:
        print(f"{monster.name} takes {total_damage}.")
        monster.hp -= total_damage
    elif m2_dmg < 0 and total_damage < 0:
        print(f"{enemy_monster.name} takes 0 damage.")
    elif m2_dmg < 0:
        print(f"{enemy_monster.name} takes {total_damage}.")
        enemy_monster.hp -= total_damage
    else:
        print(f"{monster.name} takes {m2_dmg}.")
        print(f"{enemy_monster.name} takes {m1_dmg}.")
        monster.hp -= m2_dmg
        enemy_monster.hp -= m1_dmg


def random_battler(monster, enemy_name):
    skill_num = random.randint(0, 5)
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
            command = int(input)

    return dmg, skill_str


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


def monster_battle():
    m1 = m.Ghost()
    m2 = m.RandomMonster()
    m2.increase_stats(diff_increase)

    while True:
        try:
            command = int(input("Please choose an action \n1. Attack\t2. Skill\n3. Stats\t4. Swap\n> "))
            if command == 1:
                display_skills("Ghost")
                try:
                    command = int(input())
                    m1_dmg, m1_str = skill_use(command, m1, m2.name)
                    m2_dmg, m2_str = random_battler(m2, m1)
                    print(m1_str, m2_str)
                    battle_calculator(m1, m1_dmg, m2, m2_dmg)

                    m1_dead = True if m1.hp < 0 else False
                    m2_dead = True if m2.hp < 0 else False
                    if m1_dead:
                        print("You lose")
                        break
                    if m2_dead:
                        print("Monster has been defeated. Would you like to recruit this monster? Y/N")
                        try:
                            recruit = input().split()
                        except:
                            
                        global diff_increase
                        diff_increase += 1


                        break
                except ValueError:
                    error_msg()
            elif command == 2:
                try:

                    pass
                except ValueError:
                    pass
            elif command == 3:
                print(m1)
            elif command == 4:
                if len(player.monsters_list) < 1:
                    print("No monsters to swap.")
                pass
            else:
                pass
            if command == -1:
                break
        except ValueError:
            error_msg()

def error_msg():
    print("Command must be 1, 2, 3, or 4. Press -1 to quit.")

