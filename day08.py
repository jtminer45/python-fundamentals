import numpy as np
#Day 8 Project — Premier League Stats Analyser
#what it does: uses NumPy to analyse Premier League player stats — no CSVs, no Pandas yet, pure NumPy.
#Requirements:

players = ["Haaland", "Messi", "Ronaldo", "Mbappe", "Neymar", "Lewandowski", "Kane", "Salah", "De Bruyne", "Modric"]

#create a NumPy array of player goals for 10 players
goals = np.array([36, 30, 25, 28, 20, 35, 23, 22, 18, 15])

#create a NumPy array of player assists for the same 10 players
assists = np.array([12, 10, 3, 4, 7, 5, 12, 3, 1, 18])

#Calculate and print:

#Mean goals and assists
print(f"Mean goals: {np.mean(goals):.2f}")
print(f"Mean assists: {np.mean(assists):.2f}")

#Top scorer index and their goals
top_index = np.argmax(goals)
print(f"Top scorer: {players[top_index]} with {goals[top_index]} goals")

#Total goal contributions (goals + assists) per player
# Total goal contributions
contributions = goals + assists
for i in range(len(players)):
    print(f"{players[i]}: {contributions[i]} contributions")

# Standard deviation
print(f"Standard deviation of goals: {np.std(goals):.2f}")


#Players who scored above the mean (boolean indexing)
mean = np.mean(goals)
above_mean = [players[i] for i in range(len(players)) if goals[i] > mean]
print(f"Players above mean: {above_mean}")


#Create a 2D array combining goals and assists into one matrix (shape should be 2×10)
combo = np.vstack([goals, assists])

#Print the goals row and assists row separately using 2D indexing
print(f"Goals row: {combo[0, :]}")    # entire row 0 = all goals
print(f"Assists row: {combo[1, :]}")  # entire row 1 = all assists


