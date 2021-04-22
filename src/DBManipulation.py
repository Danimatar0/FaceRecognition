from src.Connection import Connection

connection = Connection


class DBManipulation:
    def __init__(self):
        self.con = None

    def openCon(self):
        print("Establishing connection with mysql server..")
        self.con = connection.openCon(connection)

    def checkCon(self):
        if self.con is not None:
            print("Connection successfully established..")
            cnx = self.con
            return cnx
        else:
            print("Unable to connect to mysql server..")
            return

    def selectAdmin(self, uname, passwd):
        mycon = self.checkCon(self)
        try:
            cursor = mycon.cursor()
            username = cursor.execute("SELECT `username`"
                                      " FROM `facereco`"
                                      " WHERE `username`='uname' AND `password`='passwd'; ")
            return username
        except:
            print("Unable to connect to database")

    def createAdmin(self, fname, lname, uname, passwd):
        username = self.selectAdmin(uname, passwd)
        if username != "":
            cursor = connection.cursor()
            cursor.execute("INSERT INTO admin"
                           "VALUES ('fname','lname','uname','passwd');")
            connection.commit()
        else:
            print("Username already exists !")

    def deleteAdmin(self, uname, passwd):
        username = self.selectAdmin(uname, passwd)
        if username != "":
            cursor = connection.cursor()
            cursor.execute("DELETE FROM admin"
                           "WHERE "
                           "username='uname'"
                           "AND password='passwd';")
            connection.commit()
        else:
            print("Username does not exist !..Please try another username")

    def closeCon(self):
        self.con = None
        print("Disconnected from mysql server..")
