import random

'''
for i in range(3):
    print(random.randint(10,20))

members = ['John', 'Mary', 'Kareem', 'Claudia']
leader = random.choice(members)
print(leader)
'''

dice_one, dice_two = random.randint(1, 6), random.randint(1, 6)
print(f'({dice_one}, {dice_two})')