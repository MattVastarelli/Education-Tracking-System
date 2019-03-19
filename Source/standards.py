class Standards:
    def __init__(self, subject,  acc_range):
        self.subject = subject
        self.acceptable_range = acc_range # list of acceptable grades a student can recive

    def get_standards(self):
        return self.subject, self.acceptable_range




"""
s = Standards("", list())

sub, acc = s.get_standards()
"""
