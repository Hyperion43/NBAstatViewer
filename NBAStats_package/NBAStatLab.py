
import numpy as np
import csv 
import matplotlib.pyplot as plt

###
## Class which stores a players name and their statistics
##
###

class player:
    def __init__(self, firstName, lastName):
        self.lastName = lastName
        self.firstName = firstName
        self.totalgms = np.array([])
        self.points = np.array([])
        self.rbs = np.array([])
        self.ast = np.array([])
        self.fgm = np.array([])
        self.fga = np.array([])
        self.three_m = np.array([])
        self.three_a = np.array([])

    @property
    def name(self):
        return f"{self.firstName} {self.lastName}"

        

###
## Function which displays a summary of a players' statistics
##
###

def stat_summary(self, avg = False):
    if avg == True:
        print("Player:", self.name)
        print("Total Games: ", self.totalgms)
        print(f"Points per Game: {np.mean(self.points):.2f}")
        print(f"Rebounds per Game: {np.mean(self.rbs):.2f}")
        print(f"Assists per Game: {np.mean(self.ast):.2f}")
        print(f"Three Pointers Made per Game: {np.mean(self.three_m):.2f}")
        print(f"Three Pointers Attempted per Game: {np.mean(self.three_a):.2f}")
        print(f"Three Point Pct: {((np.mean(self.three_m) / np.mean(self.three_a)) * 100):.2f}%")
    else:
        print("Player:", self.name)
        print("Total Games", self.totalgms)
        print("Total Points:", np.sum(self.points))
        print("Total Rebounds:", np.sum(self.rbs))
        print("Total Assists:", np.sum(self.ast))
        print(f"Three Pointers Made: {np.sum(self.three_m):.2f}")
        print(f"Three Pointers Attempted: {np.sum(self.three_a):.2f}")
        print(f"Three Point Pct: {((np.mean(self.three_m) / np.mean(self.three_a)) * 100):.2f}%")



###
## Function which takes player's surname, name, year etc. and fetches their stats
## for that year, or for their career, depending on inputs
###
def get_playerstats(self, career = False, 
                    year = 0, yearsBetween = (0, 0)):
    ####
    ### career == true will return career totals and averages
    ### if year is specified then totals and averages for that specific year will be given
    ### yearsbetweeen will give a range of years for which stats will be displayed e.g. (2004, 2007)
    ### 
    ### Stats displayed will be Points, Assists, Total Rebounds, Blocks, Steals, Minutes, ORebounds, DRebounds, 
    ### field goals made, attempted, etc.
    ####

    if year != 0 and year < 2015:
        print("Years before the 2015-16 season not available due to github data limits, please select a valid year")
        return 0

    with open ("data/PlayerStatistics.csv", newline = "", encoding = "utf-8") as f:
        rows = np.array([
            r for r in csv.DictReader(f)
            if r["firstName"].strip().lower() == self.firstName.strip().lower()
            and r["lastName"].strip().lower() == self.lastName.strip().lower()
            and (r["gameType"].strip().lower() == "Regular Season".strip().lower()
                or r["gameType"].strip().lower() == "Playoffs".strip().lower()
                or r["gameType"].strip().lower() == "In-Season-Knockout".strip().lower()
                or r["gameType"].strip().lower() == "Play-In Tournament".strip().lower()
                or r["gameType"].strip().lower() == "NBA cup".strip().lower()
                or r["gameType"].strip().lower() == "NBA Emirates Cup".strip().lower()
                or r["gameType"].strip().lower() == "Emirates NBA cup".strip().lower()
                )
            and r["gameType"].strip().lower() != ""
        ])

    if len(rows) == 0:
        print("Player not found:", self.name)

    pts, rb, ast, fgm, fga, three_a, three_m = [], [], [], [], [], [], []

    if career:
        for row in rows:
            pts.append(float(row["points"]))
            rb.append(float(row["reboundsTotal"]))
            ast.append(float(row["assists"]))
            fgm.append(float(row["fieldGoalsMade"]))
            fga.append(float(row["fieldGoalsAttempted"]))
            three_a.append(float(row["threePointersAttempted"]))
            three_m.append(float(row["threePointersMade"]))
        self.points = np.array(pts)
        self.rbs = np.array(rb)
        self.ast = np.array(ast)
        self.fgm = np.array(fgm)
        self.fga = np.array(fga)
        self.rbs = np.array(rb)
        self.three_m = np.array(three_m)
        self.three_a = np.array(three_a)
        self.totalgms = len(self.points)
        print(f"Got stats for {self.name} for his career since 2015")
        return

    if year > 2014:
        for row in rows:
            if row["gameDate"][:4] == str(year):
                pts.append(float(row["points"]))
                rb.append(float(row["reboundsTotal"]))
                ast.append(float(row["assists"]))
                fgm.append(float(row["fieldGoalsMade"]))
                fga.append(float(row["fieldGoalsAttempted"]))
                three_a.append(float(row["threePointersAttempted"]))
                three_m.append(float(row["threePointersMade"]))
                self.points = np.array(pts)
        self.rbs = np.array(rb)
        self.ast = np.array(ast)
        self.fgm = np.array(fgm)
        self.fga = np.array(fga)
        self.rbs = np.array(rb)
        self.three_m = np.array(three_m)
        self.three_a = np.array(three_a)
        self.totalgms = len(self.points)
        print(f"Got stats for {self.name} for {year}")
        return 

