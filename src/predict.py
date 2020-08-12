import scipy as s
import numpy as num
# import matplotlib as m
import csv
import io
import sys
import warnings
import scipy.stats

# Ignore deprecation warnings
warnings.filterwarnings("ignore")

# Declare some constants: confidence level, array size (number of games), W/L counters
confidence = 0.95
numGames = 5
win = 0
loss = 0
actualWin = 0
actualLoss = 0

# Dictionary of lists containing lists for each major stat category
data = {'fg': [], 'threePt': [], 'margin': []}
utahJazz_means = {'fg': -1, 'threePt': -1, 'margin': -1}
otherTeam_means = {'fg': -1, 'threePt': -1, 'margin': -1}
means = {}


# Calculates the interval based on the array that was given
def calculate_confidence(input):
    m = s.mean(input)
    std_err = s.stats.sem(input)
    h = std_err * s.stats.t.ppf((1 + confidence) / 2, numGames - 1)
    start = m - h
    end = m + h
    print(f'Start: {start}\nEnd: {end}\n\n')


def calculate_mean(input, filename, field):
    global utahJazz_means
    global otherTeam_means

    mean = s.mean(input)
    team = filename.split('5')[0]
    means[f'{team}'] = mean
    print(f'Mean: {means[team]}')
    if team == 'UTA':
        if field == 'fg':
            utahJazz_means['fg'] = mean
        elif field == '3pt':
            utahJazz_means['threePt'] = mean
        elif field == 'margin':
            utahJazz_means['margin'] = mean

    # other team
    else:
        if field == 'fg':
            otherTeam_means['fg'] = mean
        elif field == '3pt':
            otherTeam_means['threePt'] = mean
        elif field == 'margin':
            otherTeam_means['margin'] = mean

    # compare_stats(utahJazz_means, otherTeam_means)


# Take and compare sample mean data for jazz and other
# team and determine winner, MofV being the tie breaker
def compare_stats(utahJazz, otherTeam):
    global win
    global loss

    # if jazz are better at both, we predict a win
    if utahJazz['fg'] > otherTeam['fg'] and utahJazz['threePt'] > otherTeam['threePt']:
        win += 1
        print('\nJazz win\n')
    # if jazz are worse at both, we predict a loss
    elif utahJazz['fg'] < otherTeam['fg'] and utahJazz['threePt'] < otherTeam['threePt']:
        loss += 1
        print('\nJazz lose\n')
    # tie-breaker
    else:
        if utahJazz['margin'] > otherTeam['margin']:
            win += 1
            print('\nJazz win\n')
        else:
            loss += 1
            print('\nJazz lose\n')
            


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
    global utahJazz_means
    global otherTeam_means

    print(f'{filename}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    with open(f'data/{filename}', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

        for row in reader:
            get_data(row)

        # The following function calls
        # print(f'Field Goal Confidence Interval:')
        # calculate_confidence(data["fg"])
        # print(f'Three Point Confidence Interval:')
        # calculate_confidence(data["threePt"])
        # print(f'Margin of Victory Confidence Interval:')
        # calculate_confidence(data["margin"])

        print(f'Field Goal Mean:')
        calculate_mean(data["fg"], filename, 'fg')
        print(f'Three Point Mean:')
        calculate_mean(data["threePt"], filename, '3pt')
        print(f'Margin of Victory Mean:')
        calculate_mean(data["margin"], filename, 'margin')

    compare_stats(utahJazz_means, otherTeam_means)
    data = {'fg': [], 'threePt': [], 'margin': []}
    print('\n')


# Function for disabling stdout, so that calling load_csv_calculate_and_print doesn't print out the contents of the CSV
def disable_print():
    text_trap = io.StringIO()
    sys.stdout = text_trap

# Enables stdout again, so data can be displayed


def enable_print():
    sys.stdout = sys.__stdout__

print('\n')
load_csv_calculate_and_print("UTA5.csv")
load_csv_calculate_and_print("LAC5.csv")
load_csv_calculate_and_print("MIL5.csv")
load_csv_calculate_and_print("SAC5.csv")
load_csv_calculate_and_print("GSW5.csv")

print(f'Jazz predicted record over their next 5 games (W/L): {win}-{loss}\n')

with open(f'data/ACTUAL.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        if row['result'] == 'W':
            actualWin += 1
        elif row['result'] == 'L':
            actualLoss += 1
print(f'Jazz actual record over their next 5 games (W/L): {actualWin}-{actualLoss}\n')
