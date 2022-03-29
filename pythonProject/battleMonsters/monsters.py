import random as rd
import skills as sk

random_name = ["Yaya", "Wirry", "Ohchit", "Studly", "Yoshi", "Tankysan", "Lambo"]
used_names = set()


class BaseMonster:
    name = None
    max_hp = 100
    hp = 100
    mp = 20
    attack = 10
    defense = 5

    def hit(self, enemy_name):
        attack_damage, hit_str = sk.hit(self.name, self.attack, enemy_name)
        return attack_damage, hit_str

    def guard(self, *args):
        damage_dealt, guard_str = sk.guard(monster_name=self.name, monster_defense=self.defense)
        return damage_dealt, guard_str

    def skill_one(self, enemy_name):
        attack_damage, hit_str = sk.hit(self.name, self.attack, enemy_name)
        return attack_damage, hit_str

    def skill_two(self, enemy_name):
        attack_damage, hit_str = sk.hit(self.name, self.attack, enemy_name)
        return attack_damage, hit_str

    def increase_stats(self, diff_modifier):
        self.hp += diff_modifier*10
        self.attack += diff_modifier*3
        self.defense += diff_modifier

    def decrease_stats(self, diff_modifier):
        self.hp = self.max_hp
        self.attack -= diff_modifier*3
        self.defense -= diff_modifier

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp}\nMP: {self.mp}\nAttack: {self.attack}\nDefense: {self.defense}\n"


class RandomMonster(BaseMonster):
    def __init__(self):
        while rd.choice(random_name) in used_names:
            pass
        else:
            self.name = rd.choice(random_name)
            used_names.add(self.name)
        self.max_hp = rd.randint(80, 120)
        self.hp = self.max_hp
        self.mp = 20
        self.attack = rd.randint(10, 15)
        self.defense = rd.randint(4, 8)


class Ghost(BaseMonster):
    name = "Ghost"
    max_hp = 140
    hp = 140
    attack = 15
    defense = 8

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



