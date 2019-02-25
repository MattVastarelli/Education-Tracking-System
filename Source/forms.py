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
        self.name_box = None
        self.password_box = None
        self.address_box = None
        self.grade_min_box = None
        self.grade_max_box = None
        self.phone_box = None
        self.institution_type_box = None
        self.f_name_box = None
        self.l_name_box = None
        self.courses_box = None
        self.preferred_subject_box = None
        self.email_box = None
        self.edu_license_box = None

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

            password_frame = tk.Frame(frame)
            password_frame.pack()

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
            password = tk.Label(password_frame, text="Password: ", anchor="nw")
            address = tk.Label(address_frame, text="Address: ", anchor="nw")
            grade_min = tk.Label(grade_min_frame, text="Lowest Grade: ", anchor="nw")
            grade_max = tk.Label(grade_max_frame, text="Highest Grade: ", anchor="nw")
            phone = tk.Label(phone_frame, text="Institution Phone: ", anchor="nw")
            institution_type = tk.Label(type_frame, text="Institution Type: ", anchor="nw")

            # text boxes
            self.name_box = tk.Entry(name_frame)
            self.password_box = tk.Entry(password_frame)
            self.address_box = tk.Entry(address_frame)
            self.grade_min_box = tk.Entry(grade_min_frame)
            self.grade_max_box = tk.Entry(grade_max_frame)
            self.phone_box = tk.Entry(phone_frame)
            self.institution_type_box = tk.Entry(type_frame)

            # pack items
            name.pack(side=tk.LEFT)
            self.name_box.pack(side=tk.LEFT)

            password.pack(side=tk.LEFT)
            self.password_box.pack(side=tk.LEFT)

            address.pack(side=tk.LEFT)
            self.address_box.pack(side=tk.LEFT)

            grade_min.pack(side=tk.LEFT)
            self.grade_min_box.pack(side=tk.LEFT)

            grade_max.pack(side=tk.LEFT)
            self.grade_max_box.pack(side=tk.LEFT)

            phone.pack(side=tk.LEFT)
            self.phone_box.pack(side=tk.LEFT)

            institution_type.pack(side=tk.LEFT)
            self.institution_type_box.pack(side=tk.LEFT)

            return self.top
        elif access_level is 1:
            self.top.title("Add New Educator")

            # frames
            f_name_frame = tk.Frame(frame)
            f_name_frame.pack()

            l_name_frame = tk.Frame(frame)
            l_name_frame.pack()

            phone_frame = tk.Frame(frame)
            phone_frame.pack()

            email_frame = tk.Frame(frame)
            email_frame.pack()

            password_frame = tk.Frame(frame)
            password_frame.pack()

            address_frame = tk.Frame(frame)
            address_frame.pack()

            courses_frame = tk.Frame(frame)
            courses_frame.pack()

            pref_subject_frame = tk.Frame(frame)
            pref_subject_frame.pack()

            license_frame = tk.Frame(frame)
            license_frame.pack()

            # labels
            f_name = tk.Label(f_name_frame, text="First Name: ", anchor="nw")
            l_name = tk.Label(l_name_frame, text="Last Name: ", anchor="nw")
            password = tk.Label(password_frame, text="Password: ", anchor="nw")
            address = tk.Label(address_frame, text="Address: ", anchor="nw")
            courses = tk.Label(courses_frame, text="Courses Taught: ", anchor="nw")
            phone = tk.Label(phone_frame, text="Phone: ", anchor="nw")
            pref_subject = tk.Label(pref_subject_frame, text="Preferred Subjects: ", anchor="nw")
            edu_license = tk.Label(license_frame, text="Educational License: ", anchor="nw")
            email = tk.Label(email_frame, text="Email: ", anchor="nw")

            # text boxes
            self.f_name_box = tk.Entry(f_name_frame)
            self.l_name_box = tk.Entry(l_name_frame)
            self.password_box = tk.Entry(password_frame)
            self.address_box = tk.Entry(address_frame)
            self.courses_box = tk.Entry(courses_frame)
            self.preferred_subject_box = tk.Entry(pref_subject_frame)
            self.phone_box = tk.Entry(phone_frame)
            self.email_box = tk.Entry(email_frame)
            self.edu_license_box = tk.Entry(license_frame)

            # pack items
            f_name.pack(side=tk.LEFT)
            self.f_name_box.pack(side=tk.LEFT)

            l_name.pack(side=tk.LEFT)
            self.l_name_box.pack(side=tk.LEFT)

            password.pack(side=tk.LEFT)
            self.password_box.pack(side=tk.LEFT)

            address.pack(side=tk.LEFT)
            self.address_box.pack(side=tk.LEFT)

            courses.pack(side=tk.LEFT)
            self.courses_box.pack(side=tk.LEFT)

            phone.pack(side=tk.LEFT)
            self.phone_box.pack(side=tk.LEFT)

            pref_subject.pack(side=tk.LEFT)
            self.preferred_subject_box.pack(side=tk.LEFT)

            edu_license.pack(side=tk.LEFT)
            self.edu_license_box.pack(side=tk.LEFT)

            email.pack(side=tk.LEFT)
            self.email_box.pack(side=tk.LEFT)

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
