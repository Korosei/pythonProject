import random


# When you want to return a tuple you dont need to add parentheses. Python does it for you
class Dice:
    def roll(self):
        dice_one, dice_two = random.randint(1, 6), random.randint(1, 6)
        return dice_one, dice_two


dice = Dice()
print(dice.roll())