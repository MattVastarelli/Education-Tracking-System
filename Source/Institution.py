
from Source.Account import Account


class Institution(Account):

    def __init__(self, username, password, access):

        super().__init__()

        # public
        # institution name
        self.name = None

        # public
        # institution address
        self.address = None

        # public
        # institution type
        self.institution_type = None

        # public
        # institution grade min
        self.grade_min = None

        # public
        # institution grade max
        self.grade_max = None

        # public
        # institution main phone number
        self.main_phone_num = None

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


print(Institution)