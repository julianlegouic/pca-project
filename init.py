# coding: utf-8

import csv
import os

import numpy as np
import xlrd

# Clean the terminal for more visibility
os.system('clear')
# Ask the user the name of the file
filename = input('Name of the file to use (xls or csv file only):')
# Get the extension of the file
extension = filename[-3:]

# Check if filename exists in the current folder else quit
if (os.path.isfile(filename)):
    print('File found.')
else:
    print('File not found.')
    raise SystemExit

if (extension == 'csv'):
    delim = ''
    while(delim == ''):
        print('Check your csv file delimiter and enter it.')
        try:
            delim = input('Enter the delimiter:')
        except ValueError:
            delim = ''
    # Open the file in read only
    file_r = open(filename, 'r')
    # Retrieve data from csv file in an array
    reader = csv.reader(file_r, delimiter=delim)
    raw_data = []
    # Retrive line by line data from the csv file
    for line in reader:
        raw_data.append(line)
        nbVar = len(raw_data[0]) - 1
        nbInd = len(raw_data) - 1
else:
    # Otherwise, if xls extension open file, retrieve first sheet of the file
    wb = xlrd.open_workbook(filename)
    sheet_name = wb.sheet_names()
    table = wb.sheet_by_name(sheet_name[0])
    # Get the number of variables and individuals
    nbVar = table.ncols - 1
    nbInd = table.nrows - 1

# Ask the user what restitution percentage he whises to use (default is 80%)
ans = input('Use the default restitution percentage (80%)? (y/n)')
if (ans == 'n'):
    percentage = -1
    while(percentage > 100 or percentage <= 0):
        print('Percentage must be between 0 (excluded) and 100.')
        try:
            percentage = float(input('Restitution percentage desired:'))
        except ValueError:
            percentage = -1
else:
    percentage = 80


# Display the number of variables and individuals
def init_info():
    print('Number of variable:', nbVar)
    print('Number of individuals:', nbInd, '\n')


# Retrieve the data from the array into a python dict
def init_data():
    data = np.zeros((nbInd, nbVar))
    var_names, ind_names = [], []
    if (extension == 'xls'):
        for i in range(nbInd):
            ind_names.append(table.cell_value(i+1, 0))
            for j in range(nbVar):
                data[i][j] = float(table.cell_value(i+1, j+1))
                if (i == 0):
                    var_names.append(table.cell_value(i, j+1))
    else:
        for i in range(nbInd):
            ind_names.append(raw_data[i+1][0])
            for j in range(nbVar):
                data[i][j] = float(raw_data[i+1][j+1])
                if (i == 0):
                    var_names.append(raw_data[i][j+1])
    return {'data': data, 'nbVar': nbVar, 'nbInd': nbInd,
            'ind_names': ind_names, 'var_names': var_names,
            'percentage': percentage}


# Display matrices
def display_matrices(*matrix):
    for mat in matrix:
        for i in range(len(mat)):
            print(mat[i][:])
        print('\n')


# Initialize a matrix full of zeroes
def zeros(nbcol=0, nbrow=0):
    if (nbrow == 0):
        return [0 for i in range(nbcol)]
    else:
        return [[0 for i in range(nbcol)] for k in range(nbrow)]
