
class Sections:
    def __init__(self, student_list, time, room, offered_through):

        # public
        # student list
        self.student_list = student_list

        # public
        # time
        self.time = time

        # public
        # room
        self.room = room

        # public
        # offered through
        self.offered_through = offered_through

        # public
        # view students
    def view_students(self, student_list):
        pass

        # public
        # add students
    def add_students(self, student_id):
        pass

        # public
        # drop students
    def drop_students(self, student_id):
        pass