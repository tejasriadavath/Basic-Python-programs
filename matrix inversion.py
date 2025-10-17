# defining the matrix

matrix = [

[1, 2],

[4, 5]

] 

# Finding the determinant of the matrix

det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] 

# Check if the determinant is non-zero

if det != 0:
# Calculate the inverse of the 2x2 matrix

inv = [

[matrix[1][1] / det, -matrix[0][1] / det],

[-matrix[1][0] / det, matrix[0][0] / det]

]

# Printing the inverse of the matrix

print("the inverse of the matrix is-")

for row in inv:

print(row)

else:

print("The given matrix is singular and does not have an inverse")
