import pymysql as sql


class Connection:
    def __init__(self):
        self.conn = None

    def openCon(self):
        self.conn = sql.connect(host='localhost', user='yourusername', passwd='yourpass', db='yourdb')
        return self.conn

    def closeCon(self):
        self.conn.close()
