from pygravit import PyGravit

# Creating two tables: server_users and server_users_hwids (default: users and users_hwids)
DataBase = PyGravit(db="dbname",
                                host="ip/domainname",
                                port=3306,
                                user="username",
                                passwd="password",
                                table="server_users" ) #table default users


