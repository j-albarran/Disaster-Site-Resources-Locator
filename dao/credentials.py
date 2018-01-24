from config.dbconfig import conn

class CredentialDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    # ============ #
    #    Updates   #
    # ============ #

    def addCredentials(self, username, password, aid):
        cursor = self.conn.cursor()
        query = "insert into credentials(username, password, aid) values(%s, %s, %s) returning username;"
        cursor.execute(query, (username, password, aid,))
        username = cursor.fetchone()[0]
        self.conn.commit()
        return username

    def updateCredentials(self, username, password, aid):
        cursor = self.conn.cursor()
        query = "update credentials set password = %s, aid = %s where username = %s;"
        cursor.execute(query, (password, aid, username, ))
        self.conn.commit()
        return username

    def deleteCredentials(self, username):
        cursor = self.conn.cursor()
        query = "delete from credentials where username = %s;"
        cursor.execute(query, (username,))
        self.conn.commit()
        return username


    # ============ #
    #    Gets      #
    # ============ #

    def getAllCredentials(self):
        cursor = self.conn.cursor()
        query = "select username, password from credentials"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCredentialsByUsername(self,username):
        cursor = self.conn.cursor()
        query = "select username, password from credentials where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getAccountCredentials(self,aid):
        cursor = self.conn.cursor()
        query = "select username, password from credentials natural inner join account where aid = %s;"
        cursor.execute(query, (aid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountCredentialsByUsernamePassword(self, aid, username, password):
        cursor = self.conn.cursor()
        query = "select username, password from credentials natural inner join account where aid = %s and username = %s and password = %s;"
        cursor.execute(query, (aid, username, password, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountCredentialsByUsername(self, aid, username):
        cursor = self.conn.cursor()
        query = "select username, password from credentials natural inner join account where aid = %s and username = %s;"
        cursor.execute(query, (aid, username, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountCredentialsByPassword(self, aid, password):
        cursor = self.conn.cursor()
        query = "select username, password from credentials natural inner join account where aid = %s and password = %s;"
        cursor.execute(query, (aid, password, ))
        result = []
        for row in cursor:
            result.append(row)
        return result