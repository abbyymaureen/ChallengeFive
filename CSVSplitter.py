import pandas as pd
from difflib import get_close_matches

# * * * Insert the name of your file here * * *
FILE_NAME = '2015.csv'


def correct_spelling(name, known_names):
    # Get the closest match from the list of known names
    closest_match = get_close_matches(name, known_names, n=1, cutoff=0.8)
    if closest_match:
        return closest_match[0]
    else:
        return name


if __name__ == '__main__':
    # Try to read the data from the provided CSV file
    try:
        data = pd.read_csv(FILE_NAME)

        # Get unique known institution names
        known_names = data['Institution'].str.lower().unique()

        print("Processing data...")

        # Correct misspelled institution names
        data['Institution'] = data['Institution'].apply(lambda x: correct_spelling(x.lower(), known_names))

        print("Institution names corrected.")

        # Generate unique Institution IDs
        institution_ids = {institution: i + 1 for i, institution in enumerate(data['Institution'].unique())}

        # Create a DataFrame for institutions
        institutions_df = pd.DataFrame({
            'Institution ID': [institution_ids[institution] for institution in data['Institution'].unique()],
            'Institution Name': data.groupby('Institution').first().reset_index()['Institution'].str.title(),
            'City': data.groupby('Institution').first().reset_index()['City'].str.title(),
            'State/Province': data.groupby('Institution').first().reset_index()['State/Province'].str.title(),
            'Country': data.groupby('Institution').first().reset_index()['Country'].str.title()
        })

        print("Institutions DataFrame created.")

        # Create a DataFrame for teams
        teams_df = pd.DataFrame({
            'Team Number': data['Team Number'],
            'Advisor': data['Advisor'].str.title(),
            'Problem': data['Problem'],
            'Ranking': data['Ranking'].str.title(),
            'Institution ID': [institution_ids[institution] for institution in data['Institution']]
        })

        print("Teams DataFrame created.")

        # Write both DataFrames to a CSV file
        institutions_df.to_csv('Institutions.csv', index=False)
        teams_df.to_csv('Teams.csv', index=False)

        print("Data processing complete.")

    # If the file name isn't found, catch the error and tell the reader
    except FileNotFoundError:
        print(f"The filename, '{FILE_NAME},' was not found. Please try again.")

    # If there is a NameError associated with the columns, catch that too
    except NameError:
        print(f"There was a Name Error associated with your columns. Please try again.")
