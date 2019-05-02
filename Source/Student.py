from Source.Account import Account
from Source.Institution import Institution
import csv
import os


class Student(Account):

    def __init__(self, username, password, access_level, is_new):

        super().__init__(username, password, access_level, is_new)

        # private
        # student first name
        self.__fname = ''

        # private
        # student last name
        self.__lname = ''

        # private
        # student studentID
        self.__student_id = 0

        # private
        # student emergency contact
        self.__emergency_contact = ''

        # private
        # student emergency contact relationship
        self.__relationship = ''

        # private
        # student emergency contact email
        self.__ec_email = ''

        # private
        # student medical notes
        self.__medical_notes = ''

        # private
        # student grades
        self.__grades = ''

        # private
        # student educators
        self.__educators = ''

        # private
        # student current institution
        self.__current_institution = ''

        # private
        # student current grade
        self.__current_grade = 0

        # private
        # student grade notes
        self.__grade_notes = ''

        # private
        # student home address
        self.__home_address = ''

    def set_data(self, data):
        self.__fname = data[0]
        self.__lname = data[1]
        self.__student_id = data[2]
        self.__emergency_contact = data[3]
        self.__relationship = data[4]
        self.__ec_email = data[5]
        self.__medical_notes = data[6]
        self.__current_grade = data[7]
        self.__educators = []
        self.__current_institution = data[8]
        self.__grades = data[9]
        self.__grade_notes = data[10]
        self.__home_address = data[11]

        return None

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
        name = self.__fname + " " + self.__lname
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

    def get_inst_id(self):
        return self.__current_institution

    # get current institution
    def get_current_institution(self):
        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/institutions.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        return_list = list()

        with open(abs_file_path) as f:
            content = f.readlines()
            content = [x.strip() for x in content]

            for line in content:
                split = line.split("\t")  # choose split type
                if split[0] == str(self.__current_institution):
                    return_list = line.split("\t")
                    break
            f.close()

        return return_list[4]
        # return self.__current_institution

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

    def set_id(self, new_id):
        self.ownerID = new_id

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

    def view_inst(self):
        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/institutions.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path) as file:
            content = file.readlines()
            content = [x.strip() for x in content]
            instData = list()
            for line in content:
                split = line.split("\t")  # choose split type
                if str(self.__current_institution) == split[0]:
                    instData = split # found the inst
                    # create and return obj
                    inst = Institution(username=instData[2], password=instData[3], access=0, is_new=False)
                    inst.set_data([instData[4], instData[5], instData[6], instData[8], instData[7], instData[9]])
                    return inst

        return None

    # view educator profile
    def view_educator(self, data, search_type):
        return None
