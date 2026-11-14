#Eli Baker
#Level 10 assignment: Team stats

import pandas

team_data = pandas.read_csv("cfb.csv")

#Ask user what season they want
season = input("Enter a season to analyze: ")

#Use the season to find right rows
season_data = team_data[team_data["Season"].astype(str) == season]

#Check for correct user input
if season_data.empty:
    print("That season was not found.")
else:
    
#Create Keys
    categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

    for index, row in season_data.iterrows():
        team = row["Team"]
        wins = row["Win"]

#Examine and add rows to list
        if wins >= 10:
            categories["10 or more wins"].append(team)
        elif wins >= 8:
            categories["8-9 wins"].append(team)
        elif wins >= 6:
            categories["6-7 wins"].append(team)
        else:
            categories["Fewer than 6 wins"].append(team)

#Print results
    print(f"College Football Results for {season}")

    for category, teams in categories.items():
        print(f"{category}:")

        for team in teams:
            print(team)