class SubTopic:
    def __init__(self, n, d, g):
        self.name = n
        self.description = d
        self.earliest_grade_taught = g

    def view_summary(self):
        return self.name + " Description: " + self.description \
               + " Earliest Grade Taught" + str(self.earliest_grade_taught)