###
## Function which compares the stats of two players
##
###

def stat_compare(p1, p2, pts = False, rbs = False, ast = False, totals = False):
    if totals == True:
        if pts == True:
            high = np.maximum(int(np.sum(p1.points)), int(np.sum(p2.points)))
            if high == int(np.sum(p1.points)):
                print(f"The player with the most points was {p1.name} with a total of {high} points")
            else:
                print(f"The player with the most points was {p2.name} with a total of {high} points")
            

        if rbs == True:
            high = np.maximum(int(np.sum(p1.rbs)), int(np.sum(p2.rbs)))
            if high == int(np.sum(p1.rbs)):
                print(f"The player with the most rebounds was {p1.name} with a total of {high} rebounds")
            else:
                print(f"The player with the most rebounds was {p2.name} with a total of {high} rebounds")

        if ast == True:
            high = np.maximum(int(np.sum(p1.ast)), int(np.sum(p2.ast)))
            if high == int(np.sum(p1.ast)):
                print(f"The player with the most assists was {p1.name} with a total of {high} assists")
            else:
                print(f"The player with the most assists was {p2.name} with a total of {high} assists")
    else:
        high = np.maximum(np.mean(p1.points), np.mean(p2.points))
        if high == np.mean(p1.points):
            print(f"The player with the most PPG was {p1.name} with a PPG of {high:.2f} points")
        else:
            print(f"The player with the most PPG was {p2.name} with a PPG of {high:.2f} points")
                    
        
        if rbs == True:
            high = np.maximum(np.mean(p1.rbs), np.mean(p2.rbs))
            if high == np.mean(p1.rbs):
                print(f"The player with the most Rb/game was {p1.name} with a total of {high:.2f} rebounds")
            else:
                print(f"The player with the most Rb/game was {p2.name} with a total of {high:.2f} rebounds")
        
        if ast == True:
            high = np.maximum(np.mean(p1.ast), np.mean(p2.ast))
            if high == np.mean(p1.ast):
                print(f"The player with the most assists/game was {p1.name} with a total of {high:.2f} assists")
            else:
                print(f"The player with the most assists/game was {p2.name} with a total of {high:.2f} assists")            
    return

def stat_plot(stat, label, ylabel = "Value", title = None):
    games = np.arange(1, len(stat) + 1)
    
    plt.figure(figsize = (50, 10))
    plt.scatter(games, stat, label = label, color = 'grey')
    plt.grid(True)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlabel("Game")
    plt.show()
    
    return