from abc import ABC, abstractmethod


class Account(ABC):
    # this is the main abstract base account from which all accounts
    # will inherits and define the abstract methods

    # next id for a given account
    nextID = 1

    def __init__(self, uname, password, access=0):
        # class attributes
        # public
        self.ownerID = __class__.nextID
        __class__.nextID += 1
        self.accessLevel = access

        # private
        self.__userName = uname
        self.__password = password

        # super abstract class init
        super.__init__()

    # private
    @abstractmethod
    def __log_in(self, user_name, password):
        pass

    # private
    @abstractmethod
    def __log_out(self):
        pass

    # private
    @abstractmethod
    def __view(self):
        pass

    # private
    @abstractmethod
    def __edit(self):
        pass

    # private
    @abstractmethod
    def create_new(self, access_level):
        pass
