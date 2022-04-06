import engine as e
import monsters as m
import random as rd
import character as c

m1 = m.Ghost()
m2 = m.RandomMonster()

player = c.Character("Korosei")
player.add_monster(m2)
for monster in player.monsters_list:
    print(monster)