
from tkinter import *


class InstitutionViewAccessFeedback(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Institution View Teacher Access and Feedback")
        self.resizable(False, False)

        # frame
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom_frame = Frame(self, height=500, bg="#fcc324")
        self.bottom_frame.pack(fill=X)

        # label and entry
        self.lbl_search_keyword = Label(self.bottom_frame, text="Search Teacher Input", font="arial 10 bold",
                                        fg="white", bg="#fcc324")
        self.lbl_search_keyword.place(x=40, y=40)
        self.ent_search_keyword = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_search_keyword.insert(0, "Please enter a teacher name")
        self.ent_search_keyword.place(x=200, y=40)
        self.lbl_teacher_access = Label(self.bottom_frame, text="Teacher Access", font="arial 10 bold", fg="white", bg="#fcc324")
        self.lbl_teacher_access.place(x=40, y=100)
        self.listbox_teacher_access = Listbox(self.bottom_frame, width=50, bd=4)
        self.listbox_teacher_access.place(x=200, y=100)
        self.lbl_teacher_feedback = Label(self.bottom_frame, text="Teacher Feedback", font="arial 10 bold", fg="white", bg="#fcc324")
        self.lbl_teacher_feedback.place(x=40, y=300)
        self.listbox_teacher_feedback = Listbox(self.bottom_frame, width=50, bd=4)
        self.listbox_teacher_feedback.place(x=200, y=300)

        # button
        self.btn_search = Button(self.bottom_frame, text="Teacher Search")
        self.btn_search.place(x=420, y=40)


'''
if __name__ == "__main__":
    window = InstitutionViewAccessFeedback()
    window.mainloop()
'''
