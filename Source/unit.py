class Unit:
    def __init__(self, req, covers, len, unit):
        self.requirements = req
        self.covers = covers
        self.length = len
        self.unit_name = unit

    def add_requirement(self, req):
        self.requirements.append(req)
        return None

    def give_grade(self):
        # updates the grade of the grade object
        return None