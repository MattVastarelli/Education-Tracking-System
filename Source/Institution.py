
from Source import Account


class Institution(Account):

    def __init__(self, name='', address='', institution_type='', grade_min=0, grade_max=0, main_phone_num=''):

        # public
        self.name = name

        # public
        self.address = address

        # public
        self.institution_type = institution_type

        # public
        self.grade_min = grade_min

        # public
        self.grade_max = grade_max

        # public
        self.main_phone_num = main_phone_num

    # private
    def __add_educator(self, access_level=1):
        pass

    # private
    def __add_student(self, access_level=2):
        pass

    # private
    def __offer_subject(self):
        pass

    # private
    def __change_access(self, account, level):
        pass

    # private
    def __bulk_assign_section(self, educator_id, course, section, student_id):
        pass

    # private
    def __bulk_add_records(self, access_level, upload_file_name):
        pass

