from Source.unit import Unit
from Source.sections import Sections

class Course:
    def __init__(self, subject):
        self.subject = subject

    def add_unit(self, req, covers, len, unit):
        # creates a unit and returns it
        u = Unit(req, covers, len, unit)
        return u

    def add_section(self, student_list, time, room, offered_through):
        # creates a section and returns it
        s = Sections(student_list, time, room, offered_through)
        return s
