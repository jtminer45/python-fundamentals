#Day 2 Project — Arsenal Squad Tracker
#What it does: stores Arsenal players as dictionaries inside a list, and uses functions to display and search the squad.

#Create a list of at least 5 players, each a dictionary with name, position, goals

squad = [
  {"name": "Bukayo Saka", "position": "Winger", "goals": 13},
  {"name": "Gabriel Martinelli", "position": "Winger", "goals": 8},
  {"name": "Martin Odegaard", "position": "Midfielder", "goals": 5},
  {"name": "Gabriel Jesus", "position": "Striker", "goals": 6},
  {"name": "William Saliba", "position": "Defender", "goals": 2}
]

#Write a function print_squad() that loops through and prints every player
def print_squad():
    for player in squad:
        print(f"{player['name']} | {player['position']} | {player['goals']} goals")

#Write a function top_scorer() that returns the player with the most goals
def top_scorer():
    best = squad[0]
    for player in squad:
        if player["goals"] > best["goals"]:
            best = player
    return best
#Write a function find_player(name) that searches by name and prints their info, or prints "Player not found" if they don't exist
def find_player(name):
    for player in squad:
        if player["name"].lower() == name.lower():
            print(f"Name: {player['name']} | Position: {player['position']} | Goals: {player['goals']}")
            return
    print("Player not found")

print("---- Arsenal Squad ----")
print_squad()

best = top_scorer()
print(f"\nTop scorer: {best['name']} with {best['goals']} goals")

name = input("\nSearch for a player: ")
find_player(name)