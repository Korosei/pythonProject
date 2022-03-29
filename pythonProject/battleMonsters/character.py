import monsters as m
from skills import heal, boost, dagger_throw, flash_bomb


class Character:
    monsters_list = []

    def __init__(self, name):
        self.name = name
        self.monsters_list.append(m.Ghost())
        self.skill_list = ["Heal", "Boost", "Dagger_throw", "Flash_bomb"]

    def use_skill(self, skill, monster):
        if skill in self.skill_list:
            if skill == "heal":
                heal(monster)
            elif skill == "boost":
                boost(monster)
            elif skill == "dagger_throw":
                dagger_throw(monster)
            else:
                return flash_bomb()
        else:
            return False

    def add_monster(self, monster, name):
        monster.name = name
        self.monsters_list.append(monster)

    def get_mlist(self):
        return self.monsters_list

    def get_monster(self, monster):
        return monster in self.monsters_lists
