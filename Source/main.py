from Source.Account import Account
from Source.Educator import Educator
from Source.forms import Form
from Source.Student import Student
from Source.Institution import Institution
import tkinter as tk
import csv
import os


def log_in_search(login_data, top):
    user = login_data['user_name']
    password = login_data['password']

    script_dir = os.path.dirname(__file__)  # absolute dir the script is in
    rel_path = "db/users.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    user_name_match = False
    password_match = False

    with open(abs_file_path) as f:
        content = f.readlines()
        content = [x.strip() for x in content]

        for line in content:
            split = line.split()  # choose split type
            print(split)

            if user in split[0]:
                user_name_match = True
            if password in split[1]:
                password_match = True

            if user_name_match and password_match:
                data = {
                    "user_name": user, "password": password, "user_id": split[3], "access_level": split[2]
                }

                if split[2] is 0:
                    obj = create_institution_obj(None, data, False)
                elif split[2] is 1:
                    pass
                elif split[2] is 2:
                    pass
                else:
                    return None

                main_screen(top, split[2], obj)

    return None

def write_to_file(obj_type, data):
    # write to the correct user type file
    script_dir = os.path.dirname(__file__)  # absolute dir the script is in
    rel_path = "db/" + obj_type + "s.txt" # student , institution, educator
    #rel_path = 'db/test.txt'
    abs_file_path = os.path.join(script_dir, rel_path)

    file = open(abs_file_path, 'a', newline='')
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(data)
    file.close()

    # write the the users file
    user_path = "db/users.txt"  # student , institution, educator
    abs_file_path = os.path.join(script_dir, user_path)

    user_file = open(abs_file_path, 'a', newline='')
    user_data = [data[2], data[3], data[0], data[1]] # username, pass, access level, user_id
    user_writer = csv.writer(user_file, delimiter='\t')
    user_writer.writerow(user_data)
    user_file.close()

    return None


def start_screen(top):
    # main frame
    frame = tk.Frame(top)
    frame.pack(pady=100)

    institution_frame = tk.Frame(frame)
    institution_frame.pack()

    log_in_frame = tk.Frame(frame)
    log_in_frame.pack(pady=30)

    log_in_button = tk.Button(log_in_frame, text="Log In", command=lambda: log_in(top))
    log_in_button.pack(side=tk.LEFT)

    institution_button = tk.Button(institution_frame, text="Create new Institution",
                                   command= lambda: first_creation(top))
    institution_button.pack(side=tk.LEFT)

    return top


def create_institution_obj(top, data, is_new):

    if top is not None:
        top.destroy()

    f = Form()

    inst = Institution(data['name'], data['password'], 0, is_new)

    if is_new:
        data_list = [data['name'], data["address"], data['instution_type'], data['grade_max'],
                     data['grade_min'], data['phone']]

        inst.set_data(data_list)

        write_list = [inst.ownerID, 0, data['name'], data['password'], data['name'], data["address"],
                      data['instution_type'], data['grade_min'], data['grade_max'], data['phone']]

        write_to_file('institution', write_list)
        main_screen(f, 0, inst)
    else:
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
                split = line.split()  # choose split type
                if split[0] == str(1):
                    return_list = line.split()
        # fill in data
        inst.set_id(return_list[0])
        inst.set_data(return_list[4:])

        return inst


def create_educator_obj(top, data, is_new):
    top.destroy()
    f = Form()
    main_screen(f, 0, None)
    return None


def create_student_obj(top, data, is_new):
    top.destroy()
    f = Form()
    main_screen(f, 0, None)
    return None


def institution_creation(top):
    top.destroy()
    f = Form()

    f.add_new(0)

    frame = tk.Frame()
    frame.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, 0, None))
    back.pack(side=tk.LEFT, padx=10)

    save_button = tk.Button(button_frame, text="Save",
                            command=lambda: create_institution_obj(f, f.get_institution_data(), True))
    save_button.pack(side=tk.LEFT)

    return None


