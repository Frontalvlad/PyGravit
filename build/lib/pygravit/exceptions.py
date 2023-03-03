class DatabaseConnectionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return "{0}".format(self.message)
        else:
            return "Failed to connect to MySQL database. Check the entered data, or the Internet connection."

class NicknameInDatabaseError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return "{0}".format(self.message)
        else:
            return "This user already exists in the database."

class NicknameNotInDatabaseError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return "{0}".format(self.message)
        else:
            return "This account does not exist in the database."
        
class AllowedCharactersNicknameError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return "{0}".format(self.message)
        else:
            return "The user's nickname contains prohibited characters. Use allowed Minecraft symbols for your nickname."
        
class ClassDatabaseNotConnectionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return "{0}".format(self.message)
        else:
            return "Use the GravitPy() class to create a database."
        
class NicknameLengthError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return "{0}".format(self.message)
        else:
            return "Nickname doesn't meet Minecraft nickname length guidelines."
        
class ParamNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return "{0}".format(self.message)
        else:
            return "Could not find such a parameter in the database. Check out the documentation."
        
class DataError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return "{0}".format(self.message)
        else:
            return "It looks like you entered the data incorrectly. Please note that some columns have their own parameters: type, length and other filters."