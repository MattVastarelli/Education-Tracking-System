
from Source.Account import Account

class Institution(Account):

    def __init__(self, username, password, access, is_new):

        super().__init__(username, password, access, is_new)

        # public
        # institution name
        self.name = ''

        # public
        # institution address
        self.address = ''

        # public
        # institution type
        self.institution_type = ''

        # public
        # institution grade min
        self.grade_min = ''

        # public
        # institution grade max
        self.grade_max = ''

        # public
        # institution main phone number
        self.main_phone_num = ''

    def set_data(self, data):
        self.name = data[0]
        self.address = data[1]
        self.institution_type = data[2]
        self.grade_max = data[3]
        self.grade_min = data[4]
        self.main_phone_num = data[5]

        return None

    def set_id(self, new_id):
        self.ownerID = new_id

    def get_id(self):
        return self.ownerID

    def __set_name(self, name):
        self.name = name

    def __set_address(self, address):
        self.address = address

    def __set_institution_type(self, institution_type):
        self.institution_type = institution_type

    def __set_grad_min(self, grade_min):
        self.grade_min = grade_min

    def __set_grade_max(self, grade_max):
        self.grade_max = grade_max

    def __set_main_phone_num(self, main_phone_num):
        self.main_phone_num = main_phone_num

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_institution_type(self):
        return self.institution_type

    def get_grade_min(self):
        return self.grade_min

    def get__grade_max(self):
        return self.grade_max

    def get_main_phone_num(self):
        return self.main_phone_num

    # private
    # add educator object with level = 1
    def __add_educator(self, access_level=1):

        pass

    # private
    # add student object with level = 2
    def __add_student(self, access_level=2):
        pass

    # private
    # view institution self
    def view_institution(self):
        pass

    # private
    # add offering subjects
    def __offer_subject(self):
        pass

    # private
    # assign section
    def __bulk_assign_section(self, educator_id, course, section, student_id):
        pass

    # private
    # add records
    def __bulk_add_records(self, access_level, upload_file_name):
        pass

    # private
    def __view(self):
        pass

    # private
    def __edit(self):
        pass

    # private
    def create_new(self, access_level, something):
        pass

    # view educator profile
    def view_educator(self, data, search_type):
        return None

    # view student profile
    def view_student(self, data, search_type):
        return None
