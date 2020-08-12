You must have Python 3.8 installed on your computer in order to run this script.
For instructions on how to accomplish this, visit https://www.python.org/.
For instructions installing pip, visit https://pip.pypa.io/en/stable/installing/.
To install the needed libraries, run "python -m pip install --user numpy scipy matplotlib" from the command line.

How to run the script:
1. Open a Command Window or terminal in the src folder
2. Run "python predict.py" or "python3 predict.py", depending on what version of Python your Python path variable points to. 

This Python script automatically imports the raw data from the src/data folder. 
The CSV files MUST be located in this folder, otherwise the script will not work. 
The CSV files must also be saved without encoding options, as the script does not support encoding.
The script currently only supports a dataset of 5 items, but this can be changed if n is set equal to the number of tiems in a sample or dataset. 

This script can also be further changed to work for data from other teams.

This can be done by doing the following:
1. Obtain the game data for a team of your choosing from https://www.basketball-reference.com/
2. Copy the data for field goals, three pointers, and margin of vitory into a CSV, following the format of the included CSVs (including headers)
3. Edit the following lines of code (lines 145 - 149) and use the names of the CSVs you created:
    `
    load_csv_calculate_and_print("TEAM.csv")
    load_csv_calculate_and_print("FIRSTOPPONENT.csv")
    load_csv_calculate_and_print("SECONDOPPONENT.csv")
    load_csv_calculate_and_print("THIRDOPPONENT.csv")
    load_csv_calculate_and_print("FOURTHOPPONENT.csv")
    load_csv_calculate_and_print("FIFTHOPPONENT.csv")
    `
4. Create another CSV using the actual game data for the next 5 games, following the format of ACTUAL.CSV
    You must track a win or loss using the characters 'W' or 'L', respectively
5. (NOT FULLY SUPPORTED) If you use the data for more than 5 games, you will need to update the following line of code (line 15) accordingly:
    `
    num_games = n
    `
    Where n is the number of games used in the sample

6. Run the script using the above instructions