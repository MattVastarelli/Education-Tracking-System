import os


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
        script_dir = os.path.dirname(__file__)  # absolute dir the script is in
        rel_path = "db/users.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        user_name_match = False
        password_match = False

        with open(abs_file_path) as f:
            content = f.readlines()
            content = [x.strip() for x in content]

            for line in content:
                split = line.split()  # choose split type

                if user_name in split[0]:
                    user_name_match = True
                if password in split[1]:
                    password_match = True

                if user_name_match and password_match:
                    return True

        return False

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
    def create_new(self, access_level, something):
        raise NotImplementedError

    def get_user_name(self):
        return self.__userName

    def get_password(self):
        return self.__password

    def set_userName(self, username):
        self.__userName = username

    def set_password(self, password):
        self.__password = password
