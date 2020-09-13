# coding: utf-8

import math

from init import *


# Compute the mean value of a given column from a matrix
def mean(matrix, size, numC):
    total_sum = 0
    for i in range(size):
        total_sum += matrix[i][numC]
    return (total_sum / size)


# Comute the distance of a point from its origin
def distance(coord_indiv):
    dist = 0
    for i in coord_indiv:
        dist += i**2
    return math.sqrt(dist)


# Comute the standard deviation
def std(matrix, numC):
    total_sum = 0
    size = len(matrix)
    mean_value = mean(matrix, size, numC)
    for i in range(size):
        total_sum += ((matrix[i][numC] - mean_value)**2) / size
    return math.sqrt(total_sum)


# Compute the covariance product
def covariance(matrix, matrix2, X, Y):
    total_sum = 0
    size = len(matrix)
    mean1 = mean(matrix, size, X)
    mean2 = mean(matrix, size, Y)
    for i in range(size):
        total_sum += (matrix[i][X] - mean1) * (matrix2[i][Y] - mean2)
    return (total_sum / size)


# Compute the correlation product
def correlation(vec1, vec2, i=0, j=0):
    std1 = std(vec1, i)
    std2 = std(vec2, j)
    return covariance(vec1, vec2, i, j) / (std1*std2)


# Determine the number of necessary dimensions to obtain a restitution
# percentage stricly superior to the desired percentage
def dimensions(list_eigenVal, percentage):
    nb_ev = len(list_eigenVal)
    list_pct = [round((ev / nb_ev) * 100, 3) for ev in list_eigenVal]
    print('List of respective percentages:', list_pct)
    sum_eigenVal = 0
    num_dim = 0
    while(sum_eigenVal < percentage):
        sum_eigenVal += list_pct[num_dim]
        num_dim += 1
    print('\nRestitution percentage obtained: {}%'.format(
        str(round(sum_eigenVal, 3))))
    return (num_dim, list_pct)


# Get the coordinates of each individuals on each axis
def coord_ind(result_data):
    nbInd, nbVar = len(result_data), len(result_data[0])
    coord = [[] for k in range(nbVar)]
    for j in range(nbVar):
        for i in range(nbInd):
            coord[j].append(result_data[i][j])  # Individual i on j axis
    return coord


# Get correlation coordinates for each component
def coord_corr(result_data, old_data):
    nbInd, nbVar = len(result_data), len(result_data[0])
    listxj, listfk = [], []
    for i in range(nbVar):
        xj, fk = zeros(1, nbInd), zeros(1, nbInd)
        for j in range(nbInd):
            xj[j][0] = old_data[j][i]  # Old base coordinates
            fk[j][0] = result_data[j][i]  # New base coordinates
        listxj.append(xj)
        listfk.append(fk)

    # Vertical projection of the coordinates on each component
    projv = [[] for k in range(nbVar)]
    for j in range(nbVar):
        for i in range(nbVar):
            projv[j].append(correlation(listxj[i], listfk[j]))

    return projv


# Compute the squared cos of variables
def cos2_variables(result_data, old_data):
    nbVar = len(result_data[0])
    cos2_var = coord_corr(result_data, old_data)
    for i in range(nbVar):
        for j in range(nbVar):
            cos2_var[i][j] = cos2_var[i][j]**2
    return cos2_var


# Compute the contribution of a variable to an axis
def contrib_var(result_data, list_eigenVal, old_data):
    nbVar = len(result_data[0])
    var_contrib_mat = coord_corr(result_data, old_data)
    for i in range(nbVar):
        for j in range(nbVar):
            var_contrib_mat[i][j] = (
                (var_contrib_mat[i][j]**2) / list_eigenVal[i]) * 100
    return var_contrib_mat


# Compute the squared cos of individuals
def cos2_individus(result_data):
    nbInd, nbVar = len(result_data), len(result_data[0])
    cos2_ind = zeros(nbVar, nbInd)
    for i in range(nbInd):
        dist_i = distance(result_data[i][:])
        for j in range(nbVar):
            cos2_ind[i][j] = (result_data[i][j] / dist_i)**2
    return cos2_ind


# Compute the contribution of an individual to an axis
def contrib_indiv(result_data, list_eigenVal):
    nbInd, nbVar = len(result_data), len(result_data[0])
    ind_contrib_mat = zeros(nbVar, nbInd)
    for i in range(nbInd):
        for j in range(nbVar):
            ind_contrib_mat[i][j] = (
                (result_data[i][j]**2) / (nbInd * list_eigenVal[j])) * 100
    return ind_contrib_mat
