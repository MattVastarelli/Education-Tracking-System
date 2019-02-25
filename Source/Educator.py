from Source import Account, Institution


class Educator:
    # attributes of an Educator, that are not inherited from Account class
    accessLevel = int()
    username = ""
    password = ""
    fname = ""
    lname = ""
    homeAddress = ""
    phoneNum = 0
    email = ""
    educatorID = int()
    licenses = list()
    courses = list()
    prefSubjects = list()
    gradeLevels = list()
    currentInst = Institution()

    # methods for the Educator class

    # constructor
    def __init__(self, username, password):
        Account.__init__(self, username, password, access=1)

        # inherited data items being assigned
        self.accessLevel = Account.access
        self.username = Account.username
        self.password = Account.password

    # private function to replace a current grade with a new grade
    # done by pulling the table row specified by the passed in arguments, and updating the Grade attribute
    def __changeGrade__(studentID, Section, Unit, newGrade):
        pass

    # private function to add a grade to a student's record
    # done by adding the grade to the Grade table, then linking the Section, Unit, and Student ID to that entry
    def __addGrade__(studentID, Section, Unit, Grade):
        pass

    # private function to add a new grade object/row to every student in a given section
    # done by creating grade objects for each student in the list of IDs, and adding their corresponding grade in the Grades list
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
