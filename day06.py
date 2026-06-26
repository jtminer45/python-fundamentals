#Day 6 Project — Football Club OOP System
#What it does: models a football club using proper OOP — players, a goalkeeper, and a team, all as classes.
#Requirements:

#Player class with name, position, goals — methods: describe(), score()
class Player: 
  def __init__(self, name, position, goals):
    self.name = name
    self.position = position
    self.goals = goals

  def describe(self):
    print(f"{self.name} is a {self.position} with {self.goals} goals.")

  def score(self):
    self.goals += 1
    print(f"{self.name} scored! Total goals: {self.goals}")

#GoalKeeper class that inherits from Player with clean_sheets — methods: override describe(), save() increments clean sheets 
class Goalkeeper (Player):
  def __init__(self, name, clean_sheets):
    super().__init__(name, "Goalkeeper", 0)
    self.clean_sheets = clean_sheets

  def describe(self):
    print(f"{self.name} is a Goalkeeper with {self.clean_sheets} clean sheets.")
  
  def save(self):
    self.clean_sheets += 1
    print(f"{self.name} saved a goal! Total clean sheets: {self.clean_sheets}")
  
#Team class with name, players (a list) — methods:
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_squad(self):
        print(f"\n---- {self.name} ----")
        for player in self.players:
            player.describe()

    def top_scorer(self):
        best = None
        for player in self.players:
            if best is None or player.goals > best.goals:
                best = player
        if best:
            print(f"\nTop scorer: {best.name} with {best.goals} goals")

    def table_standing(self, points):
        print(f"{self.name} | Points: {points}")

  
saka = Player("Bukayo Saka", "Winger", 16)
jesus = Player("Gabriel Jesus", "Striker", 8)
raya = Goalkeeper("David Raya", 14)

arsenal = Team("Arsenal")
arsenal.add_player(saka)
arsenal.add_player(jesus)
arsenal.add_player(raya)

arsenal.show_squad()
arsenal.top_scorer()
arsenal.table_standing(75)
