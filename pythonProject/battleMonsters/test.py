import engine as e
import monsters as m

m1 = m.Ghost()
m2 = m.RandomMonster()

dmg, skill_str = e.player_battler(2, m1, m2.name)
print(skill_str)