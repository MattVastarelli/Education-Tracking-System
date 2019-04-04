from Source.Account import Account
from Source.Educator import Educator
from Source.forms import Form
from Source.Student import Student
from Source.Institution import Institution
from Source.standards import Standards
import tkinter as tk
import csv
import os

class Main:
    def __init__(self):
        self.edu_list = list()
        self.inst = str()
        self.stu_list = list()
        self.user = None

    def log_in_search(self, login_data, f):
        user = login_data['user_name']
        password = login_data['password']

        self.edu_list = list()
        self.stu_list = list()

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
                    #print(split)
                    data = {
                        "user_name": user, "password": password, "user_id": split[3], "access_level": split[2]
                    }
                    break
        file.close()

        if int(split[2]) is 0:
            obj = self.create_institution_obj(data, False, f)
            self.user = obj
            self.get_inst_educators(self.user.get_id())
            self.get_inst_students(self.user.get_id())
        elif int(split[2]) is 1:
            pass
            obj = self.create_educator_obj(data, False, f)
            self.user = obj
        elif int(split[2]) is 2:
            pass
            obj = self.create_student_obj(data, False, f)
            self.user = obj
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

    def view_all_edu_courses(self, f, flag):
        f.destroy()
        f = Form()

        if flag == 0:
            f.view_courses(self.edu_list, flag)
        else:
            #print(type(self.user.get_courses()))
            f.view_courses(self.user.get_courses(), 1)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Back", command=lambda: self.main_screen(0, None, f))
        back.pack(side=tk.LEFT, padx=10)

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

            with open(abs_file_path) as file:
                content = file.readlines()
                content = [x.strip() for x in content]

                for line in content:
                    split = line.split("\t")  # choose split type
                    if split[0] == data['user_id']:
                        return_list = split

            file.close()
            # fill in data
            #(return_list)
            inst.set_id(return_list[0])
            inst.set_data(return_list[4:])

            return inst

    def create_educator_obj(self, data, is_new, f):

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

            with open(abs_file_path) as file:
                content = file.readlines()
                content = [x.strip() for x in content]

                for line in content:
                    split = line.split("\t")  # choose split type
                    # print(split)
                    if split[0] == data['user_id']:
                        return_list = line.split("\t")
                        break
            file.close()
            # fill in data
            #print(return_list)
            educ.set_id(return_list[0])
            educ.set_data(return_list[4:])

            return educ

    def search_student_form(self,  access_level, f):
        f.destroy()
        f = Form()
        f.search_screen()

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        var = tk.IntVar()

        R1 = tk.Radiobutton(button_frame, text="Last Name", variable=var, value=1)
        R1.pack(pady=2)

        R2 = tk.Radiobutton(button_frame, text="Student Id", variable=var, value=2)
        R2.pack(pady=2)

        new_search_button = tk.Button(button_frame, text="Search",
                                      command=lambda: self.search_for_student(access_level, f, var.get(),
                                                                              f.search_box.get()))
        new_search_button.pack(pady=2)

        back_button = tk.Button(button_frame, text="Back",
                                      command=lambda: self.main_screen(self.user.accessLevel, self.user, f))
        back_button.pack(pady=2)

        return None

    def student_view_reports(self, f):
        f.destroy()
        f = Form()

        feedback = self.search(thing_to_match=self.user.get_student_id(), file_name_to_search="studentReports", split_type=",")
        #t(feedback[0])

        edu_list = list()
        feedback_list = list()
        for x in feedback:
            count = 0
            for y in x:
                if count == 0:
                    count += 1
                    continue
                elif count == 1:
                    edu = self.search(str(y), "educators", "\t")
                    edu_list.append(edu[0][4] + " " + edu[0][5])
                else:
                    feedback_list.append(y)
                count += 1

        f.view_edu_feedback(edu_list[0], feedback_list[0])

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back_button = tk.Button(button_frame, text="Back",
                                command=lambda: self.main_screen(self.user.accessLevel, self.user, f))
        back_button.pack(pady=2)

        return None

    def search(self, thing_to_match, file_name_to_search, split_type):
        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/" + file_name_to_search + ".txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        data_list = list()

        with open(abs_file_path) as file:
            content = file.readlines()
            content = [x.strip() for x in content]

            for line in content:
                split = line.split(split_type)  # choose split type
                #print(split)
                if thing_to_match in split:
                    #print(split)
                    data_list.append(split)

        # returns a list of list
        return  data_list

    def search_for_student(self, access_level, f, var, data):
        #f.destroy()
        #f = Form()

        index = -1
        student = None
        if var is 1:
            index = 5
        else:
            index = 6

        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/students.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        studentData = list()
        match = False
        with open(abs_file_path) as file:
            content = file.readlines()
            content = [x.strip() for x in content]

            for line in content:
                split = line.split("\t")  # choose split type
                if data == split[index]:
                    #print(split)
                    match = True
                    studentData = split
                    student = Student(username=studentData[2], password=studentData[3], access_level=2, is_new=False)

                    student.set_data([studentData[4], studentData[5], studentData[6], studentData[7],
                                     studentData[8], studentData[9], studentData[10], studentData[11],
                                      studentData[12], studentData[13], studentData[14], studentData[15]])

                    self.view_student(access_level, student, f)
        if match is False:
            self.search_student_form(access_level, f)

        return None

    def view_standards(self, f, flag, data):
        f.destroy()
        f = Form()

        # do init search for all standards fore a given inst then filter
        id = int()

        if type(self.user) == Student:
            id = self.user.get_inst_id()
        elif type(self.user) == Educator:
            id = self.user.currentInst
        else:
            id = self.user.get_id()

        rows = self.search(thing_to_match=str(id), file_name_to_search="standards", split_type=",")

        #print(rows)
        standards_list = list()
        if flag == 1:
            # search
            pass
        else:
            # view all
            for x in rows:
                count = 0
                sub = ""
                for y in x:
                    if count == 0:
                        count += 1
                        continue
                    elif count == 1:
                        #print("Subject", y)
                        sub = y
                    else:
                        #print("Range", y)
                        a_range = y # y.split(" ")
                        standards_list.append(Standards(subject=sub, acc_range=a_range))

                    count += 1

        f.view_standards(standards=standards_list)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back_button = tk.Button(button_frame, text="Back",
                                command=lambda: self.main_screen(self.user.accessLevel, self.user, f))
        back_button.pack(pady=15)

        return None

    def search_standards(self, f):
        f.destroy()
        f = Form()
        f.search_screen()

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        var = tk.IntVar()

        R1 = tk.Radiobutton(button_frame, text="Subject", variable=var, value=1)
        R1.pack(pady=2)

        new_search_button = tk.Button(button_frame, text="Search",
                                      command=lambda: self.view_standards(f, 1, f.search_box.get()))
        new_search_button.pack(pady=2)

        view_all_button = tk.Button(button_frame, text="View All",
                                      command=lambda: self.view_standards(f, 0, f.search_box.get()))
        view_all_button.pack(pady=2)

        back_button = tk.Button(button_frame, text="Back",
                                command=lambda: self.main_screen(self.user.accessLevel, self.user, f))
        back_button.pack(pady=15)

        return None

    def search_edu_form(self,  access_level, f,):
        f.destroy()
        f = Form()
        f.search_screen()

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        var = tk.IntVar()

        R1 = tk.Radiobutton(button_frame, text="Last Name", variable=var, value=1)
        R1.pack(pady=2)

        R2 = tk.Radiobutton(button_frame, text="Educator Id", variable=var, value=2)
        R2.pack(pady=2)

        new_search_button = tk.Button(button_frame, text="Search",
                                      command=lambda: self.search_for_edu(access_level, f, var.get(), f.search_box.get()))
        new_search_button.pack(pady=2)

        back_button = tk.Button(button_frame, text="Back",
                                command=lambda: self.main_screen(self.user.accessLevel, self.user, f))
        back_button.pack(pady=2)

        return None

    def get_feedback(self, id):
        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/feedback.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path) as file:
            content = file.readlines()
            content = [x.strip() for x in content]
            for line in content:
                split = line.split(",")  # choose split type

                if str(id) == split[0]:  # last item
                    return split[1]

        return ""

    def feedback_search(self, f):
        f.destroy()
        f = Form()
        f.search_screen()

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        var = tk.IntVar()

        #R1 = tk.Radiobutton(button_frame, text="Last Name", variable=var, value=1)
        #R1.pack(pady=2)

        R2 = tk.Radiobutton(button_frame, text="Educator Id", variable=var, value=2)
        R2.pack(pady=2)

        new_search_button = tk.Button(button_frame, text="Search",
                                      command=lambda: self.view_feedback(f.search_box.get(), f))
        new_search_button.pack(pady=2)

        back_button = tk.Button(button_frame, text="Back",
                                command=lambda: self.main_screen(self.user.accessLevel, self.user, f))
        back_button.pack(pady=2)

        return None

    def view_feedback(self, data, f):
        f.destroy()
        f = Form()
        name = None
        for edu in self.edu_list:
            if edu.get_id() == data:
                name = edu.get_name()
                f.view_edu_feedback(name, edu.get_feedback())

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back_button = tk.Button(button_frame, text="Back",
                                command=lambda: self.main_screen(self.user.accessLevel, self.user, f))
        back_button.pack(pady=2)

        return None

    def get_inst_educators(self, inst_ID):
        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/educators.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path) as file:
            content = file.readlines()
            content = [x.strip() for x in content]

            for line in content:
                split = line.split("\t")  # choose split type
                if inst_ID == split[-1]: # last item
                    edu_data = split
                    edu = Educator(username=edu_data[2], password=edu_data[3], is_new=False)

                    edu.set_data(edu_data[4:])
                    edu.set_feedback(self.get_feedback(edu.get_id()))
                    self.edu_list.append(edu)
        return None

    def get_inst_students(self, id_to_match):
        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/students.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        studentData = list()
        with open(abs_file_path) as file:
            content = file.readlines()
            content = [x.strip() for x in content]

            for line in content:
                split = line.split("\t")  # choose split type
                if id_to_match == split[12]:
                    #print(split)
                    match = True
                    studentData = split
                    student = Student(username=studentData[2], password=studentData[3], access_level=2, is_new=False)

                    student.set_data([studentData[4], studentData[5], studentData[6], studentData[7],
                                      studentData[8], studentData[9], studentData[10], studentData[11],
                                      studentData[12], studentData[13], studentData[14], studentData[15]])
                    self.stu_list.append(student)

        return None

    def search_for_edu(self, access_level, f, var, data):
        # f.destroy()
        #f = Form()

        match = False
        index = -1
        if var is 1:
            index = 5
        else:
            index = 0

        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/educators.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path) as file:
            content = file.readlines()
            content = [x.strip() for x in content]

            for line in content:
                split = line.split("\t")  # choose split type
                if data == split[index]:
                    #print(split)
                    match = True
                    edu_data = split
                    edu = Educator(username=edu_data[2], password=edu_data[3], is_new=False)

                    edu.set_data(edu_data[4:])
                    edu.set_feedback(self.get_feedback(edu.get_id()))
                    self.view_edu(access_level, edu, f)

        if match is False:
            self.search_edu_form(access_level, f)

        return None

    def get_standards(self, standards):
        f = Form()

        f.view_standards(standards)

        return None

    def create_student_obj(self, data, is_new, f):

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

            with open(abs_file_path) as file:
                content = file.readlines()
                content = [x.strip() for x in content]

                for line in content:
                    split = line.split("\t")  # choose split type
                    # print(split)
                    if split[0] == data['user_id']:
                        return_list = line.split("\t")
                        break
            file.close()
            # fill in data
            #print(return_list)
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

    def view_edu(self, access_level, edu, f):
        f.destroy()
        f = Form()

        # get the data from the obj
        data = [edu.get_name()]
        data.extend(edu.get_personal_info())
        data.extend(edu.get_professional_info())
        #print(data)

        f.view_educator(access_level, data)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Back", command=lambda: self.main_screen(access_level, None, f))
        back.pack(side=tk.LEFT, padx=10)

        return None

    def view_inst(self,access_level, inst, f):
        f.destroy()
        f = Form()

        # get the data form the obj
        data = [inst.get_name(), inst.get_address(), inst.get_institution_type(),
                inst.get_grade_min(), inst.get__grade_max(), inst.get_main_phone_num()]

        f.view_institution(access_level, data)

        frame = tk.Frame()
        frame.pack(pady=10)

        button_frame = tk.Frame(frame)
        button_frame.pack()

        back = tk.Button(button_frame, text="Back", command=lambda: self.main_screen(access_level, None, f))
        back.pack(side=tk.LEFT, padx=10)

        return None

    def view_student(self, access_level, stu, f):
        f.destroy()
        f = Form()

        # get the data form the obj
        data = [stu.get_name(), stu.get_student_id(), stu.get_current_grade(), stu.get_current_institution(),
                stu.get_home_address(), stu.get_emergency_contact(), stu.get_relationship(), stu.get_ec_email(),
                stu.get_medical_notes(), stu.get_grades()]

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

        button_frame_7 = tk.Frame(frame)
        button_frame_7.pack()

        standards_frame = tk.Frame(frame)
        standards_frame.pack()

        close_frame = tk.Frame(frame)
        close_frame.pack()

        if access_level is 0:
            new_edu_button = tk.Button(button_frame, text="New Educator", command=lambda: self.educator_creation(f))
            new_edu_button.pack(side=tk.LEFT, pady=10)

            new_inst_button = tk.Button(button_frame_1, text="New Institution",
                                        command=lambda: self.institution_creation(f))
            new_inst_button.pack(side=tk.LEFT, pady=10)

            new_student_button = tk.Button(button_frame_2, text="New Student",
                                           command=lambda: self.student_creation(f))
            new_student_button.pack(side=tk.LEFT, pady=10)

            view_edu_button = tk.Button(button_frame_3, text="View Educator",
                                        command=lambda: self.search_edu_form(0, f))
            view_edu_button.pack(side=tk.LEFT, pady=10)

            view_inst_button = tk.Button(button_frame_4, text="View Institution",
                                         command=lambda: self.view_inst(0, user, f))
            view_inst_button.pack(side=tk.LEFT, pady=10)

            view_student_button = tk.Button(button_frame_5, text="View Student",
                                            command=lambda: self.search_student_form(0, f))
            view_student_button.pack(side=tk.LEFT, pady=10)

            view_edu_courses = tk.Button(button_frame_6, text="View All Educator Courses",
                                            command=lambda: self.view_all_edu_courses(f, 0))
            view_edu_courses.pack(side=tk.LEFT, pady=10)

            view_edu_feedback = tk.Button(button_frame_7, text="Educator Feedback",
                                         command=lambda: self.feedback_search(f))
            view_edu_feedback.pack(side=tk.LEFT, pady=10)

        if access_level is 1:
            view_edu_button = tk.Button(button_frame_1, text="View Educator", command=lambda: self.view_edu(1, user, f))
            view_edu_button.pack(side=tk.LEFT, pady=10)

            view_inst_button = tk.Button(button_frame_2, text="View Institution",
                                         command=lambda: self.view_inst(1, self.user.view_inst(), f))
            view_inst_button.pack(side=tk.LEFT, pady=10)

            view_student_button = tk.Button(button_frame_3, text="View Student",
                                            command=lambda: self.search_student_form(1, f))
            view_student_button.pack(side=tk.LEFT, pady=10)

            view_edu_courses = tk.Button(button_frame_4, text="View All Courses",
                                         command=lambda: self.view_all_edu_courses(f, 1))
            view_edu_courses.pack(side=tk.LEFT, pady=10)

        if access_level is 2:
            view_student_button = tk.Button(button_frame_1, text="View Student",
                                            command=lambda: self.view_student(2, user, f))
            view_student_button.pack(side=tk.LEFT, pady=10)

            view_inst_button = tk.Button(button_frame_2, text="View Institution",
                                         command=lambda: self.view_inst(2, self.user.view_inst(), f))
            view_inst_button.pack(side=tk.LEFT, pady=10)

            view_edu_button = tk.Button(button_frame_3, text="View Educators",
                                        command=lambda: self.search_edu_form(2, f))
            view_edu_button.pack(side=tk.LEFT, pady=10)

            view_stu_reports = tk.Button(button_frame_4, text="View My Reports",
                                        command=lambda: self.student_view_reports(f))
            view_stu_reports.pack(side=tk.LEFT, pady=10)

        standards_button = tk.Button(standards_frame, text="Standards", command=lambda: self.search_standards(f))
        standards_button.pack(side=tk.LEFT, pady=10)

        close_button = tk.Button(close_frame, text="Log Out", command=lambda: self.log_in(f))
        close_button.pack(side=tk.LEFT, pady=25)

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
