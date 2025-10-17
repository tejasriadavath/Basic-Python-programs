# Defining the first matrix
m1 = [

[45, 65, 23],

[90, 67, 12],

[65, 12 ,46]

]

# defining the second matrix

m2 = [

[9, 8, 7],

[6, 5, 4],

[3, 2, 1]

]

# Adding two matrices

addition_mat = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

# Printing the matrix

print("The addition of two matrices are:")

# Using for-in to print the matrix

for row in addition_mat:

    print(row)

# subtracting two matrices

subtracting_mat = [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

# Printing the matrix

print("The subtraction of two matrices are:") 

# Using for-in to print the matrix

for row in subtracting_mat:

    print(row)
