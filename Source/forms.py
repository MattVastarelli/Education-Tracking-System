import tkinter as tk
import tkinter.messagebox as message_box


class Form:
    # main forms class

    def __init__(self):
        self.top = tk.Tk()
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
        self.emergency_contact_box = None
        self.ec_phone_box = None
        self.ec_relation = None
        self.ec_email_box = None
        self.current_grade_box = None
        self.medical_notes_box = None
        self.user_name_box = None
        self.password_box = None
        self.note = None

    def main_screen(self):
        self.top.geometry("300x450")
        self.top.title("EduTrac Dashboard")

        return self.top

    def run(self):
        self.top.mainloop()
        return None

    def destroy(self):
        self.top.destroy()
        return None

    def start_screen(self):
        self.top.geometry("300x450")
        self.top.title("Get Started")

        return self.top

    def log_in(self):
        # form to add a new record
        self.top.resizable(width=False, height=False)
        self.top.geometry("300x450")
        self.top.title("Login")

        # main frame
        frame = tk.Frame(self.top)
        frame.pack(pady=75)

        # form fields names
        user_name_frame = tk.Frame(frame)
        user_name_frame.pack()

        password_frame = tk.Frame(frame)
        password_frame.pack(pady=25)

        # labels
        user_name = tk.Label(user_name_frame, text="User Name: ", anchor="nw")
        password = tk.Label(password_frame, text="Password: ", anchor="nw")

        # entry
        self.user_name_box = tk.Entry(user_name_frame)
        self.password_box = tk.Entry(password_frame)

        # pack
        user_name.pack(side=tk.LEFT)
        self.user_name_box.pack(side=tk.LEFT)

        password.pack(side=tk.LEFT)
        self.password_box.pack(side=tk.LEFT)

        return self.top

    def get_login_data(self):
        # use to retrieve login form data

        u = self.user_name_box.get()
        p = self.password_box.get()

        data = {
            "user_name": u, "password": p
        }

        return data

    def add_new(self, access_level):
        # form to add a new record
        self.top.resizable(width=False, height=False)
        self.top.geometry("550x350")

        # main frame
        frame = tk.Frame(self.top)
        frame.pack(pady=25)

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

            # frames
            f_name_frame = tk.Frame(frame)
            f_name_frame.pack()

            l_name_frame = tk.Frame(frame)
            l_name_frame.pack()

            ec_phone_frame = tk.Frame(frame)
            ec_phone_frame.pack()

            ec_email_frame = tk.Frame(frame)
            ec_email_frame.pack()

            emergency_contact_frame = tk.Frame(frame)
            emergency_contact_frame.pack()

            relation_frame = tk.Frame(frame)
            relation_frame.pack()

            password_frame = tk.Frame(frame)
            password_frame.pack()

            medical_notes_frame = tk.Frame(frame)
            medical_notes_frame.pack()

            current_grade_frame = tk.Frame(frame)
            current_grade_frame.pack()

            address_frame = tk.Frame(frame)
            address_frame.pack()

            # labels
            f_name = tk.Label(f_name_frame, text="First Name: ", anchor="nw")
            l_name = tk.Label(l_name_frame, text="Last Name: ", anchor="nw")
            password = tk.Label(password_frame, text="Password: ", anchor="nw")
            address = tk.Label(address_frame, text="Address: ", anchor="nw")
            emergency_contact = tk.Label(emergency_contact_frame, text="Emergency Contact Name: ", anchor="nw")
            ec_phone = tk.Label(ec_phone_frame, text="Emergency Contact Phone: ", anchor="nw")
            ec_email = tk.Label(ec_email_frame, text="Emergency Contact Email: ", anchor="nw")
            ec_relation = tk.Label(relation_frame, text="Emergency Contact Relation: ", anchor="nw")
            current_grade = tk.Label(current_grade_frame, text="Current Grade: ", anchor="nw")
            medical_notes = tk.Label(medical_notes_frame, text="Medical Notes: ", anchor="nw")

            # text boxes
            self.f_name_box = tk.Entry(f_name_frame)
            self.l_name_box = tk.Entry(l_name_frame)
            self.password_box = tk.Entry(password_frame)
            self.address_box = tk.Entry(address_frame)
            self.emergency_contact_box = tk.Entry(emergency_contact_frame)
            self.ec_phone_box = tk.Entry(ec_phone_frame)
            self.ec_relation = tk.Entry(relation_frame)
            self.ec_email_box = tk.Entry(ec_email_frame)
            self.current_grade_box = tk.Entry(current_grade_frame)
            self.medical_notes_box = tk.Entry(medical_notes_frame)

            # pack items
            f_name.pack(side=tk.LEFT)
            self.f_name_box.pack(side=tk.LEFT)

            l_name.pack(side=tk.LEFT)
            self.l_name_box.pack(side=tk.LEFT)

            password.pack(side=tk.LEFT)
            self.password_box.pack(side=tk.LEFT)

            address.pack(side=tk.LEFT)
            self.address_box.pack(side=tk.LEFT)

            emergency_contact.pack(side=tk.LEFT)
            self.emergency_contact_box.pack(side=tk.LEFT)

            ec_phone.pack(side=tk.LEFT)
            self.ec_phone_box.pack(side=tk.LEFT)

            ec_email.pack(side=tk.LEFT)
            self.ec_email_box.pack(side=tk.LEFT)

            ec_relation.pack(side=tk.LEFT)
            self.ec_relation.pack(side=tk.LEFT)

            current_grade.pack(side=tk.LEFT)
            self.current_grade_box.pack(side=tk.LEFT)

            medical_notes.pack(side=tk.LEFT)
            self.medical_notes_box.pack(side=tk.LEFT)

            return self.top
        else:
            return None

    def get_educator_data(self):
        f_name = self.f_name_box.get()
        l_name = self.l_name_box.get()
        password = self.password_box.get()
        address = self.address_box.get()
        courses = self.courses_box.get()
        pref_subject = self.preferred_subject_box.get()
        phone = self.phone_box.get()
        email = self.email_box.get()
        edu_license = self.edu_license_box.get()

        data = {
            "first_name": f_name, "last_name": l_name, "password": password, "address": address,
            "courses": courses, "preferred_subject": pref_subject, "phone": phone, "email": email,
            "edu_license": edu_license
        }

        return data

    def get_student_data(self):
        f_name = self.f_name_box.get()
        l_name = self.l_name_box.get()
        password = self.password_box.get()
        address = self.address_box.get()
        ec_contact = self.emergency_contact_box.get()
        phone = self.ec_phone_box.get()
        relation = self.ec_relation.get()
        email = self.ec_email_box.get()
        current_grade = self.current_grade_box.get()
        medical = self.medical_notes_box.get()

        data = {
            "first_name": f_name, "last_name": l_name, "password": password, "address": address,
            "emergency_contact": ec_contact, "emergency_contact_phone": phone, "emergency_contact_email": email,
            "emergency_contact_relation": relation, "current_grade": current_grade, "medical": medical
        }

        return data

    def get_institution_data(self):

        name = self.name_box.get()
        password = self.password_box.get()
        address = self.address_box.get()
        min_grade = self.grade_min_box.get()
        max_grade = self.grade_max_box.get()
        phone = self.phone_box.get()
        institution_type = self.institution_type_box.get()

        data = {
            "name": name, "password": password, "address": address,
            "grade_min": min_grade, "grade_max": max_grade,
            "phone": phone, "instution_type": institution_type
        }

        return data

    def view_student(self, access_level, data):
        self.top.resizable(width=False, height=False)
        self.top.geometry("550x350")
        self.top.title("Student")

        # main frame
        frame = tk.Frame(self.top)
        frame.pack()

        # the items everyone can see
        # frames
        f_name_frame = tk.Frame(frame)
        f_name_frame.pack()

        l_name_frame = tk.Frame(frame)
        l_name_frame.pack()

        current_grade_frame = tk.Frame(frame)
        current_grade_frame.pack()

        current_institution_frame = tk.Frame(frame)
        current_institution_frame.pack()

        student_id_frame = tk.Frame(frame)
        student_id_frame.pack()

        # labels
        f_name_label = tk.Label(f_name_frame, text="First Name: ", anchor="nw")
        l_name_label = tk.Label(l_name_frame, text="Last Name: ", anchor="nw")
        current_grade_label = tk.Label(current_grade_frame, text="Current Grade: ", anchor="nw")
        current_institution_label = tk.Label(current_institution_frame, text="Current Institution: ", anchor="nw")
        student_id_label = tk.Label(student_id_frame, text="Student ID: ", anchor="nw")

        # data labels
        f_name = tk.Label(f_name_frame, text="Data", anchor="nw")
        l_name = tk.Label(l_name_frame, text="Data", anchor="nw")
        current_grade = tk.Label(current_grade_frame, text="Data", anchor="nw")
        current_institution = tk.Label(current_institution_frame, text="Data", anchor="nw")
        student_id = tk.Label(student_id_frame, text="Data", anchor="nw")

        # pack
        f_name_label.pack(side=tk.LEFT)
        f_name.pack(side=tk.LEFT)

        l_name_label.pack(side=tk.LEFT)
        l_name.pack(side=tk.LEFT)

        current_grade_label.pack(side=tk.LEFT)
        current_grade.pack(side=tk.LEFT)

        current_institution_label.pack(side=tk.LEFT)
        current_institution.pack(side=tk.LEFT)

        student_id_label.pack(side=tk.LEFT)
        student_id.pack(side=tk.LEFT)

        if access_level is 0 or access_level is 2:
            # institution view student
            ec_phone_frame = tk.Frame(frame)
            ec_phone_frame.pack()

            ec_email_frame = tk.Frame(frame)
            ec_email_frame.pack()

            emergency_contact_frame = tk.Frame(frame)
            emergency_contact_frame.pack()

            relation_frame = tk.Frame(frame)
            relation_frame.pack()

            medical_notes_frame = tk.Frame(frame)
            medical_notes_frame.pack()

            current_grade_frame = tk.Frame(frame)
            current_grade_frame.pack()

            address_frame = tk.Frame(frame)
            address_frame.pack()

            address_label = tk.Label(address_frame, text="Address: ", anchor="nw")
            emergency_contact_label = tk.Label(emergency_contact_frame, text="Emergency Contact Name: ", anchor="nw")
            ec_phone_label = tk.Label(ec_phone_frame, text="Emergency Contact Phone: ", anchor="nw")
            ec_email_label = tk.Label(ec_email_frame, text="Emergency Contact Email: ", anchor="nw")
            ec_relation_label = tk.Label(relation_frame, text="Emergency Contact Relation: ", anchor="nw")
            current_grade_label = tk.Label(current_grade_frame, text="Current Grade: ", anchor="nw")
            medical_notes_label = tk.Label(medical_notes_frame, text="Medical Notes: ", anchor="nw")

            # data
            address = tk.Label(address_frame, text="Data", anchor="nw")
            emergency_contact = tk.Label(emergency_contact_frame, text="Data", anchor="nw")
            ec_phone = tk.Label(ec_phone_frame, text="Data", anchor="nw")
            ec_email = tk.Label(ec_email_frame, text="Data", anchor="nw")
            ec_relation = tk.Label(relation_frame, text="Data", anchor="nw")
            current_grade = tk.Label(current_grade_frame, text="Data", anchor="nw")
            medical_notes = tk.Label(medical_notes_frame, text="Data", anchor="nw")

            address_label.pack(side=tk.LEFT)
            address.pack(side=tk.LEFT)

            emergency_contact_label.pack(side=tk.LEFT)
            emergency_contact.pack(side=tk.LEFT)

            ec_phone_label.pack(side=tk.LEFT)
            ec_phone.pack(side=tk.LEFT)

            ec_email_label.pack(side=tk.LEFT)
            ec_email.pack(side=tk.LEFT)

            ec_relation_label.pack(side=tk.LEFT)
            ec_relation.pack(side=tk.LEFT)

            current_grade_label.pack(side=tk.LEFT)
            current_grade.pack(side=tk.LEFT)

            medical_notes_label.pack(side=tk.LEFT)
            medical_notes.pack(side=tk.LEFT)

            return self.top
        elif access_level is 1:
            return  self.top
        else:
            return None

    def view_educator(self, access_level, data):
        self.top.resizable(width=False, height=False)
        self.top.geometry("550x350")
        self.top.title("Educator")

        # main frame
        frame = tk.Frame(self.top)
        frame.pack()

        f_name_frame = tk.Frame(frame)
        f_name_frame.pack()

        l_name_frame = tk.Frame(frame)
        l_name_frame.pack()

        email_frame = tk.Frame(frame)
        email_frame.pack()

        current_institution_frame = tk.Frame(frame)
        current_institution_frame.pack()

        # labels
        f_name_label = tk.Label(f_name_frame, text="First Name: ", anchor="nw")
        l_name_label = tk.Label(l_name_frame, text="Last Name: ", anchor="nw")
        email_label = tk.Label(email_frame, text="Email: ", anchor="nw")
        current_institution_label = tk.Label(current_institution_frame, text="Current Institution: ", anchor="nw")


        # data labels
        f_name = tk.Label(f_name_frame, text="Data", anchor="nw")
        l_name = tk.Label(l_name_frame, text="Data", anchor="nw")
        email = tk.Label(email_frame, text="Data", anchor="nw")
        current_institution = tk.Label(current_institution_frame, text="Data", anchor="nw")

        # pack
        f_name_label.pack(side=tk.LEFT)
        f_name.pack(side=tk.LEFT)

        l_name_label.pack(side=tk.LEFT)
        l_name.pack(side=tk.LEFT)

        email_label.pack(side=tk.LEFT)
        email.pack(side=tk.LEFT)

        current_institution_label.pack(side=tk.LEFT)
        current_institution.pack(side=tk.LEFT)

        if access_level is 2:
            return self.top
        elif access_level is 0 or access_level is 1:
            phone_frame = tk.Frame(frame)
            phone_frame.pack()

            address_frame = tk.Frame(frame)
            address_frame.pack()

            courses_frame = tk.Frame(frame)
            courses_frame.pack()

            pref_subject_frame = tk.Frame(frame)
            pref_subject_frame.pack()

            license_frame = tk.Frame(frame)
            license_frame.pack()

            # labels
            address_label = tk.Label(address_frame, text="Address: ", anchor="nw")
            courses_label = tk.Label(courses_frame, text="Courses Taught: ", anchor="nw")
            phone_label = tk.Label(phone_frame, text="Phone: ", anchor="nw")
            pref_subject_label = tk.Label(pref_subject_frame, text="Preferred Subjects: ", anchor="nw")
            edu_license_label = tk.Label(license_frame, text="Educational License: ", anchor="nw")

            address = tk.Label(address_frame, text="Data", anchor="nw")
            courses = tk.Label(courses_frame, text="Data", anchor="nw")
            phone = tk.Label(phone_frame, text="Data", anchor="nw")
            pref_subject = tk.Label(pref_subject_frame, text="Data", anchor="nw")
            edu_license = tk.Label(license_frame, text="Data", anchor="nw")

            # pack
            address_label.pack(side=tk.LEFT)
            address.pack(side=tk.LEFT)

            courses_label.pack(side=tk.LEFT)
            courses.pack(side=tk.LEFT)

            phone_label.pack(side=tk.LEFT)
            phone.pack(side=tk.LEFT)

            pref_subject_label.pack(side=tk.LEFT)
            pref_subject.pack(side=tk.LEFT)

            edu_license_label.pack(side=tk.LEFT)
            edu_license.pack(side=tk.LEFT)

            return self.top
        else:
            return None

    def view_institution(self, access_level, data):
        self.top.resizable(width=False, height=False)
        self.top.geometry("550x350")
        self.top.title("Institution")

        # main frame
        frame = tk.Frame(self.top)
        frame.pack()

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
        name_label = tk.Label(name_frame, text="Institution Name: ", anchor="nw")
        address_label = tk.Label(address_frame, text="Address: ", anchor="nw")
        institution_type_label = tk.Label(type_frame, text="Institution Type: ", anchor="nw")
        grade_min_label = tk.Label(grade_min_frame, text="Lowest Grade: ", anchor="nw")
        grade_max_label = tk.Label(grade_max_frame, text="Highest Grade: ", anchor="nw")
        phone_label = tk.Label(phone_frame, text="Institution Phone: ", anchor="nw")

        name = tk.Label(name_frame, text=data[0], anchor="nw")
        address = tk.Label(address_frame, text=data[1], anchor="nw")
        institution_type = tk.Label(type_frame, text=data[2], anchor="nw")
        grade_min = tk.Label(grade_min_frame, text=data[3], anchor="nw")
        grade_max = tk.Label(grade_max_frame, text=data[4], anchor="nw")
        phone = tk.Label(phone_frame, text=data[5], anchor="nw")


        name_label.pack(side=tk.LEFT)
        name.pack(side=tk.LEFT)

        address_label.pack(side=tk.LEFT)
        address.pack(side=tk.LEFT)

        institution_type_label.pack(side=tk.LEFT)
        institution_type.pack(side=tk.LEFT)

        grade_min_label.pack(side=tk.LEFT)
        grade_min.pack(side=tk.LEFT)

        grade_max_label.pack(side=tk.LEFT)
        grade_max.pack(side=tk.LEFT)

        phone_label.pack(side=tk.LEFT)
        phone.pack(side=tk.LEFT)

        return self.top

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
        self.top.resizable(width=False, height=False)
        self.top.geometry("550x350")
        self.top.title("Institution")

        # main frame
        frame = tk.Frame(self.top)
        frame.pack()

        # frames
        name_frame = tk.Frame(frame)
        name_frame.pack()

        courses_frame = tk.Frame(frame)
        courses_frame.pack()

        name_label = tk.Label(name_frame, text="Course Name", anchor="nw")
        name_label.pack()

        courses_label = tk.Label(courses_frame, text="Courses: ", anchor="nw")
        courses_label.pack()

        return self.top

    def add_license(self):
        # add a license to a teacher
        pass

    def view_history(self):
        # view a students history
        pass

    def add_medical_note(self):
        # add a medical note to a students account
        pass

    def add_note(self):
        # form add notes to records
        self.top.resizable(width=False, height=False)
        self.top.geometry("550x350")

        # main frame
        frame = tk.Frame(self.top)
        frame.pack(pady=25)

        self.top.title("Add Notes")

        # frames
        name_frame = tk.Frame(frame)
        name_frame.pack()

        # labels
        name_label = tk.Label(name_frame, text="Add Notes: ", anchor="nw")
        name_label.pack()

        # text field
        text_frame = tk.Frame(frame)
        text_frame.pack()

        self.note = tk.Text(text_frame)
        self.note.pack()

        return self.top

    def view_note(self):
        # view a students notes
        pass

    def view_grade(self):
        # finds and displays a students grade
        pass

    def edit_account_info(self):
        # edit form
        pass

    def view_profile(self):
        # view a given profile
        pass
