from Source.Account import Account


class Student(Account):

    def __init__(self, username, password, access_level, fname='', lname='', studentID=0, emergency_contact='',
                 relationship='', ecEmail='', medical_notes='', Grades='', educators='', current_institution='',
                 current_grade=0, grade_notes='', home_address=''):

        super().__init__(username, password, access_level)

        # private
        # student first name
        self.__fname = fname

        # private
        # student first name
        self.__lname = lname

        # private
        # student studentID
        self.__studentID = studentID

        # private
        # student emergency contact
        self.__emergency_contact = emergency_contact

        # private
        # student emergency contact relationship
        self.__relationship = relationship

        # private
        # student emergency contact email
        self.__ecEmail = ecEmail

        # private
        # student medical notes
        self.__medical_notes = medical_notes

        # private
        # student grades
        self.__Grades = Grades

        # private
        # student educators
        self.__educators = educators

        # private
        # student current institution
        self.__current_institution = current_institution

        # private
        # student current grade
        self.__current_grade = current_grade

        # private
        # student grade notes
        self.__grade_notes = grade_notes

        # private
        # student home address
        self.__home_address = home_address

    # private
    # view History
    def viewHistory(self):
            pass

    # private
    # add medical contact info
    def __addMedicalnotes(self):
            pass

    # private
    # add view notes
    def viewNotes(self, unit, Grade):
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

