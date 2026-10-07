"""una list comprehension conbina el for y el if en una sola linea de codigo,
y permite crear una lista de manera mas concisa y legible."""
squares = [value**2 for value in range(1,11)]
print(squares)

students = ['montes', 'david', 'el de las flautas', 'el dictador', 'dante']
print("lista de estudiantes: ", students)
students_email = [student + "@upv.edu.mx" for student in students]
print(students_email)