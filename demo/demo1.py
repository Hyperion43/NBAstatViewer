import NBAStats_package.NBAStatLab as nba
import csv
import numpy as np

p = nba.player("Jordan", "Michael")

print(p.lastName)
print(p.firstName)

nba.get_playerstats(p, career = True)

print(np.sum(p.points))


# with open("data/PlayerStatistics.csv", newline="", encoding="utf-8") as f:
#     print(csv.DictReader(f).fieldnames)
    