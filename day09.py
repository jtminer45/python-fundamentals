#Day 9 Project — Premier League DataFrame Analysis
import pandas as pd
#What it does: builds a full Premier League player dataset using Pandas and runs a proper analysis on it.
#requirements:

#Create a DataFrame with at least 15 players, columns: name, team, position, goals, assists, minutes_played
data = {
    "name": ["Haaland", "Messi", "Ronaldo", "Mbappe", "Neymar", "Salah", "De Bruyne", "Kane", "Lewandowski", "Son", "Sterling", "Vardy", "Foden", "Mount", "Sancho"],
    "team": ["Man City", "Inter Miami", "Al Nassr", "PSG", "Al Hilal", "Liverpool", "Man City", "Tottenham", "Bayern Munich", "Spurs", "Man City", "Leicester", "Man City", "Chelsea", "Borussia Dortmund"],
    "position": ["Forward", "Forward", "Forward", "Forward", "Forward", "Forward", "Midfielder", "Forward", "Forward", "Forward", "Midfielder", "Forward", "Midfielder", "Forward", "Forward"],
    "goals": [36, 30, 25, 28, 20, 22, 10, 23, 35, 18, 12, 15, 8, 14, 16],
    "assists": [10, 12, 8, 9, 11, 7, 15, 5, 10, 6, 14, 9, 13, 10, 7],
    "minutes_played": [3000, 2800, 2700, 2900, 2500, 2600, 3100, 2400, 2800, 2700, 2500, 2600, 3000, 2800, 2700]        
}

df = pd.DataFrame(data)

#Add a contributions column (goals + assists)
df['contributions'] = df['goals'] + df['assists']
print(f"Total contributions : {df[['name', 'contributions']]}")

#Add a goals_per_90 column (goals divided by minutes played, multiplied by 90)
df['goals_per_90'] = (df['goals'] / df['minutes_played']) * 90
print(f"goals per 90 : {df[['name' , 'goals_per_90']]}")

#Print the full standings sorted by contributions descending
full_standings = df.sort_values("contributions", ascending=False)
print(f"full standings : {full_standings}")

#Print only players with more than 10 goals
players_greater_ten = df[df['goals'] > 10]
print(f"players with goals > 10: {players_greater_ten[['name', 'goals']]}")


#Print the top 3 players by goals_per_90
top_goals = df.nlargest(3, 'goals_per_90')
print(f"Top 3 players by goals per 90: {top_goals[['name', 'goals_per_90']]}")

#Print mean goals, assists, and contributions by position using groupby
print(df.groupby("position")[["goals", "assists", "contributions"]].mean())

#Save the full DataFrame to players.csv
df.to_csv("players.csv", index=False)








