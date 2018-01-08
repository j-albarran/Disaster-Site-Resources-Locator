from config.dbconfig import conn

class CategoryDAO:

    def __init__(self):
        self.conn = conn

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
        result = cursor.fetchone()
        return result

    def insert(self, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "insert into Category(cat_name, cat_pname) values (%s, %s);"
        cursor.execute(query, (cat_name, cat_pname))
        self.conn.commit()
        return cat_name

    def updateCategory(self, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "update Category set cat_pname = %s where cat_name = %s;"
        cursor.execute(query, (cat_pname, cat_name))
        self.conn.commit()
        return cat_name

    def delete(self, cat_name):
        cursor = self.conn.cursor()
        query = "delete from Category where cat_name = %s;"
        cursor.execute(query, (cat_name,))
        self.conn.commit()
        return cat_name

    def getCategoriesByCityName(self, cname):
        cursor = self.conn.cursor()
        query = "Select cat_name, cat_pname from (Category natural inner join Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoriesByRegionName(self, rname):
        cursor = self.conn.cursor()
        query = "Select cat_name, cat_pname from (Category natural inner join Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoriesByResourceId(self, rsid):
        cursor = self.conn.cursor()
        query = "Select cat_name, cat_pname from Category natural inner join Resource where rsid = %s;"
        cursor.execute(query, (rsid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoriesByKeywordId(self, kid):
        cursor = self.conn.cursor()
        query = "Select cat_name, cat_pname from Category natural inner join Resource natural inner join ResourceHasKeyword where kid = %s;"
        cursor.execute(query, (kid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoriesByResourceRequestedId(self, rrid):
        cursor = self.conn.cursor()
        query = "Select cat_name, cat_pname from Category natural inner join Resource_Requested where rrid = %s;"
        cursor.execute(query, (rrid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoriesByCategoryName(self, cat_pname):
        cursor = self.conn.cursor()
        query = "Select cat_name, cat_pname from Category where cat_pname = %s;"
        cursor.execute(query, (cat_pname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoriesByTransactionId(self, tid):
        cursor = self.conn.cursor()
        query = "Select cat_name, cat_pname from Category natural inner join Resource natural inner join Transaction where tid = %s;"
        cursor.execute(query, (tid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
