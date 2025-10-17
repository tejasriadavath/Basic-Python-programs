# Defining the first matrix

m1 = [

[45, 65, 23],

[90, 67, 12],

[65, 12 ,46]

]

 

# Calculate the trace of the matrix

ans_matrix = sum(m1[i][i] for i in range(len(m1))) # finding the trace i.e., sum of the diagonal elements

 

# print the matrix

print(f"Trace of the matrix: {ans_matrix}")

