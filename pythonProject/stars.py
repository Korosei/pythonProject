numbers = [5, 2, 5, 2, 2]

for i in numbers:
    for u in range(i):
        print('x', end="")
    print()

print()
for i in numbers:
    print('x' * i)
