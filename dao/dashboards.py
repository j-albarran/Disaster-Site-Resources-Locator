from config.dbconfig import conn

class DashBoardsDAO:
    def __init__(self):
        self.conn = conn

    #daily
    def getResourcesNeedsDaily(self):
        cursor = self.conn.cursor()
        query = "select sum(rrqty) as partial_sum from resource_requested where rr_changed_date = date_trunc('day', now()) and rrqty >0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvailablesDaily(self):
        cursor = self.conn.cursor()
        query = "select sum(rqty) as partial_sum from resource where r_changed_date = date_trunc('day', now()) and rqty >0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesMatchesDaily(self):
        cursor = self.conn.cursor()
        query = ("select COALESCE(sum(rqty), 0) as partial_sum from resource where r_changed_date = date_trunc('day', now()) and rqty >0"
                " union all"
                " select COALESCE(sum(rrqty), 0) as partial_sum from resource_requested where rr_changed_date = date_trunc('day', now()) and rrqty >0")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #weekly
    def getResourcesNeedsWeekly(self):
        cursor = self.conn.cursor()
        query = "select sum(rrqty) as partial_sum from resource_requested where rr_changed_date between (date_trunc('day', now()) - interval '7 days')  and date_trunc('day', now()) and rrqty >0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvailablesWeekly(self):
        cursor = self.conn.cursor()
        query = "select sum(rqty) as partial_sum from resource where r_changed_date between (date_trunc('day', now()) - interval '7 days') and date_trunc('day', now()) and rqty >0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesMatchesWeekly(self):
        cursor = self.conn.cursor()
        query = ("select COALESCE(sum(rqty), 0) as partial_sum from resource where r_changed_date between (date_trunc('day', now()) - interval '7 days') and date_trunc('day', now()) and rqty >0"
                " union all"
                " select COALESCE(sum(rrqty), 0) as partial_sum from resource_requested where rr_changed_date between (date_trunc('day', now()) - interval '7 days') and date_trunc('day', now()) and rrqty >0")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #region

    def getResourcesAvailablesByRegion(self):
        cursor = self.conn.cursor()
        query = "Select sum(rqty), region.rname from (resource natural inner join supplier inner join account on sid = aid) natural inner join address natural inner join city right outer join region on city.rname = region.rname group by region.rname order by region.rname"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesNeedsByRegion(self):
        cursor = self.conn.cursor()
        query = "Select sum(rrqty), region.rname from (resource_requested natural inner join requester inner join account on rid = aid) natural inner join address natural inner join city right outer join region on city.rname = region.rname group by region.rname order by region.rname"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesMatchesByRegion(self, rname):
        cursor = self.conn.cursor()
        query = ("with partials_sum as"
                "("
                    "(Select sum(rqty) as partial_sum, rname from (resource natural inner join supplier inner join account on sid = aid) natural inner join address natural inner join city group by rname)"
                    "union"
                    "(Select sum(rrqty) as partial_sum, rname from (resource_requested natural inner join requester inner join account on rid = aid) natural inner join address natural inner join city group by rname)"
                "),"
                "total_sum as"
                "(select sum(partials_sum.partial_sum), rname as region from partials_sum group by rname),"
                "available as"
                "(Select sum(rqty) as partial_sum, rname as region from (resource natural inner join supplier inner join account on sid = aid) natural inner join address natural inner join city group by rname),"
                "need as"
                "(Select sum(rrqty) as partial_sum, rname as region from (resource_requested natural inner join requester inner join account on rid = aid) natural inner join address natural inner join city group by rname)"
                "Select A.percent as Availabe_Resources, B.percent as Need_Resources, A.regionTwo from (Select available.partial_sum/total_sum.sum*100 as percent, region.rname as regionTwo from total_sum inner join available on total_sum.region = available.region right outer join region on total_sum.region = region.rname) as A full outer join (Select need.partial_sum/total_sum.sum*100 as percent, total_sum.region as region from total_sum inner join need on total_sum.region = need.region) as B on A.regionTwo = B.region"
                " where A.regionTwo = %s"
                )
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
