
class Grades:
    def __init__(self, number_grade, letter_grade, unit_form, notes):

        # public
        # number of grade
        self.number_grade = number_grade

        # public
        # letter of grade
        self.letter_grade = letter_grade

        # public
        # unit form
        self.unit_form = unit_form

        # public
        # notes
        self.notes = notes

        # public
        # get grades
    def get_grade(self, student_id, section, unit):
        pass

        # public
        # add notes
    def add_notes(self, student_id, section, unit):
        pass

        # public
        # compare to standards
    def compare_to_standard(self, subject):
        pass
