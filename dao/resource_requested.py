from config.dbconfig import conn

class ResourceRequestedDAO:

    def __init__(self):
        self.conn = conn

    def getAllResourcesRequested(self):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByQtyRequestDateChangedDate(self, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested where rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByQtyRequestDate(self, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested where rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByQtyChangedDate(self, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested where rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequestDateChangedDate(self, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested where rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByQty(self, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested where rrqty = %s;"
        cursor.execute(query, (rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequestDate(self, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested where rr_request_date = %s;"
        cursor.execute(query, (rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByChangedDate(self, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested where rr_changed_date = %s;"
        cursor.execute(query, (rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedById(self, rrid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested where rrid = %s;"
        cursor.execute(query, (rrid,))
        result = cursor.fetchone()
        return result

    def insert(self, rrqty, rrname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "insert into Resource_Requested(rrqty, rrname, rr_request_date, rr_changed_date) values (%s, %s, %s, %s) returning rrid;"
        cursor.execute(query, (rrqty, rrname, rr_request_date, rr_changed_date,))
        rrid = cursor.fetchone()[0]
        self.conn.commit()
        return rrid

    def update(self, rrid, rrqty, rrname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "update Resource_Requested set rrqty = %s rrname = %s rr_request_date = %s rr_changed_date = %s where rrid = %s;"
        cursor.execute(query, (rrqty, rrname, rr_request_date, rr_changed_date, rrid,))
        self.conn.commit()
        return rrid

    def delete(self, rrid):
        cursor = self.conn.cursor()
        query = "delete from Resource_Requested where rrid = %s;"
        cursor.execute(query, (rrid,))
        self.conn.commit()
        return rrid

    def getResourcesRequestedByCityName(self, cname):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s;"
        cursor.execute(query, (cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionName(self, rname):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByQtyRequestDateChangedDate(self, rname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where rname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByQtyRequestDate(self, rname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where rname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (rname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByQtyChangedDate(self, rname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where rname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (rname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByRequestDateChangedDate(self, rname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where rname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByQty(self, rname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where rname = %s and rrqty = %s;"
        cursor.execute(query, (rname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByRequestDate(self, rname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where rname = %s and rr_request_date = %s;"
        cursor.execute(query, (rname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByChangedDate(self, rname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where rname = %s and rr_changed_date = %s;"
        cursor.execute(query, (rname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordId(self, kid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where kid = %s order by rrname;"
        cursor.execute(query, (kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByQtyRequestDateChangedDate(self, kid, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where kid = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByQtyRequestDate(self, kid, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where kid = %s and rrqty = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (kid, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByQtyChangedDate(self, kid, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where kid = %s and rrqty = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByRequestDateChangedDate(self, kid, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where kid = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByQty(self, kid, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where kid = %s and rrqty = %s order by rrname;"
        cursor.execute(query, (kid, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByRequestDate(self, kid, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where kid = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (kid, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByChangedDate(self, kid, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where kid = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterId(self, rid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByQtyRequestDateChangedDate(self, rid, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where rid = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rid, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByQtyRequestDate(self, rid, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where rid = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (rid, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByQtyChangedDate(self, rid, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where rid = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (rid, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByRequestDateChangedDate(self, rid, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where rid = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rid, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByQty(self, rid, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where rid = %s and rrqty = %s;"
        cursor.execute(query, (rid, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByRequestDate(self, rid, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where rid = %s and rr_request_date = %s;"
        cursor.execute(query, (rid, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByChangedDate(self, rid, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where rid = %s and rr_changed_date = %s;"
        cursor.execute(query, (rid, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryName(self, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (cat_name, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByQtyRequestDateChangedDate(self, cat_name, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cat_name, cat_name, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByQtyRequestDate(self, cat_name, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cat_name, cat_name, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByQtyChangedDate(self, cat_name, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cat_name, cat_name, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByRequestDateChangedDate(self, cat_name, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where (cat_name = %s or cat_pname = %s) and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cat_name, cat_name, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByQty(self, cat_name, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where (cat_name = %s or cat_pname = %s) and rrqty = %s;"
        cursor.execute(query, (cat_name, cat_name, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByRequestDate(self, cat_name, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where (cat_name = %s or cat_pname = %s) and rr_request_date = %s;"
        cursor.execute(query, (cat_name, cat_name, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByChangedDate(self, cat_name, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where (cat_name = %s or cat_pname = %s) and rr_changed_date = %s;"
        cursor.execute(query, (cat_name, cat_name, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeyword(self, cname, kid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and kid = %s order by rrname;"
        cursor.execute(query, (cname, kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByQtyRequestDateChangedDate(self, cname, kid, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and kid = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByQtyRequestDate(self, cname, kid, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and kid = %s and rrqty = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByQtyChangedDate(self, cname, kid, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and kid = %s and rrqty = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByRequestDateChangedDate(self, cname, kid, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and kid = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByQty(self, cname, kid, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and kid = %s and rrqty = %s order by rrname;"
        cursor.execute(query, (cname, kid, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByRequestDate(self, cname, kid, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and kid = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByChangedDate(self, cname, kid, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and kid = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategory(self, cname, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (cname, cat_name, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByQtyRequestDateChangedDate(self, cname, cat_name, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, cat_name, cat_name, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByQtyRequestDate(self, cname, cat_name, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, cat_name, cat_name, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByQtyChangedDate(self, cname, cat_name, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, cat_name, cat_name, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByRequestDateChangedDate(self, cname, cat_name, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, cat_name, cat_name, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByQty(self, cname, cat_name, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s;"
        cursor.execute(query, (cname, cat_name, cat_name, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByRequestDate(self, cname, cat_name, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s;"
        cursor.execute(query, (cname, cat_name, cat_name, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByChangedDate(self, cname, cat_name, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and (cat_name = %s or cat_pname = %s) and rr_changed_date = %s;"
        cursor.execute(query, (cname, cat_name, cat_name, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeyword(self, rname, kid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where rname = %s and kid = %s order by rrname;"
        cursor.execute(query, (rname, kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByQtyRequestDateChangedDate(self, rname, kid, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where rname = %s and kid = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByQtyRequestDate(self, rname, kid, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where rname = %s and kid = %s and rrqty = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByQtyChangedDate(self, rname, kid, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where rname = %s and kid = %s and rrqty = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByRequestDateChangedDate(self, rname, kid, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where rname = %s and kid = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByQty(self, rname, kid, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where rname = %s and kid = %s and rrqty = %s order by rrname;"
        cursor.execute(query, (rname, kid, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByRequestDate(self, rname, kid, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where rname = %s and kid = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByChangedDate(self, rname, kid, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where rname = %s and kid = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategory(self, rname, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (rname, cat_name, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByQtyRequestDateChangedDate(self, rname, cat_name, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rname, cat_name, cat_name, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByQtyRequestDate(self, rname, cat_name, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (rname, cat_name, cat_name, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByQtyChangedDate(self, rname, cat_name, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (rname, cat_name, cat_name, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByRequestDateChangedDate(self, rname, cat_name, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rname, cat_name, cat_name, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByQty(self, rname, cat_name, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s;"
        cursor.execute(query, (rname, cat_name, cat_name, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByRequestDate(self, rname, cat_name, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s;"
        cursor.execute(query, (rname, cat_name, cat_name, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByChangedDate(self, rname, cat_name, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and (cat_name = %s or cat_pname = %s) and rr_changed_date = %s;"
        cursor.execute(query, (rname, cat_name, cat_name, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequester(self, kid, rid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where kid = %s and rid = %s order by rrname;"
        cursor.execute(query, (kid, rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByQtyRequestDateChangedDate(self, kid, rid, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where kid = %s and rid = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByQtyRequestDate(self, kid, rid, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where kid = %s and rid = %s and rrqty = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByQtyChangedDate(self, kid, rid, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where kid = %s and rid = %s and rrqty = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByRequestDateChangedDate(self, kid, rid, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where kid = %s and rid = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByQty(self, kid, rid, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where kid = %s and rid = %s and rrqty = %s order by rrname;"
        cursor.execute(query, (kid, rid, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByRequestDate(self, kid, rid, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where kid = %s and rid = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByChangedDate(self, kid, rid, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where kid = %s and rid = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategory(self, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where kid = %s and (cat_name = %s or cat_pname = %s) order by rrname;"
        cursor.execute(query, (kid, cat_name, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByQtyRequestDateChangedDate(self, kid, cat_name, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, cat_name, cat_name, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByQtyRequestDate(self, kid, cat_name, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (kid, cat_name, cat_name, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByQtyChangedDate(self, kid, cat_name, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, cat_name, cat_name, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByRequestDateChangedDate(self, kid, cat_name, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where kid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, cat_name, cat_name, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByQty(self, kid, cat_name, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s order by rrname;"
        cursor.execute(query, (kid, cat_name, cat_name, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByRequestDate(self, kid, cat_name, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where kid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s order by rrname;"
        cursor.execute(query, (kid, cat_name, cat_name, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByChangedDate(self, kid, cat_name, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where kid = %s and (cat_name = %s or cat_pname = %s) and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, cat_name, cat_name, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategory(self, rid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (rid, cat_name, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByQtyRequestDateChangedDate(self, rid, cat_name, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where rid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rid, cat_name, cat_name, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByQtyRequestDate(self, rid, cat_name, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where rid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (rid, cat_name, cat_name, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByQtyChangedDate(self, rid, cat_name, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where rid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (rid, cat_name, cat_name, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByRequestDateChangedDate(self, rid, cat_name, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where rid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (rid, cat_name, cat_name, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByQty(self, rid, cat_name, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where rid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s;"
        cursor.execute(query, (rid, cat_name, cat_name, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByRequestDate(self, rid, cat_name, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where rid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s;"
        cursor.execute(query, (rid, cat_name, cat_name, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByChangedDate(self, rid, cat_name, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where rid = %s and (cat_name = %s or cat_pname = %s) and rr_changed_date = %s;"
        cursor.execute(query, (rid, cat_name, cat_name, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategory(self, cname, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and kid = %s and (cat_name = %s or cat_pname = %s) order by rrname;"
        cursor.execute(query, (cname, kid, cat_name, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByQtyRequestDateChangedDate(self, cname, kid, cat_name, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, cat_name, cat_name, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByQtyRequestDate(self, cname, kid, cat_name, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, cat_name, cat_name, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByQtyChangedDate(self, cname, kid, cat_name, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, cat_name, cat_name, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByRequestDateChangedDate(self, cname, kid, cat_name, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, cat_name, cat_name, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByQty(self, cname, kid, cat_name, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s order by rrname;"
        cursor.execute(query, (cname, kid, cat_name, cat_name, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByRequestDate(self, cname, kid, cat_name, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, cat_name, cat_name, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByChangedDate(self, cname, kid, cat_name, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (cname, kid, cat_name, cat_name, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategory(self, rname, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where rname = %s and kid = %s and (cat_name = %s or cat_pname = %s) order by rrname;"
        cursor.execute(query, (rname, kid, cat_name, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByQtyRequestDateChangedDate(self, rname, kid, cat_name, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where rname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, cat_name, cat_name, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByQtyRequestDate(self, rname, kid, cat_name, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where rname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, cat_name, cat_name, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByQtyChangedDate(self, rname, kid, cat_name, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where rname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, cat_name, cat_name, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByRequestDateChangedDate(self, rname, kid, cat_name, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where rname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, cat_name, cat_name, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByQty(self, rname, kid, cat_name, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where rname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s order by rrname;"
        cursor.execute(query, (rname, kid, cat_name, cat_name, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByRequestDate(self, rname, kid, cat_name, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where rname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, cat_name, cat_name, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByChangedDate(self, rname, kid, cat_name, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where rname = %s and kid = %s and (cat_name = %s or cat_pname = %s) and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (rname, kid, cat_name, cat_name, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategory(self, kid, rid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where kid = %s and rid = %s and (cat_name = %s or cat_pname = %s) order by rrname;"
        cursor.execute(query, (kid, rid, cat_name, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByQtyRequestDateChangedDate(self, kid, rid, cat_name, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where kid = %s and rid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, cat_name, cat_name, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByQtyRequestDate(self, kid, rid, cat_name, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where kid = %s and rid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_request_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, cat_name, cat_name, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByQtyChangedDate(self, kid, rid, cat_name, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where kid = %s and rid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, cat_name, cat_name, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByRequestDateChangedDate(self, kid, rid, cat_name, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where kid = %s and rid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, cat_name, cat_name, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByQty(self, kid, rid, cat_name, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where kid = %s and rid = %s and (cat_name = %s or cat_pname = %s) and rrqty = %s order by rrname;"
        cursor.execute(query, (kid, rid, cat_name, cat_name, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByRequestDate(self, kid, rid, cat_name, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where kid = %s and rid = %s and (cat_name = %s or cat_pname = %s) and rr_request_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, cat_name, cat_name, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByChangedDate(self, kid, rid, cat_name, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrname, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where kid = %s and rid = %s and (cat_name = %s or cat_pname = %s) and rr_changed_date = %s order by rrname;"
        cursor.execute(query, (kid, rid, cat_name, cat_name, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result
