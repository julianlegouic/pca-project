# coding: utf-8

import sys
import time
from io import StringIO

import numpy as np

from graphics import *
from init import *
from iterated_power import *
from matrix_calculus import *
from unitary_calculus import *

# Save the behaviour of the print output
save = sys.stdout
# Create a string which will contain all the print outputs
output = StringIO()
# Print output are redirect to 'output' variable
sys.stdout = output

# Get time to compute execution time
init_time = time.clock()

# Display some infos about the population
init_info()
# Retrieve the content of the xls table into a python dict
data_dict = init_data()
data = data_dict['data']
nbVar = data_dict['nbVar']
nbInd = data_dict['nbInd']
ind_names = data_dict['ind_names']
var_names = data_dict['var_names']
percentage = data_dict['percentage']

# Initialization of the matrices
mat_type = centered_type(data)
mat_canon = mat_type['canon']  # Canonical form matrix
mat_normed = mat_type['normed']  # Normed matrix
mat_correlated = mat_corr(mat_normed)  # Correlation matrix

print('Canonical form and centered matrix:')
display_matrices(np.around(mat_canon, 2))
# print('Normed and centered matrix:')
# display_matrices(np.around(mat_normed, 2))
print('Correlation matrix:')
display_matrices(np.around(mat_correlated, 2))

# Compute eigen values and eigen vectors with iterated power method
eigen = deflation(mat_correlated)
print('Eigen values:', [round(elem, 5) for elem in eigen[0]])
print('\nEigen vectors:')
display_matrices(np.around(eigen[1], 5))

# Compute new coordinates of individuals in the new base
result_norm_raw = mat_normed * eigen[1]
result_redu_raw = mat_canon * eigen[1]

# Switch back to list-of-list-matrix type (np.matrix -> list of list)
rows, cols = result_norm_raw.shape[0], result_norm_raw.shape[1]
result_norm, result_canon = zeros(cols, rows), zeros(cols, rows)
for i in range(rows):
    for j in range(cols):
        result_norm[i][j] = result_norm_raw.item((i, j))
        result_canon[i][j] = result_redu_raw.item((i, j))

print('Individuals in the new base (normed):')
display_matrices(np.around(result_norm, 8))

print('Individuals in the new base (canonical):')
display_matrices(np.around(result_canon, 8))

corr_var_comp = coord_corr(result_canon, data)
print('Correlation matrix of variables (cols) with components (rows):')
display_matrices(np.around(corr_var_comp, 5))

cos2_var = cos2_variables(result_canon, data)
print('Squared cos matrix of variables (cols) with axes (rows):')
display_matrices(np.around(cos2_var, 5))

contribution_var = contrib_var(result_canon, eigen[0], data)
print('Contribution matrix of variables (cols) to axes (rows):')
display_matrices(np.around(contribution_var, 5))

cos2_indiv = cos2_individus(result_canon)
print('Squared cos matrix of individuals (rows) with axes (cols):')
display_matrices(np.around(cos2_indiv, 4))

contribution_indiv = contrib_indiv(result_canon, eigen[0])
print('Contribution matrix of individuals (rows) to axes (cols):')
display_matrices(np.around(contribution_indiv, 5))

# Determine number of dimensions to use
nb_dim, list_pct = dimensions(eigen[0], percentage)

# display execution time
print('\nExecution time is {}s'.format(
    str(round(time.clock() - init_time, 4))))

# Restore normal behaviour of standard output
sys.stdout = save

# Get the value of output as a full string
result = output.getvalue()

rep = input('Do you want to save the results in a text file? (y/n)')
if(rep == 'y'):
    # Write obtained results in a file
    new_filename = input('Enter the name of the file without any extension:')
    if (new_filename != ''):
        file_res = open(new_filename+'.txt', 'w')
    else:
        file_res = open(filename[:-4]+'_res.txt', 'w')
    file_res.write(result)
    file_res.close()
else:
    print(result)

# Plot individuals
graph(result_canon, data, nb_dim, list_pct, ind_names, var_names)
