import random as rd

def heal(char_name, monster_name):  # Heals current monster to full hp
    print(f"{char_name} heals ")
    pass


def boost(self, monster):  # Raise one monsters' attack and defense by 30 points for 2 turns
    pass


def dagger_throw(self, enemy_name):  # Inflict 25 points of damage to the enemy
    pass


def flash_bomb(self):  # Blinds the enemy causing their turn to be skipped
    pass


def claw_swipe(*args, enemy_name):  # Ghost swipes his claws at the enemy inflicting damage equal to 20 damage
    claw_str = f"Ghost swipes his claws at {enemy_name} for 20 damage!"
    return 20, claw_str


def meow_barrage(*args, enemy_name):  # Ghost meows at the enemy 5-10 times dealing 5 damage each time
    meow_count = rd.randint(5, 11)
    total_damage = meow_count*5
    meow_str = f"Ghost meows {meow_count} times at {enemy_name} dealing {total_damage}!"
    return total_damage, meow_str


def flame_ball(self, monster, enemy_name):  # Shoots a ball of fire at the enemy dealing 15 damage
    pass


def radiant_light(self, monster, enemy_name):  # Blinds the enemy, dealing 15 damage and causing their turn to be skipped
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
