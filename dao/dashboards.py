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
        query = ("select sum(rqty) as partial_sum from resource where r_changed_date <= date_trunc('day', now()) and rqty >0"
                " union"
                " select sum(rrqty) as partial_sum from resource_requested where rr_changed_date <= date_trunc('day', now()) and rrqty >0")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #weekly
    def getResourcesNeedsWeekly(self):
        cursor = self.conn.cursor()
        query = "select sum(rrqty) as partial_sum from resource_requested where rr_changed_date between date_trunc('day', now()) and (date_trunc('day', now()) - interval '7 days') and rrqty >0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvailablesWeekly(self):
        cursor = self.conn.cursor()
        query = "select sum(rqty) as partial_sum from resource where r_changed_date between date_trunc('day', now()) and (date_trunc('day', now()) - interval '7 days') and rqty >0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesMatchesWeekly(self):
        cursor = self.conn.cursor()
        query = ("select sum(rqty) as partial_sum from resource where r_changed_date between date_trunc('day', now()) and (date_trunc('day', now()) - interval '7 days') and rqty >0"
                " union"
                " select sum(rrqty) as partial_sum from resource_requested where rr_changed_date between date_trunc('day', now()) and (date_trunc('day', now()) - interval '7 days') and rrqty >0")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

