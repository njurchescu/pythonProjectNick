
employees_file = open("C:/Users/Nick/PycharmProjects/pythonProjectNick/employees", "r")
for employees in employees_file.readlines():
    print(employees)

# print(employees_file.read())
# print(employees_file.readlines(1))

employees_file.close()  # always close the file when done
