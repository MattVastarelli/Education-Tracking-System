import tkinter as tk
import tkinter.messagebox as message_box


class Form(tk):
    # main forms class

    def __int__(self):
        self.top = tk.Tk()

    def add_new(self, access_level=0):
        # form to add a new record

        if access_level is 1:
            pass
        elif access_level is 2:
            pass
        else:
            message_box.showerror(title="Error", message="Invalid selection")

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
