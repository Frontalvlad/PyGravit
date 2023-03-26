# PyGravit
Module for managing accounts in GravitLauncher Database.

## About
The library is designed to manage the database of GravitLauncher players. This library is not considered official. It has four methods for managing players, which are provided below, as well as in the examples. There are also error handlers, which can also be found in the documentation below.


## Installation

1. Update your pip
2. Install the pygravit package either via pip or from the pypi website
**Installation command**
```powershell
python -m pip install pygravit 
```
3. Import it into your project
**Imports**
```python
import pygravit
from pygravit.exceptions import DatabaseConnectionError, NicknameInDatabaseError, NicknameNotInDatabaseError, AllowedCharactersNicknameError, ClassDatabaseNotConnectionError, NicknameLengthError, ParamNotFoundError, DataError
```
4. Check out the documentation for further work.

## Documentation
### Examples
**api_gravitpy_example.py**
```python
from pygravit import PyGravit

# Connecting to a database
GravitLauncher = PyGravit(db="dbname", host="ip/domainname", port=3306, user="username", passwd="password", table="tablename (default users)")

# Creating a player in the database
GravitLauncher.player_create("Nickname", "Password")

# Removing a player from the database
GravitLauncher.player_delete("Nickname")

# Changing the player (the parameters are in the GravitLauncher documentation as well as in the database itself)
GravitLauncher.player_change("Nickname", "Param", "Value")

# Getting the player parameter (the parameters are in the GravitLauncher documentation as well as in the database itself)
GravitLauncher.player_get("Nickname", "Param")
```

**custom_tablename.py**
```python
from pygravit import PyGravit

GravitLauncher = PyGravit(db="dbname",
                                host="ip/domainname",
                                port=3306,
                                user="username",
                                passwd="password",
                                table="server_users" ) #table default "users"

# Creating two tables: server_users and server_users_hwids (default: users and users_hwids)
```

**except_processing.py**
```python
from pygravit import PyGravit
from pygravit.scripts.exceptions import (DatabaseConnectionError, NicknameInDatabaseError, NicknameNotInDatabaseError,
                                AllowedCharactersNicknameError, ClassDatabaseNotConnectionError, NicknameLengthError,
                                ParamNotFoundError, DataError)
try:
    GravitLauncher = PyGravit(db="dbname", host="ip/domainname", port=3306, user="username", passwd="password", table="tablename (default users)")
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
```
