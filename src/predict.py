import scipy as s
import numpy as n
import matplotlib as m
import csv

# data = {}

with open('src/data/test1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    print(type(reader))
    for row in reader:
        print(row)
