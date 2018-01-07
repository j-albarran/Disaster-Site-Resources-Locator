from config.dbconfig import pg_config
import psycopg2

class ResourceRequestedDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResourcesRequested(self):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequested1ByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequested1ByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequested1ByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequested1ByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequested1ByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequested1ByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequested1ByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedById(self, rrid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested where rrid = %s;"
        cursor.execute(query, (rrid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rrqty, rrdescription, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "insert into Resource_Requested(rrqty, rrdescription, rr_request_date, rr_changed_date) values (%s, %s, %s, %s) returning rrid;"
        cursor.execute(query, (rrqty, rrdescription, rr_request_date, rr_changed_date,))
        rrid = cursor.fetchone()[0]
        self.conn.commit()
        return rrid

    def update(self, rrid, rrqty, rrdescription, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "update Resource_Requested set rrqty = %s rrdescription = %s rr_request_date = %s rr_changed_date = %s where rrid = %s;"
        cursor.execute(query, (rrqty, rrdescription, rr_request_date, rr_changed_date, rrid,))
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
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s;"
        cursor.execute(query, (cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityNameByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Requester) as R inner join Account as A on R.rid = A.aid natural inner join Address where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionName(self, rname):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionNameByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordId(self, kid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where kid = %s;"
        cursor.execute(query, (kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordIdByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterId(self, rid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterIdByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryName(self, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where cat_name = %s;"
        cursor.execute(query, (cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCategoryNameByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Category where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeyword(self, cname, kid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and kid = %s;"
        cursor.execute(query, (cname, kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategory(self, cname, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s;"
        cursor.execute(query, (cname, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityCategoryByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join Category where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeyword(self, rname, kid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where rname = %s and kid = %s;"
        cursor.execute(query, (rname, kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategory(self, rname, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s;"
        cursor.execute(query, (rname, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionCategoryByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join Category where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequester(self, kid, rid):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where kid = %s and rid = %s;"
        cursor.execute(query, (kid, rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join ResourceRequestedHasKeyword where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategory(self, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where kid = %s and cat_name = %s;"
        cursor.execute(query, (kid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordCategoryByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategory(self, rid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where rid = %s and cat_name = %s;"
        cursor.execute(query, (rid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRequesterCategoryByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join Requester natural inner join Category where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategory(self, cname, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s;"
        cursor.execute(query, (cname, kid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByCityKeywordCategoryByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategory(self, rname, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s;"
        cursor.execute(query, (rname, kid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByRegionKeywordCategoryByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from (Resource_Requested natural inner join Supplier) as R inner join Account as A on R.rid = A.aid natural inner join Address natural inner join City natural inner join ResourceRequestedHasKeyword natural inner join Category where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategory(self, kid, rid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where kid = %s and rid = %s and cat_name = %s;"
        cursor.execute(query, (kid, rid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByQtyRequestDateChangedDate(self, cname, rrqty, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByQtyRequestDate(self, cname, rrqty, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where cname = %s and rrqty = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByQtyChangedDate(self, cname, rrqty, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where cname = %s and rrqty = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rrqty, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByRequestDateChangedDate(self, cname, rr_request_date, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where cname = %s and rr_request_date = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_request_date, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByQty(self, cname, rrqty):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where cname = %s and rrqty = %s;"
        cursor.execute(query, (cname, rrqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByRequestDate(self, cname, rr_request_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where cname = %s and rr_request_date = %s;"
        cursor.execute(query, (cname, rr_request_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByKeywordRequesterCategoryByChangedDate(self, cname, rr_changed_date):
        cursor = self.conn.cursor()
        query = "Select rrid, rrqty, rrdescription, rr_request_date, rr_changed_date from Resource_Requested natural inner join ResourceRequestedHasKeyword natural inner join Requester natural inner join Category where cname = %s and rr_changed_date = %s;"
        cursor.execute(query, (cname, rr_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result
