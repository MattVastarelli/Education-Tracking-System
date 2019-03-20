from Source.Course import Course
from Source.subtopic import SubTopic

class Subject:
    def __init__(self, topic):
        self.topic = topic

    def get_subject(self):
        return self.topic

    def make_course(self, subject):
        # makes a course and returns the course
        c = Course(subject)
        return c

    def add_subtopic(self, name, desc, grade):
        # makes a sub topic and returns a subtopic
        s = SubTopic(name, desc, grade)
        return s
