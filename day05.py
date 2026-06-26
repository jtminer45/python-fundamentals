#Day 5 Project — Bulletproof Player Stats System
#Take your Day 4 project and make it unbreakable. This isn't a new project — it's a professional upgrade of what you already built. Real engineering is often improving existing code, not just writing new code.
##Requirements:

#Wrap every int() conversion in proper error handling — bad input never crashes the program
#Handle FileNotFoundError in load_players() and top_scorer() — if the file doesn't exist, print a helpful message instead of crashing
#Add input validation — empty names or positions get rejected with a message

import random

#Function save_player(name, position, goals) — appends a player to players.csv in this format: Saka,Winger,16
def save_player(name, position, goals):
  with open("players.csv", "a") as file:
    file.write(f"{name},{position},{goals}\n")
 

#Function load_players() — reads players.csv, parses each line using split(","), and prints every player neatly
def load_players():
    try: 
      with open("players.csv", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            print(f"Name: {parts[0]} | Position: {parts[1]} | Goals: {parts[2]}")
    except FileNotFoundError:
       print("Sorry mate File doesn't exist but we can create one.")

#Function find_top_scorer() — loads the file, finds and prints the player with the most goals
def top_scorer():
    try:
     with open("players.csv", "r") as file:
        best = None
        for line in file:
            parts = line.strip().split(",")
            if best is None or int(parts[2]) > int(best[2]):
                best = parts
        if best:
          print(f"Top scorer: {best[0]} with {best[2]} goals")
    except FileNotFoundError:
       print("Sorry mate, file not found, but we can create a new one. ")


#Use random module to add a new function random_player() — picks and displays a random player from the file
def random_player():
  try:
   with open("players.csv", "r") as file: 
      players = []
      for line in file:
         parts = line.strip().split(",")
         players.append(parts)
      if players:
         player = random.choice(players)
         print(f"Random Player : {player[0]} | {player[1]} | {player[2]} goals")
      else:
         print("Player not found")
  except FileNotFoundError:
     print("Sorry mate, File not found, but we can create one. ")

#Add option 4 to the menu for random player


while True:
  try:
    menu = input(""" ------- Menu -------
               Option 1: Add Player
               Option 2: Show all players
               Option 3: Top Scorer
               Option 4: Random Player
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
      if not player_name or not player_position or not players_goals:
        print("Sorry mate, all fields required.")
      else: 
        save_player(player_name, player_position, players_goals)

    elif(menu == "2"):
      load_players()

    elif(menu == "3"):
      top_scorer()

    elif (menu == "4"):
       random_player()

  except ValueError:
     print("sorry entered invalid request try again: ")
  
  

