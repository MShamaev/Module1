grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(list(students))
average_grades = [sum(item)/len(item) for item in grades]
average_grades_dict = {students_sort[0]:average_grades[0],students_sort[1]:average_grades[1],students_sort[2]:average_grades[2],students_sort[3]:average_grades[3],students_sort[4]:average_grades[4]}
print(average_grades_dict)