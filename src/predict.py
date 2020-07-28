import scipy as s
import numpy as n
import matplotlib as m
import csv

# data = {}

with open('data/Jazz5.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    print(type(reader))
    for row in reader:
        print(row)
