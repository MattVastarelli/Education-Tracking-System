
from Source.Account import Account
from Source import forms
import tkinter as tk


class Institution(Account):

    def __init__(self, username, password, access, name, address, institution_type, grade_min, grade_max,
                 main_phone_num):

        super().__init__(username, password, access)

        self.username = username
        self.password = password
        self.access = access

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

    def __get_name(self):
        return self.name

    def __get_address(self):
        return self.address

    def __get_institution_type(self):
        return self.institution_type

    def __get_grade_min(self):
        return self.grade_min

    def __get__grade_max(self):
        return self.grade_max

    def __get_main_phone_num(self):
        return self.main_phone_num

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

        # form to add a new record
        self.top = tk.Tk()
        self.top.resizable(width=False, height=False)
        self.top.geometry("550x350")

        # main frame
        frame = tk.Frame(self.top)
        frame.pack()

        self.top.title("View Institution")

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

        # set string variable to entry box
        self.e1_name = tk.StringVar(self.top)
        self.e1_name.set(self.__get_name())

        self.e2_password = tk.StringVar(self.top)
        self.e2_password.set(self.password)

        self.e3_address = tk.StringVar(self.top)
        self.e3_address.set(self.__get_address())

        self.e4_grade_min = tk.StringVar(self.top)
        self.e4_grade_min.set(self.__get_grade_min())

        self.e5_grade_max = tk.StringVar(self.top)
        self.e5_grade_max.set(self.__get__grade_max())

        self.e6_main_phone_num = tk.StringVar(self.top)
        self.e6_main_phone_num.set(self.__get_main_phone_num())

        self.e7_institution_type = tk.StringVar(self.top)
        self.e7_institution_type.set(self.__get_institution_type())

        # labels
        name = tk.Label(name_frame, text="Institution Name: ", anchor="nw")
        password = tk.Label(password_frame, text="Password: ", anchor="nw")
        address = tk.Label(address_frame, text="Address: ", anchor="nw")
        grade_min = tk.Label(grade_min_frame, text="Lowest Grade: ", anchor="nw")
        grade_max = tk.Label(grade_max_frame, text="Highest Grade: ", anchor="nw")
        phone = tk.Label(phone_frame, text="Institution Phone: ", anchor="nw")
        institution_type = tk.Label(type_frame, text="Institution Type: ", anchor="nw")

        # text boxes
        self.name_box = tk.Entry(name_frame, textvariable=self.e1_name)
        self.password_box = tk.Entry(password_frame, textvariable=self.e2_password)
        self.address_box = tk.Entry(address_frame, textvariable=self.e3_address)
        self.grade_min_box = tk.Entry(grade_min_frame, textvariable=self.e4_grade_min)
        self.grade_max_box = tk.Entry(grade_max_frame, textvariable=self.e5_grade_max)
        self.phone_box = tk.Entry(phone_frame, textvariable=self.e6_main_phone_num)
        self.institution_type_box = tk.Entry(type_frame, textvariable=self.e7_institution_type)

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

        self.top.mainloop()

        return self.top

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
    i = Institution(username="GT", password="0000", access=0, name="CHT", address="300 Boston Post Rd", institution_type="A", grade_min=0, grade_max=100, main_phone_num='203-000-1111')
    i._Institution__view_institution()
