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

    def add_new(self, access_level):
        # form to add a new record
        self.top.resizable(width=False, height=False)
        self.top.geometry("550x350")

        # main frame
        frame = tk.Frame(self.top)
        frame.pack()

        if access_level is 0:
            self.top.title("Add New Institution")

            # frames
            name_frame = tk.Frame(frame)
            name_frame.pack()

            address_frame = tk.Frame(frame)
            address_frame.pack()

            grade_min_frame = tk.Frame(frame)
            grade_min_frame.pack()

            grade_max_frame = tk.Frame(frame)
            grade_max_frame.pack()

            phone_frame = tk.Frame(frame)
            phone_frame.pack()

            type_frame = tk.Frame(frame)
            type_frame.pack()

            # labels
            name = tk.Label(name_frame, text="Institution Name: ", anchor="nw")
            address = tk.Label(address_frame, text="Address: ", anchor="nw")
            grade_min = tk.Label(grade_min_frame, text="Lowest Grade: ", anchor="nw")
            grade_max = tk.Label(grade_max_frame, text="Highest Grade: ", anchor="nw")
            phone = tk.Label(phone_frame, text="Institution Phone: ", anchor="nw")
            institution_type = tk.Label(type_frame, text="Institution Type: ", anchor="nw")

            # text boxes
            name_box = tk.Entry(name_frame)
            address_box = tk.Entry(address_frame)
            grade_min_box = tk.Entry(grade_min_frame)
            grade_max_box = tk.Entry(grade_max_frame)
            phone_box = tk.Entry(phone_frame)
            institution_type_box = tk.Entry(type_frame)

            # pack items
            name.pack(side=tk.LEFT)
            name_box.pack(side=tk.LEFT)

            address.pack(side=tk.LEFT)
            address_box.pack(side=tk.LEFT)

            grade_min.pack(side=tk.LEFT)
            grade_min_box.pack(side=tk.LEFT)

            grade_max.pack(side=tk.LEFT)
            grade_max_box.pack(side=tk.LEFT)

            phone.pack(side=tk.LEFT)
            phone_box.pack(side=tk.LEFT)

            institution_type.pack(side=tk.LEFT)
            institution_type_box.pack(side=tk.LEFT)

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
