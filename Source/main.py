from Source.Account import Account
from Source.Educator import Educator
from Source.forms import Form
from Source.Student import Student
from Source.Institution import Institution
import tkinter as tk

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
                                   command= lambda: create_institution(top, 0))
    institution_button.pack(side=tk.LEFT)

    return top


def create_institution(top):
    return None

def create_educator(top):
    return None

def create_student(top):
    return None

def institution_creation(top):
    top.destroy()
    f = Form()

    f.add_new(0)

    frame = tk.Frame()
    frame.pack(pady=10)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, 0))
    back.pack(side=tk.LEFT, padx=10)

    save_button = tk.Button(button_frame, text="Save", command=lambda: create_institution(f))
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

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, 0))
    back.pack(side=tk.LEFT, padx=10)


    save_button = tk.Button(button_frame, text="Save", command=lambda: create_student(f))
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

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, 0))
    back.pack(side=tk.LEFT, padx=10)


    save_button = tk.Button(button_frame, text="Save", command=lambda: create_educator(f))
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

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, access_level))
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

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, access_level))
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

    back = tk.Button(button_frame, text="Back", command=lambda: main_screen(f, access_level))
    back.pack(side=tk.LEFT, padx=10)

    return None

def main_screen(top, access_level):
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

