import math
import random

import numpy as np


# Euclidean norm
def norm(X):
    return np.linalg.norm(X, 2)


# For a matrix, compute its biggest eigen value and the associated eigen vector
def iterated_power(mat, epsilon=0.000001):
    m = np.shape(mat)[0]  # Number of rows
    X = np.matrix([[1.0] for i in range(m)])  # Initialize an empty vector
    eig_tmp, eig_val = 1, 0  # Initialization of eigen values
    # Condition of convergence with epsilon as the approximation
    while (abs(eig_val - eig_tmp) > epsilon):
        eig_tmp = eig_val
        eig_vec = X / norm(X)
        X = mat*eig_vec
        eig_val = (np.transpose(eig_vec)*X).item(0)
    return (eig_val, eig_vec)


# Compute the rest of the eigen values/vectors from the biggest one
def deflation(A):
    cnt = 1  # Initialize a counter
    A = np.matrix(A)  # Transform into a numpy matrix
    max_iter = np.shape(A)[0]  # Max number of iterations = variables number
    result = iterated_power(A)
    big_eigVal, big_eigVec = result[0], result[1]
    eig_values = [big_eigVal]  # Create a list for eigen values
    eig_vectors = big_eigVec  # Create a matrix for eigen vectors
    while (cnt != max_iter):
        eigVec_tmp = big_eigVec / (np.transpose(big_eigVec) * big_eigVec)
        A = A - big_eigVal * big_eigVec * np.transpose(eigVec_tmp)

        # Apply iterated power method on the updated matrix
        result = iterated_power(A)
        big_eigVal, big_eigVec = result[0], result[1]

        eig_values.append(big_eigVal)

        eig_vectors = np.hstack((eig_vectors, big_eigVec))
        cnt += 1
    return (eig_values, eig_vectors)
