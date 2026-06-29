#The Project — Football League Management System
#This is everything from week 1 combined into one real program.
#What it does: manages a full football league — teams, players, standings, and stats — saved to a file so data persists.
#Requirements:
#OOP:

#Player class — name, position, goals, methods: describe(), score()
class Player:
  def __init__(self, name, position, goals):
    self.name = name
    self.position = position 
    self.goals = goals

  def describe(self):
    print(f"{self.name} I play {self.position} and I have {self.goals} goals")
  
  def score(self):
    self.goals += 1
    print(f"Well that's a goal for {self.name} , Total goals is {self.goals}")
    
#Team class — name, players list, points, methods: add_player(), show_squad(), top_scorer(), add_points(n)
class Team:
  def __init__(self, name):
    self.name = name
    self.players_list = []
    self.points = 0  

  def add_player(self, player):
    self.players_list.append(player) 

  def show_squad(self):
    print(f"------ {self.name} ------")
    for player in self.players_list:
      player.describe()

  def top_scorer(self):
    best = None
    for player in self.players_list:
      if best is None or player.goals > best.goals:
        best = player
    if best:
      print(f"{best.name} is highest goal scorer with {best.goals} goals")

  def add_points(self, n):
    self.points += n


#League class — name, teams list, methods: add_team(), show_standings() sorted by points, top_scorer() across all teams
class League:
  def __init__(self, name):
    self.name = name
    self.team_list = []

  def add_team(self, team):
    self.team_list.append(team)
  
  def show_standings(self):
    print(f"------ {self.name} Standings ------")
    sorted_teams = sorted(self.team_list, key=lambda x: x.points, reverse=True)
    for team in sorted_teams:
        print(f"{team.name} | Points: {team.points}")

  def top_scorer(self):
    best = None
    for team in self.team_list:
      for player in team.players_list:
        if best is None or player.goals > best.goals:
          best = player
    if best:
      print(f"{best.name} is the top scorer across all teams with {best.goals} goals")
    

    

#File I/O:
#Error handling:

#No crashes on bad input anywhere
#FileNotFoundError handled on load

#save_league(league) — saves all teams and players to league.csv
def save_league(league):
    with open("league.csv", "w") as file:
        file.write(f"{league.name}\n")
        for team in league.team_list:
            file.write(f"TEAM,{team.name},{team.points}\n")
            for player in team.players_list:
                file.write(f"PLAYER,{player.name},{player.position},{player.goals}\n")
 

#load_league() — loads and reconstructs the league from league.csv
def load_league():
    try:
        with open("league.csv", "r") as file:
            lines = file.readlines()
            league = League(lines[0].strip())
            current_team = None
            for line in lines[1:]:
                parts = line.strip().split(",")
                if parts[0] == "TEAM":
                    current_team = Team(parts[1])
                    current_team.points = int(parts[2])
                    league.add_team(current_team)
                elif parts[0] == "PLAYER" and current_team:
                    player = Player(parts[1], parts[2], int(parts[3]))
                    current_team.add_player(player)
        return league
    except FileNotFoundError:
        print("File not found.")
        return None

print(f"""----Welcome to the Football League Management System----
      1 - Show Standings
      2 - Show Team Squad
      3 - Add goal to player
      4 - Save League
      5 - Load League
      6 - Add Player to Team
      7 - Add Team
      Q - Quit 
    """)

league = League("Premier League")
while True:
  try:
    choice = input("Enter your choice (1-7 or Q to quit): ")
    if choice == "1":
      league.show_standings()
    elif choice == "2":
      team_name = input("Enter Team name: ")
      team = next((t for t in league.team_list if t.name == team_name), None)
      if team:
        team.show_squad()
      else:
        print("Team not found.")
    elif choice == "3":
      team_name = input("Enter Team name: ")
      team = next((t for t in league.team_list if t.name == team_name), None)
      if team:
        player_name = input("Enter Player name: ")
        player = next((p for p in team.players_list if p.name == player_name), None)
        if player:
          player.score()
        else:
          print("Player not found.")
      else:
        print("Team not found.")
    elif choice == "4":
      save_league(league)
      print("League saved.")
    elif choice == "5":
      league = load_league()
      if league:
        print("League loaded.")
    elif choice == "6":
      team_name = input("Enter team name: ")
      team = next((t for t in league.team_list if t.name == team_name), None)
      if team:
        player_name = input("Player name: ")
        player_position = input("Player position: ")
        try:
          player_goals = int(input("Player goals: "))
        except ValueError:
          print("Goals must be a number")
          continue
        team.add_player(Player(player_name, player_position, player_goals))
        print(f"{player_name} added to {team.name}")
      else:
        print("Team not found.")
    elif choice == "7":
      team_name = input("Enter new team name: ")
      try:
        team_points = int(input("Enter team points: "))
      except ValueError:
        print("Points must be a number")
        continue
      new_team = Team(team_name)
      new_team.add_points(team_points)
      league.add_team(new_team)
      print(f"{team_name} with {team_points} points added to the league")
    elif choice.upper() == "Q":
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")
  except Exception as e:
    print(f"An error occurred: {e}")
  finally:
    print("Loading complete.....")