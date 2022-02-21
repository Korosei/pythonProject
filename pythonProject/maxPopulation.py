# find year that had the biggest population

import random as rd
import heapq as hq

birthYear = [rd.randint(1980, 2020) for _ in range(rd.randint(190, 210))]
deathYear = [rd.randint(1970, 2022) for _ in range(rd.randint(180, 200))]

events = [(year, 1) for year in birthYear] + [(year+1, -1) for year in deathYear]
hq.heapify(events)

currentPop = 0
maxPop = 0
maxYear = None

for event in range(len(events)):
    year, val = hq.heappop(events)
    currentPop += val

    if currentPop > maxPop:
        maxPop = currentPop
        maxYear = year

print(maxYear)