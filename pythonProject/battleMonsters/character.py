import monsters as m
from skills import heal, boost, dagger_throw, flash_bomb


class Character:
    monsters_list = []
    skill_list = ["Heal", "Boost", "Dagger Throw", "Flash Bomb"]

    def __init__(self, name):
        self.name = name
        self.monsters_list.append(m.Ghost())

    def use_skill(self, command, monster):
        if command == 1:
            return heal(self.name, monster)
        elif command == 2:  # returns an int and a string
            return boost(self.name, monster)
        elif command == 3:  # returns an int and a string
            return dagger_throw(self.name, monster)
        else:
            return flash_bomb(self.name, monster)

    def add_monster(self, monster):
        self.monsters_list.append(monster)

    def get_mlist(self):
        fmonster_list = []
        for index, monster in enumerate(self.monsters_list):
            health_points = f"({monster.curr_hp}/{monster.def_hp})"
            append_str = f"{index+1}. {monster.name} {health_points}"
            fmonster_list.append(append_str)

        return fmonster_list
