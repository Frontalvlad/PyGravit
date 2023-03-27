from pygravit import PyGravit

GravitLauncher = PyGravit(db="dbname", host="ip/domainname", port=3306, user="username", passwd="passwd", table="tablename (default users)")
GravitLauncher.player_create("Nickname", "Password") #create
GravitLauncher.player_delete("Nickname") # delete
GravitLauncher.player_change("Nickname", "Param", "Value") # change
GravitLauncher.player_get("Nickname", "Param") # get
