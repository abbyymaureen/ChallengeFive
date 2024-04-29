# CSV Splitter & Statistics Generator
This CSV splitter will take any csv following the formatting of the
annual international math competition. The columns for this file should
read as follows:

- `Institution`
- `Team Number`
- `City`
- `State/Province`
- `Country`
- `Advisor`
- `Problem`
- `Ranking`

The program will then take this CSV and split it into 2 separate CSVs,
one for institution information and the other for team information.
This will better normalize the data for database entry.

Institution CSV Columns:
- `Institution ID`
- `Institution Name`
- `City`
- `State/Province`
- `Country`

Teams CSV Columns:
- `Team Number`
- `Advisor`
- `Problem`
- `Ranking`
- `Institution ID`

## Running the Application
1. Install an IDE of your choice

You can choose any Integrated Development Environment (IDE) for Python development. Linked below are our recommendations.
- PyCharm: https://www.jetbrains.com/pycharm/download/?section=mac
- Visual Studio Code: https://code.visualstudio.com/download
- Eclipse: https://www.eclipse.org/downloads/

2. Install Python

If you haven't already installed Python, you can download and install it from the official Python website.
- Python Download Link: https://www.python.org/downloads/

3. Install Pandas and difflib

Pandas can be installed using pip, the Python package installer. Open your command line interface and run the following command:
```
pip install pandas
pip install difflib
```

4. Clone Git Repository

Clone our Git Repository using the following line of code in your terminal:
```
git clone https://github.com/abbyymaureen/ChallengeFive.git
```

5. Open Project in IDE

Once you've cloned the repository, open the project folder in your chosen IDE.

6. Add CSV file

Place the CSV file that you want to split into the same folder as your project files.

7. Replace 'FILE_NAME' variable

In your Python script, replace the 'FILE_NAME' variable with the appropriate path to your CSV file. For example:
```
FILE_NAME = 'your_file.csv'
```

And you are all set! Simply press 'Run' to run our program and start splitting CSVs.
To then use your split CSVs, navigate to the Statistics.py file, then
hit the 'play' button. The program will walk you through how to generate
various statistics and will both save them to a CSV and print the values to the console.