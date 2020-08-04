import scipy as s
import scipy.stats
import numpy as n
import matplotlib as m
import csv

# data object containing lists for each major stat category
data = {'fg': [], 'threePt': [], 'margin': []}

# Not totally sure what this does?
confidence = 0.95
n = 5

# m = mean(data)
# std_err = sem(data)
# h = std_err * t.ppf((1 + confidence) / 2, n - 1)
# start = m - h


def calculateConfidence(input):
    m = s.mean(input)
    std_err = s.stats.sem(input)
    h = std_err * s.stats.t.ppf((1 + confidence) / 2, n - 1)
    start = m - h
    print(start)

# Grabs each of these fields from each row of the
# CSV and adds it to its corresponding list
def getData(r):

    data['fg'].append(float(r['FG%']))
    data['threePt'].append(float(r['3pt%']))
    data['margin'].append(float(r['MofV']))


with open('data/UTA5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)
        print(row)

    calculateConfidence(data['fg'])
    calculateConfidence(data['threePt'])
    calculateConfidence(data['margin'])
data = {'fg': [], 'threePt': [], 'margin': []}
print()


with open('data/SAC5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    calculateConfidence(data['fg'])
    calculateConfidence(data['threePt'])
    calculateConfidence(data['margin'])

data = {'fg': [], 'threePt': [], 'margin': []}
print()


with open('data/MIL5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    calculateConfidence(data['fg'])
    calculateConfidence(data['threePt'])
    calculateConfidence(data['margin'])

data = {'fg': [], 'threePt': [], 'margin': []}
print()


with open('data/PHI5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    calculateConfidence(data['fg'])
    calculateConfidence(data['threePt'])
    calculateConfidence(data['margin'])

data = {'fg': [], 'threePt': [], 'margin': []}
print()


with open('data/GSW5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    calculateConfidence(data['fg'])
    calculateConfidence(data['threePt'])
    calculateConfidence(data['margin'])

data = {'fg': [], 'threePt': [], 'margin': []}
print()


with open('data/LAC5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    calculateConfidence(data['fg'])
    calculateConfidence(data['threePt'])
    calculateConfidence(data['margin'])

data = {'fg': [], 'threePt': [], 'margin': []}
print()
