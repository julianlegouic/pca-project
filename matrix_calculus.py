# coding: utf-8

import math

from init import *
from unitary_calculus import correlation, mean, std


# Compute correlation matrix
def mat_corr(matrix):
    mat = zeros(nbVar, nbVar)
    for i in range(nbVar):
        mat[i][i] = float(1)
    for i in range(nbVar):
        for j in range(i+1, nbVar):
            res1 = correlation(matrix, matrix, i, j)
            mat[i][j] = res1
            mat[j][i] = res1
    return mat


# Compute the centered matrices normed and in canonical form
def centered_type(matrix):
    mat_canon = zeros(nbVar, nbInd)
    mat_normed = zeros(nbVar, nbInd)
    for j in range(nbVar):
        for i in range(nbInd):
            m = mean(matrix, nbInd, j)
            s = std(matrix, j)
            mat_canon[i][j] = (matrix[i][j] - m) / s
            mat_normed[i][j] = (matrix[i][j] - m) / (s*math.sqrt(nbInd))
    return {'canon': mat_canon, 'normed': mat_normed}


# Remove an individual in a matrix from its index
def remove_ind(mat, index):
    matrix = zeros(len(mat[0]), len(mat)-1)
    for i in range(index):
        matrix[i][:] = mat[i][:]
    for i in range(index + 1, len(mat)):
        matrix[i-1][:] = mat[i][:]
    return matrix
