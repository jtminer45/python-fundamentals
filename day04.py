#Day 4 Project — Player Stats Save System
#What it does: lets the user add players and their stats, saves them to a file, and can load them back and display them.
#Requirements:

#Function save_player(name, position, goals) — appends a player to players.csv in this format: Saka,Winger,16
def save_player(name, position, goals):
  with open("players.csv", "a") as file:
    file.write(f"{name},{position}, {goals}\n")

#Function load_players() — reads players.csv, parses each line using split(","), and prints every player neatly
def load_players():
    with open("players.csv", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            print(f"Name: {parts[0]} | Position: {parts[1]} | Goals: {parts[2]}")

#Function find_top_scorer() — loads the file, finds and prints the player with the most goals
def top_scorer():
    with open("players.csv", "r") as file:
        best = None
        for line in file:
            parts = line.strip().split(",")
            if best is None or int(parts[2]) > int(best[2]):
                best = parts
    if best:
        print(f"Top scorer: {best[0]} with {best[2]} goals")
#A while loop menu with 4 options:

while True:
  menu = input(""" ------- Menu -------
               Option 1: Add Player
               Option 2: Show all players
               Option 3: Top Scorer
               Quit : Q

               what you wanna do: 
               """)
  if(menu == "Q"):
    print("thanks see you next time")
    break
  
  elif(menu == "1"):
    player_name = input("player's name: ")
    player_position = input("player's position: ")
    players_goals = input("Player's goals: ")
    save_player(player_name, player_position, players_goals)

  elif(menu == "2"):
    load_players()

  elif(menu == "3"):
    top_scorer()
