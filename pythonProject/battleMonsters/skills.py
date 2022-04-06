import random as rd


def heal(char_name, monster_name):  # Heals current monster to full hp
    return f"{char_name} heals {monster_name} to max hp."


def boost(char_name, monster_name):  # Raise one monsters' attack and defense by 20 points for 2 turns
    b_str = f"{char_name} raises {monster_name} attack and defense by 20 points for the next 2 turns."
    return 20, b_str


def dagger_throw(char_name, enemy_name):  # Inflict 25 points of damage to the enemy
    dt_str = f"{char_name} throws a dagger at {enemy_name} and inflicts 25 points of damage!"
    return 25, dt_str


def flash_bomb(char_name, enemey_name):  # Blinds the enemy causing their turn to be skipped
    return f"{char_name} throws a flash bomb at the enemy! {enemey_name} is blinded and cannot attack for one turn."


def claw_swipe(*args, enemy_name):  # Ghost swipes his claws at the enemy inflicting damage equal to 20 damage
    claw_str = f"Ghost swipes his claws at {enemy_name} for 20 damage!"
    return 20, claw_str


def meow_barrage(*args, enemy_name):  # Ghost meows at the enemy 5-10 times dealing 5 damage each time
    meow_count = rd.randint(5, 11)
    total_damage = meow_count*5
    meow_str = f"Ghost meows {meow_count} times at {enemy_name} dealing {total_damage}!"
    return total_damage, meow_str


def flame_ball(monster, enemy_name):  # Shoots a ball of fire at the enemy dealing 15 damage
    pass


def radiant_light(monster, enemy_name):  # Blinds the enemy, dealing 15 damage and causing their turn to be skipped
    pass


def fire_slash(self, monster, enemy_name):  # Covers the monsters tail in fire and slashes the enemy dealing 15 damage
    pass


def inner_flame(self, monster, enemy_name):
    pass


def wind_blade(self, monster, enemy_name):
    pass


def skill_two(self, monster, enemy_name):
    pass


def skill_one(self, monster, enemy_name):
    pass


def skill_two(self, monster, enemy_name):
    pass


def skill_one(self, monster, enemy_name):
    pass


def skill_two(self, monster, enemy_name):
    pass


def skill_one(self, monster, enemy_name):
    pass


def skill_two(self, monster, enemy_name):
    pass


def skill_one(self, monster, enemy_name):
    pass


def skill_two(self, monster, enemy_name):
    pass


def skill_one(self, monster, enemy_name):
    pass


def skill_two(self, monster, enemy_name):
    pass


def hit(monster_name, monster_attack, enemy_name):
    hit_str = f"{monster_name} hits {enemy_name} for {monster_attack} damage!"
    return monster_attack, hit_str


def guard(*args, monster_name, monster_defense):
    guard_str = f"{monster_name} blocks for {monster_defense}."
    return -monster_defense, guard_str


def gen_one(monster_name, monster_attack, enemy_name):
    hit_str = f"{monster_name} hits {enemy_name.name} for {monster_attack} damage!"
    return monster_attack, hit_str


def gen_two(monster_name, monster_attack, enemy_name):
    hit_str = f"{monster_name} hits {enemy_name.name} for {monster_attack} damage!"
    return monster_attack, hit_str
