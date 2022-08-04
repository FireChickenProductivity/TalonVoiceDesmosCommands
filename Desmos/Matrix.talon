title: /Desmos \| Matrix Calculator/
-
tag(): user.simple_exponentiation

#This command may not work properly if the current calculation is not the last
#It will also have unexpected results if the new matrix button is unavailable
#Such as when every available matrix letter has been used
new matrix <user.desmos_matrix_dimension> [by] <user.desmos_matrix_dimension>: 
    user.desmos_new_matrix(desmos_matrix_dimension_1, desmos_matrix_dimension_2)

#Matrix only exponentiation
transpose: user.desmos_exponentiation('T')

#Matrix functions
(reduced|reduce) [row] [echelon] [form]|r r e f: 'rref('

debt|determine|determinant|d e t: 'det('

trace: 'trace('
