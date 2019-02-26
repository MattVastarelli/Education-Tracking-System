from Source.Account import Account


class Educator(Account):
    # attributes of an Educator, that are not inherited from Account class
    accessLevel = int()
    username = ""
    password = ""
    fname = ""
    lname = ""
    __homeAddress = ""
    __phoneNum = 0
    __email = ""
    __educatorID = int()
    licenses = list()
    __courses = list()
    __prefSubjects = list()
    gradeLevels = list()
    currentInst = None

    # constructor
    def __init__(self, username, password):
        super().__init__(username, password, 1)

    # private
    def __log_in(self, user_name, password):
            pass

    # private
    def __log_out(self):
            pass

    # private
    def __view(self):
        pass

    # private
    def __edit(self):
        pass

    # private
    def create_new(self, access_level):
        pass

    # ------------- Setters & Getters -------------------------
    def get_name(self):
        name = ' '.join(self.fname, self.lname)
        return name

    def get_personal_info(self):
        return [self.__phoneNum, self.__email, self.__homeaddress]

    def get_professional_info(self):
        return [self.license, self.__educatorID, self.__prefSubject, self.gradeLevel, self.currentInstitution]

    # Functions for actions done by an Educator within system

    # private function to replace a current grade with a new grade
    # done by pulling the table row specified by the passed in arguments, and updating the Grade attribute
    def __changeGrade__(studentID, Section, Unit, newGrade):
        pass

    # private function to add a grade to a student's record
    # done by adding the grade to the Grade table, then linking the Section, Unit, and Student ID to that entry
    def __addGrade__(studentID, Section, Unit, Grade):
        pass

    # private function to add a new grade object/row to every student in a given section
    # done by creating grade objects for each student in the list of IDs
    # and adding their corresponding grade in the Grades list
    def __bulkAddGrades(studentIDs, Section, Unit, Grades):
        pass

    # function to add a note for a grade, linked to a student account
    def addGradeNote(studentID, Section, Unit, Grade):
        pass

    # private function to add a license to the list currently in the account
    def __newLic__(self, newLicense):
        self.licenses.append(newLicense)

    # function to view courses linked to current educator
    def viewCourses(self):
        pass

    # function to view students assigned to Educator's active sections
    def viewStudents(self):
        pass
