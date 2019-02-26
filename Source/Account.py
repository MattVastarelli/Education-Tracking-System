class Account:
    # this is the main abstract base account from which all accounts
    # will inherits and define the abstract methods

    # next id for a given account
    nextID = 1

    def __init__(self, uname, password, access):
        # class attributes
        # public
        self.ownerID = __class__.nextID
        __class__.nextID += 1

        self.accessLevel = access

        # private
        self.__userName = uname
        self.__password = password

    # private
    def log_in(self, user_name, password):
        raise NotImplementedError

    # private
    def log_out(self):
        raise NotImplementedError

    # private
    def __view(self):
        raise NotImplementedError

    # private
    def __edit(self):
        raise NotImplementedError

    # private
    def create_new(self, access_level):
        raise NotImplementedError

    def get_user_name(self):
        return self.__userName

    def get_password(self):
        return self.__password

    def set_userName(self, username):
        self.__userName = username

    def set_password(self, password):
        self.__password = password
