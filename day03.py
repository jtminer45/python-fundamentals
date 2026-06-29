#Day 3 Project — Premier League Search Engine
#What it does: stores multiple teams with their players and stats, lets the user search by team or player name.
#Requirements:

#At least 4 teams, each with points, position, and a list of players (each player has name and goals)
premier_league ={
  "Arsenal": {
    "position": 1, 
    "points": 75, 
    "players": [
      {"name": "Bukayo Saka", "goals": 13},
      {"name": "Gabriel Martinelli", "goals": 8},
      {"name": "Martin Odegaard", "goals": 5}
    ]
  },
  "Manchester City": {
    "position": 2,
    "points": 70, 
    "players": [
      {"name": "Erling Haaland", "goals": 20},
      {"name": "Phil Foden", "goals": 10},
      {"name": "Kevin De Bruyne", "goals": 5}
    ]
  },
  "Liverpool": {
    "position": 3,
    "points": 65, 
    "players": [
      {"name": "Mohamed Salah", "goals": 15},
      {"name": "Darwin Nunez", "goals": 12},
      {"name": "Trent Alexander-Arnold", "goals": 3}          
    ]
  },

"Aston Villa": {
  "position": 4,
  "points": 60,
  "players": [
    {"name": "Ollie Watkins", "goals": 10},     
    {"name": "Emiliano Buendia", "goals": 5},
    {"name": "Leon Bailey", "goals": 3} 
  ]
}
}

#Function show_table() — prints all teams ordered by position with their points
def show_table():
  for team_name, team_info in premier_league.items():
    print(f"{team_name} | position: {team_info['position']} | points: {team_info['points']}")

#Function find_team(name) — prints a team's info and all their players
def find_team(name):
  for team_name, team_info in premier_league.items():
    if team_name.lower() == name.lower():
      print(f"{team_name} | position: {team_info['position']} | points: {team_info['points']}")
      print("Players:")
      for player in team_info['players']:
        print(f"  - {player['name']}: {player['goals']} goals")
      return
  print(f"Team does not exist")

#Function find_player(name) — searches across all teams, prints the player and which team they're at

def find_player(name):
  for team_name, team_info in premier_league.items():
    for player in team_info['players']:
      if player['name'].lower() == name.lower():
        print(f"{player['name']} | {team_name}")
        return
  print(f"Player does not exist")

#A menu that keeps running until the user types quit
while True:
    menu = input("""\n------ Menu -----
1 - Show table
2 - Find team
3 - Find player
q - Quit

Enter option: """)

    if menu == "q":
        print("Goodbye!")
        break
    elif menu == "1":
        show_table()
    elif menu == "2":
        team_name = input("Enter team name: ")
        find_team(team_name)
    elif menu == "3":
        player_name = input("Enter player name: ")
        find_player(player_name)
    else:
        print("Invalid option, try again")