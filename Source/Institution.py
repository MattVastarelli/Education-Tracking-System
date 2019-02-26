
from Source.Account import Account
from Source.Educator import Educator
from Source.Student import Student

from Source import forms
import tkinter as tk

class Institution(Account):

    def __init__(self, username, password, access, name, address, institution_type, grade_min, grade_max,
                 main_phone_num):

        super().__init__(username, password, access)

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
        e = forms.Form()  # create instance
        top = e.add_new(access_level=2)  # call the method to receive the top level obj
        top.title("Add New Educator")
        button_frame = tk.Frame(top)
        button_frame.pack()
        save_button = tk.Button(button_frame, text="Save", command=None)
        save_button.pack(side=tk.LEFT)
        close_button = tk.Button(button_frame, text="Close", command=top.destroy)
        close_button.pack(side=tk.LEFT)
        top.mainloop()

    # private
    # add student object with level = 2
    def __add_student(self, access_level=2):
        s = forms.Form()  # create instance
        top = s.add_new(access_level=2)  # call the method to receive the top level obj
        top.title("Add New Student")
        button_frame = tk.Frame(top)
        button_frame.pack()

        save_button = tk.Button(button_frame, text="Save", command=lambda: self.create_new(2, s.f_name_box.get()))
        save_button.pack(side=tk.LEFT)
        close_button = tk.Button(button_frame, text="Close", command=top.destroy)
        close_button.pack(side=tk.LEFT)

        top.mainloop()  # run the code

    # private
    # view institution self
    def __view_institution(self):
        pass

    # private
    # view educator profile
    def __view_educator(self):
        pass

    # private
    # view student profile
    def __view_student(self):
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

    # private
    def __view(self):
        pass

    # private
    def __edit(self):
        pass

    # private
    def create_new(self, access_level, something):
        if access_level is 2:
            print(something)

        return None

if __name__ == '__main__':
    i = Institution(username="GT", password="0000", access=0, name="CHT", address="300 Boston Post Rd", institution_type="A", grade_min=0, grade_max=100, main_phone_num=203-000-1111)
    #i._Institution__add_student()
    i.add_student(2)

