import pandas as pd
import streamlit as st

# Load the dataset
file_path = "C:/Users/lukeh/Downloads/slothstatsdata.csv"
data = pd.read_csv(file_path)

# Extract unique team names
team_names = data['teamName'].dropna().unique()

# Select 6 teams randomly for the grid
import random
random_teams = random.sample(list(team_names), 6)

# Create a dictionary of players and their associated teams
player_teams = data.groupby('name')['teamName'].apply(set).to_dict()

# Initialize the game grid
grid_size = 3
horizontal_teams = random_teams[:grid_size]
vertical_teams = random_teams[grid_size:]

st.title("Fantasy Football Immaculate Grid")

for i in range(grid_size + 1):
    cols = st.columns(grid_size + 1)
    for j in range(grid_size + 1):
        if i == 0 and j == 0:
            cols[j].write("")
        elif i == 0:
            cols[j].write(f"**{horizontal_teams[j - 1]}**")
        elif j == 0:
            cols[j].write(f"**{vertical_teams[i - 1]}**")
        else:
            input_name = cols[j].text_input(f"Row {i} Col {j}", "")
            if st.button(f"Check Row {i} Col {j}"):
                team_1 = horizontal_teams[j - 1]
                team_2 = vertical_teams[i - 1]
                input_name_lower = input_name.strip().lower()

                if input_name_lower in player_teams:
                    player_teams_set = player_teams[input_name_lower]
                    if team_1 in player_teams_set and team_2 in player_teams_set:
                        cols[j].write("✅ Correct!")
                    else:
                        cols[j].write("❌ Incorrect!")
                else:
                    cols[j].write("❌ Incorrect!")
