<p align="center">
      <img src="https://cdn.discordapp.com/attachments/1084489981193621580/1089661272682934303/hero.png" alt="Project Logo" width="512" height="512">
</p>

# PyGravit
Module for managing accounts in GravitLauncher Database

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
from pygravit import PyGravit
from pygravit import (DatabaseConnectionError, NicknameInDatabaseError, NicknameNotInDatabaseError, AllowedCharactersNicknameError, ClassDatabaseNotConnectionError, NicknameLengthError, ParamNotFoundError, DataError)
```
4. Check out the documentation for further work.

## Updates

### v0.0.1
- No change

## Documentation
### 1. Examples
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
from pygravit import (DatabaseConnectionError, NicknameInDatabaseError, NicknameNotInDatabaseError,
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


### 2. Exceptions
```
DatabaseConnectionError - Failed to connect to database
NicknameInDatabaseError - Nickname already exists in the database
NicknameNotInDatabaseError - Nickname not found in database
AllowedCharactersNicknameError - Nickname has forbidden characters (forbidden in normal minecraft)
ClassDatabaseNotConnectionError - The database object is not a MySQLConnection
NicknameLengthError - Nickname does not meet standard length (either short or long)
ParamNotFoundError - The player parameter was not found in the database (used to get and change values in the database)
DataError - Failed to send data to database
```


### 3. Classes and Methods
#### Classes
```python
PyGravit(db, user, passwd, host, port) -  An object class for connecting to a database
```
#### Methods
```python
player_create(nickname, password) - Creating a player in the database
player_delete(nickname) - Removing a player from the database
player_change(nickname, param, value) - Changing the player
player_get(nickname, param) - Getting the player parameter
```

### 4. FAQ
#### F: I get an error, what should I do? (java.sql.SQLSyntaxErrorException: Table 'database.hwids' doesn't exist)
**An error has been made in the official GravitLauncher documentation, so you should replace the string "tableHwid" with "tableHWID" in LaunchServer.json file.**
```json
        "auth": {
            ...
            "table": "{{table_name}}", 
            "tablehwid": "{{table_name}}_hwids", => "tableHWID": "{{table_name}}_hwids"
            "uuidColumn": "uuid",
            "usernameColumn": "nickname",
            "passwordColumn": "password",
            "accessTokenColumn": "accessToken",
            "hardwareIdColumn": "hwidId",
            "serverIDColumn": "serverID"

```
