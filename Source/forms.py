import tkinter as tk
import tkinter.messagebox as message_box


class Form:
    # main forms class

    def __init__(self):
        self.top = tk.Tk()
        self.f_name = str()
        self.l_name = str()
        self.address = str()
        self.grade_min = 0
        self.grade_max = 12
        self.phone = str()
        self.license = list()
        self.email = str()
        self.preferred_subject = str()
        self.student_id = int()
        self.emergency_phone = str()
        self.emergency_contact = str()
        self.emergency_relation = str()
        self.emergency_email = str()
        self.notes = str()
        self.type = str()

        # gui elements
        self.frame = None
        self.address_frame = None
        self.name_frame = None
        self.grade_min_frame = None
        self.grade_max_frame = None
        self.phone_frame = None
        self.type_frame = None

        self.name = None
        self.address = None
        self.grade_min = None
        self.grade_max = None
        self.phone = None
        self.institution_type = None

        self.name_box = None
        self.address_box = None
        self.grade_min_box = None
        self.grade_max_box = None
        self.phone_box = None
        self.institution_type_box = None

    def add_new(self, access_level):
        # form to add a new record
        self.top.resizable(width=False, height=False)
        self.top.geometry("550x350")

        # main frame
        self.frame = tk.Frame(self.top)
        self.frame.pack()

        if access_level is 0:
            self.top.title("Add New Institution")

            # frames
            self.name_frame = tk.Frame(self.frame)
            self.name_frame.pack()

            self.address_frame = tk.Frame(self.frame)
            self.address_frame.pack()

            self.grade_min_frame = tk.Frame(self.frame)
            self.grade_min_frame.pack()

            self.grade_max_frame = tk.Frame(self.frame)
            self.grade_max_frame.pack()

            self.phone_frame = tk.Frame(self.frame)
            self.phone_frame.pack()

            self.type_frame = tk.Frame(self.frame)
            self.type_frame.pack()

            # labels
            self.name = tk.Label(self.name_frame, text="Institution Name: ", anchor="nw")
            self.address = tk.Label(self.address_frame, text="Address: ", anchor="nw")
            self.grade_min = tk.Label(self.grade_min_frame, text="Lowest Grade: ", anchor="nw")
            self.grade_max = tk.Label(self.grade_max_frame, text="Highest Grade: ", anchor="nw")
            self.phone = tk.Label(self.phone_frame, text="Institution Phone: ", anchor="nw")
            self.institution_type = tk.Label(self.type_frame, text="Institution Type: ", anchor="nw")

            # text boxes
            self.name_box = tk.Entry(self.name_frame)
            self.address_box = tk.Entry(self.address_frame)
            self.grade_min_box = tk.Entry(self.grade_min_frame)
            self.grade_max_box = tk.Entry(self.grade_max_frame)
            self.phone_box = tk.Entry(self.phone_frame)
            self.institution_type_box = tk.Entry(self.type_frame)

            # pack items
            self.name.pack(side=tk.LEFT)
            self.name_box.pack(side=tk.LEFT)

            self.address.pack(side=tk.LEFT)
            self.address_box.pack(side=tk.LEFT)

            self.grade_min.pack(side=tk.LEFT)
            self.grade_min_box.pack(side=tk.LEFT)

            self.grade_max.pack(side=tk.LEFT)
            self.grade_max_box.pack(side=tk.LEFT)

            self.phone.pack(side=tk.LEFT)
            self.phone_box.pack(side=tk.LEFT)

            self.institution_type.pack(side=tk.LEFT)
            self.institution_type_box.pack(side=tk.LEFT)

            return self.top
        elif access_level is 1:
            self.top.title("Add New Educator")
            return self.top
        elif access_level is 2:
            self.top.title("Add New Student")
            return self.top
        else:
            pass

    def offer_subject(self):
        # form to offer a subject
        pass

    def change_access(self):
        # change a users access level
        pass

    def add_records(self):
        # add a single record
        pass

    def bulk_add_records(self):
        # add many records
        pass

    def change_grade(self):
        # change a students grade
        pass

    def add_grade(self):
        # give a student a grade
        pass

    def bulk_add_grade(self):
        # add many grades
        pass

    def view_courses(self):
        # view one or many courses
        pass

    def add_license(self):
        # add a license to a teacher
        pass

    def view_history(self):
        # view a students history
        pass

    def add_medical_note(self):
        # add a medical note to a students account
        pass

    def view_note(self):
        # view a students notes
        pass

    def view_grade(self):
        # finds and displays a students grade
        pass

    def eddit_account_info(self):
        # edit form
        pass

    def view_profile(self):
        # view a given profile
        pass
