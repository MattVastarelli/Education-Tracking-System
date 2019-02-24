
from Source import Account


class Institution(Account):

    def __init__(self, username, password, access, name='', address='', institution_type='', grade_min=0, grade_max=0, main_phone_num=''):

        Account.__init__(self, username, password, access)

        # public
        # institution name
        self.name = name

        # public
        # institution address
        self.address = address

        # public
        # institution type
        self.institution_type = institution_type

        # public
        # institution grade min
        self.grade_min = grade_min

        # public
        # institution grade max
        self.grade_max = grade_max

        # public
        # institution main phone number
        self.main_phone_num = main_phone_num

    # private
    # add educator object with level = 1
    def __add_educator(self, access_level=1):
        pass

    # private
    # add student object with level = 2
    def __add_student(self, access_level=2):
        pass

    # private
    # add offering subjects
    def __offer_subject(self):
        pass

    # private
    # change account access level
    def __change_access(self, account, level):
        pass

    # private
    # assign section
    def __bulk_assign_section(self, educator_id, course, section, student_id):
        pass

    # private
    # add records
    def __bulk_add_records(self, access_level, upload_file_name):
        pass

