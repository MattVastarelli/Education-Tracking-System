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
    def __log_in(self, user_name, password):
        raise NotImplementedError

    # private
    def __log_out(self):
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
