from config.dbconfig import conn

class PaymentDAO:
    def __init__(self):
        self.conn = conn
# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getPaymentnById(self, payid):
        cursor = self.conn.cursor()
        query = "Select payid from payment where payid = %s"
        cursor.execute(query, (payid,))
        result = []
        for row in cursor:
            result.append(row)
        return result