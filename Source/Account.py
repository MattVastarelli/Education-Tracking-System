from abc import ABC, abstractmethod


class Account(ABC):
    # this is the main abstract base account from which all accounts
    # will inherits and define the abstract methods

    # next id for a given account
    nextID = 1

    def __init__(self, uname, password, access=1):
        # class attributes
        self.ownerID = __class__.nextID
        __class__.nextID += 1
        self.accessLevel = access
        self.userName = uname
        self.password = password

        # super abstract class init
        super.__init__()

    @abstractmethod
    def log_in(self):
        pass

    @abstractmethod
    def log_out(self):
        pass

    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def create_new(self):
        pass
