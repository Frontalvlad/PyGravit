from pygravit import PyGravit
from pygravit import (DatabaseConnectionError, NicknameInDatabaseError, NicknameNotInDatabaseError,
                                AllowedCharactersNicknameError, ClassDatabaseNotConnectionError, NicknameLengthError,
                                ParamNotFoundError, DataError)
try:
    GravitLauncher = PyGravit(db="dbname", host="ip/domainname", port=3306, user="username", passwd="passwd", table="tablename (default users)")
except DatabaseConnectionError as e: 
    print(e)

try:
    GravitLauncher.player_create("Nickname", "Password") # create exceptions
except (NicknameInDatabaseError or AllowedCharactersNicknameError or NicknameLengthError or DataError or ClassDatabaseNotConnectionError) as e:
    print(e)

try:
    GravitLauncher.player_delete("Nickname") # delete exceptions
except (NicknameNotInDatabaseError or DataError or ClassDatabaseNotConnectionError) as e:
    print(e)

try:
    GravitLauncher.player_change("Nickname", "Param", "Value") # change and get exceptions
    GravitLauncher.player_get("Nickname", "Param")
except (NicknameNotInDatabaseError or ParamNotFoundError or DataError or ClassDatabaseNotConnectionError) as e:
    print(e)
