import scipy as s
import numpy as n
import matplotlib as m
import csv
import io
import sys
import warnings
import scipy.stats

# Ignore deprecation warnings
warnings.filterwarnings("ignore")

# Dictionary of lists containing lists for each major stat category
data = {'fg': [], 'threePt': [], 'margin': []}

# Declare some constants: confidence level, array size (number of games)
confidence = 0.95
numGames = 5


# Calculates the interval based on the array that was given
def calculate_confidence(input):
    m = s.mean(input)
    std_err = s.stats.sem(input)
    h = std_err * s.stats.t.ppf((1 + confidence) / 2, numGames - 1)
    start = m - h
    end = m + h
    print(f'Start: {start}\nEnd: {end}\n\n')


# Grabs each of these fields from each row of the
# CSV and adds it to its corresponding list
def get_data(r):

    data['fg'].append(float(r['FG%']))
    data['threePt'].append(float(r['3pt%']))
    data['margin'].append(float(r['MofV']))


# Opens the CSV with the given filename, then iterates through it, grabbing the neccessary data from each row
# Then calls the calculate_confidence function to calculate the interval
def load_csv_calculate_and_print(filename):
    global data
    print(f'{filename}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    disable_print()
    with open(f'data/{filename}', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

        for row in reader:
            get_data(row)
            print(row)

        enable_print()
        print(f'Field Goal Confidence Interval:')
        calculate_confidence(data["fg"])
        print(f'Three Point Confidence Interval:')
        calculate_confidence(data["threePt"])
        print(f'Margin of Victory Confidence Interval:')
        calculate_confidence(data["margin"])
    data = {'fg': [], 'threePt': [], 'margin': []}


# Function for disabling stdout, so that calling load_csv_calculate_and_print doesn't print out the contents of the CSV
def disable_print():
    text_trap = io.StringIO()
    sys.stdout = text_trap


# Enables stdout again, so data can be displayed
def enable_print():
    sys.stdout = sys.__stdout__


load_csv_calculate_and_print("UTA5.csv")
load_csv_calculate_and_print("GSW5.csv")
load_csv_calculate_and_print("UTA5.csv")
load_csv_calculate_and_print("GSW5.csv")
load_csv_calculate_and_print("GSW5.csv")
