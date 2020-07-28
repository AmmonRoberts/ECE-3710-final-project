import scipy as s
import numpy as n
import matplotlib as m
import csv

global fg
global threePt
global margin
fg = []
threePt = []
margin = []

confidence = 0.95
n = 5

# m = mean(data)
# std_err = sem(data)
# h = std_err * t.ppf((1 + confidence) / 2, n - 1)
# start = m - h


def calculateConfidence(input):
    m = s.mean(data)


def getData(r):
    fg.append(r['FG %'])
    threePt.append(r['3pt %'])
    margin.append(r['MofV'])


def clearLists():
    print('heck')
    fg = []
    threePt = []
    margin = []
    print(margin)


with open('data/UTA5.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)
        # print(row['FG %'])
    print(margin)
    clearLists()
    print(margin)


# with open('data/SAC5.csv', newline='', encoding='utf8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

#     for row in reader:
#         print(row)


# with open('data/MIL5.csv', newline='', encoding='utf8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

#     for row in reader:
#         print(row)


# with open('data/PHI5.csv', newline='', encoding='utf8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

#     for row in reader:
#         print(row)


# with open('data/GSW5.csv', newline='', encoding='utf8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

#     for row in reader:
#         print(row)


# with open('data/LAC5.csv', newline='', encoding='utf8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

#     for row in reader:
#         print(row)
