import random as rd


def heal(char_name, monster):  # Heals current monster to full hp
    return f"{char_name} heals {monster.name} to max hp."


def boost(char_name, monster):  # Raise one monsters' attack and defense by 20 points for 2 turns
    b_str = f"{char_name} raises {monster.name} attack and defense by 20 points for the next 2 turns."
    return 20, b_str


def dagger_throw(char_name, enemy):  # Inflict 25 points of damage to the enemy
    dt_str = f"{char_name} throws a dagger at {enemy.name} and inflicts 25 points of damage!"
    return 25, dt_str


def flash_bomb(char_name, enemy):  # Blinds the enemy causing their turn to be skipped
    return f"{char_name} throws a flash bomb at the {enemy.name}! {enemy.name} is blinded and cannot attack " \
           f"for one turn."


def claw_swipe(*args, enemy):  # Ghost swipes his claws at the enemy inflicting damage equal to 20 damage
    claw_str = f"Ghost swipes his claws at {enemy.name}!"
    return 20, claw_str


def meow_barrage(*args, enemy):  # Ghost meows at the enemy 5-10 times dealing 5 damage each time
    meow_count = rd.randint(5, 11)
    total_damage = meow_count*5
    meow_str = f"Ghost meows {meow_count} times at {enemy.name}!"
    return total_damage, meow_str


def flame_ball(*args, monster, enemy):  # Shoots a ball of fire at the enemy dealing 15 damage
    flame_str = f"{monster.name} shoots a ball of fire at {enemy.name}!"
    return 15, flame_str


def radiant_light(*args, monster, enemy):  # Blinds the enemy, dealing 15 damage and causing their turn to be skipped
    radiant_str = f"{monster.name} harnesses the light of the sun and blinds {enemy.name}. {enemy.name} cant attack " \
                  f"next turn."
    return 15, radiant_str


def water_blast(*args, monster, enemy):  # Blasts the enemy with water
    water_str = f"{monster.name} blasts {enemy.name} with a gush of water!"
    return 15, water_str


def geyser(*args, monster, enemy):
    geyser_str = f"{monster.name} summons a geyser and douses {enemy.name}. {enemy.name} loses 5 defense."
    enemy.atk -= 5
    return 15, geyser_str


def wind_blade(*args, monster, enemy):
    wind_str = f"{monster.name} slashes {enemy.name} with a blade of wind."
    return 15, wind_str


def wind_claws(*args, monster, enemy):
    air_str = f"{monster.name} sharpens their claws with wind and goes in for the attack!."
    return monster.atk + 30, air_str


def boulder_throw(*args, monster, enemy):
    boulder_str = f"{monster.name} chucks a boulder at {enemy.name}."
    return 15, boulder_str


def earthquake(*args, monster, enemy):
    earth_str = f"{monster.name} slams the ground disrupting {enemy.name}'s footing! {enemy.name} loses 5 atk."
    return 20, earth_str


def hit(monster, enemy):
    hit_str = f"{monster.name} hits {enemy.name}!"
    return monster.atk, hit_str


def guard(*args, monster):
    guard_str = f"{monster.name} blocks for {monster.defense}."
    return -monster.defense, guard_str


def rd_skill(choice):
    one_name = ["Flame Ball", "Water Blast", "Wind Blade", "Boulder Throw"]
    two_name = ["Radiant Light", "Geyser", "Wind Claws", "Earthquake"]
    one = [flame_ball, water_blast, wind_blade, boulder_throw]
    two = [radiant_light, geyser, wind_claws, earthquake]
    index = rd.randint(0, 3)

    if choice == 1:
        return one_name[index], one[index]
    else:
        return two_name[index], two[index]


def skills_info():
    print("Player Skills: ")
    print("-Heal: Heals the current monster back to full health.")
    print("-Boost: Increases the current monsters attack and defense by 20 points.")
    print("-Dagger Throw: Throw a dagger at the opposing monster to deal 25 damage.")
    print("-Flash Bomb: Throw a flash bomb at the opposing monster to blind them (monsters next turn is skipped).\n")
    print("Monster Skills: ")
    print("-Claw Swipe: Ghost swipes his claws at the enemy dealing 20 damage.")
    print("-Meow Barrage: Ghost meows at the enemy 5-10 times dealing 5 damage each time.")
    print("-Fireball: Shoots a fireball at the enemy dealing 15 damage.")
    print("-Radiant Light: Blinds the opposing monster (monsters next turn is skipped) and deals 15 damage.")
    print("-Water Blast: Blasts the opposing monster with a gush of water dealing 15 damage.")
    print("-Geyser: Creates a geyser under the opponent inflicting 15 damage and decreasing their defense by 5.")
    print("-Wind Blade: Slashes the enemy with a blade of wind dealing 15 damage.")
    print("-Wind Claws: Monster sharpens their claws dealing a massive attack (monster attack + 30)")
    print("-Boulder Throw: Chucks a boulder at the enemy dealing 15 damage.")
    print("-Earthquake: Slams the ground disrupting the enemies footing. Deals 20 damage and attack down by 5.\n")

