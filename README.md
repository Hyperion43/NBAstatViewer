# NBAStatLab

A small Python tool for loading NBA player game logs from a CSV file, summarising them, comparing players, and plotting stats.

## Requirements

- Python 3
- `numpy`
- `matplotlib`

```bash
pip install numpy matplotlib
```

## Data setup

Place your game log CSV at:

```
data/PlayerStatistics.csv
```

It needs one row per game, with these columns:

`firstName`, `lastName`, `gameType`, `gameDate`, `points`, `reboundsTotal`, `assists`, `fieldGoalsMade`, `fieldGoalsAttempted`, `threePointersMade`, `threePointersAttempted`

Only seasons from 2015-16 onwards are supported.

## Quick start

```python
from NBAStatLab import player, get_playerstats, stat_summary, stat_compare, stat_plot

# 1. Create a player (first name, last name)
lebron = player("LeBron", "James")

# 2. Load their stats
get_playerstats(lebron, career=True)   # all games since 2015
# get_playerstats(lebron, year=2019)   # or a single year

# 3. Show a summary
stat_summary(lebron)                   # career totals
stat_summary(lebron, avg=True)         # per-game averages
```

## Functions

| Function | What it does |
|---|---|
| `player(firstName, lastName)` | Class that stores a player's name and stat arrays (`points`, `rbs`, `ast`, `fgm`, `fga`, `three_m`, `three_a`). `player.name` gives the full name. |
| `get_playerstats(p, career=False, year=0)` | Reads the CSV and fills in the player's stats, either for their career or for one year (2015 or later). |
| `stat_summary(p, avg=False)` | Prints totals, or per-game averages if `avg=True`. |
| `stat_compare(p1, p2, pts, rbs, ast, totals)` | Prints which of two players leads in each chosen stat. Use `totals=True` for totals, otherwise it compares per-game averages. |
| `stat_plot(stat, label, ylabel, title)` | Scatter plot of a stat array, one dot per game. |

## Examples

Compare two players:

```python
curry = player("Stephen", "Curry")
get_playerstats(curry, career=True)

stat_compare(lebron, curry, pts=True, rbs=True, ast=True)               # per game
stat_compare(lebron, curry, pts=True, rbs=True, ast=True, totals=True)  # totals
```

Plot points per game:

```python
stat_plot(lebron.points, label=lebron.name, ylabel="Points", title="LeBron James: points per game")
```

## Notes and limitations

- Names are matched ignoring case and extra spaces.
- `year` filters by the calendar year of `gameDate` (e.g. `2019`), not by NBA season.
- Regular season, playoff, play-in and NBA Cup games are all included.
- If no player is found, a message is printed and the stat arrays stay empty.