from exceptions import (DatabaseConnectionError, ClassDatabaseNotConnectionError, 
                                NicknameNotInDatabaseError, ParamNotFoundError, DataError,
                                NicknameLengthError, NicknameInDatabaseError, AllowedCharactersNicknameError)
import pymysql
import bcrypt
import datetime

class PyGravit():
    def __init__(self, db, user, passwd, host, port = 3306, table = "users"):
        try:
            self.connection = pymysql.connect(
                db = db,
                user = user,
                password = passwd,
                host = host, 
                port = port,
                autocommit = True
            )
            
            self.table = table
            
            with self.connection.cursor() as crs:
                S = "SELECT table_name FROM information_schema.tables WHERE table_name=%s"
                if not crs.execute(S, (table,)):
                    print("Executing a MySQL query to create the {} table..".format(table))
                    MYSQLREQUESTS_ARRAY = [
                        "CREATE TABLE `{}` (`id` int(11) NOT NULL AUTO_INCREMENT,`nickname` varchar(16) NOT NULL,`password` varchar(255) NOT NULL,`joined` int(8) NOT NULL,PRIMARY KEY (`id`),KEY `id` (`id`));".format(table),
                        "ALTER TABLE `{}` ADD COLUMN uuid CHAR(36) UNIQUE DEFAULT NULL, ADD COLUMN accessToken CHAR(32) DEFAULT NULL, ADD COLUMN serverID VARCHAR(41) DEFAULT NULL, ADD COLUMN hwidId BIGINT DEFAULT NULL;".format(table),
                        "UPDATE `{}` SET uuid=(SELECT UUID()) WHERE uuid IS NULL;".format(table),
                        "CREATE TABLE `{}_hwids` (`id` bigint(20) NOT NULL,`publickey` blob,`hwDiskId` varchar(255) DEFAULT NULL,`baseboardSerialNumber` varchar(255) DEFAULT NULL, `graphicCard` varchar(255) DEFAULT NULL, `displayId` blob, `bitness` int(11) DEFAULT NULL, `totalMemory` bigint(20) DEFAULT NULL, `logicalProcessors` int(11) DEFAULT NULL, `physicalProcessors` int(11) DEFAULT NULL, `processorMaxFreq` bigint(11) DEFAULT NULL, `battery` tinyint(1) NOT NULL DEFAULT '0', `banned` tinyint(1) NOT NULL DEFAULT '0' ) ENGINE=InnoDB DEFAULT CHARSET=utf8;".format(table),
                        "ALTER TABLE `{}_hwids` ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `publickey` (`publickey`(255));".format(table),
                        "ALTER TABLE `{}_hwids` MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;".format(table),
                        "ALTER TABLE `{0}` ADD CONSTRAINT `{1}` FOREIGN KEY (`hwidId`) REFERENCES `{1}_hwids` (`id`);".format(table, table),
                        "CREATE TRIGGER `{0}.setUUID` BEFORE INSERT ON `{1}` FOR EACH ROW  SET NEW.uuid = COALESCE(NEW.uuid, UUID());".format(table,table)
                    ]
                    for request in MYSQLREQUESTS_ARRAY:
                        crs.execute(request)
                    print("Successfully!")
                    return
            
        except: raise DatabaseConnectionError

    def __check_nickname(self, nickname):
        '''
        Parameters:
            :nickname: (str): The nickname of the user to check.
        A private method that is part of a class that interacts with a database table.
        It checks if a given nickname is valid and can be added to the database.
        return -> True (bool)
        '''
        with self.connection.cursor() as crs:
            crs.execute("SELECT `nickname` FROM {};".format(self.table)) 
            sql_nicks_unpack = crs.fetchall()
            
            list_nicks = [nick[0] for nick in sql_nicks_unpack]

            if nickname in list_nicks: 
                raise NicknameInDatabaseError
            else: 
                if len(nickname) <= 3 or len(nickname) > 16 :
                    raise NicknameLengthError
                else:
                    allowed = "Q W E R T Y U I O P A S D F G H J K L Z X C V B N M q w e r t y u i o p a s d f g h j k l z x c v b n m 1 2 3 4 5 6 7 8 9 0 _".split()
                    for n in nickname: 
                        if n not in allowed:
                            raise AllowedCharactersNicknameError
                    return True

    def player_create(self, nickname, password) -> None:
        '''
        Adds a new user account to the database.
        Parameters:
            :nickname: (str): The nickname of the user to add.
            :password: (str): The password of the user to add.
        return -> None
        '''
        if not isinstance(self.connection, pymysql.Connection): raise ClassDatabaseNotConnectionError

        if not self.__check_nickname(nickname):
            return

        data_user = {
            "nickname": nickname,
            "password": bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
            "joined": datetime.datetime.today().strftime("%Y%m%d") 
        }
        with self.connection.cursor() as crs:
            crs.execute("INSERT INTO `{}` (`nickname`,`password`,`joined`) VALUES (%s, %s, %s)".format(self.table), (data_user["nickname"], data_user["password"], data_user["joined"],))

        
    def player_delete(self, nickname) -> None:
        '''
        Deletes a user account from the database.
        Parameters:
            :nickname: (str): The nickname of the user to delete.
        return -> None
        '''
        if not isinstance(self.connection, pymysql.Connection): raise ClassDatabaseNotConnectionError
        
        with self.connection.cursor() as crs:
            if not crs.execute("SELECT `nickname` FROM `{}` WHERE `nickname` = %s".format(self.table), (nickname,)): raise NicknameNotInDatabaseError    
            crs.execute("DELETE FROM `{}` WHERE (`nickname` = %s);".format(self.table), (nickname,))


    def player_change(self, nickname, param, value) -> None:
        '''
        Changes a user account parameter in the database.
        Parameters:
            :nickname: (str): The nickname of the user to modify.
            :param: (str): The parameter of the user to modify (e.g. "password").
            :value: (str): The new value of the parameter to set.
        return -> None
        '''
        if not isinstance(self.connection, pymysql.Connection): raise ClassDatabaseNotConnectionError

        with self.connection.cursor() as crs:
            if not crs.execute("SELECT `nickname` FROM `{}` WHERE `nickname` = %s".format(self.table), (nickname,)): raise NicknameNotInDatabaseError   
            crs.execute("SHOW COLUMNS FROM `{}`;".format(self.table))
            columns = [column[0] for column in crs.fetchall()]
                
            if param not in columns: raise ParamNotFoundError
            match param:
                    case "password":
                        value = bcrypt.hashpw(value.encode(), bcrypt.gensalt())
                        crs.execute("UPDATE `{}` SET `password` = %s WHERE `nickname` = %s;".format(self.table), (value, nickname,))
                    case _:
                        try:
                            crs.execute("UPDATE `{0}` SET `{1}` = %s WHERE `nickname` = %s;".format(self.table, param), (value, nickname,))
                        except: raise DataError

    def player_get(self, nickname, param) -> str:
        '''
        Retrieves a user account parameter from the database.
        Parameters:
            :nickname: (str): The nickname of the user to retrieve information for.
            :param: (str): The parameter of the user to retrieve (e.g. "password").
        '''
        if not isinstance(self.connection, pymysql.Connection): raise ClassDatabaseNotConnectionError

        with self.connection.cursor() as crs:
            if not crs.execute("SELECT `nickname` FROM `{}` WHERE `nickname` = %s".format(self.table), (nickname,)): raise NicknameNotInDatabaseError

            crs.execute("SHOW COLUMNS FROM {};".format(self.table))
            columns = [column[0] for column in crs.fetchall()]
                
            if param not in columns: raise ParamNotFoundError
            elif param == "all":
                crs.execute("SELECT * FROM `{}` WHERE `nickname` = %s".format(self.table), (nickname,))
                return crs.fetchall()[0]
            
            crs.execute("SELECT `{0}` FROM `{1}` WHERE `nickname` = %s".format(param, self.table), (nickname,))
            return crs.fetchall()[0][0]
