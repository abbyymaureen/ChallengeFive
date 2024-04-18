import pandas as pd

# * * * Insert the name of your file here * * *
FILE_NAME = '2015.csv'

if __name__ == '__main__':
    # Try to read the data from the provided CSV file
    try:
        data = pd.read_csv(FILE_NAME)

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

        # Create a DataFrame for teams
        teams_df = pd.DataFrame({
            'Team Number': data['Team Number'],
            'Advisor': data['Advisor'].str.title(),
            'Problem': data['Problem'],
            'Ranking': data['Ranking'].str.title(),
            'Institution ID': [institution_ids[institution] for institution in data['Institution']]
        })

        # Write DataFrames to CSV files
        institutions_df.to_csv('Institutions.csv', index=False)
        teams_df.to_csv('Teams.csv', index=False)

    # If the file name isn't found, catch the error and tell the reader
    except FileNotFoundError:
        print(f"The filename, '{FILE_NAME},' was not found. Please try again.")

    # If there is a NameError associated with the columns, catch that too
    except NameError:
        print(f"There was a Name Error associated with your columns. Please try again.")
