import pygravit
from pygravit.exceptions import (DatabaseConnectionError, NicknameInDatabaseError, NicknameNotInDatabaseError,
                                AllowedCharactersNicknameError, ClassDatabaseNotConnectionError, NicknameLengthError,
                                ParamNotFoundError, DataError)
try:
    GravitLauncher = pygravit.PyGravit(db="dbname", host="ip/domainname", port=3306, user="username", passwd="password", table="tablename (default users)")
except DatabaseConnectionError as e: 
    print(e)

try:
    GravitLauncher.player_create("Nickname", "Password")
except (NicknameInDatabaseError or AllowedCharactersNicknameError or NicknameLengthError or DataError or ClassDatabaseNotConnectionError) as e:
    print(e)

try:
    GravitLauncher.player_delete("Nickname")
except (NicknameNotInDatabaseError or DataError or ClassDatabaseNotConnectionError) as e:
    print(e)

try:
    GravitLauncher.player_change("Nickname", "Param", "Value")
    GravitLauncher.player_get("Nickname", "Param")
except (NicknameNotInDatabaseError or ParamNotFoundError or DataError or ClassDatabaseNotConnectionError) as e:
    print(e)