

class CategoryDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (self, pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(self, connection_url)

    def getAllCategories(self):
        cursor = self.conn.cursor()
        query = "select * from Category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryByName(self, cat_name):
        cursor = self.conn.cursor()
        query = "select * from Category where cat_name = %s;"
        cursor.execute(query, (cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ***def insert(self, cat_name):
        cursor = self.conn.cursor()
        query = "insert into Category(cat_name) values (%s);"
        cursor.execute(query, (cat_name,))
        kid = cursor.fetchone()[0]
        self.conn.commit()
        return kid

    ***def updateCategory(self, cat_name):
        cursor = self.conn.cursor()
        query = "update Keyword set keyword = %s where kid = %s;"
        cursor.execute(query, (keyword, kid))
        self.conn.commit()
        return kid

    ***def delete(self, cat_name):
        cursor = self.conn.cursor()
        query = "delete from Keyword where kid = %s;"
        cursor.execute(query, (kid,))
        self.conn.commit()
        return kid

    def getCategoriesByCityName(self, cname):
        pass

    def getCategoriesByRegionName(self, rname):
        pass

    def getCategoriesByResourceId(self, rsid):
        pass

    def getCategoriesByKeywordId(self, kid):
        pass

    def getCategoriesByResourceRequestedId(self, rrid):
        pass

    def getCategoriesByCategoryName(self, cat_name):
        pass

    def getCategoriesByTransactionId(self, tid):
        pass
