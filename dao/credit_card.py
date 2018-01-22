from config.dbconfig import conn

class CreditCardDAO:
    def __init__(self):
        self.conn = conn

    def getAllCreditCards(self):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByNameNumber(self,ccname,card_number):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card where ccname = %s and card_number = %s;"
        cursor.execute(query, ( ccname, card_number,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByName(self,ccname):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card where ccname = %s;"
        cursor.execute(query, ( ccname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByNumber(self,card_number):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card where card_number = %s;"
        cursor.execute(query, ( card_number,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardById(self, cid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card where cid = %s;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByIdNameNumber(self,ccname,card_number, cid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card where ccname = %s and card_number = %s and cid = %s;"
        cursor.execute(query, ( ccname, card_number, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByIdName(self,ccname, cid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card where ccname = %s and cid = %s;"
        cursor.execute(query, ( ccname, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByIdNumber(self,card_number, cid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card where card_number = %s and cid = %s;"
        cursor.execute(query, ( card_number, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByTransaction(self, tid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info inner join transaction on Order_Info.oid = transaction.oid where tid = %s;"
        cursor.execute(query, (tid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByTransactionNameNumber(self,ccname,card_number, tid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info inner join transaction on Order_Info.oid = transaction.oid where ccname = %s and card_number = %s and tid = %s;"
        cursor.execute(query, ( ccname, card_number, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByTransactionName(self,ccname, tid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info inner join transaction on Order_Info.oid = transaction.oid where ccname = %s and tid = %s;"
        cursor.execute(query, ( ccname, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByTransactionNumber(self,card_number, tid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info inner join transaction on Order_Info.oid = transaction.oid where card_number = %s and tid = %s;"
        cursor.execute(query, ( card_number, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByRequester(self, rid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card natural inner join Requester where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByRequesterNameNumber(self,ccname,card_number, rid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card natural inner join Requester where ccname = %s and card_number = %s and rid = %s;"
        cursor.execute(query, ( ccname, card_number, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByRequesterName(self,ccname, rid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card natural inner join Requester where ccname = %s and rid = %s;"
        cursor.execute(query, ( ccname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByRequesterNumber(self,card_number, rid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from Credit_Card natural inner join Requester where card_number = %s and rid = %s;"
        cursor.execute(query, ( card_number, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByOrder(self, oid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info where oid = %s;"
        cursor.execute(query, (oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByOrderNameNumber(self,ccname,card_number, oid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info where ccname = %s and card_number = %s and oid = %s;"
        cursor.execute(query, ( ccname, card_number, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByOrderName(self,ccname, oid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info where ccname = %s and oid = %s;"
        cursor.execute(query, ( ccname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCreditCardsByOrderNumber(self,card_number, oid):
        cursor = self.conn.cursor()
        query = "Select cid, card_number, security_code, ccname, exp_date from (Credit_Card inner join payment on payid = cid) natural inner join Order_Info where card_number = %s and oid = %s;"
        cursor.execute(query, ( card_number, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertCreditCard(self, card_number, security_code, ccname, exp_date, rid, addid):
        cursor = self.conn.cursor()
        query = "insert into payment(rid) values (%s) returning payid;"
        cursor.execute(query, (rid,))
        payid = cursor.fetchone()[0]
        query = "insert into credit_card(cid, card_number, security_code, ccname, exp_date, rid, addid) values (%s, %s, %s, %s, %s, %s, %s) returning cid;"
        cursor.execute(query, (payid, card_number, security_code, ccname, exp_date, rid, addid))
        cid = cursor.fetchone()[0]
        self.conn.commit()
        return cid

    def deleteCreditCard(self, cid):
        cursor = self.conn.cursor()
        query = "delete from credit_card where cid = %s;"
        cursor.execute(query, (cid, ))
        query = "delete from payment where payid = %s"
        cursor.execute(query, (cid,))
        self.conn.commit()
        return

    def updateCreditCard(self, cid, card_number, security_code, ccname, exp_date):
        cursor = self.conn.cursor()
        query = "update credit_card set card_number = %s, security_code = %s, ccname = %s, exp_date = %s where cid = %s;"
        cursor.execute(query, (card_number, security_code, ccname, exp_date, cid))
        self.conn.commit()
        return



