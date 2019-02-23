class Account:
    nextID = 1

    def __init__(self):
        self.ownerID = nextID
        nextID += 1
        self.accessLevel = ''
        self.userName = ''
        self.password = ''

    def log_in(self):
        #login

    def log_out(self):
        # logout

    def view(self):
        #view

    def edit(self):
        #edit

    def create_new(self):
        #create new
