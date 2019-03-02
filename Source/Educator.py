import tkinter as tk
import os
import csv
from Source.Account import Account
from Source.Institution import Institution
from Source.Student import Student


class Educator(Account):

    # constructor
    def __init__(self, username, password, is_new):
        super().__init__(username, password, 1, is_new)

        # public
        # first name
        self.fname = ''

        # public
        # last name
        self.lname = ''

        # private
        # home address
        self.__homeAddress = ''

        # private
        # phone number
        self.__phoneNum = ''

        # private
        # email
        self.__email = ''

        # private
        # educator ID
        self.__educatorID = 0

        # public
        # list of licenses held
        self.licenses = list()

        # private
        # courses taught/teaching
        self.__courses = list()

        # private
        # preferred subjects to teach (if any)
        self.__prefSubjects = ''

        # public
        # grade levels currently teaching
        self.gradeLevels = list()

        # public
        # current Institution/Employer
        self.currentInst = ''

    def set_data(self, data):
        self.fname = data[0]
        self.lname = data[1]
        self.__homeAddress = data[2]
        self.__phoneNum = data[3]
        self.__email = data[4]
        self.__educatorID = data[5]
        self.licenses = data[6]
        self.__courses = data[7]
        self.__prefSubjects = data[8]
        self.gradeLevels = data[9]
        self.currentInst = data[10]

        return None

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

    def set_id(self, new_id):
        self.set_id(new_id)

    def set_pw(self, password):
        self.set_password(password)

    def set_name(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def set_homeAddress(self, newadd):
        self.__homeAddress = newadd

    def set_phone(self, newphone):
        self.__phoneNum = newphone

    def set_email(self, newemail):
        self.__email = newemail

    def set_edID(self, newid):
        self.__educatorID = newid

    # private function to add a license to the licenses list
    def new_lic(self, newLicense):
        self.licenses.append(newLicense)

    # private function to remove a license from the licenses list
    def remove_lic(self, license):
        self.licenses.remove(license)

    # function to add new preferred subject to the preferred subject list
    def new_pref_subj(self, subject):
        self.__prefSubjects.append(subject)

    # function to remove a subject type from the preferred subjects list
    def remove_subject(self, subject):
        self.__prefSubjects.remove(subject)

    # function to add a grade level to the Educator's gradeLevels list
    def new_gradelevel(self, gradenum):
        self.gradeLevels.append(gradenum)

    # function to remove a grade level from the gradeLevels list
    def remove_gradelevel(self, gradenum):
        self.gradeLevels.remove(gradenum)

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

    # function to view courses linked to current educator
    def viewCourses(self):
        pass

    # function to view students assigned to Educator's active sections
    def viewStudents(self):
        pass
