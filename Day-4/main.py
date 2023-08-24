import pandas as pd
import matplotlib.pyplot as plt

# Task-1
data = pd.read_excel('IPL.xlsx', index_col=0)
print("Task-1: Player and date of all matches:")
print(data)

# Task-2
player_name = input("Task-2: Enter the player name: ")
if player_name in data.columns:
    player_data = data[player_name]
    total_score = player_data.sum()
    highest_score = player_data.max()
    lowest_score = player_data.min()
    average_score = player_data.mean()

    print(f"Total score of {player_name}: {total_score}")
    print(f"Highest score of {player_name}: {highest_score}")
    print(f"Lowest score of {player_name}: {lowest_score}")
    print(f"Average score of {player_name}: {average_score}")
else:
    print(f"{player_name} not found in the data.")

# Task-3
print("Task-3: Data for all matches:")
for match_number, row in data.iterrows():
    print(f"Match {match_number}:")
    for player, score in row.items():
        print(f"    Score of {player} is {score}")

# Task-4
match_number = int(input("Task-4: Enter the match number: "))
if match_number in data.index:
    match_data = data.loc[match_number]
    highest_score = match_data.max()
    player_with_highest_score = match_data.idxmax()
    print(f"Highest score in Match {match_number}: {highest_score} by {player_with_highest_score}")
else:
    print(f"Match {match_number} not found in the data.")

# Task-5
match_number = (data == 101).any().idxmax()
if match_number is not None:
    print(f"Task-5: Dhawan scored 101 in Match {match_number}.")
else:
    print("Task-5: Dhawan did not score 101 in any match.")

# Task-6
player_name = input("Task-6: Enter the player name to plot the bar graph of match scores: ")
if player_name in data.columns:
    player_data = data[player_name]
    plt.bar(data.index, player_data)
    plt.xlabel('Match Number')
    plt.ylabel('Score')
    plt.title(f"Match Scores of {player_name}")
    plt.show()
else:
    print(f"{player_name} not found in the data.")
