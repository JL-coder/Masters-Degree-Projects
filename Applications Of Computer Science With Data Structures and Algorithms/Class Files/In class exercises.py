def to_string(self):
    s = "Teacher: " + self.get_teacher_name()
    s += "\nNb Students: " + str(self.get_NbStudents())
    s += "\n---"
    for a in self.get_studentList():
        s += a.toString()
        s += "\n"
    return s