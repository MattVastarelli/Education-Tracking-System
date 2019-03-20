class SubTopic:
    def __init__(self, name, desc, grade):
        self.name = name
        self.description = desc
        self.earliest_grade_taught = grade

    def view_summary(self):
        return self.name + " Description: " + self.description \
               + " Earliest Grade Taught" + str(self.earliest_grade_taught)
