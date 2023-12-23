"""
This a practice with sets
"""
students = {'Carlos', 'Brandom', 'Ramiro', 'Karolina'}
teachers = {'Ana', 'Saul', 'Yani', 'Mary', 'Doris', 'Kevin'}

print('hay mas maestros que estudiantes') if len(teachers) > len(students) else print('hay mas estudiantes que maestros')

print('The loguitud is mayor to 4.') if len(students) > 3 else print('Not is mayor.')
