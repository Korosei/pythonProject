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
        self.hp = self.def_hp  # current hit points
        self.mp = self.def_mp
        self.atk = self.def_atk
        self.defense = self.def_defense

    def hit(self, enemy):
        attack_damage, hit_str = sk.hit(self, enemy)
        return attack_damage, hit_str

    def guard(self, *args):
        damage_dealt, guard_str = sk.guard(monster=self)
        return damage_dealt, guard_str

    def reset_stats(self):
        self.hp = self.def_hp
        self.mp = self.def_mp
        self.atk = self.def_atk
        self.defense = self.def_defense

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp}\nMP: {self.mp}\nAttack: {self.atk}\nDefense: " \
               f"{self.defense}\n"


class RandomMonster(BaseMonster):
    def __init__(self):
        """The following 6 lines of code removes random monsters with the same name to appear one after another.
           This is just a design choice and has no actual effect on the game."""
        rd_index = rd.randint(0, len(random_name)-1)
        self.name = random_name[rd_index]
        used_names.add(random_name.pop(rd_index))

        if len(random_name) == 0:
            for num in range(len(used_names)):
                random_name.append(used_names.pop())

        self.def_hp = rd.randint(80, 120)
        self.hp = self.def_hp
        self.def_mp = 20
        self.mp = self.def_mp
        self.def_atk = rd.randint(10, 15)
        self.atk = self.def_atk
        self.def_defense = rd.randint(4, 8)
        self.defense = self.def_defense
        self.one_name, self.sk_one = sk.rd_skill(1)
        self.two_name, self.sk_two = sk.rd_skill(2)

    def increase_stats(self, diff_modifier):
        self.hp += diff_modifier * 10
        self.mp += diff_modifier * 5
        self.atk += diff_modifier * 3
        self.defense += diff_modifier

    def skill_one(self, enemy):
        self.mp -= 5
        damage_dealt, one_str = self.sk_one(monster=self, enemy=enemy)
        return damage_dealt, one_str

    def skill_two(self, enemy):
        self.mp -= 15
        damage_dealt, two_str = self.sk_two(monster=self, enemy=enemy)
        return damage_dealt, two_str

    def skills_list(self):
        return ["Hit", "Guard", self.one_name, self.two_name]


class Ghost(BaseMonster):
    name = "Ghost"
    def_hp = 140
    def_mp = 20
    def_atk = 15
    def_defense = 8

    def skill_one(self, enemy):
        self.mp -= 5
        damage_dealt, claw_str = sk.claw_swipe(enemy=enemy)
        return damage_dealt, claw_str

    def skill_two(self, enemy):
        self.mp -= 15
        damage_dealt, meow_str = sk.meow_barrage(enemy=enemy)
        return damage_dealt, meow_str

    @staticmethod
    def skills_list(*args):
        return ["Hit", "Guard", "Claw Swipe", "Meow Barrage"]



