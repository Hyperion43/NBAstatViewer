import NBAStats_package.NBAStatLab as nba
import csv
import numpy as np

p = nba.player("Curry", "Stephen")

print(p.lastName)
print(p.firstName)

nba.get_playerstats(p, career = True)

nba.stat_summary(p, avg = True)
nba.stat_summary(p)


# with open("data/PlayerStatistics.csv", newline="", encoding="utf-8") as f:
#     print(csv.DictReader(f).fieldnames)
    