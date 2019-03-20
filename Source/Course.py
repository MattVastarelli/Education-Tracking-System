from Source.unit import Unit

class Course:
    def __init__(self, subject):
        self.subject = subject

    def add_unit(self, req, covers, len, unit):
        # creates a unit and returns it
        u = Unit(req, covers, len, unit)
        return u

    def add_section(self):
        # creates a section and returns it
        return None
