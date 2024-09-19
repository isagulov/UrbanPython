grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students)

middle_grade = {}
middle_grade['Aaron'] = sum(grades[0]) / len(grades[0])
middle_grade['Bilbo'] = sum(grades[1]) / len(grades[1])
middle_grade['Johny'] = sum(grades[2]) / len(grades[2])
middle_grade['Khendrik'] = sum(grades[3]) / len(grades[3])
middle_grade['Steve'] = sum(grades[4]) / len(grades[4])
print(middle_grade)