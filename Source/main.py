from Source.Account import Account
from Source.Educator import Educator
from Source.forms import Form
from Source.Student import Student
from Source.Institution import Institution
import tkinter as tk
import csv
import os

class Main:
    def __init__(self):
        self.edu = list()
        self.inst = str()
        self.stu = list()

    def log_in_search(self, login_data, f):
        user = login_data['user_name']
        password = login_data['password']

        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/users.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        user_name_match = False
        password_match = False

        with open(abs_file_path) as file:
            content = file.readlines()
            content = [x.strip() for x in content]

            for line in content:
                split = line.split()  # choose split type
                # print(split)

                if user in split[0]:
                    user_name_match = True
                if password in split[1]:
                    password_match = True

                if user_name_match and password_match:
                    print(split)
                    data = {
                        "user_name": user, "password": password, "user_id": split[3], "access_level": split[2]
                    }
                    break
        file.close()

        if int(split[2]) is 0:
            obj = self.create_institution_obj(data, False, f)
        elif int(split[2]) is 1:
            pass
            obj = self.create_educator_obj(data, False, f)
        elif int(split[2]) is 2:
            pass
            obj = self.create_student_obj(data, False, f)
        else:
            return None

        self.main_screen(int(split[2]), obj, f)
        return None

    def write_to_file(self, obj_type, data):
        # write to the correct user type file
        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/" + obj_type + "s.txt"  # student , institution, educator
        # rel_path = 'db/test.txt'
        abs_file_path = os.path.join(script_dir, rel_path)

        file = open(abs_file_path, 'a', newline='')
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(data)
        file.close()

        # write the the users file
        user_path = "db/users.txt"  # student , institution, educator
        abs_file_path = os.path.join(script_dir, user_path)

        user_file = open(abs_file_path, 'a', newline='')
        user_data = [data[2], data[3], data[0], data[1]]  # username, pass, access level, user_id
        user_writer = csv.writer(user_file, delimiter='\t')
        user_writer.writerow(user_data)
        user_file.close()

        return None

    def start_screen(self):
        f = Form()

        go = f.start_screen()

        frame = tk.Frame(go)
        frame.pack(pady=100)

        institution_frame = tk.Frame(frame)
        institution_frame.pack()

        log_in_frame = tk.Frame(frame)
        log_in_frame.pack(pady=30)

        log_in_button = tk.Button(log_in_frame, text="Log In", command=lambda: self.log_in(f))
        log_in_button.pack(side=tk.LEFT)

        institution_button = tk.Button(institution_frame, text="Create new Institution",
                                       command=lambda: self.first_creation(f))
        institution_button.pack(side=tk.LEFT)

        go.mainloop()

        return None

    def create_institution_obj(self, data, is_new, f):

        if is_new:
            inst = Institution(data['name'], data['password'], 0, is_new)
            data_list = [data['name'], data["address"], data['instution_type'], data['grade_max'],
                         data['grade_min'], data['phone']]

            inst.set_data(data_list)

            write_list = [inst.ownerID, 0, data['name'], data['password'], data['name'], data["address"],
                          data['instiution_type'], data['grade_min'], data['grade_max'], data['phone']]

            self.write_to_file('institution', write_list)
            self.main_screen(0, inst, f)
        else:
            inst = Institution(data['user_name'], data['password'], 0, is_new)
            # "user_name": user, "password": password, "user_id": split[3], "access_level": split[2]
            # search for record
            script_dir = os.path.dirname(__file__)  # absolute dir the script is in
            rel_path = "db/institutions.txt"
            abs_file_path = os.path.join(script_dir, rel_path)

            return_list = list()

            with open(abs_file_path) as f:
                content = f.readlines()
                content = [x.strip() for x in content]

                for line in content:
                    split = line.split("\t")  # choose split type
                    if split[0] == data['user_id']:
                        return_list = split

            f.close()
            # fill in data
            print(return_list)
            inst.set_id(return_list[0])
            inst.set_data(return_list[4:])

            return inst

    def create_educator_obj(self, data, is_new, f):
        f.destroy()

        f = Form()

        educ = Educator(data['user_name'], data['password'], is_new)

        if is_new:
            data_list = [
                data['first_name'], data["last_name"], data["address"], data['phone'],
                data['email'], data['emp_ID'], data['licenses'], data['preferred_courses'],
                data['preferred_subjects'], data['grade_levels'], data['current_inst_ID']
            ]

            educ.set_data(data_list)

            write_list = [
                educ.ownerID, 1, data['user_name'], data['password'], data['first_name'],
                data["last_name"], data["address"], data['phone'], data['email'], data['emp_ID'],
                data['licenses'], data['preferred_courses'], data['preferred_subjects'],
                data['grade_levels'], data['current_inst_ID']
            ]

            self.write_to_file('educator', write_list)
            self.main_screen(0, educ, f)
        else:
            # "user_name": user, "password": password, "user_id": split[3], "access_level": split[2]
            # search for record
            script_dir = os.path.dirname(__file__)  # absolute dir the script is in
            rel_path = "db/educators.txt"
            abs_file_path = os.path.join(script_dir, rel_path)

            return_list = list()

            with open(abs_file_path) as f:
                content = f.readlines()
                content = [x.strip() for x in content]

                for line in content:
                    split = line.split("\t")  # choose split type
                    # print(split)
                    if split[0] == data['user_id']:
                        return_list = line.split("\t")
                        break
            f.close()
            # fill in data
            print(return_list)
            educ.set_id(return_list[0])
            educ.set_data(return_list[4:])

            return educ

    def create_student_obj(self, data, is_new, f):
        f.destroy()
        f = Form()

        stud = Student(data['user_name'], data['password'], 2, is_new)

        if is_new:
            data_list = [
                data['first_name'], data["last_name"], data["student_ID"], data["ec_name"],
                data['ec_relationship'], data['ec_email'], data['med_notes'],
                data['grade_level'], data['current_inst_ID'], data['grades'],
                data['grade_notes'], data['address']
            ]

            stud.set_data(data_list)

            write_list = [stud.ownerID, 2, data['first_name'], data["last_name"], data["student_ID"], data["ec_name"],
                          data['ec_relationship'], data['ec_email'], data['med_notes'], data['grade_level'],
                          data['current_inst_ID'], data['grades'], data['grade_notes'], data['address']]

            self.write_to_file('student', write_list)
            self.main_screen(0, stud, f)
        else:
            # "user_name": user, "password": password, "user_id": split[3], "access_level": split[2]
            # search for record
            script_dir = os.path.dirname(__file__)  # absolute dir the script is in
            rel_path = "db/students.txt"
            abs_file_path = os.path.join(script_dir, rel_path)

            return_list = list()

            with open(abs_file_path) as f:
                content = f.readlines()
                content = [x.strip() for x in content]

                for line in content:
                    split = line.split("\t")  # choose split type
                    # print(split)
                    if split[0] == data['user_id']:
                        return_list = line.split("\t")
                        break
            f.close()
            # fill in data
            print(return_list)
            stud.set_id(return_list[0])
            stud.set_data(return_list[4:])

            return stud

    def institution_creation(self, f):
        f.destroy()
        f = Form()

        f.add_new(0)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Back", command=lambda: self.main_screen(0, None, f))
        back.pack(side=tk.LEFT, padx=10)

        save_button = tk.Button(button_frame, text="Save",
                                command=lambda: self.create_institution_obj(f.get_institution_data(), True, f))
        save_button.pack(side=tk.LEFT)

        return None

    def first_creation(self, f):
        f.destroy()
        f = Form()

        f.add_new(0)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Close", command=f.destroy)
        back.pack(side=tk.LEFT, padx=10)

        save_button = tk.Button(button_frame, text="Save",
                                command=lambda: self.create_institution_obj(f.get_institution_data(), True, f))
        save_button.pack(side=tk.LEFT)

        return None

    def student_creation(self, f):
        f.destroy()
        f = Form()

        f.add_new(2)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Back", command=lambda: self.main_screen(0, None, f))
        back.pack(side=tk.LEFT, padx=10)

        save_button = tk.Button(button_frame, text="Save", command=lambda: self.create_student_obj(None, False, f))
        save_button.pack(side=tk.LEFT)

        return None

    def educator_creation(self, f):
        f.destroy()
        f = Form()

        f.add_new(1)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Back", command=lambda: self.main_screen(0, None, f))
        back.pack(side=tk.LEFT, padx=10)

        save_button = tk.Button(button_frame, text="Save", command=lambda: self.create_educator_obj(None, False, f))
        save_button.pack(side=tk.LEFT)

        return None

    def view_edu(self, access_level, user, f):
        f.destroy()
        f = Form()

        # get the data from the obj
        data = [user.get_name()]
        data.extend(user.get_personal_info())
        data.extend(user.get_professional_info())
        print(data)

        f.view_educator(user.accessLevel, data)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Back", command=lambda: self.main_screen(access_level, None, f))
        back.pack(side=tk.LEFT, padx=10)

        return None

    def view_inst(self,access_level, user, f):
        f.destroy()
        f = Form()

        # get the data form the obj
        data = [user.get_name(), user.get_address(), user.get_institution_type(),
                user.get_grade_min(), user.get__grade_max(), user.get_main_phone_num()]

        f.view_institution(user.accessLevel, data)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Back", command=lambda: self.main_screen(access_level, None, f))
        back.pack(side=tk.LEFT, padx=10)

        return None

    def view_student(self, access_level, user, f):
        f.destroy()
        f = Form()

        # get the data form the obj
        data = [user.get_name(), user.get_student_id(), user.get_current_grade(), user.get_current_institution(),
                user.get_home_address(), user.get_emergency_contact(), user.get_relationship(), user.get_ec_email(),
                user.get_medical_notes(), user.get_grades()]

        f.view_student(access_level, data)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Back", command=lambda: self.main_screen(access_level, None, f))
        back.pack(side=tk.LEFT, padx=10)

        return None

    def main_screen(self, access_level, user, f):
        f.destroy()

        f = Form()
        f.main_screen()

        frame = tk.Frame()
        frame.pack(pady=50)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        button_frame_1 = tk.Frame(frame)
        button_frame_1.pack()

        button_frame_2 = tk.Frame(frame)
        button_frame_2.pack()

        button_frame_3 = tk.Frame(frame)
        button_frame_3.pack()

        button_frame_4 = tk.Frame(frame)
        button_frame_4.pack()

        button_frame_5 = tk.Frame(frame)
        button_frame_5.pack()

        button_frame_6 = tk.Frame(frame)
        button_frame_6.pack()

        if access_level is 0:
            new_edu_button = tk.Button(button_frame, text="New Educator", command=lambda: self.educator_creation(f))
            new_edu_button.pack(side=tk.LEFT, pady=10)

            new_inst_button = tk.Button(button_frame_1, text="New Institution",
                                        command=lambda: self.institution_creation(f))
            new_inst_button.pack(side=tk.LEFT, pady=10)

            new_student_button = tk.Button(button_frame_2, text="New Student",
                                           command=lambda: self.student_creation(f))
            new_student_button.pack(side=tk.LEFT, pady=10)

            """ will error need intermediate screen to pick teacher """
            view_edu_button = tk.Button(button_frame_3, text="View Educator",
                                        command=lambda: self.view_edu(0, None, f))
            view_edu_button.pack(side=tk.LEFT, pady=10)

            view_inst_button = tk.Button(button_frame_4, text="View Institution",
                                         command=lambda: self.view_inst(0, user, f))
            view_inst_button.pack(side=tk.LEFT, pady=10)
            """ will error need intermediate screen to pick student """
            view_student_button = tk.Button(button_frame_5, text="View Student",
                                            command=lambda: self.view_student(0, None, f))
            view_student_button.pack(side=tk.LEFT, pady=10)

        if access_level is 1:
            view_edu_button = tk.Button(button_frame_3, text="View Educator", command=lambda: self.view_edu(1, user, f))
            view_edu_button.pack(side=tk.LEFT, pady=10)
            """ need find inst that the edu belongs to """
            view_inst_button = tk.Button(button_frame_4, text="View Institution",
                                         command=lambda: self.view_inst(1, None, f))
            view_inst_button.pack(side=tk.LEFT, pady=10)
            """ will error need intermediate screen to pick student """
            view_student_button = tk.Button(button_frame_5, text="View Student",
                                            command=lambda: self.view_student(1, None, f))
            view_student_button.pack(side=tk.LEFT, pady=10)

        if access_level is 2:
            view_student_button = tk.Button(button_frame_5, text="View Student",
                                            command=lambda: self.view_student(2, user, f))
            view_student_button.pack(side=tk.LEFT, pady=10)
            """ need find inst that the edu belongs to """
            view_inst_button = tk.Button(button_frame_4, text="View Institution",
                                         command=lambda: self.view_inst(2, None, f))
            view_inst_button.pack(side=tk.LEFT, pady=10)

        close_button = tk.Button(button_frame_6, text="Log Out", command=lambda: self.log_in(f))
        close_button.pack(side=tk.LEFT, padx=10)

        return None

    def log_in(self, f):
        f.destroy()
        f = Form()

        f.log_in()

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        close_button = tk.Button(button_frame, text="Close", command=f.destroy)
        close_button.pack(side=tk.LEFT, padx=10)

        log_in_button = tk.Button(button_frame, text="Log In",
                                  command=lambda: self.log_in_search(f.get_login_data(), f))
        log_in_button.pack(side=tk.LEFT, padx=10)

        return None

    def run(self):
        self.start_screen()


if __name__ == '__main__':
    m = Main()
    m.run()
