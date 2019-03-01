from Source.Account import Account


class Student(Account):

    def __init__(self, username, password, access_level, fname='', lname='', student_id=0, emergency_contact='',
                 relationship='', ec_email='', medical_notes='', grades='', educators='', current_institution='',
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
        self.__student_id = student_id

        # private
        # student emergency contact
        self.__emergency_contact = emergency_contact

        # private
        # student emergency contact relationship
        self.__relationship = relationship

        # private
        # student emergency contact email
        self.__ec_email = ec_email

        # private
        # student medical notes
        self.__medical_notes = medical_notes

        # private
        # student grades
        self.__grades = grades

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
    def view_history(self):
            pass

    # private
    # add medical contact info
    def __add_medical_notes(self):
            pass

    # private
    # add view notes
    def view_notes(self, unit, Grade):
        pass

    # private
    # add educator object with level = 1
    def get_grade(self, section, unit, Grade):
        pass

    # get name concatenate fname and lname
    def get_name(self):
        name = self.fname + " " + self.lname
        return name

    # get Student ID
    def get_student_id(self):
        student_id = self.__student_id
        return student_id

    # get emergency contact
    def get_emergency_contact(self):
        emergency_contact = self.__emergency_contact
        return emergency_contact

    # get relationship
    def get_relationship(self):
        ec_relationship = self.__relationship
        return ec_relationship

    # get ec email
    def get_ec_email(self):
        ec_email = self.__ec_email
        return ec_email

    # get medical notes
    def get_medical_notes(self):
        medical_notes = self.__medical_notes
        return medical_notes

    # get grades
    def get_grades(self):
        grades = self.__grades
        return grades

    # get educators
    def get_educators(self):
        stud_educators = self.__educators
        return stud_educators

    # get current
    def get_current_institution(self):
        current_institution = self.__current_institution
        return current_institution

    # get current grade
    def get_current_grade(self):
        current_grade = self.__current_grade
        return current_grade

    # get grades
    def get_grade_notes(self):
        grades_notes = self.__grade_notes
        return grades_notes

    # get home address
    def get_home_address(self):
        return self.__home_address

    def set_fname(self, fname, lname):
        self.__fname = fname
        self.__lname = lname
        return None

    def set_student_id(self, student_id):
        self.__student_id = student_id
        return student_id

    def set_emergency_contact(self, emergency_contact):
        self.__emergency_contact = emergency_contact
        return emergency_contact

    def set_relationship(self,  ec_relationship):
        self.__relationship = ec_relationship
        return None

    def set_ec_email(self, ec_email):
        self.__ec_email = ec_email
        return None

    def set_medical_notes(self, medical_notes):
        self.__medical_notes = medical_notes
        return None

    def set_grades(self, grades):
        self.__grades = grades
        return None

    def set_educators(self, stud_educators):
        self.__educators = stud_educators
        return None

    def set_current_institution(self, current_institution):
        self.__current_grade = current_institution
        return None

    def set_current_grade(self, current_grade):
        self.__current_grade = current_grade
        return None

    def set_grade_notes(self, grades_notes):
        self.__grade_notes = grades_notes
        return None

    def set_home_address(self, home_address):
        self.__home_address = home_address
        return None

    # private function
    def __grades(self):
        pass

    # private
    def __view(self):
        pass

    # private
    def __edit(self):
        pass

    # private
    def create_new(self, access_level, something):
        return None

