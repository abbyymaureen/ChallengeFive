import pandas as pd

if __name__ == '__main__':
    running = True
    teams = pd.read_csv('Teams.csv')
    institutions_mapping = pd.read_csv('Institutions.csv')

    while running:
        print("\n* * * Statistics Generator * * *\n")
        user_choice = input("1. Average Number of Teams\n2. List of Most Teams\n3. List of Outstanding Winners\n4. "
                            "List of USA Meritorious Winners\n5. Quit\n")

        if user_choice == "1":
            avg_teams = teams.groupby('Institution ID').count().mean()['Team Number']
            print(f"Average number of teams per institution: {avg_teams}")

        elif user_choice == "2":
            # Group the institutions together and then sort by number
            teams_count = teams.groupby('Institution ID').size()
            most_teams = teams_count.sort_values(ascending=False)
            print(most_teams)
            most_teams.to_csv('MostTeams.csv', index=False)

        elif user_choice == "3":
            # Grab only teams with the Outstanding Winner category
            outstanding_teams = teams[teams['Ranking'] == 'Outstanding Winner']
            # Match the institution ID to the institution name
            outstanding_teams_with_institution = pd.merge(outstanding_teams, institutions_mapping, on='Institution ID',
                                                          how='left')
            # Sort the institutions by name
            outstanding_teams_with_institution_sorted = outstanding_teams_with_institution.sort_values(by='Institution Name',
                                                                                                       ascending=True)
            print(outstanding_teams_with_institution_sorted[
                      ['Team Number', 'Ranking', 'Institution Name']])
            outstanding_teams_with_institution_sorted.to_csv('OutstandingTeams.csv', index=False)

        elif user_choice == "4":
            # Get the teams that are ranked Meritorious
            merit = teams[teams['Ranking'] == 'Meritorious']
            # Match the institution IDs to the Institution names
            merit_institution = pd.merge(merit, institutions_mapping, on='Institution ID', how='left')
            # Make sure to get only the USA teams that satisfy this
            usa_teams = merit_institution[merit_institution['Country'] == 'Usa']
            usa_teams_sorted = usa_teams.sort_values(by='Institution Name', ascending=True)
            print(usa_teams_sorted[
                      ['Team Number', 'Advisor', 'Problem', 'Ranking', 'Institution ID', 'Institution Name']])
            usa_teams_sorted.to_csv('USATeams.csv', index=False)

        else:
            print("Thank you for using our services! Goodbye!")
            running = False
