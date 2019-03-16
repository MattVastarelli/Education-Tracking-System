
from tkinter import *


class UserSearchRecords(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Users Search Records by Keyword")
        self.resizable(False, False)

        # frame
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom_frame = Frame(self, height=500, bg="#fcc324")
        self.bottom_frame.pack(fill=X)

        # label and entry
        self.lbl_search_keyword = Label(self.bottom_frame, text="Search Keyword Input", font="arial 10 bold", fg="white", bg="#fcc324")
        self.lbl_search_keyword.place(x=40, y=40)
        self.ent_search_keyword = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_search_keyword.insert(0, "Please enter a keyword")
        self.ent_search_keyword.place(x=200, y=40)
        self.lbl_search_record = Label(self.bottom_frame, text="Search Record", font="arial 10 bold", fg="white", bg="#fcc324")
        self.lbl_search_record.place(x=40, y=100)
        self.listbox_search_record = Listbox(self.bottom_frame, width=50, height=20, bd=4)
        self.listbox_search_record.place(x=200, y=100)

        # button
        self.btn_search = Button(self.bottom_frame, text="Keyword Search")
        self.btn_search.place(x=420, y=40)


'''
if __name__ == "__main__":
    window = UserSearchRecords()
    window.mainloop()
'''
