
from Source import Account


class Institution(Account):

    # public
    def __init__(self):
        self.name = ''
        self.address = ''
        self.type = ''
        self.gradeMin = 0
        self.gradeMax = 0
        self.mainPhoneNum = ''

    # private
    def __add_educator(self, accessLevel=1):
        pass

    def __add_student(self, accessLevel=2):
        pass

    def __offer_subject(self):
        pass

    def __change_access(self, account, level):
        pass

    def __bulk_assign_section(self, educator_ID, course, section, student_ID):
        pass

    def __bulk_add_records(self, accessLevel, uploadFileName):
        pass

