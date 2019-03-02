from Source.Account import Account
from Source.Educator import Educator
from Source.forms import Form
from Source.Student import Student
from Source.Institution import Institution
import tkinter as tk
import csv
import os


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
    user_data = [data[2], data[3], data[0]]
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


def create_institution_obj(top, data):
    top.destroy()
    f = Form()

    inst = Institution(data['name'], data['password'], 0)

    data_list = [data['name'], data["address"], data['instution_type'], data['grade_max'],
                 data['grade_min'], data['phone']]

    inst.set_data(data_list)

    write_list = [0, inst.ownerID, data['name'], data['password'], data['name'], data["address"],
                  data['instution_type'], data['grade_max'], data['grade_min'], data['phone']]

    write_to_file('institution', write_list,)

    main_screen(f,0, inst)
    return None

def create_educator_obj(top):
    top.destroy()
    f = Form()
    main_screen(f, 0, None)
    return None

def create_student_obj(top):
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

    save_button = tk.Button(button_frame, text="Save", command=lambda: create_institution_obj(f,
                                                                                              f.get_institution_data()))
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

    save_button = tk.Button(button_frame, text="Save", command=lambda: create_institution_obj(f,
                                                                                              f.get_institution_data()))
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

def view_inst(top, access_level):
    top.destroy()
    f = Form()

    f.view_institution(access_level, None)

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

        view_inst_button = tk.Button(button_frame_4, text="View Institution", command=lambda: view_inst(f, 0))
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

    log_in_button = tk.Button(button_frame, text="Log In", command=lambda: main_screen(f, 0))
    log_in_button.pack(side=tk.LEFT, padx=10)

    return None

# start the program
forms = Form()

start = start_screen(forms.start_screen())

start.mainloop()

