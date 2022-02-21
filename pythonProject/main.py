from pathlib import Path

path = Path()
# print(path.glob('*.*')) # gets all files in current directory
for file in path.glob('*'):
    print(file)