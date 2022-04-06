import random as rd
import skills as sk

random_name = ["Yaya", "Wirry", "Ohchit", "Studly", "Yoshi", "Tankysan", "Lambo"]
used_names = set()


class BaseMonster:
    name = None
    def_hp = 100  # default hit points
    def_mp = 20
    def_atk = 10
    def_defense = 5

    def __init__(self):
        self.curr_hp = self.def_hp  # current hit points
        self.curr_mp = self.def_mp
        self.curr_atk = self.def_atk
        self.curr_defense = self.def_defense

    def hit(self, enemy_name):
        attack_damage, hit_str = sk.hit(self.name, self.curr_atk, enemy_name)
        return attack_damage, hit_str

    def guard(self, *args):
        damage_dealt, guard_str = sk.guard(monster_name=self.name, monster_defense=self.curr_defense)
        return damage_dealt, guard_str

    def skill_one(self, enemy_name):
        attack_damage, hit_str = sk.hit(self.name, self.curr_atk, enemy_name)
        return attack_damage, hit_str

    def skill_two(self, enemy_name):
        attack_damage, hit_str = sk.hit(self.name, self.curr_atk, enemy_name)
        return attack_damage, hit_str

    def increase_stats(self, diff_modifier):
        self.curr_hp += diff_modifier*10
        self.curr_atk += diff_modifier*3
        self.curr_defense += diff_modifier

    def decrease_stats(self, diff_modifier):
        self.curr_hp = self.def_hp
        self.curr_atk = self.def_atk
        self.curr_defense = self.def_defense

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.curr_hp}\nMP: {self.curr_mp}\nAttack: {self.curr_atk}\nDefense: " \
               f"{self.curr_defense}\n "


class RandomMonster(BaseMonster):
    def __init__(self):
        while rd.choice(random_name) in used_names:
            pass
        else:
            self.name = rd.choice(random_name)
            used_names.add(self.name)
        self.def_hp = rd.randint(80, 120)
        self.curr_hp = self.def_hp
        self.def_mp = 20
        self.curr_mp = self.def_mp
        self.def_atk = rd.randint(10, 15)
        self.curr_atk = self.def_atk
        self.curr_defense = rd.randint(4, 8)
        self.def_defense = self.curr_defense


class Ghost(BaseMonster):
    name = "Ghost"
    def_hp = 140
    def_mp = 20
    def_atk = 15
    def_defense = 8

    @staticmethod
    def skill_one(enemy_name):
        damage_dealt, claw_str = sk.claw_swipe(enemy_name=enemy_name)
        return damage_dealt, claw_str

    @staticmethod
    def skill_two(enemy_name):
        damage_dealt, meow_str = sk.meow_barrage(enemy_name=enemy_name)
        return damage_dealt, meow_str


class LightFire(BaseMonster):
    name = "LightFire"
    max_hp = 80
    hp = 80
    mp = 20
    attack = 7
    defense = 5


def get_skills(name):
    skills_list = {"Ghost": ["Hit", "Guard", "Claw Swipe", "Meow Barrage"]}

    if name in skills_list:
        return skills_list[name]
    else:
        return ["Hit", "Guard", "Skill_One", "Skill_two"]