def first_creation(top):
    top.destroy()
    f = Form()

    f.add_new(0)

    frame = tk.Frame()
    frame.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back = tk.Button(button_frame, text="Close", command=f.destroy)
    back.pack(side=tk.LEFT, padx=10)

    save_button = tk.Button(button_frame, text="Save",
                            command=lambda: create_institution_obj(f, f.get_institution_data(), True))
    save_button.pack(side=tk.LEFT)

    return None


def student_creation(top):
    top.destroy()
    f = Form()

    f.add_new(2)

    frame = tk.Frame()
    frame.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, 0, None))
    back.pack(side=tk.LEFT, padx=10)


    save_button = tk.Button(button_frame, text="Save", command=lambda: create_student_obj(f))
    save_button.pack(side=tk.LEFT)

    return None


def educator_creation(top):
    top.destroy()
    f = Form()

    f.add_new(1)

    frame = tk.Frame()
    frame.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, 0, None))
    back.pack(side=tk.LEFT, padx=10)

    save_button = tk.Button(button_frame, text="Save", command=lambda: create_educator_obj(f))
    save_button.pack(side=tk.LEFT)

    return None


def view_edu(top, access_level):
    top.destroy()
    f = Form()

    f.view_educator(0, None)

    frame = tk.Frame()
    frame.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, access_level, None))
    back.pack(side=tk.LEFT, padx=10)

    return None


def view_inst(top, access_level, user):
    top.destroy()
    f = Form()

    # get the data form the obj
    data = [user.get_name(), user.get_address(), user.get_institution_type(),
            user.get_grade_min(), user.get__grade_max(), user.get_main_phone_num()]

    f.view_institution(access_level, data)

    frame = tk.Frame()
    frame.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, access_level, None))
    back.pack(side=tk.LEFT, padx=10)

    return None


def view_student(top, access_level):
    top.destroy()
    f = Form()

    f.view_student(access_level, None)

    frame = tk.Frame()
    frame.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, access_level, None))
    back.pack(side=tk.LEFT, padx=10)

    return None


def main_screen(top, access_level, user):
    top.destroy()
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
        new_edu_button = tk.Button(button_frame, text="New Educator", command=lambda:educator_creation(f))
        new_edu_button.pack(side=tk.LEFT, pady=10)

        new_inst_button = tk.Button(button_frame_1, text="New Institution", command=lambda: institution_creation(f))
        new_inst_button.pack(side=tk.LEFT, pady=10)

        new_student_button = tk.Button(button_frame_2, text="New Student", command=lambda: student_creation(f))
        new_student_button.pack(side=tk.LEFT, pady=10)

        view_edu_button = tk.Button(button_frame_3, text="View Educator", command=lambda: view_edu(f, 0))
        view_edu_button.pack(side=tk.LEFT, pady=10)

        view_inst_button = tk.Button(button_frame_4, text="View Institution", command=lambda: view_inst(f, 0, user))
        view_inst_button.pack(side=tk.LEFT, pady=10)

        view_student_button = tk.Button(button_frame_5, text="View Student", command=lambda: view_student(f, 0))
        view_student_button.pack(side=tk.LEFT, pady=10)



    close_button = tk.Button(button_frame_6, text="Close", command=f.destroy)
    close_button.pack(side=tk.LEFT, padx=10)

    return None


def log_in(top):
    top.destroy()
    f = Form()

    f.log_in()

    frame = tk.Frame()
    frame.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    close_button = tk.Button(button_frame, text="Close", command=f.destroy)
    close_button.pack(side=tk.LEFT, padx=10)

    log_in_button = tk.Button(button_frame, text="Log In", command=lambda: log_in_search(f.get_login_data(), f))
    log_in_button.pack(side=tk.LEFT, padx=10)

    return None

# start the program
forms = Form()

start = start_screen(forms.start_screen())

start.mainloop()

