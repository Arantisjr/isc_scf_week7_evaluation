with open("student.txt", "w") as stud_names:
    stud_names.write("Arantis\n")
    stud_names.write("hans\n")
    stud_names.write("lois\n")
    stud_names.write("sir\n")
    stud_names.write("maie\n")


with open("student.txt", "r") as stud_names:
    stud_names.read()
    stud_names.read()
    stud_names.read()
    stud_names.read()
    stud_names.read()