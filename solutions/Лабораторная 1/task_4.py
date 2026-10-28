student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10
print('первая буква имени:', student[0], '| последняя буква имени:', student[student.index(' ') -1])
print('имя:', student[:student.index(' ')], '| фамилия:', student[student.index(' ') + 1:])
print(student.lower(), '|', student.upper())
print(student[0], '.', student[student.index(' ') + 1], '.', sep = '')
print(course[::-1])
print('%s - %s: %d/%d (%.1f%%)' % (student, course, completed, total, (completed/total)*100))
print('{} - {}: {}/{} ({:.1f}%)'.format(student, course,completed, total, (completed/total)*100))
print(f'{student} - {course}: {completed}/{total} ({completed/total*100}%)')

print('-----------------------')
symbol = 'Я'
print(symbol, ord(symbol), chr(ord(symbol)), symbol.encode('utf-8'), len(symbol.encode('utf-8')), sep = '\n')

#student[0] = 'И'
#print(student)
