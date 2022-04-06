import monsters as m
from skills import heal, boost, dagger_throw, flash_bomb


class Character:
    monsters_list = []
    skill_list = ["Heal", "Boost", "Dagger_throw", "Flash_bomb"]

    def __init__(self, name):
        self.name = name
        self.monsters_list.append(m.Ghost())

    def use_skill(self, command, monster_name):
        if command == 1:
            return heal(self.name, monster_name)
        elif command == 2:  # returns an int and a string
            return boost(self.name, monster_name)
        elif command == 3:  # returns an int and a string
            return dagger_throw(self.name, monster_name)
        else:
            return flash_bomb(self.name, monster_name)

    def add_monster(self, monster):
        self.monsters_list.append(monster)

    def get_mlist(self):
        return self.monsters_list

    def get_monster(self, monster):
        return monster in self.monsters_lists
