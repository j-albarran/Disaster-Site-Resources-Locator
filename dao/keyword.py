from config.dbconfig import pg_config
import psycopg2

class KeywordDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllKeywords(self):
        cursor = self.conn.cursor()
        query = "Select * from Keyword;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getKeywordsByKeyword(self, keyword):
        cursor = self.conn.cursor()
        query = "Select * from Keyword where keyword = %s;"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getKeywordById(self, kid):
        cursor = self.conn.cursor()
        query = "Select * from Keyword where kid = %s;"
        cursor.execute(query, (kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, keyword):
        cursor = self.conn.cursor()
        query = "insert into Keyword(keyword) values (%s) returning kid;"
        cursor.execute(query, (keyword,))
        kid = cursor.fetchone()[0]
        self.conn.commit()
        return kid

    def update(self, kid, keyword):
        cursor = self.conn.cursor()
        query = "update Keyword set keyword = %s where kid = %s;"
        cursor.execute(query, (keyword, kid))
        self.conn.commit()
        return kid

    def delete(self, kid):
        cursor = self.conn.cursor()
        query = "delete from Keyword where kid = %s;"
        cursor.execute(query, (kid,))
        self.conn.commit()
        return kid

    def getKeywordsByResourceId(self, rsid):
        cursor = self.conn.cursor()
        query = "Select kid, keyword from Keyword natural inner join ResourceHasKeyword where rsid = %s;"
        cursor.execute(query, (rsid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getKeywordsByResourceIdByKeyword(self, rsid, keyword):
        cursor = self.conn.cursor()
        query = "Select kid, keyword from Keyword natural inner join ResourceHasKeyword where rsid = %s and keyword = %s;"
        cursor.execute(query, (rsid, keyword))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getKeywordsByResourceRequestedId(self, rrid):
        cursor = self.conn.cursor()
        query = "Select kid, keyword from Keyword natural inner join ResourceRequestedHasKeyword where rrid = %s;"
        cursor.execute(query, (rrid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getKeywordsByResourceRequestedIdByKeyword(self, rrid, keyword):
        cursor = self.conn.cursor()
        query = "Select kid, keyword from Keyword natural inner join ResourceRequestedHasKeyword rrid = %s and keyword = %s;"
        cursor.execute(query, (rrid, keyword))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getKeywordsByCategoryName(self, cat_name):
        cursor = self.conn.cursor()
        query = "Select kid, keyword from Keyword natural inner join ResourceHasKeyword natural inner join ResourceRequestedHasKeyword where cat_name = %s;"
        cursor.execute(query, (cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getKeywordsByCategoryNameByKeyword(self, cat_name, keyword):
        cursor = self.conn.cursor()
        query = "Select kid, keyword from Keyword natural inner join ResourceHasKeyword natural inner join ResourceRequestedHasKeyword where cat_name = %s and keyword = %s;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
