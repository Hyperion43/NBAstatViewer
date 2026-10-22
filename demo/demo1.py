import NBAStats_package.NBAStatLab as nba
import csv

# Create an object for players we want to take a look at
p = nba.player("Stephen", "Curry")
p2 = nba.player("Kyrie", "Irving")

# Print their names
print(p.name)
print(p2.name)

# Fetch their statistics for processing
# Can do a specific year or over their whole career
nba.get_playerstats(p, year = 2015)
nba.get_playerstats(p2, year = 2015)

nba.get_playerstats(p, career = True)
nba.get_playerstats(p2, career = True)

# Summarize their stats, either on average (per game) or total
nba.stat_summary(p, avg = True)
nba.stat_summary(p)

nba.stat_summary(p2, avg = True)
nba.stat_summary(p2)

# Compare their stats, including points, assists, or rebounds, or all three (either totals, if totals == True, or averages if totals == False)
nba.stat_compare(p, p2, pts = True, rbs = True, ast = True, totals = False)

# plot a scatter plot of a player's statistics
nba.stat_plot(p.points, label = "Steph Curry Points Over Time", ylabel = "Points", frame = "By Game")
    