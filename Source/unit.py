class Unit:
    def __init__(self, req, covers, len, unit):
        self.requirements = req
        self.covers = covers
        self.length = len
        self.unit_name = unit

    def add_requirement(self, req):
        self.requirements.append(req)
        return None

    def give_grade(self, grade_obj, n, l):
        # updates the grade of the grade object
        grade_obj.number_grade = n
        grade_obj.letter_grade = l
        return None