import gravitpy

GravitLauncher = gravitpy.GravitPy(db="dbname", host="ip/domainname", port=3306, user="username", passwd="password", table="tablename (default users)")
GravitLauncher.player_create("Nickname", "Password")
GravitLauncher.player_delete("Nickname")
GravitLauncher.player_change("Nickname", "Param", "Value")
GravitLauncher.player_get("Nickname", "Param")