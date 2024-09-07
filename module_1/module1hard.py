grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# convert an unordered sequence of a 'set' into an ordered 'tuple' sorted alphabetically
students = tuple(sorted(students))

# calculate the gpa (Grade Point Average) of each student using the formula and indexes

grades_gpa = (
    sum(grades[0]) / len(grades[0]),
    sum(grades[1]) / len(grades[1]),
    sum(grades[2]) / len(grades[2]),
    sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4]),
)

# fill the dictionary using dict and zip
dict_GPA = dict(zip(students, grades_gpa))
print(dict_GPA)
