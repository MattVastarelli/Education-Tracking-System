class Account:
    nextID = 1

    def __init__(self, uname, password, access=1):
        self.ownerID = __class__.nextID
        __class__.nextID += 1
        self.accessLevel = access
        self.userName = uname
        self.password = password

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
