import sqlite3

class dbInterface(object):
    def __init__(self, dbFile):
        self._con = sqlite3.connect(dbFile)
        self._cur = self._con.cursor()

    def close(self):
        self._con.close()
    
    def query(self, queryString):
        self._cur.execute(queryString)
        self._con.commit()
        return self._cur

    def addSubscriber(self, address):
        cur = self.query('SELECT address FROM User WHERE address="%s"' % address)
        if len(cur.fetchall()) == 0:
            self.query('INSERT INTO User (isSender, isActive, address) VALUES (0, 1, "%s")' % address)
        else:
            self.query('UPDATE User SET isActive=1 WHERE address="%s"' % address)

    def removeSubscriber(self, address):
        self.query('UPDATE User SET isSender=0, isActive=0 WHERE address="%s"' % address)

    def addSender(self, address):
        self.addSubscriber(address)
        self.query('UPDATE User SET isSender=1 WHERE address="%s"' % address)
    
    def removeSender(self, address):
        self.query('UPDATE User set isSender=0 WHERE address="%s"' % address)

    def getAllSubscribers(self):
        cur = self.query('SELECT address FROM User WHERE isActive=1')
        return cur.fetchall()

    def isSender(self, address):
        cur = self.query('SELECT address FROM User WHERE address="%s"' % address)
        if len(cur.fetchall()) > 0:
            return True
        else:
            return False
