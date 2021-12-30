class CS5007:
    def __init__(self, student_list, teacher_name, semester):
        self.__nbStudents = len(student_list)
        self.__student_list = student_list
        self.__teacher_name = teacher_name
        self.__semester = semester

    def get_NbStudents(self):
        return self.__nbStudents

    def set_NbStudents(self, student_list):
        self.__nbStudents = len(student_list)

    def get_studentList(self):
        return self.__student_list

    def add_student(self, student):
        self.__student_list.append(student)
        self.set_NbStudents(self.get_studentList())

    def remove_student(self, student):
        try:
            self.__student_list.remove(student)
            self.set_NbStudents(self.get_studentList())
        except:
            print("No such student, " + student.get_firstname())

    def get_teacher_name(self):
        return self.__teacher_name

    def set_teacher_name(self, teacher_name):
        self.__teacher_name = teacher_name

    def get_semester(self):
        return self.__semester

    def set_semester(self, semester):
        self.__semester = semester

    # ** Code **
