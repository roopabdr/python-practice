names = input("Enter names seperated by commas: ")
assignments = input("Enter assignment counts seperated by commas: ")
grades = input("Enter grades seperated by commas: ")

names = names.split(",")
assignments = assignments.split(",")
grades = grades.split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    potential_grade = int(grade) + 2 * int(assignment)
    print(message.format(name.title(), assignment, grade, potential_grade))