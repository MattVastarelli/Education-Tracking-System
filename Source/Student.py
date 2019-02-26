from Source.Account import Account


class Student(Account):

    def __init__(self, username, password, access_level, fname='', lname='', studentID=0, emergency_contact='',
                 relationship='', ecEmail='', medical_notes='', Grades='', educators='', current_institution='',
                 current_grade=0, grade_notes='', home_address=''):

        super().__init__(username, password, access_level)

        # private
        # student first name
        self.fname = fname

        # private
        # student first name
        self.lname = lname

        # private
        # student studentID
        self.studentID = studentID

        # private
        # student emergency contact
        self.emergency_contact = emergency_contact

        # private
        # student emergency contact relationship
        self.relationship = relationship

        # private
        # student emergency contact email
        self.ecEmail = ecEmail

        # private
        # student medical notes
        self.medical_notes = medical_notes

        # private
        # student grades
        self.Grades = Grades

        # private
        # student educators
        self.educators = educators

        # private
        # student current institution
        self.current_institution = current_institution

        # private
        # student current grade
        self.current_grade = current_grade

        # private
        # student grade notes
        self.grade_notes = grade_notes

        # private
        # student home address
        self. home_address = home_address

    # private
    # view History
    def __viewHistory(self):
            pass

    # private
    # add medical contact info
    def addMedicalnotes(self):
            pass

    # private
    # add view notes
    def __viewNotes(self, unit, Grade):
        pass

    # private
    # add educator object with level = 1
    def getGrade(self, section, unit, Grade):
        pass

    # private
    def __view(self):
        pass

    # private
    def __edit(self):
        pass

    # private
    def create_new(self, access_level):
        return None

