
import numpy as np
import csv 
import matplotlib.pyplot as plt

###
## Class which stores a players name and their statistics
##
###

class player:
    def __init__(self, lastName, firstName):
        self.lastName = lastName
        self.firstName = firstName
        self.points = np.array([])
        self.rbs = np.array([])
        self.ast = np.array([])
        self.fgm = np.array([])
        self.fga = np.array([])
        self.three_m = np.array([])
        self.three_a = np.array([])

@property
def name(self):
    return f"{self.lastName}, {self.firstName}"

def stat_summary(self):
    print("Player:", self.firstName, self.lastName)
    print("Total Points:", np.sum(self.points))
    print("Total Rebounds", np.sum(self.rbs))
    print("Total Assists", np.sum(self.ast))


###
## Function which takes player's surname, name, year etc. and displays their stats
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
        print("Years before the 2015-16 season not available do to github data limits, please select a valid year")
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
        print("Player not found:", self.firstName, self.lastName)

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

    

###
## Function which displays player information, such as position, school which they played,
## teams they played for, etc. for each year of their career 
###
def get_playerinfo():
    return 0

###
## Function which displays team information, such as year founded, year dissolved, 
##
###

###
## Function which displays season information, such as which team won that year, who won
## the MVP award, etc
###








###
## Function which returns all teams' ID's
##
###