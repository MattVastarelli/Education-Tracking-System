import tkinter as tk
import os as os
from Source.Account import Account
from Source.Institution import Institution
from Source.Student import Student


class Educator(Account):

    # constructor
    def __init__(self, username, password, fname, lname, home_add, phonenum, email = "", ed_id = int(), licenses = list(), courses = list(), pref_subjs = list(), gradelevels = list(), currentinst = None):
        super().__init__(username, password, 1)

        # public
        # first name
        self.fname = fname

        # public
        # last name
        self.lname = lname

        # private
        # home address
        self.__homeAddress = home_add

        # private
        # phone number
        self.__phoneNum = phonenum

        # private
        # email
        self.__email = email

        # private
        # educator ID
        self.__educatorID = ed_id

        # public
        # list of licenses held
        self.licenses = licenses

        # private
        # courses taught/teaching
        self.__courses = courses

        # private
        # preferred subjects to teach (if any)
        self.__prefSubjects = pref_subjs

        # public
        # grade levels currently teaching
        self.gradeLevels = gradelevels

        # public
        # current Institution/Employer
        self.currentInst = currentinst

    # private
    def __view(self):
        # what an Educator can see on their own profile
        formInfo = [1,1]
        formInfo.append(self.get_name())
        formInfo.extend(self.get_personal_info())
        formInfo.extend(self.get_professional_info())

        # returns list: [viewer profile access level, viewed profile access level, Full Name,
        # Phone Number, Email address, Home Address, Licenses Held, Educator ID, Preferred Subjects,
        # Grade Levels Currently Teaching, Employer/Institution]
        return formInfo


    # private
    def __viewStudent(self, Student):
        # What an Educator sees on a Student's profile

        pass

    # private
    def __viewInstitution(self):
        # What an Educator sees on an Institution's profile
        # 2-25-19 NOT FINISHED! IN PROGRESS
        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/info.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        file = open(abs_file_path, 'r')
        file.close()
        InstForm = [1, 0]
        return InstForm

    # private
    def __edit(self):
        pass

    # private
    def create_new(self, access_level):
        return None

    # ------------- Getters & Setters -------------------------
    def get_name(self):
        name = self.fname + " " + self.lname
        return name

    def get_personal_info(self):
        return [self.__phoneNum, self.__email, self.__homeAddress]

    def get_professional_info(self):
        return [self.licenses, self.__educatorID, self.__prefSubjects, self.gradeLevels, self.currentInst]

    # getter for only public attributes, for when profile view called by lower access level
    def get_public_info(self):
        return [self.get_name(), self.licenses, self.gradeLevels, self.currentInst]

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
